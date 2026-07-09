# nabla-lab — read first (the lighthouse)

`tier: project · host: office · status: building`
`what this is: a mathematical-poetic ideation laboratory — shapes rough ideas into`
`grounded research artifacts and supplies them downstream to sibling projects.`
`contract: PROJECT.yaml · primary shapers: Nabla + Symmetry (claude.ai)`

## What nabla-lab is

A research supplier. Rough ideas arrive from the operator — voice notes, field observations,
mathematical poetry — and are shaped by Nabla + Symmetry (claude.ai personas) into
mathematically-grounded instrument cards, papers, and seeds. Each draft passes three reality
gates before it clears. Cleared artifacts push downstream to existing projects or, when large
enough, earn their own project seat.

The lab does not own implementations.

---

## The shaping team

| Seat | Surface | Role |
|------|---------|------|
| majkee | — | Brings the rough idea; gavels all canon |
| @Flight | CLI global | Executive architect — project direction, structural improvements |
| @Oraculum | CLI global | Lead scientist · process orchestrator · architecture |
| Nabla | claude.ai | Mathematical shaper — context, grounding, prior-art framing |
| Symmetry | claude.ai | Doctrine / invariants layer — tests whether the idea holds across frames |
| @Epoch | CLI global | Reality check — prior-art search, literature re-verification |
| @Color | CLI global | Mathematical rigor — proofs, bounds, formal-language correctness |
| @Janus | CLI global | Adversarial gate — "is it theatre?" — one verdict, one risk |
| @atlas-ui | CLI global | Primitive builder — harness architect, project scaffolding |

No project-scoped CLI agents. Globals are spawned per need from the main session.

## Three reality gates

Run on every draft before it moves from `drafts/` to `shaped/`:

1. **Reinventing the wheel** — does this already exist, fully or partially?
2. **Theatre** — beautiful but unmoored? No engineering path?
3. **Technical wall** — math is sound but not buildable with current capabilities or capacity?

A draft clears all three or parks with an honest status label (`THEORY` · `OPERATIONALIZE`).

## Folder discipline

    nabla-lab/
    ├── AGENTS.md              ← you are here
    ├── CLAUDE.md              ← @AGENTS.md redirect (gitignored)
    ├── PROJECT.yaml           ← contract
    ├── session/
    │   ├── pulse.md           ← volatile state (read this first)
    │   ├── plan.md            ← what we are building toward
    │   ├── flag.md            ← locked decisions
    │   ├── research.journal.md   ← backtracking
    │   └── research-<slug>/   ← dated, cited research snapshots
    ├── guides/                ← operational handbook (depth on every workflow step)
    │   └── lab-workflow.md    ← idea lifecycle · gates · output format · research protocol
    ├── drafts/                ← raw incoming (voice notes, poetry, rough sketches)
    ├── shaped/                ← cleared artifacts (instrument cards, papers, seeds)
    ├── papers/                ← finalized; ready to push downstream
    └── _mail/                 ← inter-agent mail bus (ask-first; gitignored except README + .gitignore)

## Output format (instrument card)

Each shaped artifact carries: **Concept** · **Mapping** · **Prior art** (with status +
build-readiness + freshness tag) · **Production** · **NOTES (majkee)**. Living document —
a map to build against, not an argument to defend.
→ Full format and status labels: `guides/lab-workflow.md` Chapter 3.

## Decisions (inline — promote to flag.md when they accrue)

None yet.

## Conventions

- **Canon is @majkee's gavel** (temple 0002). Agents draft; he approves; then it locks.
- **Honesty over show.** Kill your own darlings. If a draft is theatre, say so first.
- **Verify before build.** @Epoch prior-art check before any artifact is treated as original.
- **Challenge before lock.** @Janus pass before any draft crosses from `shaped/` to `papers/`.
- **Living documents.** Shaped artifacts are maps to extend, not arguments to defend.
- **Cross-brand triangulation.** Full-range blind triangulation requires at least one leg from outside the Claude family. Staying within one model brand constrains the angle of sight. Source one leg from a different brand for any genuine cross-check. Current roster: `reposoma/triangle.md`.

## Standing disciplines

- **Token economy / ask-first** — surface what exists before reading large files or inbox items; ask before loading. Full protocol: `/home/hruzam/reposoma/raw.canon/canon.mail-protocol.md`.
- **Context discipline** — read thin first; load depth only when the task demands it. Inbox items: list filenames first, ask before reading content.

## FYI untracked personal majkee space

This is ***NOT*** canonical, majkee need some folder for his personal notes and temporary process files, human stuff. Acessible for others but not in process scope.
- `_monkeynet/` is derivated neologism from 'monkey' and 'cabinet'. 

## Read order

1. `session/pulse.md` — volatile state (thin, always first) →
2. this file (`AGENTS.md`) →
3. `PROJECT.yaml` →
4. active draft in `drafts/` or `shaped/` →
5. `guides/lab-workflow.md` — if you need depth on any workflow step or the full gate protocol
