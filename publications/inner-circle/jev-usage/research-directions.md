# Representation, history and selective observation

Date: 2026-11-04 · Oraculum-main · SHIFT_2 · research proposal and source assessment

Operator approved the next research direction and requested this prerequisite review of the decision-methods vault and the cited technical study. This reading chapter is derived from the [dated research note](../../../session/research-jev-usage/next-phase.2026-11-04.md). The intake was closed and the experiments parked by majkee on November 4; the phase names below describe possible future work, not an active queue. It adds to the [2026-11-03 edition](study.md); it does not retrospectively expand that edition's reading coverage or construction receipts. No empirical Jev experiment or downstream implementation was performed.

## 1. Intake and usable material

Read in the requested order: [decision-methods README](/home/hruzam/reposoma/.majkee/projects/decision-methods/README.md), [decision trees](/home/hruzam/reposoma/.majkee/projects/decision-methods/decision-trees.md), [capability routing](/home/hruzam/reposoma/.majkee/projects/decision-methods/capability-routing.md). Then inspected TC03 and TC07 in the [intake catalog](/home/hruzam/reposoma/.majkee/projects/technical-clippings/CATALOG.md), and the [technical study](/home/hruzam/reposoma/raw.research/nature/report/study-two.technical.2026-07-13.md), concentrating verification on §6 and the cross-cutting claims relevant here. Other catalog entries and the other external nature study were not assessed. The technical study's references and quantitative claims were not comprehensively reverified.

The vault notes distinguish established mechanisms, captured claims and proposed exercises appropriately. TC03's reel result is not transferable performance evidence. TC07 establishes a paper source, not local routing effectiveness. Scoped technical consultation does not enter the personal vault's journal/continuity workflow or transfer its coordination seat.

| Input | Carry into Jev research | Evidence limit |
|---|---|---|
| Decision trees and forests | Inspectable classification baselines; tests of feature sufficiency; comparison with learned semantic interpretation | An explanatory cascade has no measured accuracy. More depth and trees cannot reconstruct omitted observations. |
| Trinity capability routing | Choose a compatible observer or execution configuration using task requirements and recorded outcomes | Selection policy is an experiment. Paper results do not establish Jev performance or local transfer. |
| Technical study §6 | Explicit state, timers, observation history and recovery probes | Its universal two-threshold and asymmetry-as-hysteresis statements need qualification. |
| Technical study's representation discussion | Ask which decision-relevant distinctions a compressed record discards | This is a design question; it does not establish a novel ontology or universal impossibility under additional side information. |

This complements the later Jev drafts: [edge-space](../../../session/research-jev-usage/archived-inputs/thread.edge-space.2026-09-29.md), [Nabla coin](../../../session/research-jev-usage/archived-inputs/thread.nabla-coin.2026-09-29.md), and [edge-first session state](../../../session/research-jev-usage/archived-inputs/design.edge-first-session-state.2026-09-29.md). Their operational and geometric hypotheses require separate experiments.

## 2. Three mathematical bridges

The following are direct derivations, not experimental results or claims from Trinity.

**A Boolean decision tree can express more than one weighted threshold.** The prior edition's counterexample

`f(x) = (x1 AND x2) OR (x3 AND x4)`

is computable by testing the first conjunction, accepting if it succeeds, and otherwise testing the second. Its failure to admit one weighted-threshold representation does not imply that Boolean logic is inadequate or that Jev is necessary. Finite representability does not guarantee a compact tree for arbitrary functions. A learned tree is a separate matter: fitting examples does not guarantee exact recovery of this function or preservation of monotonicity. Include the exact rule as a baseline where the rule is known.

**Gini and binary margin share a scalar, not a new dimension.** For the same binary probability `p`, let `c = |2p − 1|` and `G = 2p(1 − p)`. Expansion gives

`G = (1 − c²) / 2`.

Thus Gini adds no independent information to that margin. In a tree, `p` is a node's class proportion; it is not automatically the same quantity as a Jev estimate for one case. Neither scalar by itself identifies edge orientation, missing evidence, physical stability or calibration. Tree split selection also weights child impurities by sample counts. [Primary tree documentation](https://scikit-learn.org/stable/modules/tree.html#mathematical-formulation).

**History can resolve an ambiguity that a snapshot cannot.** Consider the illustrative relay with `l < h` and a specified initial state `q(0)`:

```text
q(t) = 1          when x(t) >= h
       0          when x(t) <= l
       q(t-1)     otherwise
```

Two histories can end at the same `x(t)` inside the band with different retained states. A snapshot-only classifier receiving that identical input cannot reproduce both labels perfectly; a classifier given the relevant previous state can. This is a constructed demonstration of omitted state. It does not prove a physical third state, and the relay's output remains binary.

More generally, if a representation maps two cases to the same record while the stipulated correct decisions differ, no deterministic decision function of that record alone can be correct on both. Additional history, a new observation or justified side information may resolve the collision. Distinguish this structural failure from finite-data learning error and probabilistic uncertainty.

## 3. Corrections before reusing the technical study

Section 6 describes different opening and closing thresholds as universal to circuit breakers. A concrete counterexample is Resilience4j: it uses CLOSED/OPEN/HALF_OPEN states, a wait interval and a limited trial batch; failure rates in the trial batch are compared against the configured threshold. Separate opening and closing numerical thresholds are not required by this implementation. Carry forward state-dependent recovery and probing, with the exact mechanism specified. [Official implementation documentation](https://resilience4j.readme.io/docs/circuitbreaker).

The study's cross-cutting paragraph also treats several kinds of asymmetry as the defining property of hysteresis. These need different definitions. Different reactions to random versus targeted failures alone do not demonstrate memory of an input path. AIMD is an established feedback mechanism, but Chiu and Jain's convergence result belongs to their modeled class and assumptions; it does not license a universal necessity claim about all controllers. [Authors' primary-paper entrance](https://www.cs.wustl.edu/~jain/papers/cong_av.htm).

The practical correction is to record which past observations, retained state, timers and reset rules actually determine the present decision. History dependence, explicit hysteresis and ordinary asymmetric response should be tested separately. The historical source remains unchanged.

## 4. Refined research design

### Phase A — define the observation and the target

Represent session evidence along separate axes: process existence, observed progress, expected waiting, ownership/lease evidence and observation freshness. A valid process can be waiting; a stale observation can coexist with a healthy process. Avoid treating these axes as mutually exclusive states.

Create cases that distinguish three failures:

1. **Compression loss:** complete evidence differs, but its Boolean summary is identical and the required decisions differ.
2. **History loss:** current snapshots coincide, but relevant prior events differ.
3. **Unobserved cause:** the entire available packet is indistinguishable, so another observation is needed to distinguish the cases.

Retain physical coin/rotation tests as a separate branch with explicit measurement maps. Session classifiers cannot validate the cylinder or rotating-ball dynamics by analogy.

### Phase B — measure the value of representation and history

Freeze decision-time evidence packets before later outcomes are available. Split by incident/session and time, keeping related log lines together. Preserve unresolved/censored outcomes rather than inventing failure labels.

Cross two factors: representation (Boolean summary versus structured evidence) and history (snapshot versus bounded event history). Compare exact rules where available, ordinary timeouts, an explicit state machine, a shallow tree, a small forest, Jev and rules plus Jev. Use an accrual detector only where the observation stream supports its timing model.

For a fair comparison, expose the same underlying observations to each eligible method; disclose encoding differences. Tune on validation data and evaluate once on held-out incidents. Tree/forest models need training data; include their fitting cost and do not present them as zero-shot equivalents. Scikit-learn's random forest averages probability predictions rather than taking a hard class vote from each tree. [Primary ensemble documentation](https://scikit-learn.org/stable/modules/ensemble.html#forest).

Primary measures: missed incidents and detection delay at matched false-alert rates, abstention/coverage, probability calibration where probabilities are claimed, and total observation/inference cost. Report results separately for quiet healthy work, awaiting-human states, long tools, crashes, stale ownership records and stalled progress. A forest can reduce estimation variance; it cannot distinguish cases represented identically.

### Phase C — choose the next observation

Use the capability-routing idea to distinguish **what evidence is missing** from **which available observer can obtain it**. Candidate observations might include a fresh process check, ownership check, tool-result receipt or an operator clarification. Each has a stated capability, cost, latency and evidence return. Availability and permission are hard eligibility checks; a model score cannot establish them.

Trinity §3.6 provides a useful methodological pattern: a fixed versioned candidate pool, pre-execution choice, verified outcomes and matching configuration records. Its memory is updated sequentially after outcomes, so a frozen-memory test and an online-learning test are different protocols. Untried configurations have unknown outcomes. [Primary paper](https://arxiv.org/html/2610.36077v2#S3.SS6).

Our proposed Jev use is narrower: interpret ambiguous task/evidence descriptions or rank eligible observations. Compare with a fixed observer, random eligible choice, cheapest eligible choice and a deterministic capability rule. Choose observations by expected decision improvement after cost, not merely by tree impurity reduction. An informative observation need not change the action.

Record every candidate considered, selection, version, outcome, cost and missing result. Selected-route logs alone cannot establish the outcomes of unselected routes. For empirical comparisons, use controlled replay where valid or an explicitly designed allocation experiment; future outcomes must not leak into routing inputs. Account for failed calls and routing overhead.

### Phase D — evaluate recovery separately

Accurate suspicion does not establish which recovery action works. Study recovery only after the observation target and classifier evaluation are defined. Specify action preconditions, ownership authority, costs and outcome horizon. Compare recovery outcomes under a controlled design; correlations in passive logs do not establish intervention effects.

Time spent in a mode is occupancy, not basin stability. Rare states may still carry most of the loss. Assess consequence and recovery time alongside frequency. Jev's proposed role is evidence interpretation or observation selection; the policy governing destructive actions needs its own explicit contract.

## 5. Research handoff and present status

Next research deliverable: **When session evidence is insufficient: representation, selective observation and recovery.** Its concrete handoff to Cartan should contain the evidence-packet schema, adjudication protocol, feature/history ablations, baseline definitions, observer capability table, metrics and failure cases. Separate proposed experiments from measured findings.

The vault review is complete and this research direction is parked. It strengthens the baseline and experimental design; it supplies no local Jev accuracy, routing gain or recovery result. The missing technical-study reference has now been inspected for this follow-up, but the broader distributed-substrate synthesis remains incomplete. No gavel or architectural lock follows from this note.

Verification: main checked the cited primary passages and the three derivations. A bounded read-only follow-up to `/root/jev_math` independently checked the derivations and returned them sound, with the initial-state and finite-representability qualifications incorporated above. This is same-provider mathematical review, not a named Janus pass or cross-vendor triangulation.
