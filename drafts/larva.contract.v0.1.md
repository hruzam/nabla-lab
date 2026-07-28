# larva — file contract v0.1 (DRAFT)
_Status: proposed, not frozen. Open questions in §9 block the freeze._
_Authored 2026-07-24 by Nabla, from the majkee/Nabla architecture thread._

---

## 0. What this document is

The **only** thing in the system that must be right before anything is built. Every other
decision — monolith vs split, Python vs anything, panel design, which multiplexer — is an
implementation detail *behind* this contract and is therefore reversible.

Everything below is either **[FROZEN]** (decided, load-bearing) or **[OPEN]** (§9, needs a call).

---

## 1. Layout

```
room/
  roll.md              # THE history. hub is sole writer, append-only
  state.json           # live state only. hub sole writer, latest-only
  modes/*.yaml         # policy definitions
  cursors/             # per-participant read offsets over roll.md   [OPEN — Q3]
    agent-a.offset
  rounds/0042/
    meta.json          # opened_at, mode, participants, turn_order, canonical order
    human.md           # one writer each, immutable after close
    agent-a.md
    agent-b.md
    view-a.md          # DERIVED — the projection delivered to a
  raw/
    agent-a.pty.log    # adapter sole writer, append-only, PUBLISHED
    agent-a.cursor     # extractor's own offset {log_id, offset}
  derived/             # anchors, index, summaries. rm -rf safe by definition
```

## 2. The four invariants [FROZEN]

Everything else in this document follows from these. If a proposed feature breaks one,
the feature is wrong, not the invariant.

1. **One writer per file.** No exceptions, no advisory-lock workarounds.
2. **All writes are temp + `rename()`** within the same directory. A reader never observes
   a partial file. This is the atomic commit primitive, free from POSIX.
3. **Turn files are immutable** once the round closes.
4. **`derived/` is disposable** — deletable and rebuildable from `roll.md` + `raw/`.
   If something can't be rebuilt from those two, it does not belong in `derived/`.

Corollary — **truth ranking**: `raw/` (what was actually said) > `roll.md` (what was
committed) > everything else (derived, cached, indexed). A disagreement is always resolved
downward toward `raw/`.

## 3. Roll entry format [FROZEN]

```markdown
<!-- turn r=0042 speaker=agent-a ts=2026-07-24T11:02:31Z src=rounds/0042/agent-a.md -->
## R0042 · agent-a

<body>
```

Machine parses the comment; human reads the heading; Sublime renders it clean. Grep-able
both ways. `src=` is the back-pointer to the immutable turn file — the roll is an ordered
**index over turn files**, not a second copy of the truth.

## 4. Round lifecycle [FROZEN]

| phase | action |
|---|---|
| **open** | hub creates `rounds/NNNN/`, writes `meta.json`, projects views per mode, delivers |
| **close** | `quorum satisfied OR timeout` |
| **no-reply** | non-responder gets an explicit `[no-reply]` file — **silence and pending are never the same state on disk** |
| **commit** | append all turns to `roll.md` in **canonical participant order** (from `meta.json`, never arrival order — otherwise the roll is nondeterministic) |
| **advance** | git commit (one per round close), open `NNNN+1` |

## 5. Cursor semantics [FROZEN]

Strict, non-negotiable ordering in the extractor:

```
extract region  →  write turn (temp+rename)  →  advance cursor
```

Crash anywhere: on restart the same region is re-extracted and the rename overwrites
identically. **Replay is idempotent.** Reverse the last two steps and a crash eats a turn.

Cursor file is `{log_id, offset}`. `log_id` exists so that log rotation cannot silently
reset a byte offset into a different file.

## 6. Mode schema [FROZEN]

```yaml
mode: blind-triangulation
turn_order: parallel        # or an ordered list: [architect, tester]
close: {quorum: all, timeout: 300s}
reveal: at-close            # or: immediate
view:
  agent-a: {source: roll, strip_own: true,  since: last_read}
  agent-b: {source: roll, strip_own: true,  since: last_read}
  human:   {source: roll, strip_own: false, since: last_read}
```

- `turn_order: parallel` → **barrier**; hub tracks *who's pending*.
- `turn_order: [list]` → **sequential**; hub tracks *who's up*. One field, two machines.
- Known modes as policy, not code: FLAT · BLIND-TRIANGULATION · LOOP (architect→tester)
  · SPECIFIC-TAG (private routing).

**The test for this schema:** if a new protocol requires touching router code, the schema
was wrong. Every mode in the sketch must be expressible as data.

**View policy is per-participant, not global** — a *resident* agent holds its own turn in
its KV context, so re-feeding it causes echo (`strip_own: true`); a *cold-invoked* agent
holds nothing, so stripping its own turns amputates its lineage (`strip_own: false`).

## 7. Published streams [FROZEN]

`raw/*.pty.log` is a **published** stream, not a private pipe between adapter and extractor.
Multiple consumers, each with its own cursor file. Nobody truncates it. Rotation by rename
only. Costs nothing today; makes a telemetry watcher or a second/experimental extractor a
non-event later.

## 8. state.json [FROZEN]

- **Live state only** — round no., mode, who's pending/up, adapter liveness, extractor
  cursor position. Rebuildable from disk on hub start. Safe to `rm`.
- **Writes are event-driven**, on transition only (~10/min at peak). Debounce clumps at
  ~100ms.
- **Durations are never written.** The file carries facts and timestamps
  (`round_opened_at`, `last_seen_at`); the renderer computes `41s` at draw time.
  Writing elapsed seconds converts an event-driven file into a 1Hz write loop.
- **Readers may miss intermediate states — by design.** The panel needs *latest*, not *every*.
- **Durable events** (mode change, force-close, adapter death) are appended to `roll.md`
  as `speaker=system` turns. One history; *"why was R0038 force-closed at 3am"* is answered
  by grepping the roll, same as everything else.
- **The panel never reads the raw tail.** State comes from the committed layer only — a
  lagging extractor must not be able to tell the panel a round is done.

---

## 9. OPEN — blocks the freeze

### Q1 · Per-participant read cursors: where do they live?
`since: last_read` implies the hub keeps a read offset per participant over `roll.md`.

- **(a)** inside `state.json` — fewer files, but `state.json` is declared rebuildable-from-disk,
  and *rebuilt from what?* A read cursor is not derivable from the roll itself.
- **(b)** `cursors/agent-a.offset`, one file per participant — durable, same discipline as
  the extractor cursor, but a fifth thing to keep consistent.

**Lean: (b).** It makes `state.json` honestly disposable and keeps every cursor in the system
under one identical rule (`{log_id, offset}`, advance-last). Listed in §1 provisionally.

### Q2 · Delivery: how does a projected view *reach* an agent?
Not specified anywhere yet, and it determines the token bill and per-round latency.

- **(a)** paste projected text into the PTY — works everywhere, re-sends roll content every round
- **(b)** write `view-a.md`, paste only *"read this file"* — cheap, but the agent must actually
  read it, and a tool-call round-trip now sits inside the turn

**Lean: none yet.** This is the highest-consequence unspecified item in the design; it deserves
its own pass, not a paragraph. The contract can freeze without it *only because* `view-a.md`
is already in the layout — (b) is expressible, (a) ignores the file. No path change either way.

### Q3 · Interactive permission prompts
Agent CLIs block on `allow this edit? (y/n)`. The PTY does not return, no sentinel arrives,
the barrier times out, and `[no-reply]` is written for an agent that is alive and waiting on a
keypress. Contract-level question: **is a blocked-on-prompt adapter a distinct state on disk**,
or is it invisible until timeout?

**Lean: distinct state.** Same reasoning as `[no-reply]` — never let two different realities
share one representation. Costs one enum value in `state.json` now; costs a week of debugging
later.

### Q4 · Session restart mid-conversation
Commands exist (kill-window, session-restart, session-sleep). Unanswered: when a window fills
at round 40 and the process is restarted, **what does the fresh process read to become the same
participant?** Replaying 40 rounds is not feasible; reading nothing makes it a different
participant wearing the same name.

**Lean: out of scope for v0.1, but reserve the path.** This is the reincarnation problem landing
in a live loop and it needs its own design pass. Reserve `rounds/NNNN/handoff-a.md` in the
layout so the answer, whatever it is, doesn't force a contract revision.

---

## 10. Deliberately NOT pinned

- whether the extractor is a thread or a separate PID
- what language any component is written in
- the process supervision method (systemd scopes, tmux, bare fork)
- panel rendering, keymap location (zle vs multiplexer), editor choice
- whether TRANSLATOR / anchors / cache ever get built (they are `derived/` by construction)

All reversible behind §1–§8.

---

_Freeze condition: Q1 and Q3 answered. Q2 and Q4 may remain open — the layout already
accommodates both branches of each._
