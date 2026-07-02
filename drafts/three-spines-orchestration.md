# The Three Spines

### A Continuum-Mechanics Architecture for Multi-Agent Orchestration over a File-Backed Substrate

*Conceptual paper — Nabla & majkee. Drafted 2026-06-25. Status: positioning document, not an empirical result. Prior-art claims verified against literature current to mid-2026; mark any volatile claim that ages out as `[unverified · training-era]` on re-read.*

---

## 0. Thesis

A multi-agent system is usually engineered as plumbing: queues, routers, retries, JSON schemas. This paper argues that the plumbing is the wrong abstraction layer for the failure modes that actually matter — drift, context-pollution, circular reasoning, and consensus collapse — and that all four are more naturally read as the behaviour of a **field over a semantic manifold** and a **feedback-controlled trajectory** moving through it. The eight mathematical instruments that motivated this work (spectral analysis, tensor algebra, complex analysis, a gravity/potential analogy, the nabla operator, an RLC-circuit analogy, associative recall, and a non-Boolean aggregation rule) are not eight separate ideas. They collapse into **three spines** sharing one underlying object, and the architecture's anti-fragility comes from that collapse, not from any single instrument.

The contribution claimed here is explicitly *synthesis and application*, not new mathematics. Every operator below already exists in an established discipline. What does not yet exist in the literature — as of mid-2026 — is (i) the unification of these spines into a single object exposing a single health scalar, (ii) its application to a **file-backed, append-only agent bus** rather than to document question-answering, and (iii) diagnostic granularity at the level of differential operators where the surrounding field still uses coarse scalar metrics. Sections 8 and 9 draw that boundary honestly.

---

## 1. Substrate axioms

The architecture inherits four invariants from the operational philosophy it was designed under. They are not decoration; each one constrains the mathematics that follows.

**A1 — The text contract.** Every inter-agent payload is plain text. If two components can emit and consume text, they can be piped, multiplexed, and recombined without bespoke adapters. This is what makes the substrate a *measurable* object: a uniform medium admits a uniform metric.

**A2 — Append-only history.** State is never mutated in place; it is appended and filtered on read. The durable record is a monotonic timeline. This invariant collides productively with the spectral machinery of Spine I — eigendecomposition is not incremental, so the architecture must separate a *runtime* path (recomputed per call on the live graph) from a *batch* path (periodic global recompute). Section 4.4 resolves this.

**A3 — Truth lives in files, resonance lives in streams.** Durable memory is file-backed (`.jsonl`, `.md`); live duplex negotiation between agents happens in streams (PTYs, sockets, multiplexer panes). The two are complementary, not competing. The field (Spine I) is reconstructed from files; the trajectory (Spine II) is observed in streams; the decision (Spine III) is condensed back to a file. The whole loop is *stream to find consensus, file to remember it*.

**A4 — Single responsibility.** Each operator does one thing. The curl detector does not also summarize; the summarizer does not also route. This keeps the diagnostic layer decoupled from the actuation layer and lets the health scalar of Section 7 be assembled from independent, individually-testable measurements.

### 1.1 The substrate, concretely

Agent outputs are normalized into JSONL lines — one line per turn, per agent. This is the load-bearing design choice and it differs from the prevailing associative-memory-RAG systems (HippoRAG and successors, which index *document passages*). Here the JSONL line **is** the durable substrate, and a vector representation rides on top of it as a derived "language" — a coordinate, not the source of truth. The graph is built over these lines. The embeddings are demoted to a cheap index into a structure whose authority is the file. This inverts the usual vector-DB hierarchy: the file is canonical, the vector is a lens, and the graph is the brain.

---

## 2. The shared object

Define a semantic space `M` — in practice the embedding space of the substrate's content units, treated as a manifold or, in its discrete approximation, a weighted graph `G = (V, E, W)` whose nodes are content units (agent turns, claims, atomic notes) and whose edge weights `W` encode association strength.

Over `M` the architecture places three coupled structures:

1. A **scalar potential** `Φ` and the fields derived from it — the landscape (Spine I).
2. A **trajectory** `x(t)` through `M`, governed by a feedback law — the path (Spine II).
3. A **discrete evidence-aggregation** rule deciding transitions — the gate (Spine III).

The central claim of Section 7 is that these three are not independent: the landscape and the trajectory are dual (the same `Φ` governs both), and the gate is the discrete shadow of the landscape, with one spectral quantity — the spectral radius — appearing on both sides.

---

## 3. Notation

| Symbol | Meaning |
|---|---|
| `M` | semantic space (manifold or its graph approximation `G`) |
| `Φ(p)` | scalar potential at point `p` — encodes goal-attraction |
| `Q(p)` | relevance scalar field (closeness to task objective) |
| `F(p)` | information-flow vector field over `M` |
| `L = D − W` | graph Laplacian of `G` (`D` = degree matrix) |
| `λ_i, v_i` | eigenvalues / eigenvectors of `L` |
| `λ₂` | Fiedler value (algebraic connectivity; mixing-rate proxy) |
| `D/Dt` | material derivative, `∂/∂t + (v·∇)` |
| `ζ` | damping ratio of the second-order control loop |
| `μ(A)` | fuzzy measure (capacity) of input subset `A ⊆ N` |
| `ρ` | branching ratio = spectral radius of the excitation kernel |

---

## 4. Spine I — Field dynamics on the semantic manifold

This spine absorbs four of the original instruments: tensor algebra (it builds the space), the nabla operator (it operates on the space), spectral analysis (it diagonalizes the space's Laplacian), and the gravity analogy (it is the space's potential).

### 4.1 The potential and its gradient

Commit to an actual potential `Φ`, not a loose "attraction" metaphor — the rigor is entirely contingent on writing `Φ` down. Let the task objective sit at a minimum of `Φ`; each agent is a body in this potential with mass equal to its authority/effort; semantic distance is distance. Then:

- **grad** `∇Q` is the steering direction. Progress is gradient descent on `Φ` (equivalently ascent on relevance `Q`). Drift is sustained motion *against* the gradient.
- **div** `∇·F` localizes pollution. A persistent positive-divergence source sitting in a low-`Q` region is content being *spawned* where it has no business being — the signature of a hallucination or tangent. Divergence does not merely flag that pollution exists; it gives its *coordinates*.
- **curl** `∇×F` is the loop detector. Healthy multi-agent flow should be irrotational: progress is path-independent, so the field is conservative and `∇×F = 0`. **Non-zero curl is circular reasoning made measurable.** This is not a free invention — reinforcement-learning theory already defines a discounted curl on transition graphs, where conservative reward fields have zero curl and potential shaping is exactly a gradient (Calculus on MDPs, arXiv:2208.09570). The contribution here is repurposing it from reward-shaping to dialogue-drift diagnosis.

### 4.2 The fourth operator — the missing piece

The instrument originally sought as "my own convergence operator" beyond grad/div/curl already exists and is precisely the right tool: the **material derivative**

```
D/Dt = ∂/∂t + (v·∇)
```

It decomposes change into two physically distinct sources. The `∂/∂t` term is *genuine local change* — an agent actually revised its position. The `(v·∇)` advective term is *change due to being swept along by the current* — an agent that did not reconsider anything but got carried by the conversation's flow. **That decomposition is drift diagnosis at its root.** The surrounding literature (e.g. the agentic-loop dynamics work, arXiv:2512.10350) measures drift as a single scalar — similarity to the previous step. The material derivative says *why* the system drifted, separating conviction from convection. If a named bespoke operator `⊙` is still wanted, define it as a contraction rate `⊙ ≡ −d/dt Var(agent states)`, positive when trajectories pull together — but this is composing known operators, and the material derivative is the deeper answer.

### 4.3 The spectral layer

The graph Laplacian `L = D − W` is the linear algebra a graph runs on, and its spectrum is the engine, not a bolt-on:

- **Spectral clustering.** The Fiedler vector (eigenvector of the second-smallest eigenvalue) gives the natural cut — "which context belongs to which sub-task." The first `k` non-trivial eigenvectors retrieve a *coherent connected neighborhood*, curing top-k cosine's failure mode of returning chunks each individually similar to the query but mutually incoherent.
- **The Laplacian is `∇²` on the graph.** This is the formal bridge to Section 4.1: spectral methods are not a separate technique from the field operators; they *are* the discrete differential geometry of the same field.
- **Spectral sparsification.** Low-rank projection onto dominant eigenvectors denoises spurious weak edges, and the eigenvalue dropoff reports the corpus's intrinsic dimensionality — how many dimensions the knowledge actually occupies.

### 4.4 Associative retrieval as diffusion — and the append-only reconciliation

The cleanest realization of "associations, not vectors" is **diffusion / heat-kernel retrieval**. Seed activation on the nodes a query matches, then spread it by the propagator `exp(−tL) = Σ exp(−tλ_i) v_i v_iᵀ`. Two units become close not when their text is similar but when *many short associative paths* connect them — this is **diffusion distance** (Coifman–Lafon), literal synaptic reach turned into a metric. The time `t` is the associative-spread knob; the spectral gap `λ₂` sets the mixing time, so you know what a given `t` buys. This is spreading activation from cognitive science made rigorous: spreading activation ≈ graph diffusion ≈ heat kernel ≈ governed by the Laplacian spectrum.

**Prior art, named honestly.** This is essentially the mechanism of HippoRAG (arXiv:2405.14831) and HippoRAG 2 (arXiv:2502.14802), which run **Personalized PageRank** — the resolvent propagator `(I − αW)⁻¹`, a sibling of the heat kernel — over a knowledge graph to perform hippocampal-style *pattern completion*. The retrieval mechanism is therefore **not novel**. Two things distinguish the present use: (i) the corpus is *agent turns on a file-backed bus*, not document passages, making this an orchestration brain rather than a QA front-end; (ii) the substrate is canonical (A1–A3), so retrieval is a lens over files rather than the system of record.

**The A2 collision and its resolution.** Eigendecomposition is `O(n³)` and not incremental; appending a node invalidates a precomputed spectrum. This directly contradicts the append-only invariant if the spectrum is treated as global state. The resolution is a two-path split:

- **Runtime path (append-safe).** Diffuse from the query's seed nodes on the *live* graph each call, with no global precompute. Chebyshev-polynomial approximation of the graph filter (the ChebNet trick) applies the heat kernel without ever forming an eigenvector; Lanczos handles the genuine bottom-`k` need. This path honors A2 — it reads the current file-backed edge list and computes on demand.
- **Batch path (scheduled).** Recompute the global embedding / clustering view only on a cadence, accepting staleness between runs. This is for the *coherence* view, which tolerates lag.

The honest performance boundary: pure-associative retrieval does **not** beat a good embedding model on single-hop lookups, where cosine ANN is faster and sufficient. It wins decisively on **multi-hop** — two units textually dissimilar but bridged through a chain of intermediates that no single vector comparison sees. The defensible architecture is therefore hybrid: vectors demoted to cheap first-hop candidate generation, spectral diffusion on the association graph doing multi-hop expansion and coherence. Subordinate the vectors; do not delete them.

---

## 5. Spine II — Dynamical systems and stability

This spine absorbs the RLC-circuit analogy (it is the differential equation), complex analysis (its poles are the equation's eigenvalues), spectral-analysis-as-signal (the Fourier view of the trajectory), and the inertial half of the gravity analogy (mass as inductance).

### 5.1 The circuit as the control frame

Map the orchestrator's feedback elements to an RLC circuit, where the rigor is again contingent on writing the actual transfer function `H(s)`:

- **R — dissipation.** A summarizer or rate-limiter that discards redundancy. Damps energy.
- **C — a high-pass element.** A buffer that blocks the steady background ("DC") and passes change — it responds to *novelty* and ignores repetition.
- **L — a low-pass element.** Inertia in throughput: blocks rapid jitter, passes steady direction. This is the *same mass* as Spine I's gravity, viewed dynamically.

Together they form a second-order system with damping ratio `ζ`:

- `ζ < 1` (underdamped) — overshoot and ping-pong before settling.
- `ζ > 1` (overdamped) — sluggish; the conversation stalls.
- `ζ = 1` (**critically damped**) — fastest settle with no oscillation. **This is the tuning target.** Choosing the orchestrator's feedback gains *is* choosing R, L, C to land on `ζ = 1`.

### 5.2 The complex plane unifies it

The RLC values, the poles of `H(s)` in the complex `s`-plane, and the transfer function are one object viewed three ways — this is where complex analysis earns its place (it has no standalone role here; its entire value is the phasor and pole lenses). Read stability directly off pole location:

- **Right-half-plane poles** → runaway divergence (unbounded drift).
- **Poles on the imaginary axis** → sustained oscillation (ping-pong that never settles).
- **Left-half-plane poles** → convergence.

A single boolean — *is any pole in the right half-plane?* — is a runaway-drift alarm.

### 5.3 The n-body argument for a central bus

This is the spine's sharpest and least-occupied result. If many agents mutually attract (Spine I's gravity, applied symmetrically), the system is an **n-body problem**: chaotic, no closed-form solution, sensitive to initial conditions. The only structure that tames an n-body system is a **dominant central mass** that holds the others in stable orbit instead of chaotic mutual capture.

**That is the mathematical justification for the central orchestrator.** The bus is not an engineering convenience; it is the sun. Naive agent-to-agent dialogue without a dominant coordinator is mathematically predisposed to the drift and context-pollution failures observed empirically — and the empirical record agrees: recent work finds that accumulated drift in multi-agent systems becomes *self-reinforcing past a critical threshold* (arXiv:2601.04170) and proposes drift-aware routing as mitigation. The n-body framing explains *why* a central mass is necessary rather than merely *that* it helps.

### 5.4 Where this sits in the literature

The trajectory-in-semantic-space view became an active front in late 2025. The control-theory bridge is now explicit — LLMs and control systems are both dynamical systems amenable to controllability/observability/stability analysis (e.g. *When control meets large language models*, 2026). Loop detection via graph trajectory exists (sentences as hidden-state points, transitions as directed edges; arXiv:2601.05693). **But every such system measures coarse scalars** — local/global drift, dispersion, displacement, curvature. None deploys the full operator set of Section 4 (curl, divergence, material derivative) as named diagnostics, and none makes the n-body central-mass argument. The field is, at the moment, explicitly moving "beyond scalars" — which is the direction this operator-level framing already points.

---

## 6. Spine III — Evidence, association, aggregation

This spine absorbs associative recall (attractor retrieval plus cascade) and the non-Boolean aggregation rule, bridged to Spine I by the spectral radius.

### 6.1 Associative recall is a gravity well at small scale

"Self-extracting from a cue" is associative memory: store a pattern, recall the whole from a partial wording. Modern Hopfield networks are provably equivalent to softmax attention (Ramsauer et al., 2020), so this is the substrate already living underneath the tokenizer — a wording is a partial cue pulling a full stored pattern out of an energy landscape whose basins are the associations. **Those basins are Spine I's gravity wells; identical mathematics, smaller scale.** The architecture's associative RAG and its attention layers are not two systems — they are one energy-landscape retrieval at two resolutions.

### 6.2 The cascade and its branching ratio

A "cascade" — one activation triggering associated ones — is a branching process. Whether it dies, sustains, or explodes is set by the **branching ratio `ρ` = spectral radius of the excitation kernel** (back to Spine I's spectrum):

- `ρ < 1` (subcritical) — under-association; the system misses real connections.
- `ρ > 1` (supercritical) — runaway tangent; **this is context pollution.**
- `ρ = 1` (critical) — rich but controlled; the edge of chaos.

This is borrowed-and-solid: criticality theory establishes that a branching parameter near unity *optimizes information transmission while preventing runaway excitation* (neuronal-avalanche literature, Beggs–Plenz and successors). A live branching-ratio monitor on the cascade is therefore a concrete, theoretically-grounded pollution alarm.

### 6.3 The non-Boolean gate

The requirement — "pass when at least 3 of 5, but *which* 3 matters, and 2-of-5 is not the same as 1-of-5" — is not plain fuzzy logic, which remains pointwise. The exact object is a **fuzzy measure (capacity) aggregated by the Choquet integral**. A capacity `μ` assigns a weight to *every subset* of inputs, so `μ({1,3}) ≠ μ({1}) + μ({3})` — synergy and redundancy are encoded directly, which is precisely "which 3." For *which voters actually matter*, compute each input's **Shapley or Banzhaf value** over `μ`: if they come out equal, the gate is identity-blind; if not, identity is load-bearing and the index says by how much. For fusing noisy multi-agent evidence specifically, **Dempster–Shafer** belief functions assign mass to *sets* of hypotheses and combine super-additively — "2 ≠ 1" by construction.

This is the most thoroughly pre-built spine. Choquet-integral fusion of multiple classifiers is decades deep, and the fuzzy Choquet integral over a non-additive measure `μ: 2^N → [0,1]` has already been applied to combining conflicting LLM evidence (arXiv:2506.05675). Lead with the Choquet integral over a learned capacity — it is the single most exact answer to the requirement — and treat the whole region as the cooperative-game-theory of weighted voting games, which is built for exactly this consensus gate.

---

## 7. The unification

The three spines are one structure.

**Spine I and Spine II are dual.** The same potential `Φ` defines the landscape (I) and governs the trajectory (II); gravity appears in both — as the potential well in I, as inductive inertia in II. The landscape is *where* the system can go; the trajectory is the path it takes. You cannot tune one without moving the other.

**Spine III is the discrete shadow of Spine I.** The associative basins of III are the gravity wells of I; the cascade's branching ratio `ρ` is the spectral radius of the same operator family whose Laplacian spectrum drives I's diffusion. The spectral radius therefore appears on *both* sides of the I↔III bridge.

At bottom there is one object: **an energy landscape over semantic space, a feedback-controlled trajectory flowing through it, and discrete evidence-aggregation deciding the transitions.**

### 7.1 The single health scalar

Because the spines share an object, the diagnostics compose into one readout for the whole bus:

```
health = f( curl_magnitude,         # Spine I/II : circular-reasoning detector
            right_half_plane_pole,  # Spine II   : runaway-drift boolean
            branching_ratio ρ )     # Spine III  : context-pollution alarm
```

Each term is an independent, individually-testable measurement (invariant A4). The anti-drift triangulation policy, stated mathematically, reduces to three simultaneous conditions:

> **Keep the flow curl-free. Keep the loop critically damped. Keep the cascade branching ratio below one.**

That sentence is the entire control objective of the orchestrator, drawn from all three spines, expressible as one scalar.

---

## 8. Mapping to the bus

The architecture rides on the existing orchestration spine — a multiplexer-owned PTY loop with per-turn acknowledged exchange and file-backed logs — without replacing it.

- **The substrate (A1–A3)** is the JSONL turn log already being written. The association graph `G` is built over those lines; the field of Spine I is reconstructed from them on the runtime path (Section 4.4); nothing new needs to be the system of record.
- **The orchestrator is the dominant central mass (Section 5.3).** Its existence is now *justified*, not assumed: it is what prevents the n-body chaos of naive agent-to-agent dialogue.
- **The diagnostic layer (Section 7)** is a read-only observer over the stream and the files. It does not actuate; it emits the health scalar. Actuation — reset a drifting agent, anchor with exemplars, throttle a polluting source — is a separate, decoupled concern (A4), and maps cleanly onto the drift-aware-routing and behavioral-anchoring strategies the empirical literature already validates.
- **Resonance vs. truth (A3).** Agents negotiate in streams to find consensus; the consensus is condensed and appended to a file. The field is rebuilt from the file; the loop closes. *Stream to resolve, file to remember.*

---

## 9. Novelty boundary

Stated without flattery, so the paper survives review.

| Element | Status | Nearest prior art |
|---|---|---|
| Spectral / Laplacian retrieval | **Borrowed** | GraphRAG ecosystem; spectral clustering (classical) |
| Associative diffusion RAG (PPR / heat kernel) | **Borrowed** | HippoRAG, HippoRAG 2 (arXiv:2405.14831, 2502.14802) |
| Curl / div on a semantic graph | **Borrowed, repurposed** | Calculus on MDPs (arXiv:2208.09570) — reward shaping |
| Trajectory / attractor / drift framing | **Borrowed** | Agentic-loop dynamics (arXiv:2512.10350); Agent Drift (arXiv:2601.04170) |
| Control-theoretic stability of LLM loops | **Borrowed** | *When control meets LLMs* (2026); SSM control analysis |
| Choquet / Shapley / Dempster–Shafer gate | **Borrowed** | Classifier-fusion literature; LLM evidence fusion (arXiv:2506.05675) |
| Branching-ratio criticality monitor | **Borrowed** | Neuronal-avalanche / edge-of-chaos theory |
| Hopfield ≡ attention bridge | **Borrowed** | Ramsauer et al., 2020 |
| **Material derivative as drift decomposition** | **Apparently unoccupied** | field uses scalar drift; no `∂/∂t` vs `(v·∇)` split found |
| **n-body → central-bus justification** | **Apparently unoccupied** | drift-aware routing exists; the *n-body argument* does not |
| **Three-spine unification → one health scalar** | **Contribution** | no unified curl + pole + ρ readout found |
| **Application to a file-backed append-only agent bus** | **Contribution** | associative memory targets document QA, not orchestration |

The invented mathematics: **none.** The contribution: integration, application, and operator-level granularity where the field still uses scalars. The borrowed-ness of the parts is a strength — each component is independently battle-tested, so the risk lives entirely in the seams, which is exactly where it should live.

---

## 10. Open problems

1. **Does the curl actually fire on real loops?** The RL-theoretic curl is defined on transition graphs with discrete diamonds; mapping it to a noisy embedding trajectory needs an empirical separability test against the existing classifier-based loop detectors.
2. **Is `ζ = 1` achievable with discrete, high-latency feedback?** Critical damping is a continuous-time ideal; an agent loop is sampled at coarse, irregular intervals. The discretization may push the achievable optimum away from `ζ = 1`.
3. **Capacity learning is exponential.** A full fuzzy measure has `2^N − 2` free parameters. The 2-additive Choquet restriction (Möbius representation) is the tractable compromise, but it caps the synergies it can express; whether that cap loses the "which 3" expressiveness in practice is untested.
4. **Runtime diffusion cost at scale.** Chebyshev approximation makes per-call diffusion affordable for `10³–10⁵` nodes; the crossover where even the runtime path becomes too slow, and a different append-friendly structure is needed, is unmeasured.
5. **The single scalar may over-compress.** Folding curl, pole-location, and `ρ` into one number is convenient but lossy; whether operators should be surfaced separately to the actuation layer is a design question, not a settled answer.

---

## References

- Edge et al. (2024). *From Local to Global: A Graph RAG Approach to Query-Focused Summarization.* arXiv:2404.16130.
- Gutiérrez et al. (2024). *HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models.* arXiv:2405.14831.
- Gutiérrez et al. (2025). *From RAG to Memory: Non-Parametric Continual Learning (HippoRAG 2).* arXiv:2502.14802.
- *Geometric Dynamics of Agentic Loops in LLMs: Trajectories, Attractors and Dynamical Regimes in Semantic Space* (2025/2026). arXiv:2512.10350.
- *Agent Drift: Quantifying Behavioral Degradation in Multi-Agent LLM Systems* (2026). arXiv:2601.04170.
- *Circular Reasoning: Understanding Self-Reinforcing Loops in Large Reasoning Models* (2026). arXiv:2601.05693.
- *Beyond Scalars: Evaluating and Understanding LLM Reasoning via Geometric Progress and Stability* (2026). arXiv:2603.10384.
- *When Control Meets Large Language Models: From Words to Dynamics* (2026). Engineering Applications of Artificial Intelligence.
- *Calculus on MDPs: Potential Shaping as a Gradient* (2022). arXiv:2208.09570.
- *Zero-Shot Event Causality Identification via Multi-source Evidence Fuzzy Aggregation with LLMs* (2025). arXiv:2506.05675.
- Ramsauer et al. (2020). *Hopfield Networks is All You Need.* arXiv:2008.02217.
- Coifman & Lafon (2006). *Diffusion Maps.* Applied and Computational Harmonic Analysis.
- Beggs & Plenz (2003). *Neuronal Avalanches in Neocortical Circuits.* Journal of Neuroscience.
- Grabisch (1996). *The Application of Fuzzy Integrals in Multicriteria Decision Making.* European Journal of Operational Research.

*Citations to arXiv preprints and recent venues are accurate to mid-2026; identifiers and venue assignments in this fast-moving area should be re-verified before any formal use.*
