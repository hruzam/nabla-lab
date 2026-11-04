# Jev usage atlas

*2026-11-03 · proposed applications, not measured product performance.*

[Study](study.md) · [Experiments](experiments.md) · [Implementer brief](implementer-brief.md)

## How to use this map

Each row names a possible measurement and the decision it would inform. Priority A means a good first evaluation target; B means a useful follow-up with a named prerequisite; C means a longer research question. These priorities are Oraculum's recommendations, not lab readiness labels or adoption permission. “Negative” means the proposed role lacks the required information or duplicates a deterministic operation.

For every row, retain evidence identifiers, rubric and model versions, raw judgment, interpretation, action/disposition, cost and independently assessed outcome. “Support” always names an evidence boundary. A system can verify that supplied text supports a false statement; truth beyond that text is a separate target.

## Immediate scientific and engineering uses

| ID / priority | Problem and supplied evidence | Proposed question and consumer action | Simpler comparator | Failure corner and decisive test |
|---|---|---|---|---|
| U01 / A | Delegation omissions; task, allowed sources, expected return | Per-criterion Noul/Choice for missing input; head revises material omissions | Schema checklist and a second head review | Cosmetic alarms or shared blind spots; independently adjudicate additional omissions and later rework (E2) |
| U02 / A | Claim grounding; claim plus exact source span and context | Choice: supported/refuted/insufficient; reviewer inspects disputed spans | Exact quote matching, trained entailment/grounding model | Source asserts but does not prove claim; adversarial negation, absent context and conflicting passages (E2) |
| U03 / A | RETURN assessability; requirement plus supplied result/artifact excerpts | Judge whether each requirement has inspectable support; request missing evidence | Required-field checks and direct artifact inspection | Fluent self-report masquerades as evidence; blinded false-success and missing-artifact fixtures |
| U04 / B | Candidate literature relevance; question and retrieved abstract/section | Score relevance under a fixed rubric; rank permitted reading candidates | Lexical retrieval or existing reranker | Missed candidate cannot be recovered by judging a shortlist; measure recall loss and review time (E6) |
| U05 / B | Conflicting evidence; attributed, dated statements with scope | Separate support/refutation judgments; retain four evidence combinations | Explicit contradiction rules and human annotation | Missingness confused with conflict, stale scope, shared source; compare independently labeled evidence packets |
| U06 / B | Human decision packet; proposal, alternatives and intended audience | Score clarity/completeness; author revises packet | Readability checklist and blinded human comprehension | Style preference substitutes for comprehension; measure answer accuracy and reading effort |
| U07 / B | Taxonomy or skill suggestion; bounded catalog with descriptions | Choice over candidates plus fit/none predicate; head considers suggestion | Keyword routing and existing classifier | Unavailable option, overlapping descriptions, option order; held-out routing with rejected/out-of-catalog cases |
| U08 / B | Worker-tier recommendation; task and available capabilities | Shadow Choice recommendation; compare later outcomes | Fixed tier and established head choice | Historical choice is not optimality; randomized/crossover outcomes under allowed budgets, not agreement alone |
| U09 / B | Resolution strategy; unresolved predicate and available evidence actions | Judge a predeclared action-relevant feature; separate policy selects evidence acquisition | Best constant strategy, random, least cost, uncertainty-only | Unreliable orientation or changed target; paired strategy outcomes and cost-sensitive evaluation (E4) |
| U10 / B | Prompt/evidence contamination; instruction-bearing source snippets | Flag suspicious passage for inspection; preserve source context | Provenance separation, exact policy checks | Semantic detector itself influenced by planted instruction; attack fixtures and false-positive costs; never treat score as authorization |
| U11 / B | Known-probability questions; synthetic case with exact probability | Compare Noul, binary Choice and a declared Score encoding | Exact arithmetic | Primitive mismatch, representation sensitivity, leakage through paraphrases; split by latent problem (E1) |
| U12 / C | Diagram and coin-image observations; labeled images with controlled views | Experimental Choice/Box observations; compare against known state | Geometry from generator, ordinary vision/localization model | Occlusion, scale, crop and lighting confused with rotation; controlled image fixture and localization/pose metrics (E5 extension) |

These applications are related to existing methods, not new merely because Jev is the judge. Vendor [citation](https://docs.typesafe.ai/cookbooks/citation_check), [retrieval](https://docs.typesafe.ai/cookbooks/classifying_rag_passages) and [skill-selection](https://docs.typesafe.ai/cookbooks/skill_suggestion) examples show overlapping proposals. [FEVER](https://aclanthology.org/N18-1074/) supplies an established evidence-label distinction; [MiniCheck](https://aclanthology.org/2024.emnlp-main.499/) supplies a concrete grounding comparator. Their results do not determine performance on this lab's corpus.

## All compendium streams and their mathematical boundary

The eleven reading editions and the separate substrate register were read by the mapping pass. The connections below preserve their explicit assumptions and open experiments. Relevant originals were checked selectively; the [coverage record](../../../session/research-jev-usage/README.md) names depth.

| Stream / ID / priority | Measurement → possible use | Existing mathematics or restriction | Comparator and first decisive check |
|---|---|---|---|
| [Stance geometry](../stance-geometry/study.md) / U13 / B | Text-category probabilities → test a representation or trajectory | Fisher geometry has a declared scale/domain; rotation invariance is not semantic validity | Same-information probability/Cartesian representation; paraphrase stability, opposition fixtures and held-out outcomes (E5) |
| [Spectral retrieval](../spectral-retrieval/study.md) / U14 / B | Candidate support scores → inspection or reranking | Graph diffusion operates on a given graph; Jev neither supplies unseen candidates nor certifies graph meaning | Fixed candidate pool, lexical/reranker baseline, recall and end-task loss (E6) |
| [Coalition evidence](../coalition-evidence/study.md) / U15 / B | Identified judgments → compare quorum, capacity and monotone rules | Capacity constraints and shared-evidence dependence remain explicit; a score is not reliability | Weighted quorum before learned interactions; grouped held-out outcomes, then E3/E4 |
| [Cascade diagnostics](../cascade-diagnostics/study.md) / U16 / C | Timestamped event labels → populate a propagation study | Exogenous drive, observation loss and the offspring operator are separate; label similarity is not causation | Synthetic known process first, then independent event labels and observation-error sensitivity |
| [Tensor analytics](../tensor-analytics/study.md) / U17 / C | Versioned rubric measurements → populate agent–turn–concept arrays | Factor ambiguity and invariance of reconstruction under common time permutation remain; factor names are not discovered meanings | Synthetic recovery, count/matrix baselines, held-out entries and order-sensitive prediction |
| [Flow/control/stopping](../flow-control-stopping/study.md) / U18 / C | Remaining-evidence or defect judgment → inform an explicit continuation policy | Loss, information set and dynamics must be specified; a score cannot establish optimal stopping | Fixed budget and simple rules; matched resources, repeated correlated errors and failure to make progress |
| [Coherence/composition](../coherence-composition/study.md) / U19 / B | Typed evidence labels → populate constrained comparison ports | `ker B` consistency and `Bx=b` solvability are model-relative; zero maps can erase meaning | Known contradictory/consistent fixtures plus collapsed-map control; verify labels independently before algebra |
| [Mental map/lineage](../mental-map/study.md) / U20 / B | Reconstruction against revealed anchors → flag contradictions or omissions | Graph reachability certifies only the supplied graph and complete successor enumeration | Commit reconstruction before held-out anchors; exact graph coverage separately from semantic fidelity |
| [Scratch instruments](../scratch-instruments/study.md) / U21 / B | Blinded rubric scoring → evaluate intermediate representations | The same judge cannot both optimize and independently validate its own preferred format | Separate human/independent evaluator; randomize format and budget independently |
| [Interactive interposition](../interactive-interposition/study.md) / U22 / negative for completion authority | Semantic completeness judgment → optional review after transport has completed | Completion requires session/request correlation and terminal lifecycle evidence | Deterministic protocol completion; never substitute a model's “done” judgment for the receipt |
| [Earlier Jev judgment](../jev-judgment/study.md) / U01–03 / A | Extra observation at a frozen research boundary | Existing paper establishes a role hypothesis and probability bounds, not measured usefulness | Checklist, repeated review and specialized judge; E2 extends its original trial |
| [Distributed substrate](../substrate-gap-register.md) / U23 / C | Relevance/failure-category judgments → proposed routing metadata | Two external study bodies remain outside this assignment; no completed three-source synthesis or causal-credit measure is supplied | Scope-local frozen workload; compare explicit routing rules before adaptive claims; do not claim to close the historical stream |

## Uses to reject or narrow

| Proposed use | Finding | Narrower useful role |
|---|---|---|
| Prove a theorem by repeated Jev agreement | Negative: agreement supplies no derivation or proof object | Classify candidate proof steps for inspection; a mathematician or formal checker establishes validity |
| Detect a true third state from one near-half probability | Negative as identification: multiple mechanisms produce the same observable | Test selective prediction; add independent observations to distinguish hypotheses |
| Calculate a known Boolean function, graph reachability or numeric formula | Usually unnecessary model inference | Let deterministic code calculate; study Jev only at the semantic measurement boundary |
| Certify truth, fidelity or completeness of excluded records | Information boundary prevents certification | State exactly which supplied evidence supports the bounded judgment |
| Treat repeated questions as independent experts | Unsupported dependence assumption | Record shared evidence/model provenance and estimate joint failures |
| Turn a confidence threshold into permission or a universal stop rule | Undefined action authority/loss | Keep the permitted action policy explicit and measure its outcomes |
| Recover physical angle from Box coordinates or text certainty alone | Observation model absent | Use calibrated visual geometry or a synthetic generator with known pose |

## Ranked recommendation

U01/U02 provide the first practical usefulness comparison; U11 diagnoses probability semantics without pretending to identify internals. U15/U09 form the central Coin research path: sound deterministic composition followed by selective acquisition. U13 supplies the separate rotating-ball representation test. Other rows remain available to the implementer with their evidence requirements, rather than being quietly collapsed into a single universal “judge” role.
