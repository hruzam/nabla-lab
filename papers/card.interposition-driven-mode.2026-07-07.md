# Instrument card — Driven Mode (interposition, full range: the bus conducts living sessions)

`shaped: 2026-07-07 · revised same day per @Janus gate (REVISE accepted: canary grace window)`
`gates: Epoch [v] · Color mechanism verdict · Janus REVISE→applied · Gate-3 co-signed majkee (G7) — all 2026-07-07`
`crossed shaped→papers 2026-07-07 (gavel G7) · runnable seed stays at shaped/seed.brick2.py`
`derived from: drafts/interposition-study.md (Loop II) + drafts/brick1.py (superseded by shaped/seed.brick2.py) + subai part1.blueprint`
`destination: subai.devenv (_bus, third mode — adoption gaveled G8) · status: BUILD-NOW (single driven pane) · OPERATIONALIZE (multi-project conductor)`
`maturity: REPURPOSED (primitives) / YOURS (integration)`

## Concept — the missing third mode

The subai bus has two modes: `living` (drop a card, fire-and-forget — **no acknowledgment**) and
`worker` (`-p` headless — **metered since 2026-06-15**, no persistent session). **`driven` is the
missing middle:** a persistent, interactive, subscription-native session in a per-project tmux pane
that the bus can write to *and get verified completion from*.

**The governing insight — channel algebra:** *write at the wire, read at the record.*
The pane (PTY) is used **only for injection** (bracketed paste). Acknowledgment and content are
**never scraped from the pane**. Three signals, all from the sanctioned ring-1 hooks seam:

| Signal | Source | Mechanism |
|---|---|---|
| **identity** | `SessionStart` hook | launch-token env (`BUS_PANE=<uuid>`) → `session_id` + `transcript_path`; fallback: `cwd` match (valid: one driven pane per project) |
| **completion** | `Stop` hook | fires **only on normal main-agent completion** — not on subagent stops, not on user interrupt. Timeout ⇒ abort/hang detection, by construction. |
| **content** | transcript JSONL | terminal assistant entry keyed by `stop_reason ≠ tool_use`, located after the per-turn **nonce'd user record** (nonce read from the structured record — no echo ambiguity) |

**Why brick1's pane sentinel is dead (Color verdict: structurally unsound):** the detector scanned
the same channel it injected into, for a token byte-identical to the one it injected. Input echo and
genuine emission are indistinguishable *by construction*; any green run rides an undocumented TUI
paste-collapse heuristic. Not a bug to patch — a channel to abandon. (Color's Part-1 fixes for a
pane-only fallback — non-contiguous marker description, per-pane sinks, OSC/DCS regex — are recorded
in the mechanism report; use only if the hooks seam is ever unavailable.)

## Mapping

- **subai `_bus`:** add `"mode": "driven"` to `bus.config.json`; one pane per project
  (`bus-<slug>`); `ask()` serialized per pane; Stop events flatten to pulses in the medium
  (`.` reply-landed, `!` timeout/abort) — completion becomes first-class bus state.
- **Economics inversion (the structural fact):** since 2026-06-15, `-p` headless draws from the
  metered Agent SDK credit pool; interactive sessions draw from the subscription. `driven` is
  therefore **the only subscription-native automation path left** — it partially *replaces*
  `worker` for Claude-target tasks rather than merely extending the bus.
- **Full range — the conductor:** one driven pane per project; `in.md` fan-out gains verified
  round-trips; replies land laned by `from` in the skin; cross-project orchestration (including the
  agent fleet's project seats) rides the same file contract. No new medium — the pulse ledger
  already is the conductor's score.
- **Compliance gradient (not a cliff)** — verified 2026-07-07, volatile, refresh monthly:
  - OAuth bright line **respected**: genuine `claude` binary, token never extracted or relayed.
  - "Ordinary, individual usage" is rate-limit prose in product docs, **not operative terms** — do
    not anchor on it.
  - Unattended / always-on / multi-session interactive automation: **GREY** — Consumer Terms §3.7
    ban automated access *except where explicitly permitted*; the official CLI is the permitted
    vehicle, and Anthropic's own docs show cron-driven examples. Exposure is **throttling and
    future reclassification, not ToS breach.**
  - First-class design requirements (not appendix): back-off, session scheduling,
    human-interrupt hook, canary.
  - **GAVELED 2026-07-07 (G9): DEFER — attended-driven only; always-on posture revisited after
    smoke data + policy watch.**
- **Resilience — the canary is load-bearing, so it must diagnose itself honestly.** Two named
  volatiles: (1) the transcript format is officially "internal, changes between versions" — the
  content parse lives behind the adapter seam with a fail-loud canary; **per @Janus, the canary
  carries a bounded grace window** (ledger and transcript are two independent writers — a flush
  transient at the instant Stop lands must resolve by retry, not be misreported as vendor drift;
  a safety alarm that misattributes its own trigger corrupts the diagnostic the design leans on);
  (2) **interactive-mode reclassification to the metered pool is the obvious next vendor move** —
  the adapter must be able to swap the backend (`--resume` sid ownership, `/export`, or metered
  `-p --output-format json`) without touching the bus.

## Prior art

- **tmuxlet** (Rust; wraps interactive coding CLIs in tmux, normalized blocking interface,
  explicitly subscription-bucket) — ACTIVE 2026. Owns the PTY-wrap primitive. `BORROWED` `[v 2026-07-07]`
- **obra/claude-session-driver** v2.0.1 (2026-05) — turn completion via hooks + JSONL event
  streams. Independent convergence on the exact channel split; evidence the mechanism is right.
  `BORROWED` `[v 2026-07-07]`
- **primeline-ai/claude-tmux-orchestration** · **Claude Squad** — adjacent multi-agent harnesses
  (parallel workers, workspace supervision); neither is a bus/medium integration. `[v 2026-07-07]`
- **ACP (Agent Client Protocol)** — bridges IDE↔**SDK**, not the interactive binary; the active
  adapter wraps the SDK (the independent CLI bridge is archived). **Parked** as a possible future
  UI surface only. `[v 2026-07-07]`
- **The integration is the contribution** — `driven` mode inside a file-bus with a pulse medium,
  per-project conductor, compliance-gradient framing: `YOURS`. The niche "subscription-native,
  PTY-write + hook-read completion for multi-project orchestration" is unfilled as of 2026-07-07.
- Policy layer + prior-art detail: `session/research-interposition-fullrange/epoch.findings.2026-07-07.md`.
  Mechanism analysis: Color pass 2026-07-07 (summarized above; ranked failure modes in session log).

## Production

- **Seed: `shaped/seed.brick2.py`** (canonical runnable; travels with this card) — the adjusted
  brick1: inject at the pane; sid via SessionStart + launch token (empirically probes env
  passthrough, self-falls-back to `cwd`); completion via Stop event in a hooks ledger; content via
  nonce-correlated terminal assistant entry with torn-line discipline (parse only
  newline-terminated lines; JSON failure = not yet); **canary with bounded grace window**
  (transient vs structural, per Janus). Ships `install` (hooks fragment →
  `.claude/settings.local.json`), `ask`, `stop`, `hook`. Stdlib only.
- **Schema, verified on this box `[v 2026-07-07]`** (officially internal — hence the canary):
  message lines `{"parentUuid":…,"sessionId":…,"type":"user"|"assistant","message":{…,"stop_reason":"tool_use"|"end_turn"}}`;
  non-message line types `mode · permission-mode · file-history-snapshot · last-prompt · ai-title`
  (so "last line = reply" misfires — key by `stop_reason`); subagent turns in separate
  `<sid>/subagents/*.jsonl` (main transcript stays clean). **Naming trap:** transcript uses
  `sessionId` (camelCase); hook stdin uses `session_id`/`transcript_path` (snake_case).
- **Hook facts `[v 2026-07-07, docs]`:** SessionStart fires on `--resume`/`--continue` too
  (`source` field distinguishes); Stop fires only on normal completion (never on interrupt);
  project hooks live in `.claude/settings.json` / `.claude/settings.local.json`.
- **Honest gaps:** (1) custom-env passthrough to hooks is a documentation gap (MEDIUM) — the
  brick's first smoke run settles it empirically (`sid_via: token|cwd` reported); (2) transcript
  parse breaks on any release by vendor declaration — canary + adapter, and the `/export` or
  metered-JSON fallbacks are named; (3) **first-inject readiness** (Janus): a fresh Ink TUI may
  drop the first paste despite the boot settle — the smoke test targets exactly this before any
  round-trip is trusted; (4) throttle discipline for always-on conductors is unproven — that is
  the OPERATIONALIZE label, not a footnote.
- **Build status:** `BUILD-NOW` — single driven pane (brick2 runnable today, zero deps, stdlib).
  `OPERATIONALIZE` — multi-project conductor (scheduling, back-off, throttle bands need real data).

> **NOTES (majkee):**
> **Janus gate 2026-07-07: REVISE → applied same day** (canary grace window; first-inject smoke
> target named). **Ballot 2026-07-07 (see `session/gavels.2026-07-07.md`):** G7 Gate-3 co-signed +
> crossed to papers/ · G8 subai adoption accepted (delivery via subai `_mail` after majkee's
> reshape of `_bus/inbox` → standard mail pattern) · G9 always-on = DEFER, explicit — attended
> driven only for now. Flag: `terminal-onion-study.md` referenced but absent from `drafts/` —
> `part1.blueprint.md` fills its role.
