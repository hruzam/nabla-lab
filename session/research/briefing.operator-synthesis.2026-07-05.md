# Operator briefing — synthesis of the orchestration drafts + gavel context

`date: 2026-07-05 · author: CLI agent (draft — nothing here is canon until majkee gavels)`
`scope: drafts/three-spines-orchestration.md · drafts/orchestration-atlas.md · session/research/review.orchestration-drafts.2026-07-05.md`
`purpose: give the operator the full picture in plain language — what the documents say, what is expected of him and why, how each pending decision connects to the existing projects — and a ready-to-sign gavel sheet`

---

## 1. What you have, in plain language

Two real documents (the third file, `orchestration-atlas-v2.md`, is a byte-identical
duplicate — see G1). Both were shaped with Nabla on 2026-06-25 from your raw ideas; both
describe the same body of thought from different angles.

### 1.1 The one idea underneath both

Your orchestration bus — the multiplexer-owned PTY loop with JSONL turn logs and
append-only files that you already run — is usually engineered as plumbing: queues,
routers, retries. The drafts argue that the failure modes you actually care about
(drift, context pollution, circular reasoning, consensus collapse) are better read as the
behaviour of **one mathematical object**:

> an energy landscape over semantic space, a feedback-controlled trajectory flowing
> through it, and a discrete evidence-aggregation rule deciding the transitions.

Every instrument you brought as raw intuition (spectral analysis, tensors, complex
analysis, gravity, nabla, RLC circuits, associative recall, "3-of-5 but which 3") turns
out to be a view of that one object. That collapse — not any single instrument — is the
claimed contribution.

### 1.2 The four spines (what each one gives you)

- **Spine I — the landscape.** A potential field `Φ` over the semantic space of agent
  turns. Its differential operators are diagnostics with coordinates: gradient = steering
  direction, divergence = *where* pollution is being spawned, curl = circular reasoning
  made measurable, and the material derivative `D/Dt = ∂/∂t + (v·∇)` splits drift into
  "the agent genuinely changed its mind" vs "the agent got swept along by the
  conversation's current." Retrieval is heat-kernel diffusion on the association graph
  over your JSONL lines (the HippoRAG mechanism, repurposed from document QA to bus
  orchestration).
- **Spine II — the trajectory.** The orchestrator's feedback loop as an RLC circuit /
  second-order control system. Tuning target: critical damping (`ζ = 1`). Stability read
  off pole locations in the complex plane; any right-half-plane pole = runaway-drift
  alarm. The sharpest claim: many mutually-attracting agents form an n-body problem
  (chaotic by nature), and only a dominant central mass tames it — **the central bus is
  mathematically justified, not just convenient.**
- **Spine III — the gate.** Associative recall (Hopfield basins = Spine I's gravity wells
  at small scale), cascade control via the branching ratio `ρ` (ρ > 1 = context
  pollution), and a consensus gate built on the Choquet integral over a fuzzy measure —
  the exact mathematical object for "pass at 3-of-5, but *which* 3 matters."
- **Spine IV — coherence/identity (atlas only).** Added in a later session: sheaf
  consistency (does agents' disagreement glue into one world or is it a formal
  obstruction), free energy / Markov blankets (the boundary that keeps the system one
  system — the formal version of your files-vs-streams axiom), operads (are the wired
  daemons well-formed before runtime), optimal stopping (when is the bus *done*). Least
  mature spine: the restriction maps are undefined, so it is honest `THEORY`/`OPERATIONALIZE`.

Everything composes into one health scalar for the whole bus: keep the flow curl-free,
the loop critically damped, the branching ratio below one — and (atlas version) the
consensus obstruction at zero. That sentence is the entire control objective.

### 1.3 How the two documents differ

| | Paper (three-spines) | Atlas |
|---|---|---|
| Role (self-declared) | positioning snapshot — an argument, dated | living reference — a map to build against, with open `NOTES (majkee)` slots |
| Spines | three | four (Spine IV added later) |
| Health scalar | 3-term | 4-term (+ cohomology obstruction) |
| Honesty posture | §9 novelty boundary: "invented mathematics: none; contribution is integration" | Part IV master table, same posture |

The divergence is the largest pending content decision (G2–G4): the two flagship
artifacts currently disagree about the architecture's shape.

### 1.4 What is genuinely yours (per the drafts' own novelty boundary)

Most parts are `BORROWED` and say so — which is a strength, since each component is
battle-tested and the risk lives in the seams. Four things are claimed as open or yours,
**all still unverified** (see §2):

1. Material derivative as drift decomposition (apparently unoccupied).
2. The n-body → central-bus justification (apparently unoccupied, and internally the
   weakest — its gravity-model lineage is only training-era `[t]`).
3. The unification into a single health scalar.
4. The application target itself: a file-backed, append-only *agent bus* rather than
   document QA.

---

## 2. Where the work stands (and why nothing has "cleared")

Per `guides/lab-workflow.md`, all drafts sit at the **end of Stage 1 (shaping)**. None of
the three reality gates has run:

- **Gate 1 (reinventing the wheel / @Epoch)** — not run. Consequence: every `[v]`
  freshness tag in the drafts was self-asserted during the Nabla session, so for
  promotion purposes it is really a well-researched `[t]`. The 2026 arXiv identifiers
  cited throughout have not been independently re-verified in this repo.
- **Gate 2 (theatre / @Janus)** — not run. The paper's own §10 open-problems list already
  anticipates the likely risks (curl separability on noisy embeddings, ζ=1 under coarse
  sampling, exponential capacity learning, over-compressed health scalar) — good raw
  material for the @Janus brief.
- **Gate 3 (technical wall / majkee + @Color)** — not run.

`shaped/` and `papers/` are empty, and that is correct and honest: nothing has cleared.
Also stale: `session/pulse.md` and `session/plan.md` (dated 2026-06-27) still say "no
drafts in flight," and the atlas is missing its promised `# Part III` heading (G8).

---

## 3. What is expected from you, and why

The lab's own doctrine (AGENTS.md conventions, temple 0002) is: **agents draft, majkee
gavels.** The review deliberately stopped at proposals; nothing in it is a decision. The
whole pipeline is now waiting on nine gavels, and really on one of them — **G5, the fork
pick** — because every downstream step (which gate to brief, what to build, what enters
`shaped/` first) depends on which fork you choose.

Equally important, what is **not** on you:

- Executing Gate 1 — @Epoch's job once you commission it (G6).
- Executing Gate 2 — @Janus's job once you commission it (G7).
- The mechanical fixes (duplicate file, missing header, stale session state) — any agent
  applies them after your gavel (G1, G8).

Your part is the picks and the locks. Below, each decision with its full context.

### G1 — Fate of `orchestration-atlas-v2.md`

**What it is.** The file is byte-identical to the atlas; no revision ever existed.
**Why it matters.** The atlas is a *living document* by its own design; versioning it by
copy contradicts the lab's append-only discipline — git history is the version trail.
Keeping a phantom "v2" also confuses every future agent that lands in `drafts/`.
**Options.** (a) delete the duplicate · (b) declare it the target for a real revision.
**Downstream link.** Pure hygiene; no project impact either way. (a) is the clean pick
unless you privately intended a fork of the atlas.

### G2 — Relationship of paper ↔ atlas

**What it is.** Do the two artifacts stay in lockstep, or does the atlas become the
living master while the paper stays a dated positioning snapshot?
**Why it matters.** Lockstep costs double maintenance *forever* — every new instrument
card forces a paper rewrite. The documents already self-describe as snapshot vs map.
**Downstream link.** Downstream projects should build against the **atlas** (it has the
`NOTES (majkee)` slots and production-tool columns); the paper is what you would show
externally or use to seed a new project (lifecycle Path B/C). Deciding this now settles
which document sibling projects treat as authoritative.

### G3 — Does Spine IV enter the paper?

**What it is.** The atlas grew a fourth spine after the paper was written. Rewrite the
paper as four spines now, or let Spine IV mature in the atlas while the paper stays three?
**Why it matters.** Spine IV is honestly labeled `OPERATIONALIZE→THEORY` — its restriction
maps (how each agent's internal frame projects into a shared comparison space) are
undefined. Pulling an unoperationalized spine into the *positioning* paper before Gate 1
weakens exactly the thing that makes the paper defensible: its honesty posture. The paper
survives adversarial review because it overclaims nothing.
**Downstream link.** If the paper someday travels (external publication, project seed),
you want its weakest claim to be strong. Spine IV can join in a later revision once
someone defines the restriction maps — which is itself a candidate future fork.

### G4 — Health scalar: 3-term or 4-term

Follows G3 mechanically. If the paper stays three spines, the atlas simply notes the
cohomology term as a candidate extension and the paper keeps `f(curl, RHP-pole, ρ)`.
No independent decision needed unless you split from your G3 answer.

### G5 — The fork pick (the one blocking everything)

**What it is.** Atlas Part V lists four candidates for the next deep-dive
(full derivation + file/stream boundary + minimal walking skeleton). The `PICK (majkee)`
slot is empty. This is the single decision the pipeline waits on.

**The four forks, mapped to what they deliver to your existing projects:**

| Fork | Readiness | What lands downstream |
|---|---|---|
| 1. Choquet consensus gate | `BUILD-NOW` — zero theory gaps | A working consensus component for the bus: the "which 3 of 5" gate. Fastest to a real artifact a sibling project can adopt (lifecycle Path A). |
| 2. Curl loop-detector | `OPERATIONALIZE` | The flagship diagnostic — circular reasoning as a measurable quantity. Highest distinctiveness, but needs an empirical separability test against existing classifier-based loop detectors first. |
| 3. n-body → central-bus proof | `THEORY` | No code — a formalized proposition that *justifies your whole bus architecture*. This is the foundation argument under everything you already run. |
| 4. Critical-damping tuner | `OPERATIONALIZE` | A tuning improvement to the orchestrator loop you already operate (couples to your turn-acknowledgment cycle). Risk: ζ=1 may be unreachable under coarse, irregular sampling. |

**How to think about it.** The pick is really a strategy question: *ship a component*
(Fork 1), *sharpen the identity* (Fork 2), *defend the architecture* (Fork 3), or
*improve the running system* (Fork 4). The review recommends Fork 1 first — it is the
only `BUILD-NOW` item, so it produces the lab's first cleared artifact and exercises the
whole drafts→gates→shaped pipeline end-to-end on the lowest-risk piece. Fork 3 is the
natural second: it is pure reasoning (cheap to commission, @Color-shaped work) and it
converts "apparently unoccupied claim #2" into something defensible. Nothing stops you
from gaveling a sequence (1 now, 3 next) rather than a single pick.

### G6 — Commission Gate 1 (blind @Epoch pass)

**What it is.** Authorize the prior-art verification run over the claims listed in the
review §2.5 — the two "apparently unoccupied" claims first (material derivative, n-body
argument), then the unification claim, then the `[t]`-tagged cards and the 2026 arXiv IDs.
**Why blind.** Per your own protocol (Force 5), the @Epoch brief must NOT contain the
drafts' hypotheses — @Epoch searches independently, then results are compared. That is
why this document deliberately performs no verification itself.
**Why blocking.** Nothing can move to `shaped/` without it, and the paper's §9 novelty
table may change if either headline claim turns out occupied.

### G7 — Commission Gate 2 (@Janus theatre pass)

**What it is.** Authorize the adversarial pass; the only scoping question is whether
@Janus sees the paper alone or the paper plus your chosen fork. Sensibly sequenced after
G5 (so the brief covers the fork) and after G6 results land.

### G8 — Session-state refresh (mechanical)

Update `pulse.md`/`plan.md` to reflect three drafts in flight, and restore the missing
`# Part III` header in the atlas. One gavel, minutes of agent work, and every future
agent landing in the repo stops being told the lab is idle.

### G9 — First `flag.md` entries

Once G1–G5 are gaveled, lock the outcomes as decisions #1…#n in the flag table (currently
empty). This is exactly what the table exists for; it turns this round of picks into
durable canon that no future session can silently re-litigate.

---

## 4. The wider frame: how this feeds your existing projects

The lab is a **supplier, not an implementer** (PROJECT.yaml, flag invariants). Everything
above ultimately exits through one of three lifecycle paths (`guides/lab-workflow.md` §2.5):

- **Path A — push to a sibling project.** The realistic near-term path. The drafts are
  not abstract: the "substrate" they formalize *is* your existing bus (JSONL turn logs,
  append-only files, PTY streams, central orchestrator). A cleared Fork-1 Choquet gate or
  Fork-4 damping tuner is a component the orchestration project adopts directly; a
  cleared Fork-3 proposition becomes that project's architectural justification document.
- **Path B — finalize as a paper.** The three-spines document is explicitly built for
  this: novelty boundary drawn, references cited, open problems named. It needs Gates 1–2
  before it can honestly cross to `papers/`.
- **Path C — earn a project seat.** If the RAG engine (atlas Part II — the "orchestration
  brain" built on diffusion retrieval over the file-backed graph) grows past a component,
  it is the natural candidate to graduate into its own repo. Rare path; not a decision
  for today, but worth knowing it is where Part II points.

So the honest answer to "what is expected from me" is: **five content gavels (G1–G5), two
commissions (G6–G7), two housekeeping locks (G8–G9)** — and of these, G5 is the one that
unblocks the pipeline, G6 is the one that protects you from building on an occupied claim.

---

## 5. Gavel sheet (ready to sign)

Recommendations second the review's except where noted; the `GAVEL` column is yours.

| # | Decision | Recommended pick | One-line rationale | GAVEL (majkee) |
|---|----------|------------------|--------------------|----------------|
| G1 | v2 duplicate | (a) delete | No revision exists; git history is the version trail | |
| G2 | paper ↔ atlas | (a) atlas = living master, paper = dated snapshot | Matches both docs' self-description; lockstep = double maintenance forever | |
| G3 | Spine IV into paper? | (a) not yet — matures in atlas | Restriction maps undefined; protects the paper's honesty posture pre-Gate-1 | |
| G4 | health scalar | follows G3 → 3-term in paper, 4th term noted in atlas as candidate | Mechanical consequence of G3 | |
| G5 | fork pick | Fork 1 (Choquet gate) now; Fork 3 (n-body proof) queued next | 1 is the only BUILD-NOW → first cleared artifact + full pipeline exercise; 3 is cheap pure reasoning that defends the architecture *(sequence is this briefing's addition — the review picked 1 xor 3)* | |
| G6 | commission Gate 1 | yes — blind @Epoch over review §2.5 list, snapshot into `session/research/` | Blocking for any promotion to `shaped/`; headline claims unverified | |
| G7 | commission Gate 2 | yes, after G5+G6 — brief @Janus on chosen fork + the two unoccupied claims | Sequencing lets one brief cover both | |
| G8 | session-state refresh | yes — update pulse/plan, fix `# Part III` header | Mechanical; ends the "lab is idle" misdirection | |
| G9 | flag.md entries | yes — lock G1–G5 outcomes once gaveled | Turns this round into durable canon | |

## 6. Suggested sequence once gaveled

1. Gavel G1–G5 (fill the sheet above, or reply with picks).
2. Any agent applies G8 + G1 mechanically and writes the G9 locks into `flag.md`.
3. Commission @Epoch (G6) — blind brief, findings snapshot to `session/research/`.
4. Fold Gate-1 results into the drafts' prior-art lines; adjust §9 table if a claim fell.
5. Start the chosen fork; brief @Janus (G7) on fork + paper when the fork has shape.
6. First artifact that clears all three gates moves to `shaped/` — the lab's first
   completed lifecycle.

---

*End of briefing. Append corrections below; do not edit above this line.*
