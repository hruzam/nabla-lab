# Sources and verification depth

**Accessed 2026-11-03.** Public unauthenticated documentation and primary research only. Links below support the edition's bounded claims. No paid API call, account query or benchmark replication occurred. A source's displayed availability is not local runtime evidence.

## Current instrument

| Source | Passage checked / use | Limit |
|---|---|---|
| [TypeSafe index](https://docs.typesafe.ai/llms.txt) | Documentation discovery, primitives/patterns/cookbooks | An index is not capability execution |
| [Models](https://docs.typesafe.ai/models) | Current IDs, context limits, aliases, retry/rate-limit description | Provider and account details require their own contract |
| [Choice](https://docs.typesafe.ai/primitives/choice) | Nominal criteria, returned probabilities, question packing | Domain accuracy not established |
| [Noul](https://docs.typesafe.ai/primitives/noul) | Probability-of-yes and absent separate confidence | Semantic truth not established |
| [Score](https://docs.typesafe.ai/primitives/score) | Ordered rubric, distribution and expected index | Cardinal interpretation not automatic |
| [Confidence](https://docs.typesafe.ai/confidence) | Explicit Choice/Score formulas; binary specialization checked algebraically | Statistic, not independent calibration evidence |
| [Fan-out](https://docs.typesafe.ai/patterns/fan-out) | Shared-state parallel questions | No statistical-independence implication |
| [Images](https://docs.typesafe.ai/images), [Box](https://docs.typesafe.ai/primitives/box) | Experimental qualification, direct-API opt-in, version support | No image request was exercised; provider adaptation unverified |
| [OpenRouter Decisions reference](https://openrouter.ai/docs/api/api-reference/alphadecisions/submit-a-decisions-request) | Endpoint and typed request example | Example still uses 1.13; not evidence that 1.14 is unavailable |
| [OpenRouter model](https://openrouter.ai/typesafe/jev-1.14/), [provider guide](https://openrouter.ai/blog/insights/what-is-jev/) | Researcher checked public listing and provider description | No account-specific price/access guarantee; manuscript avoids a funding estimate |
| [Citation cookbook](https://docs.typesafe.ai/cookbooks/citation_check), [RAG cookbook](https://docs.typesafe.ai/cookbooks/classifying_rag_passages), [skill suggestion](https://docs.typesafe.ai/cookbooks/skill_suggestion) | Existing application patterns | Demonstrations, not independent local benchmarks |

## External empirical evidence

- [Deußer et al., Evaluating and Benchmarking the System One Model Jev, v2](https://arxiv.org/html/2609.37647v2), revised 2026-10-29. Selected methods, results and limitations §§3–6 inspected by researcher; main checked abstract and decisive sequential/memorization passages. Raw data and code not audited. Model/version, threshold tuning and comparison conditions remain attached to the reported result.
- [Porcedda, Sys1Cal-v1](https://arxiv.org/html/2609.35342v1), 2026-09-28. Selected §§2–6 and appendix inspected. Main checked observational qualification and Table 3's point-versus-interval distinction. Exact version and held-out correction fitting were not established from inspected text. Full raw-data reproduction remains unperformed. Its 365 renderings represent 92 underlying problems; grouping matters. The reported interval median differs between its table/abstract and conclusion; no such headline score is adopted here.
- [Geifman and El-Yaniv, Selective Classification for Deep Neural Networks](https://proceedings.neurips.cc/paper/2017/hash/4a8423d5e91fda00bb7e46540e2b0cf1-Abstract.html), 2017. Primary abstract/record for established selective-prediction framing; guarantees are not transferred to Jev.
- [Thorne et al., FEVER](https://aclanthology.org/N18-1074/), 2018; [Tang et al., MiniCheck](https://aclanthology.org/2024.emnlp-main.499/), 2024. Primary task/benchmark records for evidence-label semantics and a specialized comparator. No benchmark reproduction or claimed local superiority.

## Mathematical ancestry

- [Ikenmeyer, Komarath and Saurabh, Karchmer–Wigderson Games for Hazard-free Computation](https://eccc.weizmann.ac.il/report/2021/100/download), 2021, introductory equation 1.1 read directly. This defines extension over all Boolean resolutions; the monotone endpoint proof in the edition is explicit. Related [Ikenmeyer et al., hazard-free circuits](https://arxiv.org/abs/1711.01904) checked by mathematical reviewer. No circuit-complexity bound is imported into the Jev application.
- [Freixas and Zwicker, Weighted voting, abstention, and multiple levels of approval](https://upcommons.upc.edu/entities/publication/ce299cbe-6842-47ef-bd0e-86fb713225fc), 2003. Primary abstract/record confirms ordered levels. Repository PDF search extract was available, direct fetch returned 403. Do not claim full-paper verification.
- [Freixas, Freixas and Kurz, On the characterization of weighted simple games](https://link.springer.com/article/10.1007/s11238-017-9606-z). Reviewer checked visible abstract/notes; manuscript supplies its own weightedness counterexample.
- [O'Donnell, Analysis of Boolean Functions](https://www.cs.cmu.edu/~odonnell/papers/Analysis-of-Boolean-Functions-by-Ryan-ODonnell.pdf), chapter 2. Reviewer inspected relevant influence/derivative treatment; main independently checked the three-swings/two-implicants example.
- [Adaptivity Gaps for the Stochastic Boolean Function Evaluation Problem](https://arxiv.org/abs/2208.03810), 2022. Primary abstract establishes the costed sequential testing problem and its independent-input premise; no approximation theorem is transplanted.
- [Golovin and Krause, Adaptive Submodularity](https://arxiv.org/abs/1003.3967). Primary abstract and author-hosted paper opening checked. Mentioned as conditional acquisition theory, not a proof that the Coin policy meets its assumptions.

## Local anchors and limits

The full corpus/depth inventory is in [README.md](README.md). Particularly decisive anchors are the original Choquet card's mandatory adoption comparator, the stance edition's measurement/rotation/Fisher distinctions, the coherence edition's semantic-port warning, and the existing Jev edition's probability-versus-calibration boundary. Original research sources are preserved. No inference that all historical pending items are merely gavels is made; unperformed experiments and missing external evidence remain separate.

The writing-style connector was unavailable in tool discovery. The prose follows the operator-supplied task and the established scientific-edition format; no retrieved personal-style match is claimed.
