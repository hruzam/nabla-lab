# Experiments that can distinguish the proposals

*2026-11-03 · experiment designs. Only the finite mathematical checks recorded in the evidence receipt were executed. No Jev calls or empirical benefits are claimed.*

[Study](study.md) · [Usage atlas](usage-atlas.md) · [Implementer brief](implementer-brief.md)

## Common evaluation contract

Freeze the target, evidence boundaries, model/version, prompts, option meanings, rule version, outcome rubric, primary contrast, error costs, maximum effort and data split before the confirmatory run. Retain raw distributions. Any local calibration layer has its own version and fitting data. Split related cases together: paraphrases of one problem, turns from one incident and near-duplicate briefs must not cross the development/evaluation boundary.

Measure at least:

```text
coverage = determinate decisions / all eligible decisions
selective risk = wrong determinate decisions / determinate decisions
unconditional wrong rate = wrong determinate decisions / all eligible decisions
```

Selective risk is undefined when there are no determinate decisions; report that explicitly. Include deferral frequency and its consequence. An always-defer system has zero unconditional wrong decisions and no decision coverage. Report risk–coverage curves or predeclared matched-coverage comparisons, plus a stated loss that accounts for wrong commitments, deferrals, unresolved deadlines and acquisition. Report money, machine latency and human effort separately unless an agreed conversion defines total loss.

Sampling follows the minimum useful effect and desired precision, not a ceremonial case count. A feasibility sample can expose defects without establishing equivalence or superiority. Under independent Bernoulli errors, zero errors in 50 determinate cases still gives the one-sided 95% upper bound `1−0.05^(1/50)≈0.0582`; clustered decisions require a different uncertainty calculation. For grouped data use cluster-level intervals or resampling, and describe what remains underpowered. “Not significant” is not evidence of equivalence.

## E0 — deterministic coalition mechanics

**Question:** does the proposed rule and interpreter preserve the declared partial-information semantics?

**Fixtures:** majority, AND, OR, the nonweighted `(x₁∧x₂)∨(x₃∧x₄)` with dummy x₅, an explicit fixed-value mistake, XOR as a nonmonotone negative control, and completion constraints.

**Checks:** boundaries, monotonicity, self-duality only if required; endpoint result against exhaustive compatible completions; potential pivotality with its existential quantifier for unconstrained fixtures; rejection of malformed states. Distinguish constrained and unconstrained completions. Under `x₁=x₂`, disagreement between feasible 00 and 11 does not imply a feasible single-coordinate swing; specify a separate constraint-aware acquisition rule rather than asserting the unconstrained equivalence. Confirm the majority-seven/four-unresolved counterexample.

**Acceptance:** zero discrepancies on the declared finite fixtures, plus explicit rejection or separate handling of nonmonotone rules. **Interpretation:** this qualifies the mechanics; it does not qualify Jev measurements. The five-element fixture and majority counterexample were checked in this research; an implementation must independently exercise its own code.

## E1 — primitive semantics and representation sensitivity

**Question:** how do outputs track known probabilities, and how stable are they across equivalent representations?

Generate new latent problems with exact probabilities: finite urns, counts, conditional cases, and explicit missing-information controls. Ask Noul, binary Choice and a precisely defined Score encoding. Vary prose/table/order while preserving the same mathematical problem. Use repeated calls to measure variation and retain per-call results rather than only averages.

A stochastic problem with a specified generating distribution can have an exact predictive probability. An urn with unspecified composition and no sampling model does not acquire ground truth p=0.5 merely because information is missing. Score such controls against an evidence-insufficiency label or a declared admissible probability set, separately from point-recovery error.

Compare direct numerical error and proper scoring measures appropriate to the target. Distinguish pointwise recovery of a known p from frequency calibration over realized binary outcomes. A Score level's numeric projection is an experimental encoding, not a guaranteed probability interpretation. Fit any post-hoc correction on development problems only; test on different latent problems and held-out representations.

**Competing explanations:** generic score distortion, prompt/primitive semantics, representation sensitivity and an unresolved-mass model. Give alternatives comparable fitting flexibility. Evaluate corrected point estimates as points; report interval coverage and width together. A wide interval cannot earn a point-prediction victory.

**Stop/revise:** no held-out improvement, unstable version transfer or representation dependence larger than the claimed gain. **Interpretation:** successful recovery or a useful residual model supports an observation method, not an identified hidden truth state. [Relevant prior experiment: Sys1Cal](https://arxiv.org/html/2609.35342v1).

## E2 — useful evidence review

**Question:** does Jev expose additional material omissions or unsupported claims at acceptable effort?

Use a consecutive or predeclared stratified set of briefs and source-grounded claims. Include straightforward, underspecified, contradicted, missing-source and misleadingly fluent cases. Record the head's initial assessment before exposing any second review. Compare deterministic checklist/quote matching, repeated head review, Jev review and an available specialized grounding comparator. Randomize review assignment or use independent blinded paired adjudication while preventing one arm's findings leaking into another.

Primary outcomes are additional actionable defects and independently verified final correctness, with false alarms and review time. Later clarification/rework is useful but can be censored or counterfactual; do not count every suggested correction as prevented rework. Agreement with the head is not the reference truth. Freeze materiality and completion-window rules.

**Stop/revise:** predominantly cosmetic changes, missed material defects, or effort exceeding the predefined acceptable trade-off. **Interpretation:** a positive result supports the tested workflow, not a general capability to judge science.

## E3 — does decomposition and EDGE help?

**Question:** which component of the Coin circuit earns its complexity?

Choose one decision type with independently labeled component predicates and final outcomes. Declare the group function before held-out evaluation. Do not force five predicates or oddness if the task does not naturally have them. Separate a diagnostic synthetic cohort with exactly known component states from a semantic cohort where Jev can err.

| Arm | Procedure | Intended comparison |
|---|---|---|
| A | Deterministic/checklist task baseline where available | Whether any semantic call is needed |
| B0 | One whole-decision Jev judgment without rejection | Whole-decision baseline for C0 |
| B1 | B0 with an ordinary reject policy | Rejection without decomposition; compare with B0 |
| C0 | Component argmax values composed through the fixed rule | Decomposition without rejection; compare with B0 |
| C1 | Same component measurements; reject if any component crosses its EDGE threshold | Conservative component rejection; compare with C0 |
| D | Same component measurements, EDGE thresholds, endpoint certificate; defer unresolved groups | Contribution of selective partial evaluation |
| E | D plus ordinary evidence acquisition without an orientation signal | Contribution of another observation |
| F | D plus declared oriented acquisition | Incremental value of orientation (E4) |

Compare C1 with D to isolate whether the group rule can safely ignore irrelevant unresolved predicates; compare E with D for acquisition and F with E for orientation. B1 versus D is a whole-system comparison that changes both decomposition and selection, not an isolated causal contrast. Use matched resources and coverage where feasible, and also report the full cost–risk–coverage trade-off. A lower wrong-commitment rate achieved only by withholding nearly every answer is not enough. Include correlated wrong components, shared false evidence, missing predicates, swapped labels and incorrect rule specifications.

**Stop/revise:** D offers no useful trade-off beyond B1/C1, or a wrong fixed predicate systematically defeats certification. Retain the simplest adequate arm. Abstention can be valuable without being ontologically novel.

## E4 — orientation as an acquisition signal

**Question:** does an independently available orientation predict which next action helps?

Specify two concrete resolution actions and the pre-outcome observable that selects between them. Examples might be retrieving provenance versus asking for a missing task constraint; names such as POS/NEG alone do not define the signal. Where possible run both actions on frozen copies of each case, randomizing order or using independent copies to avoid carryover. Ground the reference outcome independently.

Compare oriented routing with the best constant strategy selected on development data, random routing, shuffled orientation, cheapest-first and a non-oriented uncertainty policy. Match action availability and cost. Evaluate improvement in decision loss after accounting for the acquisition. Analyze whether the signal adds predictive information beyond the original probability and evidence features.

Track changes of predicate meaning. A successful answer to a different question is not successful resolution of the original one. If resolution permanently fixes previously unresolved predicates without changing the rule, at most |U| successful fixes are needed. Reopening predicates or changing the frame removes that termination argument; a resource budget merely stops computation.

**Stop/revise:** no reproducible held-out advantage or reliance on leaked post-outcome information. A sufficiently precise equivalence result can support removing orientation; an underpowered null result cannot. **Interpretation:** routing benefit supports an action-selection variable, not geometric orthogonality.

## E5 — rotating-ball and representation tests

**Question:** which observations preserve the distinctions the proposed state model needs?

Start with the study's analytic sphere model, known x/a/b and a stated EDGE band. Generate paired states with the same `a·x` and opposite `b·x`. A single pₐ observation must fail to distinguish them; a supplied second-axis observation can distinguish them away from its zero boundary. Verify passive joint-rotation invariance separately from active motion and axis changes.

For a semantic extension, define anchored textual contrasts before assigning vectors. Compare geometry against the original probability/features with the same information budget. Hold out questions and paraphrases. Track stability, meaningful opposition and task benefit; a prettier trajectory is not an outcome.

An optional image extension uses rendered scenes with known pose, then occlusion/lighting/crop controls. Experimental Box localization and pose estimation have different targets; compare with direct generator geometry and a conventional visual baseline. It requires a separate declared model/provider capability test before any performance claim.

**Stop/revise:** the required orientation has no independent observable, or geometry adds no held-out task value. **Interpretation:** a negative identifiability result is a useful conclusion; adding a new coordinate without a measurement does not fix it.

## E6 — retrieval, memory and representation evaluation

Freeze corpus, query set, candidate budget and independent support labels. Compare the existing retriever, a standard reranker and a Jev semantic pass on the same candidates. Report retained-support recall, harmful omissions, end-answer support, cost and time. Keep mandatory evidence outside discretionary filtering. Include absent and contradictory sources; judging the visible subset cannot repair initial retrieval failure.

For reconstructed memory, commit the reconstruction before exposing held-out anchors. For scratch representations, randomize representation and token budget separately and use an evaluator not used to optimize the representation. For scoring arrays or propagation labels, qualify the semantic measurement first; numerical model fit is a separate test.

**Stop/revise:** screening loses useful evidence or agrees with the existing ranker without saving effort. This experiment supplies bounded evidence for U04/U14/U20/U21; it does not complete the historical distributed-substrate program.

## Sequence and release

E0 establishes mechanics; E1 and E2 establish useful measurement candidates. E3/E4 test the Coin procedure; E5 remains a parallel representation question; E6 follows only a concrete workload. Live calls require the implementing session's funded, confirmed-send mechanism. This research creates no paid-run release and does not inspect that session's current state.
