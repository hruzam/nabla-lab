# Selective evidence, tiny weights and recursive mathematics

**2026-11-10 · proposed implementation substrate with bounded mathematical checks.** Source notes are linked from the [coverage map](README.md). This is a laboratory research design, not ownership of the Asymmetry or Jev implementations.

## Recommendation and relation to earlier Jev work

Keep the earlier recommendation: Jev supplies typed judgments over inspectable evidence, with source custody and derived measurements preserved. The new material strengthens a specific use: deciding whether another observation is needed. It does not turn probability into a proof of hidden state or authorize action from a confidence score alone.

Four meanings of “weights” must remain explicit:

| Object | What can be changed | What that would establish |
|---|---|---|
| Local tiny neural controller | Matrices/biases, features, learned parameters | A directly inspectable function; improvement still needs sequential replay |
| Local pretrained reader | A trained decision head or adapter; optionally base parameters in a separate experiment | Adaptation of that local model, not Jev |
| Calibration/decision policy | A fitted probability map, threshold or error-cost coefficients | A changed statistical map or action rule, not changed model knowledge |
| Geometry/recursive mathematics | Affine coefficients, tent-map parameter/depth | A specified mathematical transformation with precision/identifiability limits |

Current TypeSafe documentation says Jev uses the same weights across accounts and customizes through state and question instructions; customer fine-tuning/LoRA is not the offered mechanism. [TypeSafe models, checked 2026-11-10](https://docs.typesafe.ai/models). Thus “change Jev's weights” is not a presently established route. A local Laya experiment is a separate counterpart, not a drop-in proof of Jev behavior.

## E1 — query-specific observation sufficiency

Let actual state be `s_t`, observation action `a_t`, and acquired observation `y_t=H_a(s_t)`. Let `B_t` contain states compatible with acquired evidence. For query Q, conclusive reuse requires

\[
Q(s)=Q(s')\quad\text{for all }s,s'\in B_t.
\]

**Derivation:** if two compatible states give different correct answers, a deterministic reader seeing the same observations must return the same output in both and therefore cannot always be right. Small geometric residuals cannot exclude a changed label, enabled state or occlusion when these are unobserved. A probabilistic approximation may be useful, but it needs measured error and a fallback.

Build the source's deterministic synthetic observer first. Separate oracle state (evaluation only), acquisition adapter, observation ledger, transform estimator, scheduler and decision consumer. The runtime receives only observations it purchased. A full-refresh baseline should not pay incremental bookkeeping it does not need. Every observation carries origin, validity, coverage, units/coordinates and acquired time; a guessed transform cannot silently become a fresh semantic observation.

Proposed fixtures: pure translation; zoom; affine drift; disjoint region changes; identical geometry with changed text/enabled state; occlusion; stale references; incomplete coverage. Compare full refresh, deterministic incremental observation, and incremental observation with targeted/periodic audits. Use exact task correctness, wrong current answers, abstention, acquisitions, bytes, wall cost and peak memory. A replay with oracle-derived features hidden in the scheduler is invalid.

A general 2D affine transformation has six coefficients. Three noncollinear matched points identify it in exact arithmetic; near-collinearity makes estimation ill-conditioned. Use independent validation anchors and a task-relative error tolerance; avoid inverting nearly singular transforms. Composition and rounding need an explicit error budget.

Simple decision-theoretic illustration: if reuse has error probability q, wrong reuse costs L, and a perfect refresh costs c, refresh when `qL > c`. This follows by comparing expected losses under those assumptions. Real refresh can also fail; a provider confidence field is not automatically q.

**Jev entry condition:** only after deterministic evidence acquisition and labelled cases exist, compare a bounded Jev judgment on the acquired observation against the strongest simple rule at the same evidence budget. Questions about real task success and questions about conversation accounting need separate labels.

## E2 — programmed rule versus trained cache admission

The playground gives an unusually clean test of the “weights as program” idea. An 8→16→1 network with a ReLU hidden layer and a linear scalar output has `8×16 + 16 + 16 + 1 = 161` parameters. Set all weights/biases to zero except `W1[0,0]=1`, `W2[0,0]=1`, `b2=-1/2`. For a binary feature `x0` indicating a previous touch, its score is `x0-1/2`; admission iff score>0 exactly reproduces second-touch admission. Its float32 parameter payload is 644 bytes, excluding runtime objects, features and history.

The [calculation receipt](scientific-receipt.json) checks all 256 binary eight-feature inputs independently of the source's NumPy claim. This is functional parity on that domain, not learning or a cache benchmark. Hidden-unit permutations and positive incoming-unit rescaling with inverse outgoing rescaling preserve a ReLU network's function. Different raw weights need not imply different behavior.

Implementation contract from the source, refined for comparability:

- Start with 4,096 logical tiles, a 20,000-event smoke trace, then bounded larger traces. Compare capacities 64/256/1,024 entries for diagnosis and equal **total bytes including metadata** for practical claims.
- Key by scene/tile/content version/representation version. Invalidate before hit evaluation. For this controlled cache experiment, authoritative version/invalidation events must be explicit permitted runtime inputs, with acquisition cost included or the exogenous-free assumption declared. The oracle may verify them but cannot secretly supply tags to the policy. If production cannot observe a change, deterministic freshness is not established; use the E1 acquisition/unknown-state contract. A miss computes the current result even when admission rejects it. Hold eviction policy fixed while testing admission.
- Arms: always-admit LRU; second touch within the previous 1,024 requests; frequency candidate-versus-victim; the programmed network; trained logistic regression; trained tiny MLP. Require exact second-touch/network decision and cache-state parity before learning comparisons.
- Compute causal features before history update; update on hits and misses. Bound feature history and invalidate obsolete counters. Feature order/units/missingness are part of the model contract.
- Future reuse within 128 valid requests is a **training proxy**, not an inference feature or optimality guarantee. Invalidation ends usefulness; censor or drop incomplete label horizons. A label learned under always-admit victim states can shift under the learned closed-loop policy.
- Split by whole traces/regimes before fitting. Fix normalization, thresholds and comparator selection on training/validation. Test scans, bursts, stationary and changing hot sets, invalidation storms, cold starts and unseen regimes without test-set tuning.

Count stale returns separately from misses. Report recomputation, feature/history/scoring overhead, peak RSS, metadata bytes and total cost under a declared miss-cost model. If a learned policy saves ΔM misses but adds ΔT overhead, the break-even miss cost is `ΔT/ΔM` when ΔM>0. A source-proposed continuation target is at least 10% lower modeled cost than the strongest validation-selected heuristic across held-out regimes, with zero observed stale returns. This is a proposed target, not a result or universal threshold. Zero observed stale errors is not a proof for every future trace.

The source's 512 MiB RSS target and 1 GiB whole-job ceiling concern this numerical playground, not arbitrary pretrained training. Actual launch needs sufficient live headroom. Stop this branch's complexity growth if an equally optimized handwritten rule is cheaper and equally correct.

## E3 — an exact recursive function before a “fractal advantage” claim

Define on `[0,1]`, for `0<a≤2`,

\[
T_a(x)=a\min(x,1-x)
=a\operatorname{ReLU}(x)-2a\operatorname{ReLU}(x-1/2)+a\operatorname{ReLU}(x-1).
\]

This makes weight changes and repeated composition explicit. For `0<a<1`, Lipschitz constant a gives contraction toward the fixed point zero. For a=2, the L-fold composition has `2^L` linear branches and Lipschitz constant `2^L`: every existing branch maps across `[0,1]` and splits into two on the next fold. This is a direct elementary derivation. Neural depth has a broader established representation-theoretic literature; it does not imply a runtime speedup for this task. [Telgarsky, 2016](https://arxiv.org/abs/1602.04485).

For dyadic input `k/2^b`, exact T2 iteration reaches zero within b+1 steps: each nonterminal application lowers the dyadic denominator exponent, then 1 maps to 0. The finite-precision orbit is therefore a poor unqualified witness of continuous chaotic behavior. The receipt compares branch and ReLU expressions using rational arithmetic, checks the predicted alternating endpoints/slopes for depths 1–10 and dyadic collapse for b=1–8. Finite checks supplement the derivation; they are not a new theorem about all networks.

Next experiment: compare direct piecewise and ReLU implementations under the same precision and error tolerance. Separate operation count, measured execution cost, error growth and represented branch count. For a per-step arithmetic error bound η and input error δ, a Lipschitz argument bounds depth-L error at a=2 by `2^L δ + (2^L-1)η`, assuming each computed iterate remains in the region with the stated bound. No extra precision is free.

The private source's parent-region feature and hierarchical tiles provide a spatial experiment, but neither a finite quadtree nor a recursive label demonstrates fractal acceleration. A future spatial-ordering comparison must choose its objective (point locality, bounding boxes, cache misses) and equalize the workload; these criteria need not agree. [Haverkort and van Walderveen](https://arxiv.org/abs/0806.4787). Keep this branch parked if there is no task where hierarchy changes measurable work.

## E4 — local language decisions, after capacity and labels

The named Laya source is the decision runtime `NandhaKishorM/laya`, not an unrelated same-name application. The source manual pins revision `4444f2f56acdd31a633d594e9f3227f853241d9e`. It proposes multilingual short A/B/NONE choice tests for Czech/English, CPU process use first, then calibrated/frozen-encoder-head adaptation if justified. Upstream documents a single-device CPU/MPS/CUDA training path; this is capability documentation, not a benchmark on either host. [Pinned training guide](https://github.com/NandhaKishorM/laya/blob/4444f2f56acdd31a633d594e9f3227f853241d9e/docs/finetune.md).

First measure a pinned checkpoint's cold load, warm latency, RSS and task errors under the actual token budget. Compare deterministic token matching and a frozen model before any training. Separate train/dev/calibration/test, label-order/negation/distractor and Czech/English slices. A shortened local window cannot be compared to the full Jev transcript as though evidence were identical. Freeze model/tokenizer/preprocessing/label order with cached representations.

Only then consider head-only fitting. The manual's freeze-encoder path differs from temperature fitting, full fine-tuning, Vega fitting and LoRA; do not merge their evidence. The tiny-controller source's SmolLM2-135M adapter experiment is another optional English-language branch, not evidence of Czech competence or automatic replacement for Laya. Dataset/runtime compatibility and peak training memory remain unmeasured. No installation, download, model training or paid inference was performed in this round.

## Host envelope

| Host | Evidence | Consequence |
|---|---|---|
| Office, `hruzam-120922` | Live read-only probe: Intel i5-12400, 6 cores/12 threads, about 15.38 GiB RAM; earlier snapshot about 1.34 GiB available, zero swap; UHD 730 integrated graphics | Small standard-library arithmetic ran. CPU replay is plausible after current headroom check. No demonstrated training accelerator or safe pretrained-job budget. |
| Home | Stale guide: Ryzen 5 3500U, eight logical processors, 9.6 GB RAM, no swap; no remote probe | Treat as an unverified secondary CPU target. Re-measure hardware, headroom and environment before scheduling or comparing. |

The exact later office snapshot is [office-observation.json](office-observation.json); free memory varies during the session. The active Python is 3.14.7; the probe found no installed distributions for NumPy/SciPy/PyTorch/Transformers/Hub/scikit-learn/Laya/Numba/SymPy in **that interpreter**. Other environments were not inventoried. Disk capacity is not RAM capacity. A nominal 1 GiB experiment ceiling does not imply that launching beside existing workloads is safe with only about 1.34 GiB available. Do not kill unrelated jobs, change swap/resource services or infer remote home state from old guides.

Recommended order: tiny exact mathematics now; deterministic replay in a bounded job when headroom permits; one-model CPU inference pilot after an isolated compatible environment is assigned; training only after measured peak/step time and data readiness. Record live host/OS/Python/packages, process thread limits, checkpoint revision and batch/context settings with every benchmark. Guide configuration for earlyoom/zswap/resource guards is not proof those mechanisms are currently active.

## Cache taxonomy and common record contract

| Cached object | Validity condition / experiment boundary |
|---|---|
| Application value or observation | Versioned content, scope, freshness, coverage and tenant identity; eviction never replaces validity checking |
| Text embedding or frozen model feature | Exact text/preprocessing and encoder revision, task representation; training/base changes invalidate the contract |
| Decision reply | Exact evidence, model/prompt/rubric/question/label order, cutoff and nondeterminism policy; reusing an old judgment is not fresh evidence |
| Transformer KV state | Inference-engine internal state with model/position/context compatibility; ordinary transcript storage is not KV caching |
| Cross-model state | A specifically trained/tested bridge; arbitrary hosted-model KV interchange is unestablished |

The local cache notes distinguish eviction, expiry and invalidation. Their KV/AKV/SwaT chapters are research leads; their reported gains are not imported into this proposal. For the simple load model with one backend request per miss, no retries/refreshes, incoming rate R and hit rate h, backend arrival is `R(1-h)`. Capacity B gives threshold `h=1-B/R`; queue drops/tail latency still require burst, service and queue assumptions. Those assumptions fail if expensive validation or refresh work is omitted.

Shared experiment receipt, for the implementer: experiment/hypothesis ID; exact input and artifact hashes; source/observation occurrence IDs; cached-object and validity versions; train/dev/calibration/test and regime IDs; model/function/weight/precision versions; feature schema; seed; host/env; measured resource budget; complete baseline; errors/missingness/abstention; measured cost components versus assumed costs; raw result location and derived metric version. Avoid a fully connected cache graph unless measured reuse justifies its invalidation and metadata costs.

The three reality questions currently yield: **prior art exists** for every core mechanism; **operationalization is plausible** for deterministic observer and tiny numerical tests; **technical wall remains unmeasured** for local model training and irrelevant/closed internal KV access. No claim of originality, generalized speedup or gate clearance is made. The next natural implementation is E1/E2's small replay contract; the next Jev-specific work is the independent calibration protocol.
