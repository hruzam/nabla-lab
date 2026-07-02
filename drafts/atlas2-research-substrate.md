# Atlas №2 — Research Substrate: Curved-Space Logic

### Raw ideas and conjectures on stance geometry — opposition as geometry, reconciliation as motion. Prepared for blind handoff to independent researchers.

*Nabla & majkee. Released 2026-07-02. Status: **Phase A/B substrate — NOT researched.** Every claim below is either (a) timeless mathematics, stated as fact, or (b) a training-era lead tagged `[unverified · training-era]` that the researcher must confirm, correct, or kill. Nothing tagged has been checked against current literature. That is the researcher's task.*

---

## 0. Instructions for the researcher

You are receiving this document blind. You do not know who else is researching it. Work independently.

For each of the three forks below:

1. **Prior-art scan.** Find the nearest existing research and production work. The "search seeds" listed are starting keywords, not boundaries — follow the literature where it leads.
2. **Verify or kill the tagged leads.** Every `[unverified · training-era]` item is a memory, possibly wrong, possibly renamed, possibly superseded. Confirm with sources dated as recently as possible.
3. **Answer the research questions.** These are the load-bearing unknowns.
4. **Apply the keep-or-kill test.** Each fork carries an explicit falsification criterion. If the fork fails its test, say so plainly — a killed fork is a good result.
5. **Report the novelty boundary.** For each fork: what is borrowed, what is repurposed, what appears unoccupied. Absence of evidence after your scan ≠ proof of absence — say how hard you looked.

Context you need, in two sentences: the target system is a file-backed, append-only multi-agent orchestration bus (LLM agents of *different vendors* coordinating over JSONL logs, with a central orchestrator). An existing "Atlas №1" maps spectral graph methods, vector-calculus diagnostics, control-theoretic stability, and non-additive aggregation (Choquet/Dempster–Shafer) onto that bus; this document is the candidate *geometric logic layer* underneath the agents' stances.

---

## 1. The unifying picture (what all three forks share)

Boolean logic gives truth two points: {0, 1}. The proposal is to give stances a **curved space**:

- A stance (an agent's position on a question) is a **point on a sphere** (or cylinder, or higher-dimensional analogue).
- **Opposition is geometric**: maximal opposition = antipodal points (across the diameter); partial opposition = intermediate angle; identity = zero angle.
- **Reconciliation is motion**: stances are not static — they move on the surface during the process, and two stances that began opposed can be dragged close.
- The **coordinate system is non-rectangular by design** (spherical, cylindrical, or general curvilinear): the geometry of the space *is* the logic, not a visualization of it.

Motivating observation from the working system: agent outputs are normalized vectors (JSONL lines → embedding vectors), and normalized vectors **already live on a hypersphere** — cosine similarity *is* angular distance. So the question is not "should we put stances on a sphere" (they are already there) but "**what logic and what operations should live on that sphere**."

The three forks decompose the idea into: (1) the static geometry, (2) the dynamics, (3) the N-way generalization.

---

## 2. Fork 1 — Static sphere with rotation: opposition as a frame-invariant relation

### 2.1 The raw idea

All maximal opposites lie across the diameter (antipodal). Points can also be closer — partial opposition at intermediate angles. Crucially: when the whole sphere is **rotated**, every pair's angular distance is preserved — two antipodal stances remain antipodal, but they land at *different places on the map*. Therefore:

> **Opposition is an intrinsic, frame-invariant relation. Position is frame-dependent. A rotation is a change of context, not a change of content.**

Mathematically certain (no verification needed): the antipodal map `x ↦ −x` is an involution (true Boolean negation: applying it twice returns the start), and it **commutes with all rotations** — which is precisely the frame-invariance claim. This is solid.

### 2.2 The cylinder variant

If "stance" is essentially **one angular degree of freedom**, the better space is the cylinder `S¹ × ℝ`: a periodic angular axis for stance (opposite = π away, and it wraps) crossed with a linear axis for magnitude/confidence. This is exactly a **phasor with a confidence dimension** — magnitude × phase, where in-phase agents amplify and antiphase agents cancel. The full sphere (or hypersphere) is needed only if stance is genuinely multi-dimensional. **Dimension selection is a data question, not a math question**: let the measured dimensionality of disagreement pick the coordinate system.

### 2.3 Conjectured named homes — `[unverified · training-era]`, researcher must confirm

- **Quantum cognition** (Busemeyer, Bruza, Pothos): human decisions modeled as states in a projective/spherical space; orthogonal states = mutually exclusive; "measurement" = projection; **context change = rotation**. If memory serves, this is the closest line-for-line match to the raw idea, minus the word "quantum." Verify current state of the field and whether anyone has applied it to *LLM agent* stances.
- **Bloch sphere** (quantum information): antipodal points are orthogonal states; the surface between is the continuum Boolean lacks. Timeless as math; check whether anyone uses Bloch-sphere logic for *non-quantum* multi-agent stance representation.
- **Hyperspherical representation learning**: embeddings analyzed on the sphere; "alignment and uniformity" as the two quality axes (Wang & Isola, ~2020, if memory serves). Confirm citation, find the 2025–26 successors.
- **Projective spaces / RP²**: if a stance and its negation should be *identified* rather than opposed (a modeling choice), the natural space is projective, not spherical. Worth one look: does any stance-representation work use RP^n?

### 2.4 Research questions

- R1.1 — Has anyone defined a **logic** (negation, conjunction-analogue, aggregation) on the sphere/cylinder for multi-agent or LLM stance representation — as opposed to merely *measuring* cosine similarity on normalized embeddings?
- R1.2 — In quantum cognition, what is the state of the art on *context-as-rotation*, and has it been connected to LLM agents or embedding spaces anywhere?
- R1.3 — Is there existing work distinguishing frame-invariant relations from frame-dependent coordinates in embedding space (the "rotation moves the map, not the opposition" point)? Nearest guess: analyses of rotation-invariance in embedding models. Confirm or kill.
- R1.4 — For the cylinder specifically: any prior art on periodic-stance × linear-confidence product spaces? (Directional statistics — von Mises distributions on the circle — is the likely statistical home. `[unverified · training-era]`)

### 2.5 Keep-or-kill test

The sphere earns its keep **only if the angular structure drives operations** — a negation (antipodal map), an aggregation over *angles* not counts, a consensus rule reading *arc-distance* between agent stances. If, after research, "spherical logic" reduces to "normalized vectors + cosine similarity," the fork collapses into what the system already does and must be killed as a *logic* (it survives trivially as a metric, which is nothing new).

### 2.6 Cross-link to Atlas №1

The sheaf-consistency instrument (Atlas №1, I.9) needs a *shared comparison space* on each edge where two heterogeneous agents' stances are reconciled. **That comparison stalk can be this sphere, and the restriction maps can be rotations** between each agent's frame and the shared one. If Fork 1 survives, it is the concrete geometry of the sheaf's edge stalks — one structure serving two instruments.

---

## 3. Fork 2 — Stance-flow: reconciliation as motion on the surface

### 3.1 The raw idea

Fork 1 is rigid: rotations move everything together, preserving all distances. Fork 2 lifts that restriction: **points move freely and independently along the surface**. Two stances that were antipodal can be *dragged toward each other*, each cutting a small differential line (a curve on the surface) as it moves. During a process — a negotiation, a debate, a sequence of agent turns — the configuration of stances flows.

This is **not** an isometry. It is a **flow on the manifold**: each stance is a point with a velocity tangent to the surface; the trajectory is the integral of that velocity field; the "small differential line" is (in the efficient case) a **geodesic arc** on the sphere.

### 3.2 What is mathematically certain (no verification needed)

- Once points move freely on a curved surface, the differential operators (gradient, divergence, curl) exist **intrinsically on the manifold** — the flat-space versions are the special case of an infinitely large sphere. Divergence of the stance-flow = are stances spreading or converging (consensus/fragmentation); curl = are they circulating without resolving (deadlock as rotation).
- **Path degeneracy of reconciliation.** Between any two non-antipodal points on a sphere there are exactly two geodesics (the short and the long way round). Between **true antipodes there are infinitely many** — every great circle through them. Consequence: *how two opposites reconcile is not unique*; the path taken is genuine information (which intermediate stances were passed through). Flat Boolean logic has no such structure, and even the static sphere doesn't — it appears only when points **move**. Conjecture: this path-dependence is the central theorem-shaped content of the whole Atlas №2 cluster.
- **Hairy ball theorem**: every continuous tangent vector field on S² vanishes somewhere. Interpreted: any continuous global stance-dynamics on a 2-sphere has at least one **stagnation point** — a stance that the flow does not move. Whether this interpretation carries real modeling weight is a research question (R2.4), but the theorem itself is beyond doubt.

### 3.3 Conjectured named homes — `[unverified · training-era]`, researcher must confirm

- **Consensus and synchronization on manifolds/spheres**: there is (if memory serves) a control-theory literature on consensus on nonlinear spaces — Sarlette & Sepulchre on manifold consensus; the **Lohe model** as a non-abelian/higher-dimensional Kuramoto generalization (synchronization of points on spheres); "swarming on spheres" dynamics. This would be the direct mathematical home of stance-flow. Verify names, state of the art, and whether any of it touches LLM agents.
- **Opinion dynamics on the sphere**: distinct from the sheaf-based opinion dynamics in Atlas №1 — continuous opinion models where opinions live on a circle/sphere rather than an interval. Confirm existence and current state.
- **Geometric deep learning / Riemannian optimization**: optimization flows on manifolds (retraction, exponential map) as the computational toolkit for implementing any of this. Confirm the current standard libraries (geoopt? pymanopt? `[unverified · training-era]`).

### 3.4 Research questions

- R2.1 — Does a **governing law** for stance-flow exist in any literature: a potential, an interaction kernel (attraction/repulsion between agent stances on the sphere), or is all existing work purely descriptive (replaying embedding trajectories over time)? The fork's value depends on a law, not a replay.
- R2.2 — Has anyone measured **path-dependence of consensus** — that *how* two positions converged (through which intermediates) carries information beyond the endpoint? Any formalization of "the reconciliation path" as an object?
- R2.3 — LLM-specific: any work tracking agent stances as **trajectories on the unit hypersphere across turns**, with differential/geometric analysis (not just endpoint similarity)?
- R2.4 — Does the hairy-ball stagnation point have any established interpretation in opinion/consensus dynamics on S² (an "immovable stance" guaranteed by topology), or is that an over-reading?
- R2.5 — Antipodal instability: in spherical consensus models, what happens at exact antipodes (where the geodesic is non-unique)? Conjecture: it is an unstable equilibrium and the symmetry-breaking direction is where the interesting behavior lives. Confirm from the synchronization literature.

### 3.5 Keep-or-kill test

The flow earns its keep **only if it has a governing law** — a potential or interaction kernel from which trajectories follow, yielding predictions (equilibria, stability, path selection). If all that exists (or all that can be built) is *descriptive replay* of embedding positions over time with geometric vocabulary sprinkled on, the fork is decoration and must be killed.

### 3.6 Cross-link to Atlas №1

This fork **is Spine I (field dynamics) relocated onto the stance-sphere**: the nabla operators of Atlas №1 I.5 reappear intrinsic to the curvature, and the drift/pollution/loop diagnostics (div, curl) get a second, smaller home — not over the semantic content graph, but over the *stance configuration* of the agents. If both survive, the system has field diagnostics at two scales.

### 3.7 Provenance note (for the record, not for the researchers' judgment)

The core of this fork is majkee's, conceived at university (applied physics) and part-modeled in MATLAB with a doctoral student; it found no institutional home — the geometry was too elementary for pure mathematicians, the interpretation too abstract for engineers. Multi-agent stance dynamics is proposed here as the domain that finally gives it one. The researcher's job is to determine how much of it the literature has independently built since.

---

## 4. Fork 3 — Simplex ↔ sphere: N-way symmetric opposition and the dimensional limit

### 4.1 The raw idea

Antipodal opposition is strictly a **two-point phenomenon**: the antipodal map pairs each point with exactly one other. The moment you want *N* stances **all mutually and equally opposed** ("each pair in a Boolean 0/1 relation to each other"), antipodes cannot do it. The object that can is the **regular simplex**.

### 4.2 What is mathematically certain (no verification needed)

- N mutually equidistant unit vectors have pairwise angle **arccos(−1/(N−1))**. Cases: N=2 → 180° (antipodal; the Boolean special case); N=3 → 120° (the equilateral triangle — the 2-simplex); N=4 → ≈109.47° (the tetrahedron).
- **Hard dimensional limit**: on the 2-sphere, at most **4** mutually equidistant points fit (the tetrahedron). Five or more mutually symmetric stances require a higher-dimensional sphere: N mutually equidistant points need dimension ≥ N−1. Consequence, stated as a design rule: **the number of mutually distinct stances the system must represent sets the dimension of the stance space.** Only at N=2 does symmetric opposition coincide with antipodes.
- **The simplex–sphere bridge**: the square-root map `p ↦ √p` sends the probability simplex onto (an octant of) the unit sphere, and pulls the round metric back to the **Fisher–Rao metric** on the simplex. So categorical opposition (a distribution over N mutually exclusive stances — a point on the simplex) and continuous angular opposition (a point on the sphere — Forks 1–2) are **one geometry seen through one diffeomorphism**. This is the weld: it connects this whole Atlas №2 cluster to Atlas №1's Spine III, because a Dempster–Shafer mass assignment over exclusive hypotheses *is* a point on (a face structure over) the simplex.

### 4.3 Conjectured named homes — `[unverified · training-era]`, researcher must confirm

- **Information geometry** (Amari): the discipline that owns the simplex-with-Fisher–Rao-metric; check its current application to LLM output distributions and multi-agent aggregation.
- **Aitchison geometry / compositional data analysis**: the other established geometry of the simplex (log-ratio based). Researcher should compare: Fisher–Rao vs. Aitchison for stance distributions — which operations does each afford?
- **Equiangular tight frames / spherical codes**: the general theory of "many maximally-spread points on a sphere" — relevant when N stances should be *as opposed as possible* but exact equidistance is impossible in the available dimension. Also (long-shot lead) the *softmax bottleneck* and representational-capacity literature may connect: how many mutually distinguishable stances fit in d dimensions.

### 4.4 Research questions

- R3.1 — Has the square-root/Fisher–Rao bridge been used to unify **categorical** agent-vote aggregation with **continuous** embedding-space geometry anywhere? (This is the fork's central claim to usefulness.)
- R3.2 — Do Choquet-integral or Dempster–Shafer aggregation schemes (Atlas №1, I.8) have existing **geometric formulations on the simplex** with the Fisher–Rao metric — i.e., is "non-additive aggregation as geometry" already a thing?
- R3.3 — Practical: given N agent output distributions (softmax vectors), does Fisher–Rao distance measurably outperform cosine/KL for detecting genuine stance opposition? Any empirical literature?
- R3.4 — Is the "number of stances sets the dimension" design rule stated anywhere as an explicit representational-capacity result for stance/opinion spaces?

### 4.5 Keep-or-kill test

The bridge earns its keep **only if the Fisher–Rao pullback yields operations actually used on agent outputs** — aggregation, opposition-detection, or consensus rules that are measurably different from (and better than) plain cosine/KL on the raw vectors. If it only re-derives familiar quantities in fancier coordinates, kill it as an instrument (it may survive as exposition).

### 4.6 Cross-link to Atlas №1

Direct weld to **Spine III** (I.8 — Choquet/Dempster–Shafer): the simplex is where those aggregations already live, unstated. If this fork survives, Atlas №1's aggregation spine and Atlas №2's geometric cluster become one object, and the "which 3 of 5" gate gets a geometry.

---

## 5. The synthesis conjecture (what Atlas №2 would claim if all forks survive)

> **Agents are points on a curved comparison space. Opposition is geometry (frame-invariant, antipodal or simplex-symmetric). Reconciliation is motion (a flow whose paths carry information). The categorical and the continuous views are one space under the square-root map.**

And the full-stack claim, contingent on research: the sheaf's comparison stalks (Atlas №1 Spine IV) are these spheres; the restriction maps are rotations (Fork 1); stance dynamics on the stalks is the flow (Fork 2); the aggregation gate reads the simplex face of the same geometry (Fork 3). One geometry, four instruments.

The researcher is explicitly invited to attack this synthesis, not just the parts.

---

## 6. Known weak points (attack surface, pre-declared)

1. **"Phase = stance" may not be measurable.** All three forks presuppose that an agent's stance can be reliably extracted as a point/angle from its output. If stance extraction is noisy or ill-defined, the geometry computes garbage elegantly. (Carried over from Atlas №1's I.3 open question.)
2. **The sphere may be the wrong quotient.** If a stance and its negation should sometimes be identified (projective) or stances have hierarchy (stratified spaces), S^n is a first guess, not a conclusion.
3. **Curvature may be unnecessary.** The null hypothesis: everything useful here is achievable with normalized vectors + cosine + standard aggregation, and the curved-space language adds no operation. Each keep-or-kill test above is a local version of this global null. Researchers should treat the null as live.
4. **Dimension estimation is unsolved here.** "Let the data pick sphere vs. cylinder vs. S^n" is stated as a principle with no method attached. Intrinsic-dimension estimation of stance variation is an unlisted prerequisite.

---

## 7. Handoff protocol (majkee's process, stated for the record)

This document goes **blind and independently** to heterogeneous researchers (different vendors). No researcher is told of the others. Each returns: prior-art map, verified/killed leads, answers to the R-questions, keep-or-kill verdicts per fork, and an attack on §5. Results are then cross-measured against each other (the same triangulation the target system automates). Disagreements between researchers are themselves data — and, fittingly, points on the very stance-geometry this document proposes.

---

*End of substrate. Nothing here is researched; everything here is honest about that.*
