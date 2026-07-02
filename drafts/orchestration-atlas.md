# The Orchestration Atlas

### A living reference for a file-backed agentic RAG + coordination stack — every mathematical instrument, mapped to its existing research and production prior art, with open slots for your own findings.

*Nabla & majkee. Drafted 2026-06-25. This is an **atlas**, not a paper: a map you build against and extend, not an argument to defend. Prior-art and production claims verified against literature current to mid-2026; re-verify anything tagged volatile before formal use.*

---

## How to use this document

- **Part I** is the instrument catalog — one card per mathematical idea, each with concept, mapping, prior art, production tools, status, buildability, and a `NOTES (majkee)` slot for you to fill as you build.
- **Part II** is the RAG engine specifically — the thing you're building right now — with its own dense prior-art and production map.
- **Part II-B** is the **Fourth Spine — Coherence / Identity**: the four instruments that govern whether the thing *stays one system* under noise (added this session, prior art gathered same day).
- **Part III** is the spine synthesis condensed (the *why it's one object*).
- **Part IV** is the master prior-art / production table — the at-a-glance "what already exists" answer.
- **Part V** is the fork menu — pick one to go deep on next.
- **Part VI** is your running scratchpad, plus a blank entry template so new instruments slot into the same shape.

### Status legend

**Maturity of the idea**
- `BORROWED` — established elsewhere, you're applying it as-is
- `REPURPOSED` — exists in another field, you're moving it to a new use
- `OPEN` — apparently unoccupied in the literature as of mid-2026 (absence of evidence, not proof of absence)
- `YOURS` — the integration/application is the contribution

**Build readiness**
- `BUILD-NOW` — implementable today, no theory gaps
- `OPERATIONALIZE` — math is sound, mapping to noisy real signals is unproven
- `THEORY` — needs formalization before code

**Freshness**
- `[v]` verified against a mid-2026 source
- `[t]` training-era / not re-verified — treat as a lead, not a fact

---

# Part I — The Instrument Catalog

---

## I.1 — Spectral analysis

**Concept.** Two distinct uses. *Signal view:* an agent's state trajectory over turns is a time series; its power spectrum separates regimes — decaying aperiodic energy = healthy convergence, a sharp spectral spike = a loop at fixed period, a drifting spectral centroid = topic drift. *Graph view:* build an affinity matrix over content units, take the Laplacian `L = D − W`, and its eigenvectors give spectral clustering; the Fiedler vector (2nd-smallest eigenvalue) is the natural cut.

**Mapping.** Graph view is the retrieval backbone (see Part II). Signal view is a drift/loop diagnostic on the bus.

**Prior art.** Spectral clustering and the Laplacian eigenmap are classical (von Luxburg's spectral-clustering tutorial; Belkin–Niyogi eigenmaps). For the signal view applied to LLM trajectories, the 2026 "geometric dynamics" line (arXiv:2512.10350) uses trajectory metrics though not Fourier spectra specifically. `BORROWED` · `BUILD-NOW` · `[v]`

**Production.** Graph/spectral primitives ship in `scikit-learn` (SpectralClustering), `networkx`, `scipy.sparse.linalg` (eigsh/Lanczos). No agent-memory product exposes the *spectrum* as a feature — they store graphs but treat them as topology, not operators. That gap is real.

> **NOTES (majkee):**
> _(your findings, decisions, what you actually wired up)_

---

## I.2 — Vector / tensor algebra

**Concept.** Embeddings-as-vectors and cosine routing is the trivial part. The underused part: a multi-agent log is a rank-3 tensor indexed by (agent, turn, concept). A CP or Tucker decomposition factors it into agent-factors × time-factors × concept-factors — you extract "what each agent contributes" and "how concepts evolve" as separate matrices. Attention itself is already a tensor contraction (Q·Kᵀ), so a triage router computes a bilinear form between task-query and agent-key vectors whether named or not.

**Mapping.** Tensor decomposition of the JSONL turn-log = offline analytics on agent behaviour and concept drift. The bilinear-form view = the router's scoring function.

**Prior art.** CP/Tucker/PARAFAC are textbook multiway analysis (Kolda & Bader, *Tensor Decompositions and Applications*, SIAM Review 2009 — the canonical reference). Critically, this has been run on **communication logs**: email modeled as a (sender, receiver, date, content) tensor (InfTucker, arXiv:1108.6296). Your (agent, turn, concept) framing is a direct analog. Side-information-coupled variants (graph-on-mode) exist (Multi-Dictionary Tensor Decomposition, arXiv:2309.09717). `BORROWED` (small new application) · `BUILD-NOW` · `[v]`

**Production.** `TensorLy` (Python, CP/Tucker/TT), `tensortools`, MATLAB Tensor Toolbox. No agentic product does this on its logs — it'd be your own analytics layer.

> **NOTES (majkee):**
>

---

## I.3 — Complex analysis (real + imaginary parts)

**Concept.** The weakest as a standalone discipline — classical residues/contours/conformal-maps have no clean non-forced mapping here, and I won't manufacture one. Two gems do carry weight: *(a) phasors* — represent an agent's contribution as magnitude (confidence/effort) × phase (stance); in-phase agents amplify (agreement), out-of-phase cancel (conflict). Cosine similarity throws phase away; the complex form keeps it. *(b) the s-plane* — read loop stability off pole locations (belongs to I.6).

**Mapping.** Phasor aggregation = a consensus primitive that distinguishes "two agents agreeing" from "two agents in opposition" at equal magnitude. S-plane = the stability readout of the control loop.

**Prior art.** Phasor/complex-valued representations appear in complex-valued neural nets and in complex-valued Tucker decompositions for phase-related features in fMRI (e.g. dynamic complex-valued Tucker, *Biomed. Signal Process. Control* 2026). No direct "phasor consensus for agents" found. `OPEN` (phasor consensus) / `BORROWED` (s-plane, via control theory) · `OPERATIONALIZE` · `[v]`

**Production.** None specific. Phasor math is trivial to implement; the open question is whether "phase = stance" is a measurable, stable quantity on real outputs.

> **NOTES (majkee):**
>

---

## I.4 — Gravity / potential / effort

**Concept.** Rigorous only if you commit to an actual potential `Φ` — as loose metaphor it just re-says "attraction." Commit and it pays: the goal is a potential well, each agent a body, effort/authority = mass, semantic distance = distance. Drift = an agent reaching escape velocity from the goal's basin. Routing-as-gravity (flow ∝ mass / distance²) is a real quantitative tool. **The deep result:** many agents mutually attracting is an n-body problem — chaotic, no closed form — and the only thing that tames an n-body system is a dominant central mass. *That is the mathematical justification for a central bus:* the orchestrator is the sun keeping agents in stable orbit instead of chaotic mutual capture.

**Mapping.** `Φ` defines the semantic landscape (couples to I.5 and II). The n-body argument justifies the bus topology itself. Gravity-routing = a candidate-weighting rule.

**Prior art.** The gravity / spatial-interaction model (flow ∝ mass·mass / distance², a Newton analog) is established in economics and geography (Tinbergen's gravity model of trade; Wilson's spatial-interaction models) `[t]`. Direct application to *agent routing or retrieval* is the speculative leap — I did not find it published, treat as `OPEN`/unverified. The empirical *consequence* (drift becomes self-reinforcing without a stabilizing mechanism) is documented (Agent Drift, arXiv:2601.04170) and "stable anchor models" emerge in multi-agent annotation studies — the dominant-mass phenomenon observed but not named as n-body. `OPEN` (n-body→bus argument) · `THEORY` · `[v]` for the consequence, `[t]` for the gravity-model lineage

**Production.** None. This is an architectural-justification result, not a component.

> **NOTES (majkee):**
>

---

## I.5 — Nabla (grad, div, curl + the fourth operator)

**Concept.** Define a relevance scalar field `Q` and an information-flow field `F` over semantic space. Then: **grad** `∇Q` = steering direction (progress = ascent toward goal; drift = motion against). **div** `∇·F` = pollution *localizer* — a persistent positive-divergence source in a low-`Q` region is content being spawned where it doesn't belong (hallucination/tangent), and divergence gives its coordinates, not just its existence. **curl** `∇×F` = loop detector — healthy flow is irrotational (conservative, path-independent progress); **non-zero curl is circular reasoning made measurable.** The fourth operator you sought (your "own convergence") is the **material derivative** `D/Dt = ∂/∂t + (v·∇)`: it splits change into genuine local change (`∂/∂t` — an agent truly reconsidered) versus advective drift (`(v·∇)` — swept along by the conversation's current). That separation *is* drift diagnosis at the root.

**Mapping.** The whole diagnostic layer. curl → loop alarm; div → pollution-source coordinates; material derivative → "did this agent change its mind, or just get carried?"; grad → steering signal for actuation.

**Prior art.** grad + curl on *transition graphs* is defined in RL theory — a discounted curl where conservative reward fields have zero curl and potential shaping is a gradient (Calculus on MDPs, arXiv:2208.09570). Divergence-of-a-semantic-field appears, vaguely, in patent literature ("semantic drift entropy"). The material-derivative split (`∂/∂t` vs `(v·∇)`) applied to dialogue drift I did **not** find — the field uses single-scalar drift (arXiv:2512.10350) and is explicitly moving "beyond scalars" (arXiv:2603.10384). `REPURPOSED` (grad/div/curl) / `OPEN` (material derivative for drift) · `OPERATIONALIZE` · `[v]`

**Production.** None. Discrete vector-calculus on graphs is implementable (discrete exterior calculus libraries, `PyDEC`), but mapping to a noisy embedding flow is unproven — this is the operationalization risk.

> **NOTES (majkee):**
>

---

## I.6 — RLC circuit analogy

**Concept.** Map the orchestrator's feedback to an RLC circuit (rigorous once you write the transfer function `H(s)`). **R** = dissipation (summarizer/rate-limiter discarding redundancy). **C** = high-pass element (blocks the steady "DC" background, passes novelty). **L** = low-pass element / inertia (blocks jitter, passes steady direction — the same mass as I.4). Together: a second-order system with damping ratio `ζ`. Underdamped (`ζ<1`) = overshoot, ping-pong. Overdamped (`ζ>1`) = sluggish stall. **Critically damped (`ζ=1`) = fastest settle, no oscillation — the tuning target.** The RLC values, the s-plane poles, and `H(s)` are one object: right-half-plane poles = runaway, imaginary-axis poles = sustained ping-pong, left-half-plane = convergence.

**Mapping.** The control frame for the orchestrator. Tuning feedback gains = choosing R, L, C to land on `ζ=1`. A single boolean (any RHP pole?) is a runaway alarm.

**Prior art.** Control-theory ↔ LLM is now explicit: both are dynamical systems with controllability/observability/stability, state-space models enabling bounded-output analysis (*When Control Meets LLMs*, EAAI 2026). The RLC/damping framing specifically I did not find for agent loops — `OPEN` on the specific analogy, `BORROWED` on the underlying second-order control theory. `BORROWED`/`OPEN` · `OPERATIONALIZE` (ζ=1 is a continuous-time ideal; agent loops sample coarsely and irregularly, which may shift the achievable optimum) · `[v]`

**Production.** Classical control tooling (`python-control`, `scipy.signal`) handles the math. No agent framework exposes a damping-ratio tuner.

> **NOTES (majkee):**
>

---

## I.7 — Associative relations (self-extraction, cascade)

**Concept.** "Self-extracting from a cue" = associative memory: store a pattern, recall the whole from a partial wording. Modern Hopfield networks are provably equivalent to softmax attention — so this is the substrate *under* the tokenizer; a wording is a partial cue pulling a full stored pattern out of an energy landscape whose basins are the associations. **Those basins are I.4's gravity wells — same math, smaller scale.** The "cascade" is a branching process: one activation triggers associated ones. Whether it dies or explodes is set by the **branching ratio ρ = spectral radius of the excitation kernel** (back to I.1). Subcritical (`ρ<1`) = under-association; supercritical (`ρ>1`) = runaway tangent = context pollution; critical (`ρ=1`) = rich but controlled, the edge of chaos.

**Mapping.** Associative recall = the retrieval mechanism (Part II). The branching-ratio monitor = a concrete, theory-grounded pollution alarm on the bus.

**Prior art.** Hopfield ≡ attention: Ramsauer et al., *Hopfield Networks is All You Need* (arXiv:2008.02217) `[t]`. Criticality / branching-ratio-at-unity: neuronal-avalanche theory (Beggs & Plenz 2003; Bertschinger & Natschläger 2004) — a branching parameter near 1 optimizes information transmission while preventing runaway excitation `[v]`. Applying ρ as an *LLM context-pollution alarm* specifically is the new use; the mechanism is borrowed. `BORROWED` · `BUILD-NOW` (ρ is estimable from cascade size distributions) · `[v]`

**Production.** Hopfield layers ship in `hopfield-layers` (Python). Branching-ratio estimation has neuroscience tooling (`MR. Estimator` / Wilting–Priesemann). No agent product monitors ρ.

> **NOTES (majkee):**
>

---

## I.8 — Non-Boolean aggregation ("3 of 5, but which 3")

**Concept.** "Pass when ≥3 of 5, but *which* 3 matters, and 2-of-5 ≠ 1-of-5" is not plain fuzzy logic (still pointwise). The exact object is a **fuzzy measure (capacity) aggregated by the Choquet integral**: a capacity `μ` assigns weight to *every subset*, so `μ({1,3}) ≠ μ({1}) + μ({3})` — synergy and redundancy encoded directly, which is precisely "which 3." For *which voters matter*, compute each input's **Shapley or Banzhaf value** over `μ` — equal values = identity-blind gate; unequal = identity is load-bearing, and the index says by how much. For fusing noisy multi-agent evidence, **Dempster–Shafer** belief functions assign mass to *sets* of hypotheses and combine super-additively — "2 ≠ 1" by construction.

**Mapping.** The consensus gate. This is the single most buildable piece with the most exact fit to your phrasing.

**Prior art.** Choquet-integral classifier fusion is decades deep (Grabisch 1996 and the fusion literature). Applied to LLMs: fuzzy Choquet integral over a non-additive measure for combining conflicting LLM evidence (arXiv:2506.05675). Dempster–Shafer decision fusion is well-established. `BORROWED` · `BUILD-NOW` · `[v]`

**Production.** `pyfume`, `scikit-fuzzy` (partial), and bespoke capacity-learning code. Capacity learning is the only engineering cost: a full measure has `2^N − 2` free parameters, so the 2-additive Choquet restriction (Möbius representation) is the tractable compromise — at the cost of capping expressible synergies.

> **NOTES (majkee):**
>

---

# Part II — The RAG Engine (the build in flight)

This is the "real brain, not nice pictures" — the part you're mid-build on. It is field dynamics (Part I) realized as retrieval.

## II.1 — The substrate inversion (your design stance)

Agent outputs → normalized JSONL lines, one per turn. **The JSONL line is canonical** (truth lives in files); a vector representation rides on top as a derived "language" — a coordinate, not the source of truth; the association **graph over the lines is the brain.** This inverts the usual vector-DB hierarchy. It aligns with a documented production pattern: Graphiti/Zep store every fact tracing back to *episodes — the raw ingested ground-truth stream*, and a real strand of practitioners argues *files alone work well enough and graph tooling adds complexity without proportional benefit*. Your stance sits knowingly on that fault line. `YOURS` (the specific inversion + file-canonical discipline) · `[v]`

## II.2 — Diffusion / heat-kernel retrieval (the core mechanism)

Seed activation on the nodes a query matches; spread by `exp(−tL) = Σ exp(−tλᵢ) vᵢvᵢᵀ`. Two units are close when *many short associative paths* connect them — **diffusion distance** (Coifman–Lafon 2006), synaptic reach as a metric. Time `t` = associative-spread knob; spectral gap `λ₂` sets mixing time. Spreading activation ≈ graph diffusion ≈ heat kernel ≈ Laplacian spectrum.

**Prior art — your closest wheel.** HippoRAG (arXiv:2405.14831) and HippoRAG 2 (arXiv:2502.14802) run **Personalized PageRank** — the resolvent propagator `(I−αW)⁻¹`, a sibling of the heat kernel — over a knowledge graph for hippocampal-style *pattern completion*. The retrieval mechanism is **not novel**. What differs in your use: the corpus is *agent turns on a file-backed bus*, not document passages — an orchestration brain, not a QA front-end. `BORROWED` (mechanism) / `YOURS` (orchestration application) · `BUILD-NOW` · `[v]`

## II.3 — Spectral clustering for coherent retrieval

Fiedler vector + first `k` nontrivial eigenvectors retrieve a *coherent connected neighborhood*, curing top-k cosine's failure mode (chunks each similar to the query but mutually incoherent). `BORROWED` · `BUILD-NOW` · `[v]`

## II.4 — Laplacian eigenmap embedding

Coordinates derived purely from connectivity — no front-matter vector anywhere. The most direct rebuttal to the vectors-in-front-matter approach (Obsidian-style). `BORROWED` (Belkin–Niyogi) · `BUILD-NOW` · `[t]`

## II.5 — Spectral sparsification

Low-rank projection onto dominant eigenvectors denoises spurious weak edges; the eigenvalue dropoff reports the corpus's intrinsic dimensionality. `BORROWED` · `BUILD-NOW` · `[t]`

## II.6 — The hybrid architecture (honest performance boundary)

Pure-associative does **not** beat a good embedding model on single-hop lookups — cosine ANN is faster and sufficient there. It wins decisively on **multi-hop**: two units textually dissimilar but bridged through intermediates no single vector comparison sees. So: vectors demoted to cheap first-hop candidate generation, spectral diffusion on the graph doing multi-hop expansion and coherence. **Subordinate the vectors; don't delete them.** This mirrors LightRAG's dual-level (low-level fact + high-level semantic) retrieval. `BORROWED` (hybrid is standard) / `YOURS` (the file-canonical version) · `BUILD-NOW` · `[v]`

## II.7 — The append-only reconciliation (your A2 invariant vs. the spectrum)

Eigendecomposition is `O(n³)` and not incremental — appending a node invalidates a precomputed spectrum, contradicting append-only if the spectrum is global state. Resolution: **two paths.** *Runtime (append-safe):* diffuse from query seeds on the live graph each call, no global precompute — Chebyshev-polynomial approximation of the graph filter (ChebNet trick) applies the heat kernel without forming an eigenvector; Lanczos for genuine bottom-`k`. *Batch (scheduled):* recompute the global embedding/clustering only on a cadence, tolerating staleness for the coherence view. `YOURS` (the reconciliation, given your invariant) · `OPERATIONALIZE` (crossover scale where even runtime is too slow is unmeasured) · `[v]`

## II.8 — RAG engine prior-art & production map

| Your element | Nearest research | Nearest production | Relation to your approach |
|---|---|---|---|
| Associative graph + PPR recall | HippoRAG / HippoRAG 2 | Cognee, Mem0ᵍ | Same mechanism; they do doc-QA, you do agent coordination |
| Knowledge-graph RAG, communities | GraphRAG (Edge 2024), LightRAG, PathRAG | Microsoft GraphRAG lib, LlamaIndex PropertyGraph, Neo4j | Mature; heavier ingestion than your lean target |
| Temporal graph, episode→fact provenance | Zep (arXiv:2501.13956) | **Zep / Graphiti** (OSS) | Closest to your "truth-in-files, validity windows, trace to raw"; expensive ingestion |
| Sentence-level dialogue graph | SGMem (2025) | — | Close to JSONL-line-as-node |
| Zettelkasten-style evolving notes | A-MEM (2025) | Obsidian (manual) | Your file-backed notebook lineage |
| Heat-kernel / diffusion distance | Coifman–Lafon (2006) | — (DIY: scipy/networkx) | The math under II.2; no product exposes it |
| Long-mem benchmarks | LongMemEval, LOCOMO, BEAM | — | Use these to test your engine honestly |

**Stack note `[v]`:** Mem0 advertises an MCP server reachable from Claude Code — relevant to your subscription-token policy boundary (a bolt-on memory layer is API-metered infrastructure, green-zone vs. commercial depends on usage pattern, same framework you've been working under). Zep/Graphiti is OSS and self-hostable, which fits the lean/local ethos better than a metered cloud.

> **NOTES (majkee):**
>

---

# Part II-B — The Fourth Spine: Coherence / Identity

Spines I–III (Part III) describe the dynamics *of* a system — how the field flows, how the trajectory stays stable, how evidence fuses. This spine is orthogonal: it describes the condition for the thing to **remain one system** under noise, drift, and entropy. It is the floor under three commitments you arrived at separately — triangulation (consistency), append-only history (the durable boundary), and files-vs-streams (the boundary that exchanges). Its unified home is applied category theory + topology: sheaves are *consistency*, operads are *composition*, Markov categories/blankets are the *boundary*, optimal stopping is *termination* — all of it about how complexity stays coherent. The structural keystone: the **sheaf Laplacian (I.9) strictly generalizes the graph Laplacian (I.1)**, so the entire field-dynamics spine lifts onto this one the moment your agents have heterogeneous internal frames (different brands, different representations) — which they do.

---

## I.9 — Sheaf consistency (local→global gluing)

**Concept.** Assign data to each node and edge of the graph; *restriction maps* say how each node's local data projects into a shared comparison space on the edges. The **sheaf Laplacian** measures *discord* — how far each node is from harmony with its neighbours — and its kernel, the **zeroth cohomology H⁰**, is the space of *global sections*: assignments where all local views agree. A **non-trivial cohomology class is the formal obstruction to consensus** — disagreement that cannot be glued, i.e. genuinely irreconcilable rather than merely frame-different. Strictly generalizes I.1: the ordinary graph Laplacian is the special case where every agent shares one frame and all restriction maps are the identity.

**Mapping.** Your blind triangulation, formalized — and upgraded. It supplies the measurement your current method lacks: the difference between two agents disagreeing because they use **different valid frames** (reconcilable — glue through the restriction maps) versus **genuinely contradicting** (no global section exists; the obstruction is real). Heterogeneous stalks = agents with different internal representations, which is exactly the Gemini-and-Claude case.

**Prior art.** Hansen & Ghrist, *Opinion Dynamics on Discourse Sheaves* (arXiv:2005.12798) — sheaf Laplacian as discord, H⁰ as harmonized consensus, relative cohomology as agent-independence, and it even encodes exaggeration/obfuscation/"learning to lie." Spectral theory of the sheaf Laplacian (Hansen–Ghrist 2019). Active 2025–26 control front: *Distributed Multi-agent Coordination over Cellular Sheaves* (arXiv:2504.02049), *Multi-Agent System Identification with Nonlinear Sheaf Diffusion* (arXiv:2605.11204) — the nonlinear sheaf Laplacian now subsumes consensus, formation, opinion dynamics, tracking in one operator. *Neural Sheaf Diffusion* (Bodnar et al., 2022) for the ML side. Applied to social networks, control, robotics, distributed optimization — **not** to LLM multi-agent systems, which is the open ground: mature math, unoccupied application. `BORROWED` (math) / `OPEN` (LLM application) · `OPERATIONALIZE` → `THEORY` (defining the restriction maps over embedding frames is the real work) · `[v]`

**Production.** `PySheaf`, TDA tooling for the computation; nothing agent-facing. The sheaf Laplacian on a small N (2–4 agents) is cheap.

> **NOTES (majkee):**
> _(cross-link: the shared comparison stalk can be the stance-sphere — Atlas №2, fork 1. Restriction maps = the rotations into each agent's frame.)_

---

## I.10 — Active inference / free energy / Markov blanket (the boundary)

**Concept.** A system holds its identity by **minimizing variational free energy** — an information-theoretic upper bound on *surprise* (how far reality departs from the system's own model). Drift, in this language, is literally *rising free energy*: an agent wandering into states its model didn't predict. The **Markov blanket** is the statistical boundary separating internal states from external ones, permitting exchange only through sensory + active states. Completes the thermodynamics the other spines half-built (energy, dissipation, criticality) by adding their missing sibling: *information*.

**Mapping.** A candidate single variational potential *under* the three spines — the gravity well (I.4) reread as a free-energy descent. The blanket is the formal version of A3: internal truth screened from the world (files), exchanging only across a boundary (streams). Drift alarm = free-energy rate.

**Prior art.** Friston's FEP (Nat. Rev. Neurosci. 2010; *Markov blankets of life*, J. R. Soc. Interface 2018). LLM-applied, recently and directly: *Orchestrator: Active Inference for Multi-Agent Systems in Long-Horizon Tasks* (arXiv:2509.05651); *Language-Mediated Active Inference* for safer AGI with agents composed through hierarchical Markov blankets (arXiv:2508.05766); Suri et al. (2022) stabilizing multi-agent interaction by collective free-energy minimization. **Caveat, enforced by the literature itself:** the FEP is contested and frequently overclaimed as a universal law — recent work (*Markov Blanket Density* arXiv:2506.05794; *The Markov Blanket Trick*) exists to *constrain* its scope, reframing it as an emergent regime permitted by the environment, not an imperative. Use as a unifying lens; do not put load-bearing structure on it being a law. `BORROWED` · LLM-applied · `[v]`

**Production.** `pymdp`, `RxInfer.jl` (active-inference toolboxes); not productized for LLM orchestration.

> **NOTES (majkee):**
>

---

## I.11 — Operadic composition (well-formedness)

**Concept.** Systems as boxes with *typed ports*, wires as interconnections, composition governed by operad laws (associativity, identity, interchange); an *algebra* over the operad assigns semantics (e.g. differential equations) to the wiring. Your bus — agents as boxes, streams as typed wires — *is* a wiring diagram. What it buys that you don't have now: a way to check a composition is **well-formed before runtime** (interfaces match, composite behaviour follows from the parts) instead of discovering at runtime that two daemons don't fit.

**Mapping.** The formal grammar of the bus. Interface-typing on the streams; compositional guarantees on the daemon network. Markov categories (the probabilistic flavour) bridge directly to I.10 — they are the categorical form of active inference.

**Prior art.** Spivak's operad of wiring diagrams (boxes-and-ports as a symmetric monoidal category); Baez–Fong compositional frameworks for networks and Markov processes; *Operads for Designing Systems of Systems* (Baez–Foley 2021); *Operadic modeling of dynamical systems* (Libkind–Patterson–Fairbanks 2021). Markov categories (Fritz and successors) for compositional Bayesian inference. Applied to control, networks, dynamical systems — not LLM-specific, but the formalism fits the bus as-is. `BORROWED` · systems-applied, not LLM-specific · `[v]`

**Production.** `Catlab.jl` / the AlgebraicJulia ecosystem — real, maintained tooling for operads, wiring diagrams, symmetric monoidal categories.

> **NOTES (majkee):**
>

---

## I.12 — Optimal stopping / backtracking (halt and revert)

**Concept.** "When is the bus *done*" is a **stopping time** (Wald's sequential analysis; the secretary problem). "When do we backtrack" is sequential decision under uncertainty. Your own instinct — at a blind street, "a fine time to turn back and go a few steps back" — is this object, reasoned by feel.

**Mapping.** The orchestrator's halt/revert policy. Couples directly to the adaptive-loop-count-by-difficulty you already run (one loop for light problems, several for heavy ones is an implicit stopping rule).

**Prior art.** Optimal stopping theory (Wald; Chow–Robbins; secretary problem) — bounded and well-understood `[t]`. An LLM-specific "adaptive computation / when to stop reasoning" line exists (e.g. adaptive computation time, and 2025–26 "when to stop" reasoning work) which I did **not** re-verify this session — treat as a lead. `BORROWED` · `OPERATIONALIZE` · `[t]`

**Production.** None specific; the classic algorithms are trivial to implement directly.

> **NOTES (majkee):**
>

---



The eight instruments collapse into three spines sharing one object.

**Spine I — Field dynamics on the semantic manifold.** I.2 builds the space, I.5 operates on it, I.1's Laplacian *is* `∇²` on the graph, I.4's gravity is its potential. One object: a field with potential (gravity), gradient (steering), curl (looping), divergence (pollution); spectral methods diagonalize its Laplacian.

**Spine II — Dynamical systems & stability.** I.6 is the differential equation, I.3's poles are its eigenvalues, I.1-as-signal is the trajectory's Fourier view, I.4-as-mass is inertia, and I.5's material derivative lives here. One object: a feedback loop whose stability you read off the complex plane and tune to critical damping.

**Spine III — Evidence, association, aggregation.** I.7 (attractor recall + cascade) and I.8 (non-additive aggregation), bridged to I.1 by spectral radius. One object: how a cue retrieves a pattern, how activation cascades sub-/super-critically, how partial signals fuse into a decision.

**Spine IV — Coherence / Identity (Part II-B).** Orthogonal to I–III: they are the dynamics *of* a system, this is the condition for it to *stay one system*. I.9 (sheaf) = consistency (do local views glue); I.10 (FEP/blanket) = boundary + inference (what separates inside from outside, and surprise-minimization); I.11 (operad) = composition (are the parts wired well-formedly); I.12 (stopping) = termination (when is it done). The sheaf Laplacian generalizes I.1's graph Laplacian, so Spine I lifts onto Spine IV the moment agents carry heterogeneous frames. Unified home: applied category theory + topology.

**The floor under all three.** Spine I (landscape) and Spine II (trajectory through it) are dual — gravity in both. Spine III is the discrete shadow of I — its basins are I's wells, its branching ratio is the spectral radius on the other side of the bridge. At bottom: **one energy landscape over semantic space, a feedback-controlled trajectory flowing through it, discrete evidence-aggregation deciding the transitions.**

**The single health scalar.**
```
health = f( curl_magnitude,         # circular-reasoning detector   (I.5)
            right_half_plane_pole,  # runaway-drift boolean         (I.6)
            branching_ratio ρ,      # context-pollution alarm       (I.7)
            cohomology_obstruction )# do agents' views glue?        (I.9)
```
The anti-drift policy, stated mathematically: **keep the flow curl-free, keep the loop critically damped, keep the cascade branching ratio below one — and keep the consensus obstruction at zero (a global section exists).** The first three are Spines I–III; the fourth is Spine IV, and it answers a question the others can't: not *is the trajectory healthy* but *do the agents still describe one reconcilable world*.

---

# Part IV — Master Prior-Art / Production Map

The at-a-glance answer to *"is this already invented?"* — **yes, in parts; the integration is the open ground.**

| Instrument | Maturity | Nearest research | Nearest production |
|---|---|---|---|
| I.1 Spectral analysis | BORROWED | spectral clustering; geometric-dynamics (2512.10350) | scikit-learn, scipy |
| I.2 Tensor algebra | BORROWED | Kolda–Bader; InfTucker email tensors | TensorLy |
| I.3 Complex / phasor | OPEN/BORROWED | complex-valued NNs; s-plane control | — |
| I.4 Gravity / n-body bus | OPEN | Agent Drift (2601.04170); gravity model `[t]` | — |
| I.5 Nabla operators | REPURPOSED/OPEN | Calculus on MDPs (2208.09570) | PyDEC (DIY) |
| I.6 RLC / damping | BORROWED/OPEN | When Control Meets LLMs (2026) | python-control |
| I.7 Associative + ρ | BORROWED | Hopfield≡attention; Beggs–Plenz | hopfield-layers, MR.Estimator |
| I.8 Choquet gate | BORROWED | Grabisch; LLM fuzzy fusion (2506.05675) | scikit-fuzzy, DIY |
| I.9 Sheaf consistency | BORROWED / OPEN | Hansen–Ghrist discourse sheaves (2005.12798) | PySheaf (DIY) |
| I.10 Active inference / blanket | BORROWED | Orchestrator (2509.05651); Friston FEP | pymdp, RxInfer.jl |
| I.11 Operadic composition | BORROWED | Spivak wiring diagrams; Baez–Fong | Catlab.jl / AlgebraicJulia |
| I.12 Optimal stopping | BORROWED | Wald; secretary problem `[t]` | — |
| II RAG engine | BORROWED + YOURS | HippoRAG 1/2; GraphRAG; Zep | Cognee, Zep/Graphiti, Mem0 |
| Three-spine unification | YOURS | — (no unified curl+pole+ρ readout found) | — |
| Fourth-spine (coherence) application | YOURS / OPEN | sheaf Laplacian ⊃ graph Laplacian; no LLM coherence-spine found | — |
| File-backed agent-bus application | YOURS | memory work targets doc-QA, not orchestration | — |

**Invented mathematics: none. Contribution: integration, application to a file-backed append-only bus, and operator-level granularity where the field still uses scalars.** The borrowed-ness is a strength — each part is battle-tested, so risk lives in the seams, where it belongs.

---

# Part V — The Fork Menu (pick one to go deep)

Each is a candidate for the next reference-stone (full derivation + file/stream boundary + minimal walking-skeleton). Listed with honest readiness so you choose with eyes open.

1. **Choquet consensus gate** — `BUILD-NOW`. The only piece with zero theory gaps; exact fit to "which 3 of 5." Lowest risk, fastest to a working artifact. *Best if you want a usable component this week.*

2. **Curl loop-detector** — `OPERATIONALIZE`. The crown-jewel diagnostic. Needs mapping the MDP-theoretic discounted curl onto a noisy embedding trajectory, with a separability test against existing classifier-based loop detectors (arXiv:2601.05693). *Best if you want the most distinctive idea.*

3. **n-body → central-bus stability proof** — `THEORY`. Formalize "a dominant central mass tames the chaos" into a stated proposition. Pure reasoning, no code, but it *justifies your whole architecture*. *Best if you want the foundation argument.*

4. **Critical-damping tuner** — `OPERATIONALIZE`. Whether `ζ=1` is reachable under coarse, irregular agent-loop sampling. Couples directly to your existing turn-completion / acknowledgment loop. *Best if you want to improve the orchestrator you already run.*

> **PICK (majkee):**
>

---

# Part VI — Running Scratchpad

_Open space. Drop ideas, dead-ends, "fine ideas during development," benchmark numbers, decisions to revisit._

>
>
>

---

### Entry template — copy this for any new instrument you add

```
## I.N — <name>

**Concept.** <the math, terse>

**Mapping.** <how it applies to the bus / RAG>

**Prior art.** <named research> · STATUS · BUILD-READINESS · [v]/[t]

**Production.** <tools, or "none">

> **NOTES (majkee):**
>
```

---

*End of atlas. Living document — extend freely; the structure is the point, not the current contents.*
