# Distributed substrate: scientific gap register

**Bounded local-source analysis · 2026-10-27 · not the completed three-study synthesis**

The [v1 specification](../../drafts/decentralized-memory-substrate-spec.md), [v2 specification](../../drafts/decentralized-memory-substrate-spec-v2.md) and [synthesis brief](../../drafts/oraculum-synthesis-brief.2026-07-13.md) were read in full. The brief names two additional source studies outside nabla-lab. Until those are read under the operator's delegation, this document records corrections that can be established independently; it does not reconstruct their empirical findings or announce completion of Track 2.

## Obtained design and provenance

The specification proposes immutable source records, attributed value marks, a derived weighted graph, a local routing view and a fallback path independent of the adaptive substrate. It distinguishes support, contradiction and supersession, and separates cold decay, tombstones and remembered failures. Endpoints choose among offered routes and return feedback. Citation-granular credit and generation numbers are proposed observables, not validated truth measures.

The brief attributes `[CORE]` material to two-family independent first passes and `[v2]` additions to single-agent or post-exposure reasoning. Those are recorded provenance claims; the original cold-start transcripts were not inspected. The new edition preserves the distinction and does not count an informed review as a new blind leg.

## Hypotheses and prior art

| Hypothesis | Bounded finding | Remaining scientific question |
|---|---|---|
| H1: coordinator-free scarcity routing is absent | Broad absence is contradicted by established decentralized work stealing. The particular scarcity-estimation/structured-transfer combination needs a narrower comparison. | Capability matching, reliable task ownership transfer and heterogeneity under the intended workload. |
| H2: gradient-pull differs from protocol-pull | Physical gradients and computed scores differ, but a software score still needs observation, scheduling and transport. Queue-differential backpressure is relevant prior art. | Define the generator-state-to-fetch mechanism; compare latency, wasted transfers and stale-context rate. |
| H3: asymmetric error routing by role is absent | Broad absence is too strong: canary deployments deliberately limit exposure of unvalidated changes. That is an analogy, not a proof of the proposed spatial drift clock. | Promotion tests, rollback/supersession and contamination of the stable memory view. |
| H4: negative knowledge differs from decay | Meaningful behavioral distinction, with prior art in scoped negative caching. Negative numerical weights are optional. | Repeated-failure avoidance versus false suppression when conditions change. |

Work stealing transfers ready work toward underused processors under explicit scheduling assumptions; its bounds do not automatically transfer to remote heterogeneous agents. [Blumofe and Leiserson, *Scheduling Multithreaded Computations by Work Stealing*](https://www.cs.cornell.edu/courses/cs612/2006sp/papers/blumofe94.pdf). Queue-state scheduling has classical stability theory, likewise conditional on its model. [Tassiulas and Ephremides, 1992](https://www.di.ens.fr/~busic/mar/projets/TE92.pdf).

Canarying is established limited-exposure validation, not a new generic principle of keeping uncertain changes apart from an established serving population. [Google SRE, *Canarying Releases*](https://sre.google/workbook/canarying-releases/). It does not establish the external Study One's claimed relationship between space and drift, which remains uninspected.

DNS distinguishes negative answers from resolution failures and gives cached evidence scope and lifetime. Agent records likewise should distinguish “tested false,” “not found,” “timed out” and “not authorized.” [RFC 2308](https://www.rfc-editor.org/rfc/rfc2308.html); [RFC 9520](https://www.rfc-editor.org/rfc/rfc9520.html). <u>Store each failed attempt with conditions, evidence, outcome type and a recheck condition; measure avoided repeat work and newly valid routes incorrectly suppressed.</u> A negative ranking score is not a negative sampling probability. Softmax, nonnegative penalties or explicit filters can implement different policies; their behavior must be specified.

## A corrected exploration claim

The v2 assertion that zero epsilon makes topology provably freeze is too broad. A narrower cold-start deadlock follows if a new candidate starts with zero weight, can gain weight only after an offer and positive feedback, receives zero offer probability at zero weight, and has no external initialization or update path. Induction then keeps that candidate at zero. Existing edges can still change, so even this is not a proof that the entire topology freezes.

Zero explicit epsilon need not cause deadlock: positive initialization, semantic selection or an independent insertion process can admit new candidates. Conversely, positive epsilon is not sufficient if a candidate is ineligible or its chance of selection becomes too small. With a fixed finite pool of N eligible candidates and independent uniform exploration probability ε>0 at each step, the probability a particular candidate is never offered in T steps is `(1−ε/N)^T`, tending to zero. This proves eventual offering under those assumptions, not useful feedback, successful learning or finite-time certainty.

<u>Specify candidate eligibility, initialization, offer probabilities and feedback before selecting an exploration policy; evaluate both discovery and the cost of low-value offers.</u>

## Guarantees not established

Outcome-weighted feedback may resist naive popularity reinforcement, but “SEO-proof by construction” needs an adversary and a proof. Citation-based credit assumes faithful attribution; cited text need not be the causal source of an answer. A generation integer measures declared derivation depth, not factual reliability. An independent fallback reduces coupling but cannot guarantee availability against every storage, process or host failure. Authenticated attribution, poisoning, stale regimes and false promotion remain material design questions.

The earlier two independent core passes make the architecture worth studying. They do not establish novelty or correctness of every addition. The three-source synthesis, spatial empirical claims and targeted formal/source verification remain distinct tasks. This register supplies usable corrections now while leaving those evidence boundaries visible.
