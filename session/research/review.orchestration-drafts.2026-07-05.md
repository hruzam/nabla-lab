# Review — orchestration drafts (state, findings, pending gavels)

`date: 2026-07-05 · author: CLI agent (draft — nothing here is canon until majkee gavels)`
`scope: drafts/three-spines-orchestration.md · drafts/orchestration-atlas.md · drafts/orchestration-atlas-v2.md`
`purpose: orient the operator — what stage the work is at, what was found on revision, what decisions are pending`

---

## 1. Where the work actually stands (lifecycle position)

Per `guides/lab-workflow.md` Chapter 2, all three documents sit at the **end of Stage 1
(shaping)**. They were shaped with Nabla on 2026-06-25 and committed 2026-07-02
("start project"). They have **not** entered Stage 2 (the three gates):

| Gate | Runner | Status |
|------|--------|--------|
| Gate 1 — reinventing the wheel | @Epoch (blind brief) | **not run** — no snapshot in `session/research/` |
| Gate 2 — theatre | @Janus | **not run** — no verdict recorded anywhere |
| Gate 3 — technical wall | majkee + @Color | **not run** |

`shaped/` and `papers/` are empty. That is correct and honest: nothing has cleared.

**Important nuance:** the drafts carry `[v]` freshness tags, but those were self-asserted
during the Nabla shaping session. Chapter 4.1 requires an *independent, blind* @Epoch pass
(Force 5: blind before grounded) before the tags count for promotion. So for lifecycle
purposes, every `[v]` in the drafts is really a well-researched `[t]` until Gate 1 runs.

## 2. Findings from the revision

### 2.1 The v2 file is not a v2

`orchestration-atlas.md` and `orchestration-atlas-v2.md` are **byte-for-byte identical**
(verified with `diff`). No revision exists yet — the v2 file is a duplicate. If a revised
atlas was expected on this branch, it was never made or never committed.

### 2.2 The two real documents have diverged in scope

- The **paper** (three-spines) argues **three** spines and a **3-term** health scalar:
  `f(curl, RHP-pole, ρ)`.
- The **atlas** has since grown **Spine IV — Coherence/Identity** (I.9 sheaf consistency,
  I.10 free energy/Markov blanket, I.11 operads, I.12 optimal stopping) and a **4-term**
  health scalar adding the `cohomology_obstruction`.

The atlas explicitly says Spine IV was "added this session." The paper predates or ignores
it. The two flagship artifacts currently disagree about the architecture's shape. This is
the single largest content decision pending (gavel G3 below).

### 2.3 Formatting defect in the atlas

The atlas's "How to use" section promises **Part III — spine synthesis**, but the heading
is missing: after I.12 (line ~280) the synthesis text starts bare ("The eight instruments
collapse into three spines…") with no `# Part III` header. Parts IV/V/VI are fine. One-line
fix, but it breaks the document's own navigation contract.

### 2.4 Session state is stale

`session/plan.md` and `session/pulse.md` (dated 2026-06-27) still say "no drafts in flight /
bring first idea into drafts/" — while three drafts have been committed since. Plan step 1
("erase `to-show-atlas/`") refers to a directory that does not exist in this repo — either
already done or belonging to another checkout. Anyone following the read order
(pulse → AGENTS → drafts) gets told the lab is idle when it is not.

### 2.5 Claims that most need Gate 1 (blind @Epoch verification)

Ordered by how much weight they carry:

1. **Material derivative as drift decomposition** — claimed "apparently unoccupied."
   This is one of two headline novelty claims; if occupied, the paper's §9 table changes.
2. **n-body → central-bus justification** — claimed "apparently unoccupied," and it is the
   architectural keystone (justifies the bus itself). Also internally the weakest: the
   gravity-model lineage behind it is tagged `[t]` in the atlas (I.4).
3. **Three-spine unification / single health scalar** — claimed contribution; verify no
   unified curl+pole+ρ (±cohomology) readout has appeared since mid-2026.
4. All `[t]`-tagged cards: Hopfield≡attention (I.7), Belkin–Niyogi (II.4), sparsification
   (II.5), gravity-model lineage (I.4), optimal-stopping LLM line (I.12).
5. The 2026-era arXiv identifiers cited throughout (2512.10350, 2601.04170, 2601.05693,
   2603.10384, 2605.11204, 2506.05675…) — the drafts themselves instruct re-verification
   before formal use; none has been independently re-verified in this repo.

### 2.6 What reads as sound (no action needed, for orientation only)

- The novelty boundary (§9 of the paper; Part IV of the atlas) is honestly drawn —
  "invented mathematics: none; contribution is integration" is the right posture and will
  survive an adversarial pass much better than overclaiming.
- The A2-vs-spectrum collision and its two-path resolution (runtime Chebyshev diffusion /
  batch recompute) is the strongest piece of genuine engineering reasoning in both docs.
- The open-problems list (§10) already anticipates the likely @Janus risks (curl
  separability, ζ=1 under coarse sampling, capacity learning cost, over-compression of the
  health scalar). Good raw material for the Gate 2 brief.

## 3. Pending gavels (decision ledger for majkee)

Nothing below is decided. Each row is a proposal awaiting the gavel; recommendations are
the reviewing agent's opinion only.

| # | Decision | Options | Agent recommendation |
|---|----------|---------|----------------------|
| G1 | Fate of `orchestration-atlas-v2.md` | (a) delete duplicate · (b) make it the real revision target | (a) delete — the atlas is a *living* doc by design; versioning by copy contradicts append-only discipline. Git history is the version trail. |
| G2 | Relationship of paper ↔ atlas | (a) atlas = living master, paper = dated positioning snapshot · (b) keep both in lockstep | (a) — matches each doc's own self-description; lockstep costs double maintenance forever |
| G3 | Does Spine IV enter the paper? | (a) paper stays three spines, Spine IV matures in atlas · (b) rewrite paper as four spines now | (a) for now — Spine IV is `OPERATIONALIZE→THEORY` (restriction maps undefined); pulling it into the positioning paper before Gate 1 weakens the paper's honesty posture |
| G4 | Health scalar: 3-term or 4-term | follows G3 | follows G3 — if (a), atlas notes the 4th term as candidate extension, paper unchanged |
| G5 | **Fork pick (atlas Part V — the empty `PICK (majkee)` slot)** | 1 Choquet gate (BUILD-NOW) · 2 curl detector (OPERATIONALIZE) · 3 n-body proof (THEORY) · 4 damping tuner (OPERATIONALIZE) | Fork 1 (Choquet) for a working artifact fastest — zero theory gaps by the lab's own labels. Fork 3 next if the priority is defending the architecture rather than shipping a component. |
| G6 | Commission Gate 1 | run blind @Epoch pass over §2.5 list; snapshot into `session/research/` | yes — blocking; nothing can move to `shaped/` without it |
| G7 | Commission Gate 2 | @Janus theatre pass (scope: paper alone, or paper + chosen fork) | after G5, brief @Janus on the chosen fork + the paper's two unoccupied claims |
| G8 | Session-state refresh | update `pulse.md` + `plan.md` to reflect three drafts in flight; fix missing `# Part III` header | yes — mechanical, but per doctrine the agent proposes and majkee gavels |
| G9 | First `flag.md` entries | lock outcomes of G1–G5 as decisions #1…#n | once gaveled — the flag table is still empty and these are exactly the kind of locks it exists for |

## 4. What is *not* on majkee (for context)

- Gate 1 execution — @Epoch's job once commissioned (G6).
- Gate 2 execution — @Janus's job once commissioned (G7).
- The mechanical fixes in G8 — any agent can apply them after the gavel.

What only majkee can do: gavel G1–G5, fill the `NOTES (majkee)` slots as things get built,
and pick the fork (G5) — the whole pipeline is currently waiting on that one pick.

---

*End of review. Append corrections below; do not edit above this line.*
