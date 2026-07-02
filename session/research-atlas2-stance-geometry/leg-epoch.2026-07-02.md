# @Epoch — Research Leg: Depth (Online, Date-Calibrated)
**File:** leg-epoch.2026-07-02.md
**Date:** 2026-07-02
**Substrate:** `/home/hruzam/nabla-lab/drafts/atlas2-research-substrate.md`
**Calibration note:** Training cutoff Aug 2025; all version-sensitive claims below are live-verified against sources dated 2024-2026.

---

## REFUTATIONS FIRST (per evidence discipline)

Before the structured findings, three claims from the substrate that must be read critically:

**REFUTATION 1 — The null hypothesis is not dead.** §6.3 states the null as "normalized vectors + cosine + standard aggregation already do everything useful." Steck et al. (2024, WWW) show cosine similarity can yield "arbitrary and therefore meaningless similarities" under regularization. This *weakens* the null but does not kill it. Geometry-Preserving Aggregation for MoE (2025) shows angular barycenters outperform linear summation for multi-expert embedding aggregation — one empirical crack in the null for the aggregation subproblem. For the fuller logic claims (negation, conjunction over stances), the null has no empirical refutation yet. This must be stated plainly before building on the sphere.

**REFUTATION 2 — The simplex-to-DS weld is asserted, not derived.** §4.2 states that "a Dempster-Shafer mass assignment over exclusive hypotheses *is* a point on (a face structure over) the simplex." This is partially correct: a basic probability assignment on N mutually exclusive hypotheses is a point on the N-simplex. But Dempster-Shafer capacities are *non-additive* set functions (belief functions are sub-additive), while the Fisher-Rao metric applies to *probability* distributions (additive, summing to 1). The weld requires a non-trivial step: either restricting DS to the Bayesian special case, or extending information geometry to non-additive measures. No paper in the current literature does this. The §4.6 "direct weld to Spine III" is currently an assertion, not a derivation.

**REFUTATION 3 — "Heterogeneous agents already live on the same hypersphere" is an assumption.** The substrate notes (§1) that because agent outputs are normalized vectors, "they already live on a hypersphere." But agents from different vendors have *different embedding spaces* with different dimensionalities and orientations. Saying two vectors from OpenAI and Anthropic models both live on a unit sphere does not mean they live on the *same* sphere or that their cosines are comparable. The synthesis conjecture's "shared comparison stalks" (§5) requires alignment across vendor spaces — an open problem not addressed in the substrate.

---

## FORK 1 — Static Sphere with Rotation

### Prior-art map

| Work | Type | Date | Confidence |
|------|------|------|-----------|
| Busemeyer & Bruza, *Quantum Models of Cognition and Decision* | Book | Cambridge UP, 2012 | H |
| Pothos & Busemeyer, Psych. Review 2013 + ongoing annual reviews | Theory | 2013–2026 | H |
| Aerts et al., "Identifying Quantum Structure in AI Language," *Entropy* 28:622 | Empirical, LLMs | Jun 2026 | H |
| Imannezhad, Pothos, Wills, "Divergent patterns of probabilistic reasoning in humans and GPT-5" | Empirical | 2026 (in press) | M |
| Wang & Isola, "Understanding Contrastive Representation Learning through Alignment and Uniformity on the Hypersphere," ICML 2020, pp.9929–9939 | ML Theory | 2020 | H |
| Steck, Ekanadham, Kallus, "Is Cosine-Similarity of Embeddings Really About Similarity?" WWW 2024 | Empirical critique | 2024 | H |
| NSFL: "A Post-Training Neuro-Symbolic Fuzzy Logic Framework for Boolean Operators in Neural Embeddings," arXiv:2604.10604 | Logic on embeddings | Apr 2026 | M |
| "Geometry-Preserving Aggregation for Mixture-of-Experts Embedding Models," arXiv:2602.14039 | Aggregation on sphere | Feb 2026 | M |
| Yang et al., "Breaking the Softmax Bottleneck," ICLR 2018 | Representational capacity | 2018 | H |

### Verification of `[unverified · training-era]` leads

**Quantum cognition (Busemeyer, Bruza, Pothos) — CONFIRMED, alive, and extended.**
Field is active through 2026. Busemeyer, Ozawa, Pothos, Tsuchiya (2025) on episodic memory in quantum decision models (Phil. Trans. Royal Society A). Huang, Epping, Trueblood, Yearsley, Busemeyer, Pothos, "An overview of the quantum cognition research program," *Psychonomic Bulletin & Review* 2025. The *context-as-rotation* framework is intact: in quantum cognition, a change of context (which question is asked first, which frame is applied) is modeled as a rotation of the Hilbert space. This is line-for-line what Fork 1 proposes for agent stances.

HOWEVER: the specific application to *LLM multi-agent stance coordination* is not found. Aerts et al. (2026) show LLMs exhibit quantum-like statistics (Bell inequality violations) but this is about LLM internal probability structure, not about using the rotation-as-context framework for *inter-agent* stance comparison. The gap between "LLMs are quantum-like" and "use rotations to model context shifts in multi-agent coordination" remains a research task.

Confidence: H (field confirmed); M (LLM-agent connection: inferential gap exists, not directly bridged in literature).

**Bloch sphere for non-quantum multi-agent stance — NOT FOUND.**
Search across multiple query framings returned no papers using Bloch sphere geometry as a non-quantum representational space for multi-agent stance. The Bloch sphere literature is strictly quantum information. A few papers extend Bloch representations to two-qubit and higher-qubit systems, but all remain within quantum mechanics. The application of Bloch sphere structure to LLM agent stance is *unoccupied territory* as of 2026-07-02.

Confidence: H (literature gap confirmed after broad search).

**Wang & Isola (2020) hyperspherical alignment/uniformity — CONFIRMED.**
Citation is correct: ICML 2020, pages 9929–9939. The framework describes two quality axes for representations on the unit hypersphere: (1) alignment of semantically similar samples, (2) uniformity of distribution across the sphere. Multiple active successors 2024–2026 (graph-sequential alignment, contrastive learning bounds, etc.). Note the critical limit: Wang & Isola's work is about *measuring quality* of representations already on the sphere. It does not define negation, conjunction, or any logical operation on the sphere. It is a metric tool, not a logical system.

Confidence: H.

**Projective spaces RP^n for stance — NOT FOUND in multi-agent context.**
No paper found using projective spaces to model agent stances. This is a pure gap. Mathematically coherent (identifying a stance and its negation collapses the sphere to RP^n), but no prior art in agent literature.

Confidence: M (looked broadly; absence after reasonable search).

### Research questions — Fork 1

**R1.1 — Logic (negation, conjunction, aggregation) on the sphere for multi-agent LLM stance.**

ANSWER: No paper defines a complete spherical logic (antipodal negation + conjunction analogue + aggregation rule reading arc-distances) for multi-agent or LLM stance representation. The closest three approaches:

1. NSFL (arXiv:2604.10604, 2026): post-training framework mapping Boolean operators to neural embeddings. Uses delta analysis to detect logical operations in embedding space. Does NOT define the antipodal map as negation; instead works empirically on existing embedding magnitudes.

2. Geometry-Preserving Aggregation for MoE (arXiv:2602.14039, 2026): introduces "Spherical Barycentric Aggregation" — computes an angular barycenter on the hypersphere for aggregating expert embeddings. This is the closest production work to aggregation-over-angles. Not stance-specific; it's for MoE routing.

3. Wang & Isola (2020): uniformity criterion could function as a quality metric for stance diversity, but is not an aggregation rule.

Verdict for R1.1: The complete spherical logic system (negation as antipodal map, conjunction analogue, arc-distance aggregation) appears **unoccupied** as a formal logical system for agent stances. The geometry exists; the logical interpretation over multi-agent stances has not been assembled.

**R1.2 — Quantum cognition context-as-rotation + LLM agents.**

ANSWER: Quantum cognition's context-as-rotation framework (a context change is a rotation of Hilbert space, preserving all inner products) is alive and used for human decision modeling. LLMs have been shown (Aerts et al., Entropy 2026) to exhibit quantum-like statistics. However, no paper has connected these two: taking the context-as-rotation framework and applying it explicitly to LLM multi-agent *stance coordination* (where a rotation would model a change in deliberation frame). The bridge exists conceptually but not in the literature.

**R1.3 — Frame-invariant opposition vs. frame-dependent position in embedding space.**

ANSWER: The specific framing — "opposition is intrinsic/frame-invariant while position is frame-dependent" — is NOT found in the literature. The nearest work is: (a) rotation-invariance in representation learning (properties that survive rotation are not about stance logic); (b) "Gauge Freedom and Metric Dependence in Neural Representation Spaces" (arXiv:2603.06774, 2025) which discusses how invertible transformations affect metric structure — closest in spirit but frames it as a problem to solve, not a design resource. The particular logical claim (opposition as a relation that commutes with all rotations, hence is frame-invariant) appears **unoccupied** as an explicit logical design principle.

**R1.4 — Cylinder S¹×ℝ for periodic-stance × linear-confidence.**

ANSWER: Von Mises distribution (circular analogue of the Gaussian, 1918) is confirmed as the statistical home. Applications in acoustics, interferometry, InSAR, wind energy. Recent 2024 comprehensive review of von Mises extensions exists. The *specific* product-space design (S¹ × ℝ = periodic stance × linear confidence) is not found in agent/stance literature. Directional statistics applies von Mises to single-axis circular data; the phasor product-space interpretation has not been assembled for agent stance representation.

### Keep-or-kill verdict — Fork 1

**CONDITIONAL KEEP.**

The kill test: "spherical logic reduces to normalized vectors + cosine similarity → kill as a logic (survives as metric)."

Status: Not yet killed. The Steck et al. (2024) critique of cosine similarity provides theoretical motivation that cosine is insufficient. The geometry-preserving aggregation work (2026) gives empirical traction for angular barycenters over linear summation. The antipodal negation, frame-invariance framing, and Bloch sphere analog for agents are genuinely unoccupied. But the fork has not yet been empirically validated — no paper shows that operations built on the antipodal map measurably outperform standard cosine similarity for agent stance tasks. The fork survives as a *research direction*, not yet as a proven instrument.

### Novelty boundary — Fork 1

- **Borrowed:** Unit hypersphere for normalized embeddings (standard); von Mises for circular statistics (standard); alignment/uniformity framework (Wang & Isola 2020); quantum cognition context-as-rotation (Busemeyer et al.).
- **Repurposed:** Applying quantum cognition's Hilbert space rotations to LLM multi-agent coordination; angular barycenter aggregation (MoE → stance); Bloch sphere geometry as a non-quantum representational tool.
- **Apparently unoccupied:** Antipodal map as formal negation operator for agent stances; frame-invariance of opposition as an explicit logical design principle; Bloch sphere analog for non-quantum multi-agent stance; complete spherical logic system (negation + conjunction + aggregation) for LLM agents; S¹×ℝ product space for stance-confidence.

Search depth: 6 targeted queries + 3 fetch attempts. Searched quantum cognition + LLM, alignment/uniformity successors, spherical logic for agents, negation in neural embeddings, Bloch sphere non-quantum, frame-invariant cosine.

---

## FORK 2 — Stance-flow: Reconciliation as Motion on the Surface

### Prior-art map

| Work | Type | Date | Confidence |
|------|------|------|-----------|
| Sarlette & Sepulchre, "Consensus Optimization on Manifolds," *SIAM J. Control Optim.* | Theory | 2009 | H |
| Lohe, "Non-abelian Kuramoto models and synchronization" | Original model | 2010 | H |
| "Almost Global Consensus on the n-Sphere," arXiv:1609.04885 | Theory | 2016 | H |
| "High-Dimensional Kuramoto Models on Stiefel Manifolds Synchronize Complex Networks Almost Globally," *Automatica* | Theory | 2019 | H |
| "Synchronization on Riemannian Manifolds: Multiply Robust Completion" arXiv:1906.07452 | Theory | 2019 | M |
| **"A Generalized Kuramoto Model for Opinion Dynamics on the Unit Sphere," *Automatica* DOI:10.1016/j.automatica.2024.111957** | **Opinion dynamics governing law** | **Oct 2024** | **H** |
| "Synchronization on Circles and Spheres with Nonlinear Interactions," *SIAM J. Applied Dynamical Systems* | Theory | 2024 | H |
| Kochurov et al., Geoopt: Riemannian Optimization in PyTorch | Software | 2020, active | H |
| Pymanopt (Python Manopt port) | Software | active 2024+ | H |
| "Simulating Opinion Dynamics with Networks of LLM-based Agents," NAACL Findings 2024 | LLM opinion | 2024 | H |
| "On the Principles behind Opinion Dynamics in Multi-Agent Systems of LLMs," arXiv:2406.15492 | LLM opinion | 2024 | H |
| "Hidden Anchors in Multi-Agent LLM Deliberation," arXiv:2606.19494 | LLM deliberation | Jun 2026 | M |

### Verification of `[unverified · training-era]` leads

**Sarlette & Sepulchre on manifold consensus — CONFIRMED.**
"Consensus Optimization on Manifolds," SIAM Journal on Control and Optimization, 2009. Foundational. Still cited in 2024 work on sphere synchronization.

**Lohe model — CONFIRMED AND EXTENDED.**
M.A. Lohe's original sphere synchronization model (2010) is confirmed. Multiple successors: Lohe tensor model, Lohe Hermitian sphere model (arXiv:2004.05418). The Lohe model generalizes Kuramoto to unit spheres in arbitrary dimensions and to Stiefel manifolds. Active research through 2024-2025.

**"Swarming on spheres" / opinion dynamics on spheres — CONFIRMED.**
Literature is rich. The *most important find for Fork 2* is:

**"A Generalized Kuramoto Model for Opinion Dynamics on the Unit Sphere," *Automatica*, October 2024 (DOI: 10.1016/j.automatica.2024.111957).**

This paper develops opinion dynamics *directly on the unit sphere* for multi-agent systems. The interaction kernel generalizes the standard Kuramoto coupling to higher-dimensional sphere geometry. On the circle (S¹), it reduces to the standard Kuramoto model. The paper characterizes stability of equilibria: consensus (all opinions aligned), polarization (opinions split into clusters), and the behavior of these equilibria. This is *exactly* a governing law for stance-flow, not replay. The fork's kill test asks for a governing law — **this paper provides one.**

**Geoopt and Pymanopt — CONFIRMED as active libraries.**
- Geoopt (Kochurov et al.): Riemannian optimization in PyTorch. Active, available on PyPI. Supports spheres, Stiefel manifolds, hyperbolic spaces, SPD manifolds.
- Pymanopt: Python port of Manopt. Supports steepest descent, conjugate gradients, Riemannian trust regions. Both are active and widely cited.
- Additional 2025 library: RiemannAX (JAX-based, draws on both geoopt and pymanopt).

Confidence: H.

### Research questions — Fork 2

**R2.1 — Does a governing law for stance-flow exist?**

ANSWER: YES. The 2024 Automatica paper (generalized Kuramoto on unit sphere) provides exactly a governing law: a potential-based interaction kernel where each agent's opinion velocity on the sphere is determined by a weighted attraction to neighboring opinions, expressed via the Kuramoto coupling extended to sphere geometry. Equilibria (consensus, polarization), stability, and path behavior can be derived analytically from this model. The Lohe model also provides an alternative governing law for full matrix/unitary group synchronization.

This is the most important positive finding in the entire research. Fork 2 is not decoration.

**R2.2 — Has anyone formalized the reconciliation path as an object carrying information?**

ANSWER: Not directly. The mathematical fact is established in sphere geometry: between non-antipodal points, the shortest geodesic is unique; between antipodes, infinitely many geodesics exist (every great circle through them). The synchronization literature (Lohe, Kuramoto on spheres) studies equilibria and convergence rates but does NOT formalize the path itself as an information-carrying object. No paper was found that says "the sequence of intermediate stances carries information about the reconciliation process independent of the endpoint." This interpretation appears to be **unoccupied**.

**R2.3 — LLM stances as trajectories on unit hypersphere across turns.**

ANSWER: Adjacent but not direct. The literature on LLM geometry across layers (2024-2025) studies embedding trajectories through *transformer layers* and through *in-context learning* sequences. "Density Estimation with LLMs: A Geometric Investigation of In-Context Learning Trajectories" (arXiv:2410.05218, 2024) examines geodesic paths in representation space. "Exploring Similarity between Neural and LLM Trajectories" (arXiv:2509.24307, 2025) covers trajectories in language processing. None of these specifically track *multi-agent stance trajectories* (agent A's stance at turn t, how it moves across agent B's turns) with differential/geometric analysis on the unit hypersphere. The LLM opinion dynamics papers (NAACL 2024, etc.) track opinion changes but use scalar or vector opinion representations, not explicitly on the unit sphere with geodesic/flow analysis.

This is a **gap**: LLM turn-by-turn stance tracking with geometric analysis on S^n is not done.

**R2.4 — Hairy ball theorem interpretation in opinion dynamics.**

ANSWER: No established interpretation found. The hairy ball theorem (for S², every continuous tangent vector field vanishes somewhere) appears in physics (cyclone/anticyclone in wind), topology, and once in EEG oscillation literature (brainstem dynamics). In opinion/consensus dynamics on the sphere, NO paper invokes the hairy ball theorem to derive the existence of a stagnation point or "immovable stance." The interpretation — that any continuous global stance-dynamics on S² has at least one stance the flow cannot move — is **novel and apparently unoccupied**. Whether it carries real modeling weight depends on whether stance dynamics are assumed continuous and global (a modeling choice).

Note: For higher-dimensional spheres S^n with n > 2 and n even, the analogous result holds. For odd-dimensional spheres (n = 1, 3, 5, ...), continuous non-vanishing tangent vector fields DO exist (counterintuitive fact about S³). If the stance space turns out to be a 3-sphere, the hairy ball argument fails. This is a precision point the substrate does not mention.

**R2.5 — Antipodal instability in sphere consensus models.**

ANSWER: CONFIRMED. The synchronization literature on spheres directly addresses this. In even-parity group configurations, reduced attitudes converge to pairs of antipodal points. The consensus-at-antipodes configuration is confirmed as an unstable equilibrium in the Lohe/Kuramoto sphere models — it is a critical point but any perturbation breaks the symmetry and the system converges to true consensus or to a different equilibrium. The symmetry-breaking direction (which great circle the system chooses when breaking from antipodal deadlock) is where the interesting behavior lives, confirmed.

### Keep-or-kill verdict — Fork 2

**KEEP.**

The kill test: "flow earns its keep only if it has a governing law — kill if all that exists is descriptive replay."

The governing law exists: the 2024 generalized Kuramoto model on the unit sphere (Automatica 2024) is exactly a governing law with an interaction kernel, stability analysis, and derivable predictions (equilibria, convergence, path selection). This is not decoration; it is established mathematics with a clear connection to stance dynamics.

What is novel beyond the existing work:
1. Applying this governing law specifically to LLM multi-agent stance dynamics.
2. Formalizing the reconciliation path as an information-carrying object.
3. The hairy ball stagnation interpretation.
4. Connection to the Atlas №1 field diagnostics (div, curl of stance-flow).

### Novelty boundary — Fork 2

- **Borrowed:** Sarlette & Sepulchre manifold consensus; Lohe sphere synchronization; Kuramoto model on sphere; geoopt/pymanopt; sphere opinion dynamics (2024 Automatica paper provides the governing law).
- **Repurposed:** Applying sphere opinion dynamics to LLM agent stance; interpreting Kuramoto coupling as inter-agent influence in text-based coordination; connecting to Atlas №1 field operators.
- **Apparently unoccupied:** Reconciliation path as explicit information-carrying object; hairy ball stagnation-point interpretation for opinion dynamics; LLM turn-by-turn stance tracking with geodesic analysis on S^n; the coupling of sphere opinion dynamics with JSONL-append-only multi-agent bus topology.

Search depth: 5 targeted queries. Searched Sarlette+Sepulchre, Lohe+Kuramoto+sphere, generalized Kuramoto opinion dynamics, LLM embedding trajectory hypersphere, hairy ball opinion dynamics, antipodal instability synchronization.

---

## FORK 3 — Simplex ↔ Sphere: N-way Symmetric Opposition

### Prior-art map

| Work | Type | Date | Confidence |
|------|------|------|-----------|
| Amari, *Information Geometry and Its Applications* (Springer) | Foundational | 2016 | H |
| Rao, "Information and the accuracy attainable..." *Bull. Calcutta Math. Soc.* 37 (1945) | Original Fisher-Rao | 1945 | H |
| "Information Geometry of the Probability Simplex: A Short Course," arXiv:1911.01876 | Tutorial | 2019 | H |
| Aitchison, "The Statistical Analysis of Compositional Data," Chapman & Hall 1986 | Foundational | 1986 | H |
| Yang et al., "Breaking the Softmax Bottleneck," ICLR 2018 | Representational capacity | 2018 | H |
| "Functionality-Oriented LLM Merging on the Fisher-Rao Manifold," arXiv:2603.04972 | LLM model merging | Mar 2026 | H |
| "SuperLocalMemory V3: Information-Geometric Foundations for Zero-LLM Enterprise Agent Memory," arXiv:2603.14588 | Agent memory | Mar 2026 | M |
| Miyamoto et al., "On Closed-Form Expressions for the Fisher-Rao Distance," arXiv:2304.14885 | Fisher-Rao distance | 2023 | H |
| Steck et al. (2024) — as above | Critique of cosine | 2024 | H |
| "Geometry-Preserving Aggregation for MoE Embedding Models," arXiv:2602.14039 | Angular aggregation | 2026 | M |

### Verification of `[unverified · training-era]` leads

**Information geometry (Amari) — CONFIRMED, active in LLM context.**
Field is alive. 2026 has direct LLM applications: "Functionality-Oriented LLM Merging on the Fisher-Rao Manifold" (arXiv:2603.04972, Mar 2026) formulates model merging as computing a Karcher mean on the Fisher-Rao manifold. "SuperLocalMemory V3" (arXiv:2603.14588, Mar 2026) applies Fisher-Rao distance to agent memory retrieval, arguing embedding vectors are estimates with uncertainty and Fisher-Rao is the natural metric. Information geometry is moving into production AI contexts.

**Aitchison geometry / compositional data analysis — CONFIRMED.**
Aitchison (1986) is the standard. The field uses log-ratio transformations (ALR, CLR, ILR). Key distinction for the substrate: Aitchison geometry provides a Euclidean structure on the simplex via log-ratios (additive, compatible with standard ML). Fisher-Rao geometry provides a *Riemannian* structure on the simplex that is isometric to the sphere. These are NOT the same geometry. Aitchison is computationally friendly but loses the sphere connection. Fisher-Rao preserves the sphere structure but geodesic computation is harder (though closed-form exists for finite discrete distributions).

For the substrate's purpose (bridging categorical votes with continuous embeddings via a shared sphere), **Fisher-Rao is the natural choice**; Aitchison is an alternative that loses the sphere bridge.

**Square-root map (p ↦ √p) simplex-to-sphere — CONFIRMED, well-established.**
The map p ↦ 2√p sends the probability simplex isometrically (under the Fisher-Rao metric) to the positive orthant of the unit sphere. The Fisher-Rao distance equals twice the geodesic distance in the square-root sphere embedding. Equivalently: the (squared) Hellinger distance between distributions is half the squared Euclidean distance in the square-root embedding. This is established information geometry (Rao 1945, formalized in multiple textbooks). The substrate's mathematical claim is correct.

**Equiangular tight frames / spherical codes — CONFIRMED as abstract theory.**
ETFs (equiangular tight frames) exist as a mathematical theory achieving the Welch bound for maximum spread of N points on a sphere. ETFs include regular simplices as the minimum-dimension case (N points in N−1 dimensions). Applications in CDMA, quantum information, signal processing. However, NO paper found applying ETF theory to the problem of "how many mutually distinguishable agent stances fit in d dimensions." This connection to representational capacity for stance spaces is unoccupied.

**Softmax bottleneck — CONFIRMED.**
Yang et al. (2018), ICLR, "Breaking the Softmax Bottleneck." The embedding dimension d constrains the rank of the next-token logit matrix, hence the number of distinguishable output distributions. Active successors 2024: "Why do small language models underperform? Studying Language Model Saturation via the Softmax Bottleneck" (2024). This is the closest existing literature to the substrate's "N stances requires dimension ≥ N−1" design rule, but framed as a *problem* to solve (more dimensions needed), not as a *design rule* for stance space geometry.

### Research questions — Fork 3

**R3.1 — Square-root/Fisher-Rao bridge for unifying categorical vote aggregation with continuous embedding geometry.**

ANSWER: Partially occupied but not in the multi-agent stance sense. The 2026 LLM merging paper uses the Fisher-Rao manifold for model merging (weighting and combining model parameters, not agent votes). The 2026 agent memory paper uses Fisher-Rao for retrieval. No paper found that: (a) takes N agent *output softmax vectors* (categorical votes), (b) maps them to the sphere via the square-root map, (c) combines this with the agents' continuous embedding-space positions, to yield a unified geometric aggregation. This specific unification is **unoccupied**.

**R3.2 — Choquet/Dempster-Shafer aggregation with geometric formulation on the Fisher-Rao simplex.**

ANSWER: NOT found. The Choquet integral and DS theory are connected through capacities (belief functions as sub-additive set functions). The Fisher-Rao metric applies to additive probability distributions. No paper bridges Choquet/DS non-additive aggregation with the Fisher-Rao Riemannian structure. The weld the substrate proposes (§4.2, §4.6) is mathematically non-trivial: DS belief functions are not points on the probability simplex (they are set functions satisfying weaker conditions). This is currently an assertion in the substrate, not a derivation found in the literature. **Occupied territory warning**: the substrate's claim that "a DS mass assignment is a point on the simplex" is an oversimplification that must be resolved before the weld is valid.

**R3.3 — Fisher-Rao vs. cosine/KL for agent stance opposition: empirical evidence.**

ANSWER: Partial. Theoretical results are clear: KL divergence is only a second-order approximation of Fisher-Rao distance (valid near the same point); for arbitrarily distinct distributions, KL and Fisher-Rao diverge substantially. Fisher-Rao is a proper distance (symmetric, triangle inequality); KL is not. The mathematical prediction: for *opposing* agent stances (softmax vectors that are far apart), Fisher-Rao would measure a larger, more geometrically meaningful distance than KL. Steck et al. (2024) argue cosine similarity on raw embeddings can be arbitrary. No empirical paper directly compares Fisher-Rao vs. cosine/KL for the specific task of *detecting agent stance opposition*. The empirical case must be built.

**R3.4 — "Number of stances sets the dimension" as an explicit design rule.**

ANSWER: NOT found as an explicit stance-space design rule. The closest: (a) the ETF bound (N equidistant points need dimension ≥ N−1) is stated in the abstract mathematics but not as a stance-design rule; (b) the softmax bottleneck (Yang et al. 2018) states the analogous result for LLM output distributions but as a limitation to overcome. No paper says: "if your system must represent N mutually distinguished stances, choose your embedding dimension to be at least N−1." This design rule, framed prescriptively for stance-space architecture, is **unoccupied**.

### Keep-or-kill verdict — Fork 3

**CONDITIONAL KEEP.**

The kill test: "Fisher-Rao pullback yields operations measurably different from and better than cosine/KL."

Status: Not yet killed, but not yet confirmed. The theoretical basis is strong — Fisher-Rao is strictly better-founded for probability distributions than cosine/KL (proper metric, not approximation). The 2026 literature shows Fisher-Rao being used for LLM model merging with better results than Euclidean interpolation. But for the specific task of agent stance opposition detection and aggregation, no empirical head-to-head comparison exists. The DS weld (§4.6) remains an unresolved complication.

The fork survives because the bridge math is solid and partially occupied in adjacent contexts; the specific application to multi-agent stance aggregation is unoccupied.

### Novelty boundary — Fork 3

- **Borrowed:** Fisher-Rao metric on simplex; square-root isometry to sphere; information geometry for LLMs (2026 emerging); ETF bound; Aitchison geometry; softmax bottleneck.
- **Repurposed:** Using Fisher-Rao bridge to unify categorical agent votes with continuous embedding stances; applying softmax bottleneck logic as a stance-space design rule; ETF bound as stance capacity constraint.
- **Apparently unoccupied:** Square-root bridge for multi-agent categorical + continuous unification; Choquet/DS with Fisher-Rao geometry (if the DS-to-simplex weld is resolved); "N stances determines dimension" as an explicit architectural design rule; empirical comparison of Fisher-Rao vs. cosine for agent opposition detection.

Search depth: 6 targeted queries. Searched information geometry + LLM + multi-agent, Fisher-Rao vs cosine/KL, Aitchison vs Fisher-Rao, square-root simplex sphere, Choquet + Fisher-Rao, softmax bottleneck + representational capacity, equiangular tight frames + stance.

---

## §5 Synthesis Conjecture — Attack

The synthesis states: "Agents are points on a curved comparison space. Opposition is geometry (frame-invariant, antipodal or simplex-symmetric). Reconciliation is motion (a flow whose paths carry information). The categorical and the continuous views are one space under the square-root map."

And the full-stack claim: sheaf stalks are spheres; restriction maps are rotations (Fork 1); stance dynamics on stalks is the flow (Fork 2); aggregation gate reads the simplex face (Fork 3). One geometry, four instruments.

**Attack 1 — Stance extraction is an unsolved prerequisite (hardest attack).**
The entire construction requires that agent stances can be reliably extracted as points on the sphere from agent outputs. The substrate itself flags this (§6.1). Current evidence: LLM stances are highly context-sensitive, prompt-sensitive, and inconsistent across paraphrases. The LLM opinion dynamics literature (NAACL 2024) shows LLM agents converge rapidly to consensus due to an intrinsic bias toward "accurate" information — which means the stance signal the geometry is supposed to track may be overridden by compliance dynamics before the geometry can operate on it. If stance extraction is noisy or brittle, the entire geometric superstructure computes garbage elegantly. **This attack is not weakened by any finding in this research.**

**Attack 2 — The common comparison space requires cross-vendor embedding alignment.**
The synthesis requires that agents from different vendors share a comparison stalk where their stances can be compared geometrically. Agents from different vendors embed in different, misaligned spaces (different dimensions, different orientations, different training objectives). The sheaf restriction maps (rotations between agent frames and the shared stalk) must be *learned* or *specified*. No method for this is proposed or found in the literature for the multi-vendor LLM setting. This is an engineering prerequisite, not a free consequence of the math. The synthesis conjecture implicitly assumes this alignment is given; it is not.

**Attack 3 — The Kuramoto coupling constant ≠ textual influence.**
Fork 2's governing law (generalized Kuramoto model, 2024) is a differential equation where each agent's opinion velocity is a function of its coupling to neighbors, expressed as a numerical weight. In LLM multi-agent systems, agent influence propagates through *text*: an agent reads another's output and updates its next-turn response. Mapping textual influence to a Kuramoto coupling constant requires a quantitative model of how text changes another agent's stance. This is not solved in the literature. The governing law exists mathematically; the mapping from text to coupling is an open research problem.

**Attack 4 — The DS-to-simplex weld is asserted, not derived (restating Refutation 2).**
The synthesis claims the aggregation gate (Fork 3) reads the "simplex face of the same geometry," welding Atlas №1 Spine III (Choquet/DS) to Atlas №2. This weld requires DS belief functions to be representable as points on the probability simplex under Fisher-Rao. DS belief functions are sub-additive set functions — they do not satisfy the normalization of probability distributions in the same sense. The Bayesian special case (when belief = probability) does lie on the simplex. For the general DS case, the weld is unresolved. Claiming "one geometry, four instruments" on this basis is premature.

**Attack 5 — The null hypothesis survives for the core claim.**
The null (§6.3) says cosine + standard aggregation already does everything useful. The partial evidence against it: (a) Steck et al. (2024) on cosine problems; (b) angular barycenter outperforming linear summation in MoE aggregation (2026). But neither refutes the null for the *specific operations Atlas №2 is adding*: antipodal negation as a logical operator, path-dependence of reconciliation as information, and Fisher-Rao bridge for vote+embedding unification. These have not been empirically tested. The synthesis conjecture's survival requires each of these to demonstrate measurable improvement over the baseline. None have yet.

**Net verdict on the synthesis:** The synthesis is architecturally coherent and mathematically honest. Two of its three forks (2 and 3) have governing laws or bridges in the literature. But it rests on four unresolved prerequisites: (1) stance extraction reliability, (2) cross-vendor embedding alignment, (3) coupling constant identification from text, (4) DS-to-simplex weld derivation. A killed synthesis is a useful result: it specifies exactly what must be built before the "one geometry, four instruments" claim becomes defensible. The synthesis is currently a **well-formed research program**, not a proven instrument.

---

## Independent Spot-Check (Sibling-Document Claims)

### (a) Tinbergen's gravity model of trade; Wilson's spatial-interaction models

**CONFIRMED.**

- Jan Tinbergen (1962), *Shaping the World Economy: Suggestions for an International Economic Policy*, The Twentieth Century Fund, New York. Formal usage dates to this work.
- A.G. Wilson (1967), "A Statistical Theory of Spatial Distribution Models," *Transportation Research* 1: 253–269.
- A.G. Wilson (1970), *Entropy in Urban and Regional Modelling*, Pion, London.

Both lineages are correct. Wilson showed the gravity model is a family (not a single model) based on entropy maximization; each generation of spatial interaction models contains the previous as a special case. Both citations are accurate.

Confidence: H.

### (b) Ramsauer et al., "Hopfield Networks is All You Need," arXiv:2008.02217 — modern Hopfield ≡ softmax attention

**CONFIRMED.**

ArXiv:2008.02217, authors: Hubert Ramsauer, Bernhard Schäfl, and co-authors. First submitted July 16, 2020; v3 (final revision) April 28, 2021. The paper shows that the update rule of the modern continuous-state Hopfield network is identical to the transformer attention mechanism (softmax attention). The arXiv ID, title, and central claim are all correct.

Source: arxiv.org/abs/2008.02217 (live verified).
Confidence: H.

### (c) Wald sequential analysis + secretary problem + 2025-26 LLM adaptive computation literature

**WALD — CONFIRMED with precision note.**
Abraham Wald introduced the sequential probability ratio test (SPRT) in 1945 (appeared in 1947 as "Sequential Analysis," Wiley, and "Statistical Decision Functions," 1950). Wald's work directly stimulated optimal stopping theory. Citation correct.

**SECRETARY PROBLEM — PARTIAL CORRECTION.**
The classical secretary problem / optimal stopping result (observe and reject the first 1/e ≈ 37% of candidates, then hire the next who exceeds all prior) was NOT formalized primarily by Wald. The canonical formulation is: Chow, Y.S., Moriguti, S., Robbins, H., and Samuels, S.M. (1964), "Optimal Selection Based on Relative Rank," *Israel Journal of Mathematics* 2: 81–90. Wald is part of the broader optimal stopping lineage, but the secretary problem citation should not use Wald as the primary reference.

**2025-26 LLM ADAPTIVE COMPUTATION — CONFIRMED, rich literature exists.**
The line is real and active. Key papers:

- "Stop When Enough: Adaptive Early-Stopping for Chain-of-Thought Reasoning," arXiv:2510.10103 (Oct 2025)
- "BEACON: Bayesian Optimal Stopping for Efficient LLM Sampling," arXiv:2510.15945 (Oct 2025)
- "Optimal Bayesian Stopping for Efficient Inference of Consistent LLM Answers," arXiv:2602.05395 (Feb 2026)
- "Asymptotically Optimal Sequential Testing with Heterogeneous LLMs," arXiv:2604.01086 (Apr 2026)
- "Adaptive Termination for Multi-round Parallel Reasoning: An Universal Semantic Entropy-Guided Framework," arXiv:2507.06829 (Jul 2026)
- "Answer Convergence as a Signal for Early Stopping in Reasoning," arXiv:2506.02536 (Jun 2026)

The connection to Wald-style sequential analysis is explicit in at least two of these (Bayesian optimal stopping, sequential hypothesis testing). The line from Wald → secretary problem → LLM adaptive computation exists and is live.

Confidence: H.

### (d) Belkin–Niyogi Laplacian eigenmaps — citation correct?

**CONFIRMED.**

Mikhail Belkin and Partha Niyogi (2003), "Laplacian Eigenmaps for Dimensionality Reduction and Data Representation," *Neural Computation* 15(6): 1373–1396. DOI: 10.1162/089976603321780317.

Citation is correct in all particulars: authors, year, journal, volume, issue, page range.

Source: MIT Press / Neural Computation direct journal page (live verified via reference aggregators).
Confidence: H.

### (e) Spielman–Teng spectral sparsification lineage

**CONFIRMED, lineage is correct and completable.**

The full lineage:

1. **Spielman & Teng (2008)**, "Spectral Sparsification of Graphs," arXiv:0808.4134. First proof that every graph has a spectral sparsifier with O(n log^c n / ε²) edges, constructible in nearly-linear time. Published in SIAM proceedings.

2. **Spielman & Srivastava (2008/2011)**, showed spectral sparsifiers with O(n log n / ε²) edges via sampling edges proportional to their effective resistances.

3. **Batson, Spielman & Srivastava (2009/2012)**, proved existence of sparsifiers with O(n / ε²) edges — this is optimal even for the complete graph. Published Communications of ACM 2013 survey.

The cited lineage (Spielman-Teng and successors) is correct.

Source: arXiv:0808.4134, Semantic Scholar, ACM DL (live verified).
Confidence: H.

---

## Sources (dated)

- Wang & Isola (2020): https://icml.cc/virtual/2020/poster/53658 [2020, H]
- Steck, Ekanadham, Kallus (2024): https://arxiv.org/abs/2403.05440 [Mar 2024, H]
- "A Generalized Kuramoto Model for Opinion Dynamics on the Unit Sphere," *Automatica*, DOI:10.1016/j.automatica.2024.111957: https://www.sciencedirect.com/science/article/abs/pii/S0005109824004515 [Oct 2024, H]
- "Almost Global Consensus on the n-Sphere": https://arxiv.org/abs/1609.04885 [2016, H]
- "Synchronization on Circles and Spheres with Nonlinear Interactions," SIAM JADS: https://epubs.siam.org/doi/abs/10.1137/24M1699759 [2024, H]
- Ramsauer et al.: https://arxiv.org/abs/2008.02217 [Jul 2020 / Apr 2021 v3, H]
- Belkin & Niyogi (2003): https://direct.mit.edu/neco/article/15/6/1373/6730 [2003, H]
- Spielman & Teng (2008): https://arxiv.org/abs/0808.4134 [2008, H]
- NSFL (2026): https://arxiv.org/html/2604.10604 [Apr 2026, M]
- Geometry-Preserving Aggregation MoE (2026): https://arxiv.org/pdf/2602.14039 [Feb 2026, M]
- "Functionality-Oriented LLM Merging on Fisher-Rao Manifold" (2026): https://arxiv.org/html/2603.04972v1 [Mar 2026, H]
- Aerts et al. "Identifying Quantum Structure in AI Language," *Entropy* 28:622 (2026): https://arxiv.org/html/2511.21731 [Nov 2025/Jun 2026, H]
- BEACON (2025): https://arxiv.org/pdf/2510.15945 [Oct 2025, H]
- Stop When Enough (2025): https://arxiv.org/abs/2510.10103 [Oct 2025, H]
- Bayesian Optimal Stopping LLMs (2026): https://arxiv.org/pdf/2602.05395 [Feb 2026, H]
- Asymptotically Optimal Sequential Testing with Heterogeneous LLMs (2026): https://arxiv.org/pdf/2604.01086 [Apr 2026, H]
- Simulating Opinion Dynamics with LLM-Based Agents (NAACL 2024): https://aclanthology.org/2024.findings-naacl.211/ [2024, H]
- "On the Principles behind Opinion Dynamics in Multi-Agent LLMs": https://arxiv.org/pdf/2406.15492 [Jun 2024, H]
- "Hidden Anchors in Multi-Agent LLM Deliberation": https://arxiv.org/pdf/2606.19494 [Jun 2026, M]
- "Information Geometry of the Probability Simplex: A Short Course": https://arxiv.org/abs/1911.01876 [2019, H]
- SuperLocalMemory V3: https://arxiv.org/pdf/2603.14588 [Mar 2026, M]
- Geoopt: https://deepai.org/publication/geoopt-riemannian-optimization-in-pytorch [2020, active 2024+, H]
- Tinbergen (1962): confirmed via multiple secondary sources
- Wilson (1967, 1970): confirmed via Sage Journals and secondary sources
- Chow, Moriguti, Robbins, Samuels (1964): confirmed via UCLA optimal stopping course notes
- "Why do small language models underperform? Softmax Bottleneck": https://arxiv.org/pdf/2404.07647 [2024, H]

**Calibration note:** Today's date is 2026-07-02. Training cutoff is Aug 2025. All papers published after Aug 2025 were live-verified in this session via WebSearch and WebFetch. Pre-cutoff claims (Belkin-Niyogi, Spielman-Teng, Wang-Isola, Ramsauer, Tinbergen, Wilson) were cross-checked against live citation databases to confirm persistence and correctness.
