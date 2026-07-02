# Atlas №2 — Cross-measure of the blind fan-out (gate 1)

`date: 2026-07-02 · cross-measurer: Oraculum (one researcher sees all forks; legs were blind to each other)`
`substrate: drafts/atlas2-research-substrate.md · protocol: flag.md lock 6`
`legs: leg-epoch (depth, online) · leg-color (offline math authority) · leg-gemini (bluebottle cross-check) · leg-gemini-direct (§0 pass — retry in flight at time of writing)`
`status: verdicts RECOMMENDED, pending majkee gavel (gate 1)`

---

## 0. Leg inventory and standing

| Leg | Nature | Standing |
|---|---|---|
| Epoch | Full §0 research pass, live-verified 2024–2026 sources | **Complete, high quality** — 36 tool calls, dated citations throughout |
| Color | Derivation-only verification of all "mathematically certain" claims + §5 typing attack | **Complete, high quality** — self-verified derivations |
| Gemini (bluebottle) | Cross-vendor cold read — 8.7 s flash pass | **Degraded**: script's baked-in agent prompt produced a cross-check (3 agreements / 2 additions / 1 overstated), not a §0 pass. Kept as heterogeneity signal. |
| Gemini (direct CLI) | §0-conformant retry | **FINAL: parked** — sustained 503s on flash, silent exit on flash-lite; both attempts logged in the leg file. Heterogeneity leg stands on the bluebottle artifact alone — flagged per lock 6. |

Tool note for majkee: `bluebottle.zsh` itself ran clean (REST path, exit 0, jq parse OK, reproducible). Finding: as configured it is a **cross-check instrument, not a research-pass instrument** — the system prompt in `~/.gemini/agents/bluebottle.md` fixes the output genre regardless of the task in the input file. Not a bug; a design fact to know when reaching for it.

---

## 1. Convergences (independent legs agreeing — the strongest signal in the protocol)

**C1 — Fork 2's kill test is passed by the literature.** Epoch: *"A Generalized Kuramoto Model for Opinion Dynamics on the Unit Sphere," Automatica, Oct 2024 (DOI:10.1016/j.automatica.2024.111957)* — an interaction kernel on S^n with stability analysis (consensus, polarization); reduces to standard Kuramoto on S¹; Lohe/Sarlette–Sepulchre lineage confirmed alive. Color, blind to this, derived that the fork's "path is information" claim is empty *unless* a law selects the path (geodesic IVP is unique; only the boundary problem is degenerate). The two legs interlock exactly: **the law Color demands is the law Epoch found.** Bluebottle, third-blind, flagged path-centrality as overstated *"without a governing law"* — same joint.

**C2 — The general Dempster–Shafer weld is broken, twice independently.** Epoch (Refutation 2, R3.2): no literature bridges non-additive DS structure to Fisher–Rao; the substrate's weld is asserted, not derived. Color (Item 7): the precise reason — a BBA is a point on the simplex over 2^Θ∖∅ (exponential-dimensional), NOT the base simplex except in the Bayesian case; the √p map transports the mass *vector* but is blind to Dempster's rule and the subset lattice. §4.6's "direct weld to Spine III" is dead as stated.

**C3 — The null hypothesis (§6.3) is alive and must be honored.** Epoch: weakened (Steck et al. 2024 on cosine arbitrariness; angular barycenters beating linear summation, arXiv:2602.14039) but not refuted for the specific operations Atlas №2 adds. Color: the Fork 1 keep-test as written has a **trivial-pass loophole** — the antipodal map is fully cosine-reducible (sign flip). Joint consequence: Fork 1 survival requires an operation **provably not a monotone function of pairwise cosines**.

**C4 — And the candidate operation already has both a name and evidence.** Color names the witness class: Fréchet/Karcher mean on the sphere (not recoverable from pairwise cosines). Epoch independently found its production sibling: Spherical Barycentric Aggregation for MoE embedding models (arXiv:2602.14039, Feb 2026) with empirical wins over linear summation. **This weld is the concrete build path for Fork 1.**

**C5 — Hairy-ball stagnation is parity-dependent — both legs, independently.** Color: forced stagnation iff the stance sphere is even-dimensional (χ(S^n)=2 for n even, 0 for n odd); with Fork 3's own bookkeeping (N stances ↔ S^{N−2}), the guarantee alternates with N (on for N=4,6; off for N=3,5). Epoch: same S³ exception noted from the literature side; no opinion-dynamics paper uses the theorem at all — the interpretation is unoccupied, but must carry the parity tag.

**C6 — Stance extraction (§6.1) is the hardest unresolved prerequisite — all three legs.** Epoch (Attack 1): LLM stances are prompt-sensitive and consensus-collapse dynamics (NAACL 2024 Findings) may destroy the signal before geometry sees it; nothing found weakens this attack. Color: interpretability of intermediates is a precondition for the path-information claim. Bluebottle: implicit in its "overstated" flag. **The geometry computes garbage elegantly if this fails — top of the risk register for any card built on №2.**

---

## 2. Divergences and rulings

**D1 — §5 grading: "well-formed research program" (Epoch) vs "REFUTED as typed" (Color).** Not a contradiction — different attack surfaces. Color's is structurally prior: *"the sheaf's comparison stalks ARE these spheres; the restriction maps ARE rotations"* is a type error (cellular-sheaf stalks are vector spaces; a sphere is not). The repair — stalks ℝ^{n+1}, restriction maps orthogonal, spheres as invariant level sets — narrows the object to an **O(n)-synchronization / discrete-connection sheaf**, whose linear machinery (Laplacian, H⁰) does not directly see the angular logic. Epoch's four prerequisites (stance extraction; cross-vendor alignment; text→coupling identification; DS weld) then apply to the *repaired* version. **Ruling: §5 is REFUTED as written and survives only as a typed research program**: vertex-stalks = per-agent stance spaces, edge-stalks = comparison spaces, restriction maps ∈ O(n) — with Color's state-sphere/comparison-sphere distinction drawn explicitly, which the substrate never does.

**D2 — Bluebottle's naïve endorsement vs Color's two-fact split (§2.1).** Bluebottle endorsed "commutes with rotations ⇒ frame-invariance" as-is; Color shows the conclusion is carried by the isometry property (⟨Rx,Ry⟩=⟨x,y⟩), while commutation (−I central) gives only operator equivariance. The shallow leg agreeing with the uncorrected claim is itself evidence of the correction's value: the error is invisible at low depth. Ruling: adopt Color's split — two facts, not one.

**D3 — What "logic" must mean.** Bluebottle's genuinely useful contribution: the substrate says "logic" but exhibits only geometric operations; a formal logic needs at least an axiomatized operation set (lattice/algebra structure or equivalent). Epoch's R1.1 confirms no complete spherical logic system exists (unoccupied). Ruling: fold bluebottle's demand into Fork 1's tightened keep-test — the fork must name its operation set and axioms, not gesture at "the sphere."

---

## 3. Verdicts per fork — RECOMMENDED, pending gavel

### Fork 1 — Static sphere / rotation: **CONDITIONAL KEEP**
- **Survives:** antipodal negation as formal operator, frame-invariance as design principle, spherical logic as a system — all confirmed unoccupied (Epoch, broad search); quantum cognition's context-as-rotation confirmed alive and line-for-line adjacent (Busemeyer/Pothos through 2026; Aerts et al., Entropy 28:622) with the LLM-agent bridge unbuilt.
- **Required repairs:** (i) tighten keep-test per C3/C4 — the qualifying operation must be non-cosine-reducible; Karcher mean / angular barycenter is the named candidate with 2026 empirical tailwind; (ii) adopt the §2.1 two-fact split (D2); (iii) cylinder: use log-magnitude coordinates (origin singularity) and flag the circle-vs-interval topology commitment — a bipolar agree↔disagree stance does not belong on S¹ uncorrected (Color Item 6); (iv) answer bluebottle's demand — name the operation set (D3).
- **Label:** `OPERATIONALIZE` (stance extraction + irreducibility demo are the gates to BUILD).

### Fork 2 — Stance-flow: **KEEP** (strongest verdict of the run)
- **Kill test passed by the literature:** governing law exists — generalized Kuramoto on the unit sphere (Automatica 2024); Lohe model and manifold-consensus lineage confirmed; antipodal configuration confirmed as unstable equilibrium with symmetry-breaking selection (R2.5). Geoopt/Pymanopt confirmed as live tooling.
- **Unoccupied ground (the lab's claim):** LLM multi-agent application; reconciliation-path-as-information object (with Color's honest weaker version: geometry supplies the room, the law supplies the content); parity-tagged stagnation reading; text→coupling-constant identification (Epoch Attack 3 — the real research problem).
- **Provenance note:** this is majkee's university fork. The domain that finally houses it arrived with the governing law already published — nine months before this run. What remains original is the application layer and the path-information formalization.
- **Label:** `OPERATIONALIZE` (law exists; the mapping from text to coupling is the work).

### Fork 3 — Simplex ↔ sphere: **CONDITIONAL KEEP, restructured**
- **Survives:** the bridge itself, with the constant fixed — `p ↦ 2√p` is the isometry onto the **radius-2** sphere orthant (plain √p gives ¼·Fisher–Rao; curvature ¼ not 1 — Color Item 5, matching Epoch's literature form); Fisher–Rao is entering LLM production practice (model merging arXiv:2603.04972; agent memory arXiv:2603.14588, both Mar 2026); dimension design rule holds **under the corrected hypothesis** — sum-zero/maximally-opposed configuration, not mere equidistance (orthonormal counterexample, Color Item 4); ETF/spherical codes confirmed as the capacity theory when dimension is short.
- **Killed within the fork:** the general-DS weld as stated (C2). Survives only for the Bayesian face (softmax vectors) — which is, honestly, the case the bus actually has.
- **Empirical gap:** no Fisher–Rao vs cosine/KL head-to-head for stance opposition exists (R3.3) — that comparison is the fork's build task, and §4.5's test needs a pre-registered task+metric before "better" means anything (Color Item 9).
- **Label:** `OPERATIONALIZE`.

### §5 synthesis — **REFUTED AS WRITTEN → downgrade to typed research program**
Per D1. The four-instruments-one-geometry claim currently equivocates (state-sphere vs comparison-sphere; four different structures sharing only the underlying manifold). The repaired program is real but narrower: an O(n)-synchronization sheaf whose edge stalks carry the comparison geometry. Prerequisites before any card treats it as an instrument: stance extraction, cross-vendor alignment, text→coupling, Bayesian-face-only aggregation.

---

## 4. Corrections registry (fold into substrate/atlas at P2/P3)

1. Fisher–Rao constant: `2√p` / radius-2 sphere / curvature ¼ (substrate §4.2).
2. Simplex angle hypothesis: "sum-zero (maximally opposed)" replaces "mutually equidistant" (§4.2).
3. Hairy-ball reading carries the parity tag; guarantee absent for odd stance spheres, i.e. N=3,5 (§3.2).
4. §2.1: isometry carries frame-invariance; centrality of −I carries operator equivariance — two facts.
5. §2.5 keep-test tightened: qualifying operation must not be a monotone function of pairwise cosines.
6. DS weld restated: BBA lives on Δ over 2^Θ∖∅; √-bridge does not transport Dempster's rule; Bayesian face only.
7. Cylinder: log-magnitude coordinates; circle-vs-interval topology is a modeling commitment to flag (§2.2).
8. Antipodal map is not a rotation on even spheres (det −I = −1) — guard against any future "negation is a 180° rotation" phrasing.

## 5. Atlas №1 spot-check outcomes (Epoch, independent section)

| Claim | Outcome |
|---|---|
| Tinbergen 1962 / Wilson 1967–70 gravity lineage | **CONFIRMED** → I.4 `[t]`→`[v]` |
| Ramsauer et al. arXiv:2008.02217 Hopfield≡attention | **CONFIRMED** → I.7 `[t]`→`[v]` |
| Wald sequential analysis | **CONFIRMED**; **secretary problem attribution CORRECTED** → Chow–Moriguti–Robbins–Samuels 1964, not Wald |
| 2025–26 LLM stop-reasoning line | **CONFIRMED, rich** (BEACON 2510.15945; 2602.05395; 2604.01086; et al.) → I.12 upgrade |
| Belkin–Niyogi 2003 | **CONFIRMED** → II.4 `[t]`→`[v]` |
| Spielman–Teng lineage (+Srivastava, +Batson) | **CONFIRMED** → II.5 `[t]`→`[v]` |

## 6. Holes exposed by the cross-measure → follow-up dispatched

1. **O(d)-synchronization / connection-Laplacian prior art** — the repaired §5 object is a studied class (angular synchronization, vector diffusion maps lineage) that no leg scanned: Color is offline, Epoch could not know the repair. Targeted pass dispatched (`leg-epoch-followup.2026-07-02.md`).
2. **Cross-vendor embedding alignment** — Epoch's Attack 2 names it as unaddressed prerequisite; a live literature exists (embedding-space translation/alignment). Same targeted pass.

**Follow-up outcome (landed same day — `leg-epoch-followup.2026-07-02.md`):** (1) The repaired §5 object is BORROWED, well-trodden math — Singer–Wu connection Laplacian (CPAM 2012, arXiv:1102.0075) × Hansen–Ghrist sheaf Laplacians, with 2025–26 formalizations (arXiv:2501.19207, 2510.11245, 2606.10071); its application to multi-vendor LLM agent-frame reconciliation is OPEN. (2) Relative representations confirmed (Moschella et al., ICLR 2023 oral, arXiv:2303.00721); vec2vec (Jha et al., May 2025, arXiv:2505.12540) reaches >0.9 unpaired retrieval fidelity — but global DIRECTIONAL alignment, which stance comparison requires, is NOT solved (arXiv:2602.14486, Feb 2026). Cross-vendor stance comparison is itself a research problem; every downstream card carries this as an explicit gap, not an assumption.

## 7. Gate-1 ask (majkee)

Gavel requested on four items: **F1 CONDITIONAL KEEP · F2 KEEP · F3 CONDITIONAL KEEP (restructured, DS-weld killed) · §5 REFUTED-AS-WRITTEN → typed program.** Run proceeds per plan with these as working verdicts, marked pending-gavel in every downstream artifact until you confirm or override.

*End of cross-measure. Leg files hold full source lists; every citation above is dated in its leg.*
