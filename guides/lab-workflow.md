# nabla-lab — lab workflow

*The operational handbook. Living document — chapters grow as the lab grows.*
*Entry point is still `AGENTS.md`; this guide expands each section into actionable depth.*
*If you just arrived: `session/pulse.md` → `AGENTS.md` → here.*

---

## How to use this guide

- **If you are lost:** Chapter 1 reorients you. Chapter 2 maps the full idea lifecycle.
- **If you need format help:** Chapter 3 has the instrument card anatomy.
- **If you are running a gate:** Chapter 4 has the research protocol for each validator.
- **If you need depth on a specific stage:** jump by section number (e.g. "see §2.3").

Chapters are numbered so other documents can cite them precisely. When the lab adds new
practice, a new chapter or section slots in without touching what exists.

---

## Chapter 1 — Orientation

### 1.1 What this place is

nabla-lab is a research supplier. It does not build; it investigates and shapes. The operator
brings rough ideas — voice notes, field observations, mathematical poetry — and the lab
transforms them into instrument cards, papers, and proof-of-concept seeds. These outputs
travel downstream to existing projects or, when large enough, earn their own project seat.

The lab's core value is honest assessment. A draft that is theatre — beautiful but unmoored
— is more valuable labeled honestly than dressed as a contribution.

### 1.2 Who works here

| Seat | Surface | Stage they operate in |
|------|---------|----------------------|
| majkee | — | Everywhere; brings ideas, gavels all canon |
| Nabla | claude.ai | Shaping (Stage 1) — mathematical grounding and prior-art framing |
| Symmetry | claude.ai | Shaping (Stage 1) — invariants layer, frame-testing |
| @Epoch | CLI global | Gate 1 (Stage 2) — live prior-art verification |
| @Color | CLI global | Gate 3 (Stage 2) — mathematical rigor, proofs, bounds |
| @Janus | CLI global | Gate 2 (Stage 2) — adversarial challenge, theatre check |

No project-scoped CLI agents exist yet. If you are a CLI agent landing here, you were
spawned for a specific task from the main session. Read your dispatch brief; consult this
guide for workflow context.

### 1.3 Where active work lives

- `session/pulse.md` — what is in flight right now (read this first, always)
- `drafts/` — rough ideas not yet shaped
- `shaped/` — cleared instrument cards and papers, ready to push downstream
- `papers/` — finalized; already delivered or ready to deliver
- `session/research/` — dated, cited research snapshots from @Epoch passes

If `drafts/` and `shaped/` are empty, the lab is between ideas. Nothing to do until the
operator brings the next rough input.

---

## Chapter 2 — The idea lifecycle

An idea moves through five stages. Each stage has a clear entry condition, a set of actors,
and a clear exit condition. Nothing skips a stage.

```
rough idea
    │
    ▼
[ drafts/ ]     ← Stage 0: arrival — capture without polish
    │
    ▼
  shaping       ← Stage 1: Nabla + Symmetry (claude.ai) — mathematical grounding
    │
    ▼
[ gates ]       ← Stage 2: three reality checks — @Epoch · @Janus · @Color
    │
    ▼
[ shaped/ ]     ← Stage 3: cleared instrument card — honest status label
    │
    ▼
downstream      ← Stage 4: push to sibling project · papers/ · or earn own project seat
```

### 2.1 Stage 0 — Arrival (→ `drafts/`)

**Entry:** The operator has a rough idea. It may be a voice note transcript, a poetic phrase,
a mathematical hunch, or a question. No requirement for polish.

**What happens:** Drop it into `drafts/` as a plain text file. Filename is descriptive but
informal: `drafts/<topic>.md`. No template required at this stage — capture is the only goal.

**Exit:** The idea is in `drafts/` and the operator is ready to shape it.

### 2.2 Stage 1 — Shaping (in claude.ai with Nabla + Symmetry)

**Entry:** A `drafts/` file exists.

**What happens:** The operator brings the draft into a claude.ai session with Nabla
(mathematical shaper) and/or Symmetry (invariants layer). Together they:

- Give the idea mathematical context and vocabulary
- Locate it within existing disciplines (spectral theory, control theory, category theory…)
- Identify what is borrowed, what is repurposed, what might be genuinely open
- Begin drafting an instrument card (see Chapter 3)

This stage lives in claude.ai, not in the CLI. The output is a draft instrument card,
written back to `drafts/<topic>.md` with growing structure.

**Exit:** The idea has a named mathematical home, a prior-art hypothesis, and a draft
instrument card. Ready for the three reality gates.

### 2.3 Stage 2 — The three reality gates

Before any draft moves from `drafts/` to `shaped/`, it must clear three gates.
Gates run in order; failing one parks the draft with an honest label.

---

**Gate 1 — Reinventing the wheel**

*Question:* Does this already exist, fully or partially?

*Who runs it:* @Epoch — live prior-art search against current literature. Brief must be
neutral; do not include the lab's existing hypothesis (Force 5: blind before grounded).

*Pass condition:* Either nothing equivalent exists, or the existing work is accurately cited
and the delta — new application, new integration, new framing — is clearly stated.

*Fail / park:* The idea is already done, fully, with no meaningful delta. Label `BORROWED`,
cite the source. The artifact may still proceed if the *application to this context* is the
original contribution — note it explicitly.

---

**Gate 2 — Theatre**

*Question:* Is this beautiful but unmoored? Is there a concrete engineering path?

*Who runs it:* @Janus — one adversarial pass. One verdict (proceed / revise / park), one
primary risk, one alternative. Read-only; does not write files.

*Pass condition:* A concrete mapping from the mathematical idea to a buildable engineering
artifact exists. "Buildable" means a prototype path is visible — not necessarily built yet,
but not blocked by principle.

*Fail / park:* No path from the idea to anything runnable. Label `THEORY`. May still live
in `shaped/` as an honest open problem worth returning to when capabilities shift.

---

**Gate 3 — Technical wall**

*Question:* The math is sound — but can we build it with current capabilities or capacity?

*Who runs it:* Majkee + @Color (for the mathematical side) + domain knowledge of current
tooling.

*Pass condition:* At least a minimal walking skeleton is constructible with available tools
and team. Known blockers are named and sized honestly.

*Fail / park:* The gap between the idea and current capability is too large to bridge now.
Label `OPERATIONALIZE` with a named blocker. Revisit when the blocker resolves.

---

**Status labels summary:**

| Label | Meaning |
|-------|---------|
| `BUILD-NOW` | All three gates passed; implementable today, no theory gaps |
| `OPERATIONALIZE` | Math sound; mapping to real signals or current tooling is unproven |
| `THEORY` | Needs formalization before code; no confirmed engineering path yet |
| `BORROWED` | Established elsewhere; the lab is applying, not originating |
| `REPURPOSED` | Exists in another field; being moved to a new domain |
| `OPEN` | Apparently unoccupied in the literature as of verification date |
| `YOURS` | The integration, application, or framing is the contribution |

### 2.4 Stage 3 — Clearing (→ `shaped/`)

**Entry:** The draft has passed all three gates (or been honestly labeled with its park
status and the reason it parks).

**What happens:** The instrument card is finalized to the output format (Chapter 3). The
file moves from `drafts/<topic>.md` to `shaped/<topic>.md`. The `NOTES (majkee)` slot is
left open for the operator to fill as the idea develops in practice.

**Exit:** A complete instrument card lives in `shaped/`. Available for downstream projects
to adopt.

### 2.5 Stage 4 — Downstream delivery (→ `papers/` or sibling project)

**Entry:** A shaped artifact is mature enough to act on.

Three paths:

**Path A — Push to an existing project.**
The artifact (or a derivative: a test, a proof-of-concept, a spec) is handed off to the
relevant sibling project. The sibling team picks it up. Record where it went and when in
the `NOTES (majkee)` slot of the `shaped/` file.

**Path B — Finalize as a paper.**
When an artifact is polished enough to stand alone — internally consistent, prior-art cited,
build status honest — move it to `papers/<topic>.md`. Papers are the lab's most finished
output form: ready to share externally if the lab goes public, or to seed a new project.

**Path C — Earn a project seat.**
When a draft has grown large enough to warrant its own repo, lighthouse, and agent team, it
graduates out of nabla-lab entirely and becomes a registered project (a row in
`registry/index.md`). This is a rare event; the standard path is A or B.

**Exit:** The idea lives in a sibling project, in `papers/`, or has become its own project.

---

## Chapter 3 — The instrument card format

Every shaped artifact follows this template. It is a map to build against, not an argument
to defend. Fill what you know; leave blank what you do not; never fake a status.

### 3.1 Card anatomy

```markdown
## <N> — <name>

**Concept.** <the math, terse — what it is, in its own terms>

**Mapping.** <how it applies to a concrete engineering problem — what it does in practice>

**Prior art.** <named research with citation> · STATUS · BUILD-READINESS · [v]/[t]

**Production.** <existing tools that implement this, or "none">

> **NOTES (majkee):**
> <operator fills this as the idea develops; findings, decisions, what was actually wired>
```

### 3.2 Labeling a card

A card carries two orthogonal labels (see full table in §2.3):

- **Maturity** (`BORROWED` / `REPURPOSED` / `OPEN` / `YOURS`) — who originated the idea
- **Build readiness** (`BUILD-NOW` / `OPERATIONALIZE` / `THEORY`) — distance from running code

Both labels appear in the **Prior art** line. A single instrument may carry multiple labels
if different parts have different status — state each claim separately.

### 3.3 Freshness tags

Every prior-art claim carries a freshness tag:

- `[v]` — verified against a source current to the date of shaping. Treat as reliable.
- `[t]` — training-era knowledge, not re-verified this session. Treat as a lead; send to
  @Epoch before leaning on it in downstream work.

**When an artifact travels to a downstream project:** re-verify any `[t]` claims before
building on them. The tag is the honest warning that the world may have moved.

---

## Chapter 4 — Research protocol

### 4.1 Prior-art check (@Epoch)

@Epoch is the lab's live-fetch researcher. It recalibrates to today's date before every run,
treats all version strings and citations as potentially stale, and returns source + date +
confidence level.

**How to invoke:** from the main CLI session, spawn @Epoch with a neutral prior-art question.
The brief must be blind — do not include the lab's existing hypothesis; let @Epoch find
independently, then compare. (Force 5: blind before grounded.)

**Output:** a dated, cited finding. Place the raw finding in
`session/research/<topic>.<date>.md` before folding conclusions into the instrument card.

### 4.2 Mathematical verification (@Color)

@Color is the lab's math co-brain — proofs, complexity bounds, formal-language semantics,
vector/tensor algebra.

**Invoke when:** a claim involves a mathematical assertion that needs verification before the
card carries `[v]`. @Color drafts a proof or counterexample; majkee gavels whether it holds.

**@Color is read-only.** It does not write files. It returns a reasoning artifact; the lab
records what was verified in the instrument card's Prior art line and in NOTES.

### 4.3 Adversarial gate (@Janus)

@Janus runs twice per idea:
1. **Gate 2 check** — "Is there an engineering path, or is this theatre?"
2. **Pre-papers check** — before any artifact crosses from `shaped/` to `papers/`

**How to brief @Janus:** provide the instrument card and the specific question. The brief
must not carry the lab's preferred answer. One verdict (proceed / revise / park), one
primary risk, one alternative — no more.

**@Janus is read-only.** It does not write files. Its verdict goes into the NOTES slot.

---

*— Chapters to come —*

*The slots below are reserved. A chapter earns its content when the lab's practice generates
the material. Add a new chapter by appending after this block — do not renumber existing
chapters.*

- **Chapter 5** — Multi-instrument synthesis (when two or more cards combine into a unified paper)
- **Chapter 6** — Seed-to-project graduation (when an idea earns its own project seat — the handoff protocol)
- **Chapter 7** — External publication (when the lab goes public — what that means, how to prepare an artifact)
- **Chapter 8** — Voice-note ingestion (if a formal protocol for voice → `drafts/` emerges)
- **Chapter 9** — *(open slot)*

---

*End of current content. This is a living guide — extend freely; the chapter structure is the contract.*
