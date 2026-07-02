# Leg — Color (offline mathematical authority)

`substrate: drafts/atlas2-research-substrate.md · date: 2026-07-02 · role: blind verification leg`
`scope: verify every "mathematically certain" claim + formal stress-test of §5 synthesis`
`method: derivation, not citation. Online prior-art is another leg's job — not touched here.`

Verdict grammar: **HOLDS** / **HOLDS-WITH-CORRECTION** (exact correction stated) / **REFUTED**.
Where a claim is true but weaker than the prose implies, the honest weaker version is stated.

---

## Verdict table

| # | Claim (locus) | Verdict | Conf. |
|---|---|---|---|
| 1 | Antipodal map: involution + commutes with rotations ⇒ frame-invariance (§2.1) | HOLDS-WITH-CORRECTION | high |
| 2 | Geodesic counts + "path is genuine information" (§3.2) | HOLDS-WITH-CORRECTION | high |
| 3 | Hairy ball ⇒ stance-stagnation (§3.2) | HOLDS for S²; framework HOLDS-WITH-CORRECTION | very high |
| 4 | Simplex arithmetic: angle / max-4 / dim ≥ N−1 (§4.2) | HOLDS-WITH-CORRECTION | high |
| 5 | √p pulls round metric to Fisher–Rao (§4.2) | HOLDS-WITH-CORRECTION | very high |
| 6 | Cylinder S¹×ℝ as phasor+confidence (§2.2) | HOLDS-WITH-CAVEAT | high |
| 7 | DS mass = point on (face structure over) simplex (§4.2) | HOLDS-WITH-CORRECTION (near-REFUTED as literally read) | high |
| 8 | "stalk = sphere, restriction maps = rotations" (§2.6/§5) | REFUTED as typed | high |
| 9 | Keep-or-kill tests falsifiable (§2.5/§3.5/§4.5) | HOLDS; §2.5 is the weak one | high |

**Single most damaging finding:** §5's keystone — "the sheaf's comparison stalks *are* these
spheres" — is a **type error**. In a cellular sheaf, stalks are vector spaces and restriction maps
are linear; a sphere is neither closed under addition nor scalar multiplication. The only repair
(linear stalks ℝ^{n+1}, orthogonal restriction maps, spheres as invariant loci) silently **narrows
the object from a general cellular sheaf to an O(n)-synchronization sheaf**, and the sheaf's own
linear machinery (Laplacian, cohomology) then does **not see the angular "logic"** at all. "One
geometry, four instruments" survives only as "one manifold, four *different* structures welded by
prose," not one operation. Detail in Item 8.

---

## 1 — Antipodal map, involution, commuting with rotations (§2.1)

**Verdict: HOLDS-WITH-CORRECTION (high).**

Facts, all true:
- **Involution.** `A(x)=−x`, `A(A(x))=x`. No fixed point on the sphere (`−x=x ⟹ x=0 ∉ Sⁿ`).
  This mirrors Boolean `¬¬p=p` and `¬p≠p` exactly. HOLDS.
- **Commutes with all rotations.** `A=−I=(−1)I`. A scalar multiple of the identity commutes with
  *every* linear map, so with all of GL(n+1,ℝ) — in particular O(n+1) and SO(n+1).
  The checklist's stated reason ("−I central in O(n+1)") is correct: `Z(O(n+1))={±I}`, and −I ∈ it.
  (Understated, in fact: −I is central in the full general linear group, not just O(n+1).) HOLDS.

**The correction** is the inference glue. The prose says the commuting property *"is precisely the
frame-invariance claim."* It is not the same theorem. Two distinct true statements are being fused:

1. **Frame-invariance of the opposition *relation*** comes from O(n+1) acting by **isometries**:
   `⟨Rx,Ry⟩=⟨x,y⟩`, so every angular relation — including antipodality `⟨x,y⟩=−1` — is preserved
   under a change of frame. *This* is what "opposition is frame-invariant, position is not" rests on.
2. **Equivariance of the negation *map*** (`R∘A=A∘R`) is a coherence property of the operator: the
   negation of a rotated point equals the rotation of the negated point, i.e. "negation is
   well-defined independent of frame." This does **not** by itself say opposition is preserved.

Both hold; the conclusion in §2.1 is sound — but it is carried by (1), the isometry property, while
the text credits (2), the commuting property. Honest weaker version: *"Rotations are isometries, so
opposition is frame-invariant; and separately, because −I is central, the negation operator is
frame-equivariant."* Two facts, not one.

Minor note, not load-bearing: on **even**-dimensional spheres the antipodal map is **not itself a
rotation** — `det(−I)=(−1)^{n+1}=−1` for n even, so `−I∈O(3)∖SO(3)` on S². It is orientation-
reversing there. It still commutes with rotations regardless. (On S¹, S³ it *is* a proper rotation.)
The substrate never claims A is a rotation, so this doesn't wound anything — but if a later draft
says "negation is a 180° rotation," that is false on S².

---

## 2 — Geodesic multiplicity and "path is information" (§3.2)

**Verdict: HOLDS-WITH-CORRECTION (high).**

**Geometry (correct, with one scope tag):**
- Non-antipodal distinct `x,y`: `y≠±x` ⇒ `x,y` linearly independent ⇒ **unique** 2-plane through
  the origin ⇒ **unique** great circle, carrying **exactly two** simple arcs (minor = the unique
  minimizing geodesic; major = the long way). HOLDS.
- Antipodes `x,−x`: every 2-plane containing the line `span(x)` yields a great circle through both,
  each a minimizing semicircle of length π. **Infinitely many minimizers.** HOLDS **for n ≥ 2**.
  **Scope correction:** on **S¹** the "infinitely many" fails — there is only one great circle (the
  circle itself), giving exactly two antipodal arcs. The checklist asks for general Sⁿ: the
  "∞ between antipodes" statement requires **n ≥ 2**. (The substrate's S² context is safe.)
- Pedantic completeness: "exactly two" counts non-wrapping arcs on the unique great circle. If one
  admits geodesics that wrap the great circle k times, there are countably many segments between
  *any* two points. The standard reading (two arcs) is what's meant and is fine.

**"The path taken is genuine information" — sound, but weaker than framed.** The geometric fact is a
statement of **boundary-value non-uniqueness**: endpoints do not determine the connecting geodesic
(two arcs generically, ∞ at antipodes). That is real and is genuinely a *curved-space* feature — in
flat ℝⁿ the minimizing geodesic between two points is **unique** (the straight segment), so there
the path *is* pinned by the endpoints. So curvature does buy something: multiplicity.

But three things must be added before "the path carries information" is more than a possibility, and
none is supplied:
1. **A well-posed dynamics.** The geodesic *initial*-value problem is **unique** (Picard–Lindelöf on
   the second-order geodesic ODE): given a point and a tangent velocity, the trajectory is
   determined. Non-uniqueness lives only in the *boundary* problem. So "the path is information"
   means "recording the path adds information *beyond the two endpoints*" — it is not saying the
   dynamics is underdetermined. For the recorded path to *mean* anything you need a law that selects
   it (initial velocity / interaction kernel), which is exactly Fork 2's unmet keep-test (§3.5).
2. **Observability** of the intermediate configuration.
3. **Interpretability** of intermediate stances (Fork's own weak point §6.1: stance extraction).

Honest weaker version: *"On the sphere, endpoints underdetermine the connecting geodesic (2 arcs;
∞ at antipodes for n≥2) — unlike flat space. Whether that underdetermination carries information
depends entirely on there being a dynamics that selects a path and on the intermediates being
interpretable; the geometry supplies the room, not the content."* The "central theorem-shaped
content of the whole cluster" claim is aspiration, not theorem.

---

## 3 — Hairy ball and stance-stagnation (§3.2)

**Verdict: S² claim HOLDS (very high). Framework generalization HOLDS-WITH-CORRECTION.**

**Exact statement & scope.** A continuous nowhere-vanishing tangent vector field on Sⁿ exists **iff
n is odd**. Equivalently (Poincaré–Hopf): a closed manifold carries a non-vanishing field iff its
Euler characteristic is 0; `χ(Sⁿ)=1+(−1)ⁿ = 2 (n even), 0 (n odd)`. So:
- **n even** (S², S⁴, …): `χ=2≠0` ⇒ *every* continuous tangent field vanishes somewhere. The §3.2
  reading — any continuous global stance-dynamics on **S²** has ≥1 stagnation point — is correct.
- **n odd** (S¹, S³, S⁵, …): `χ=0` ⇒ nowhere-vanishing fields **exist** (e.g. on S³⊂ℝ⁴,
  `v(x)=(−x₂,x₁,−x₄,x₃)` is tangent, `|v|=1`, never zero). **No topologically forced stagnation.**

**Dimension-dependence caveat (name it explicitly).** The stance-stagnation reading is
**parity-dependent** and the substrate does not say so. It is stated only for S² (where it holds), but
the framework openly contemplates higher spheres. In Fork 3's own bookkeeping, N maximally-opposed
stances live on **S^{N−2}**, so stagnation is topologically forced **iff N is even**:

| N | stance sphere | χ | forced stagnation? |
|---|---|---|---|
| 3 | S¹ | 0 | **no** |
| 4 | S² | 2 | yes |
| 5 | S³ | 0 | **no** |
| 6 | S⁴ | 2 | yes |

So "topology guarantees an immovable stance" is a claim that **alternates on and off with the number
of stances**. Any weight placed on it (R2.4) must carry the parity tag. On an odd-dimensional stance
sphere the guarantee is simply absent.

---

## 4 — Simplex arithmetic (§4.2)

**Verdict: HOLDS-WITH-CORRECTION (high). Special cases N=2,3,4 individually HOLD.**

**The angle — corrected hypothesis.** Let `v₁…v_N` be unit vectors with common pairwise inner
product c. With `S=Σvᵢ`: `‖S‖² = N + N(N−1)c ≥ 0 ⟹ c ≥ −1/(N−1)`. So `−1/(N−1)` is the
**minimum** attainable inner product (maximum angle), **achieved iff S=0** (vectors sum to zero =
vertices of a regular simplex centered at the origin).

The prose — *"N mutually equidistant unit vectors ⇒ angle arccos(−1/(N−1))"* — is **false as a
universal implication**. Counterexample: the orthonormal basis `e₁,e₂,e₃∈ℝ³` is three mutually
equidistant unit vectors (pairwise angle **90°**, an equilateral triangle inscribed in S²) — but
90° ≠ 120° = arccos(−½). Mere equidistance admits any `c∈[−1/(N−1),1)`; the centroid need not be the
origin. The number `arccos(−1/(N−1))` is correct **specifically** for the *maximally-opposed* /
sum-zero / regular-simplex-centered-at-origin configuration — which, reading §4.1 ("all mutually and
*equally* opposed", "as opposed as possible"), is the intended object. **Correction:** replace the
hypothesis "N mutually equidistant unit vectors" with "the vertices of a regular simplex centered at
the origin (equivalently, N unit vectors summing to zero / of maximal mutual angle)." With that
hypothesis the number is exact.

Special cases (all HOLD under the corrected hypothesis):
- N=2: `arccos(−1)=180°` — antipodal, on S⁰⊂ℝ¹.
- N=3: `arccos(−½)=120°` — the "Mercedes" frame on S¹⊂ℝ².
- N=4: `arccos(−⅓)=109.4712…°` — the tetrahedral angle, on S²⊂ℝ³.

**Max 4 on S²: HOLDS.** A regular d-simplex has d+1 vertices and needs ambient dimension d.
S²⊂ℝ³ ⇒ at most 4 mutually maximally-opposed points (the tetrahedron); 5 would need ℝ⁴.

**Dimension ≥ N−1: HOLDS.** N sum-zero equiangular unit vectors have a rank-(N−1) Gram matrix, so
they span an (N−1)-dimensional linear subspace and sit on S^{N−2}. Minimal ambient (linear) dimension
= N−1. Consistent with "max 4 on S²" (N=4 ⇒ dim 3 = ambient of S²). HOLDS.

---

## 5 — Square-root map and Fisher–Rao (§4.2) — the constant

**Verdict: HOLDS-WITH-CORRECTION (very high).** This is the factor-of-4 / radius-2 catch.

Map `φ(p)=(√p₁,…,√pₙ)`. `Σφᵢ²=Σpᵢ=1` and `√pᵢ≥0` ⇒ image = **positive orthant of the unit sphere**
S^{n−1}. Surjectivity onto that orthant HOLDS.

Metric, with the constant carried explicitly. `yᵢ=√pᵢ`, `dyᵢ=\frac{1}{2√pᵢ}dpᵢ`. Round metric:
```
Σᵢ dyᵢ² = Σᵢ (1/(4pᵢ)) dpᵢ² = ¼ Σᵢ dpᵢ²/pᵢ = ¼ · g_FR.
```
So `φ` pulls the round metric back to **¼ · Fisher–Rao**, not Fisher–Rao. The prose ("pulls the
round metric back to the Fisher–Rao metric") is off by a global factor of 4.

**Exactly-true statement.** To land the Fisher–Rao metric *on the nose*, scale by 2: `ψ(p)=2√p`.
Then `Σψᵢ²=4` (the **radius-2 sphere**), `dψᵢ=\frac{1}{√pᵢ}dpᵢ`, and `Σdψᵢ²=Σdpᵢ²/pᵢ=g_FR`. So:

> `p ↦ 2√p` is an isometry from `(Δ^{n−1}, g_FR)` onto the positive orthant of the **radius-2**
> sphere in ℝⁿ with its round metric. Equivalently, `p↦√p` maps onto the **unit**-sphere orthant and
> pulls the round metric back to **¼ g_FR** (a homothety that halves all Fisher–Rao lengths).

Because ¼·g_FR and g_FR differ only by a global constant, they define the **same geometry up to
scale** (identical geodesics, angles; curvature scaled) — so the substrate's *conceptual* punchline
("one geometry under one diffeomorphism") survives intact. Only the literal metric identity needs the
radius-2 correction. Sphere curvature note: unit sphere has K=1, radius-2 sphere has K=¼ — Fisher–Rao
on the simplex therefore has constant curvature ¼, a fact worth stating correctly downstream.

---

## 6 — Cylinder S¹×ℝ as "phasor + confidence" (§2.2)

**Verdict: HOLDS-WITH-CAVEAT (high).** The manifold is well-formed and standard; three caveats.

`S¹×ℝ` is a smooth, **intrinsically flat** manifold (K=0), the standard cylinder. Pairing one
periodic DOF with one linear DOF is a textbook construction (directional statistics: cylindrical
distributions, von Mises × Gaussian). No objection to well-formedness. But:

1. **Magnitude vs. the ℝ-axis (origin singularity).** A genuine phasor is `z=r e^{iθ}` with `r≥0`;
   at `r=0` the phase is **undefined** (polar-coordinate origin). So a true "magnitude" axis is the
   half-line `[0,∞)` with a degenerate fiber at 0, not the whole line ℝ. The clean way to *get* an
   honest `S¹×ℝ` is `ℂ∖{0} ≅ S¹×ℝ` via `z↦(arg z, log|z|)` — i.e. the confidence axis should be
   **log-magnitude** (or magnitude strictly positive). Then there is no singularity and the product
   is genuine. Reading the ℝ-axis as raw magnitude gives `S¹×[0,∞)`, which pinches at r=0. This is
   actually *semantically desirable* — a zero-confidence stance has no meaningful direction — but it
   means the space is a punctured/collapsed plane, not a clean cylinder, unless you use log-magnitude.

2. **"Amplify / cancel" is addition in ℂ, not a cylinder operation.** In-phase amplification and
   antiphase cancellation are **complex addition** `z₁+z₂`, which lives in the additive group
   `(ℂ,+)=ℝ²`, not on the cylinder. Adding two phasors changes magnitude nonlinearly and can reach
   0 (perfect cancellation exits any fixed-magnitude slice and passes through the singular origin).
   So the state space (cylinder, polar) and the combination law (addition, Cartesian) are two
   different structures on the same set; the prose conflates them. Not fatal, but they must not be
   identified.

3. **Periodic vs. interval topology — an unflagged modeling commitment.** Choosing **S¹** forces
   `θ` and `θ+2π` to be the *same* stance and makes "extreme one way" wrap around toward "extreme the
   other way." That is right for a genuinely **cyclic** stance (hue, phase, wind direction) but wrong
   for a **bipolar** one (agree↔disagree), which is naturally an **interval** `[−1,1]` (contractible),
   not a circle. The substrate flags projective-vs-spherical (§6.2) and dimension selection (§2.2) but
   never flags this circle-vs-interval topology choice. It should: putting a bipolar stance on S¹
   silently asserts that maximal-agree is adjacent to maximal-disagree.

Verdict stands: well-formed, standard, but "phasor with confidence dimension" is exact only under
log-magnitude coordinates, the additive dynamics is not intrinsic to the cylinder, and the periodic
topology is a commitment, not a neutral default.

---

## 7 — Dempster–Shafer mass as "point on (a face structure over) the simplex" (§4.2)

**Verdict: HOLDS-WITH-CORRECTION, near-REFUTED as literally read (high).**

**Correct object.** A DS basic belief assignment (BBA) on a frame Θ is `m: 2^Θ→[0,1]` with `m(∅)=0`
and `Σ_{A⊆Θ, A≠∅} m(A)=1`. Mass is placed on **subsets** (focal sets), i.e. on elements of
`2^Θ∖{∅}`. So a BBA is a point in the simplex over the `2^{|Θ|}−1` nonempty subsets:
```
m ∈ Δ^{(2^{|Θ|}−2)}   —  vertices indexed by nonempty subsets of Θ.
```
This is **not** the base probability simplex `Δ^{|Θ|−1}` over the singletons. A point on the base
simplex is a probability distribution over the |Θ| exclusive hypotheses — that is the **Bayesian
special case** of DS (all focal sets singletons). General DS puts mass on non-singleton subsets
(that is the entire point of DS: mass on `Θ` itself encodes ignorance). So *"a DS mass assignment
over exclusive hypotheses **is** a point on the simplex"* is imprecise; read literally as the base
simplex it is **false** for any non-Bayesian mass function.

**What the parenthetical "(a face structure over)" is groping toward — and the exact statement.**
There is a real relation. The base simplex `Δ^{|Θ|−1}` has faces indexed by subsets `A⊆Θ`
(`F_A = conv{eₐ : a∈A}`), so **focal sets ↔ faces**, and the power-set lattice ↔ the face lattice.
A BBA therefore assigns weights to the **faces** of the base simplex — precisely a point in the
simplex whose vertices are those faces, i.e. `Δ` over `2^Θ∖{∅}`. Exact statement:

> A DS BBA is a point in the simplex `Δ^{2^{|Θ|}−2}` over the nonempty subsets of Θ, whose vertices
> correspond bijectively to the faces of the base simplex `Δ^{|Θ|−1}`. Only the all-singleton
> (Bayesian) BBAs lie on the base simplex itself. The pignistic/plausibility transforms project the
> big simplex **down** to the base simplex, non-injectively (they lose information).

**Does the √p weld still go through?** Trivially yes, meaninglessly mostly no.
- *Trivially:* the mass vector `m` is a bona fide probability vector (nonneg, sums to 1) over the
  `2^{|Θ|}−1` focal slots, so `m↦√m` maps it to the positive orthant of the unit sphere in
  `ℝ^{2^{|Θ|}−1}` with the ¼·Fisher–Rao pullback of Item 5. The map applies.
- *But:* (i) the sphere is now **exponential-dimensional** (`2^{|Θ|}−2`), not `|Θ|−1`; (ii) the
  round/Fisher–Rao geometry treats all focal sets as **exchangeable coordinates** and is **blind to
  the subset/inclusion lattice** — it cannot see that `{θ₁}⊂{θ₁,θ₂}`; (iii) the operations that make
  DS *DS* — Dempster's rule (normalized intersection-convolution over the lattice), Bel/Pl
  (Möbius/zeta transforms) — are **not simplex operations** and are invisible to the round metric.

So the weld carries a bare probability simplex to a sphere, but it does **not** transport the
Dempster–Shafer structure. The claim "DS aggregation *is* this geometry" (the Fork 3 ↔ Atlas №1
Spine III cross-link) is therefore not supported by the square-root map: the map sees the mass vector,
not the belief calculus. Honest version: *"A BBA is a point on the (exponentially larger) simplex over
2^Θ∖∅; the √p bridge maps that simplex to a sphere like any other, but the DS combination rule and
lattice structure live outside that geometry and are not welded by it."*

---

## 8 — §5 formal attack: "stalk = sphere, restriction maps = rotations" (§2.6, §5)

**Verdict: REFUTED as typed (high). Repair exists; it costs the conjecture generality and bite.**

**The type error.** A **cellular sheaf** (Hansen–Ghrist) on a graph/regular cell complex assigns to
each cell a **vector space** `F(σ)` (stalk) and to each incidence `σ⊴τ` a **linear map**
`F_{σ⊴τ}:F(σ)→F(τ)` (restriction). All the machinery Atlas №1's sheaf-consistency instrument would
use — the sheaf Laplacian `L=δᵀδ`, cohomology `H⁰=ker δ` (global sections / consensus), harmonic
sections — presupposes linear stalks. A **sphere Sⁿ is not a vector space**: no zero, not closed
under `+` or scalar multiplication, curved. Therefore **"stalk = sphere" is not well-typed.** As
written, §2.6/§5 is a category error.

**The repair, and its exact cost.**
- *Repair:* stalks `= ℝ^{n+1}` (genuine vector spaces); restriction maps `∈ O(n+1)` (orthogonal —
  these *are* linear, so "restriction maps are rotations" now type-checks); the sphere reappears as
  the **O(n+1)-invariant subset** (unit level set) inside each stalk. Frame-invariant opposition
  (antipodal, `⟨x,y⟩=−1`) is preserved because orthogonal maps preserve the inner product — coherent
  with Fork 1.
- *Cost 1 — narrowing.* A general cellular sheaf has **arbitrary** linear restriction maps. Forcing
  them orthogonal turns the object into an **O(n)-synchronization / discrete-connection sheaf**
  (the world of orthogonal-group synchronization and connection Laplacians), a real and studied but
  **strictly narrower** class. Atlas №1's sheaf instrument, if it uses general cellular sheaves,
  must be restricted to this orthogonal sub-case before the weld is legal. The cross-link is
  conditional on that restriction, which the substrate does not acknowledge.
- *Cost 2 — the machinery goes blind to the "logic."* The sheaf Laplacian and cohomology are defined
  on the **linear** stalks and measure **linear** consistency. The spherical/angular "logic"
  (antipodal negation, arc-distance aggregation) lives on the invariant subset, which the linear
  operators do not directly read. So after repair, the sheaf sees a discrete connection problem, not
  the stance-logic; "the sphere is the comparison stalk" degrades to "the stalk is a Euclidean space
  whose unit sphere *carries an interpretation* and whose restriction maps happen to be orthogonal."

**Does "one geometry, four instruments" cohere once typed — or equivocate?** It currently
**equivocates**, on two axes:

1. **State-sphere vs. comparison-sphere.** Forks 1–2 use the sphere as a **state space** (a stance
   *is* a point on Sⁿ — one point per agent). §2.6/§5 use it as a **comparison stalk** (attached to
   an *edge*, the shared space where two agents' frames are reconciled). These are different roles.
   A consistent picture is *available* — vertex-stalks = per-agent stance spaces, edge-stalks =
   comparison spaces, restriction maps = frame-aligning rotations — but the substrate never draws the
   vertex/edge or state/comparison distinction, so it slides between the two meanings of "the sphere"
   without marking the transition. Coherent-in-principle, not coherent-as-written.

2. **Four instruments = four *different* structures on one manifold, not one operation.** Even after
   typing, the four "instruments" impose four distinct and partly incompatible structures on the same
   Sⁿ: Fork 1 = **isometric** rigid rotations (metric + involution); Fork 2 = a **non-isometric**
   free flow (points move independently — explicitly *not* an isometry, §3.1); §5 = an
   **orthogonal-connection** sheaf; Fork 3 = a **Fisher–Rao simplex** octant (radius-2 per Item 5).
   A manifold can host all of these, but they share only the **underlying set + round metric**, not a
   single unifying operation. "One geometry, four instruments" is true only in the weak sense "one
   manifold, four structures welded by narrative." The synthesis is an **aspiration statement**, not
   a demonstrated unification — and it rests on the untyped identification "stalk = sphere" that fails
   without the narrowing repair above.

This is the leg's most damaging finding, because §5 is the keystone the whole Atlas №2 cluster is
sold on.

---

## 9 — Keep-or-kill tests: falsifiability (§2.5, §3.5, §4.5)

**Verdict: all three falsifiable in principle; §2.5 is the weak one (has a trivial-pass loophole).**

- **§3.5 (flow needs a governing law) — cleanest, genuinely falsifiable.** Criterion: exhibit a
  generative law (potential / interaction kernel) with **predictive** content (equilibria, stability,
  path selection) checkable against held-out trajectories. A descriptive-replay-only fork fails
  unambiguously. Names a concrete failure mode ("geometric vocabulary sprinkled on replay"). PASS as
  a test.
- **§4.5 (Fisher–Rao must beat cosine/KL) — falsifiable, one hardening needed.** Criterion:
  operations "measurably different from **and better than** plain cosine/KL." Empirically decidable —
  but "better" is only well-defined once a **task + metric + benchmark** is fixed; otherwise "better
  on some contrived metric" could sneak a pass. With an honest pre-registered benchmark, falsifiable.
  PASS with the "fix the metric first" proviso.
- **§2.5 (angular structure must drive operations) — weakest; has a trivial witness.** The stated
  PASS condition lists *"a negation (antipodal map)"* as a qualifying operation. But the antipodal
  map is **free** on any sphere and is **fully reducible to cosine** (it just flips the sign of every
  inner product: `cos∠(−x,y)=−cos∠(x,y)`). So a fork could "pass" by pointing at the antipodal map it
  gets for nothing — while doing nothing cosine can't already do. The test's own closing line ("it
  survives trivially as a metric, which is nothing new") shows the author senses this, but the PASS
  clause as written admits the loophole. **Tighten:** require an operation that is provably **not a
  monotone function of pairwise cosines alone** (i.e. genuinely uses arc geometry irreducibly — e.g.
  a Fréchet/Karcher mean on the sphere, which is *not* recoverable from pairwise cosines). As written,
  §2.5 can be passed by a trivial witness; the other two cannot.

---

## Assumptions
- "Sphere" = round unit Sⁿ⊂ℝ^{n+1} with the metric induced from the Euclidean inner product; angular
  distance `d(x,y)=arccos⟨x,y⟩`. "Rotation" = element of O(n+1) (or SO(n+1)) as context requires.
- "Cellular sheaf" = Hansen–Ghrist linear cellular sheaf (stalks vector spaces, restrictions linear),
  the standard object a sheaf-Laplacian consistency instrument would use.
- "Fisher–Rao metric" = Fisher information metric on the categorical simplex, `g_FR(u,v)=Σ uᵢvᵢ/pᵢ`.
- Fork 3 "maximally / equally opposed" read as the regular-simplex-centered-at-origin (sum-zero)
  configuration, per §4.1's own wording.

## Risks / anomalies (ranked)
1. **§5 "stalk = sphere" is a type error** (Item 8). Keystone claim; repair narrows a general
   cellular sheaf to an O(n)-synchronization sheaf and the linear machinery stops seeing the angular
   logic. Highest structural risk.
2. **DS weld does not transport DS structure** (Item 7). The √p bridge moves the mass *vector* but
   not Dempster's rule / the subset lattice; the Fork 3 ↔ Spine III cross-link is not supported by the
   map it names, and the sphere is exponential-dimensional.
3. **Equidistance ≠ the simplex angle** (Item 4). Orthonormal-basis counterexample (90°≠120°). Idea
   survives with the hypothesis fixed to sum-zero.
4. **Fisher–Rao pullback is ¼·g_FR** (Item 5). Cosmetic (radius-2 fixes it), but any downstream
   distance/curvature number computed from "unit sphere = Fisher–Rao" will be off by a factor of 2
   (lengths) / 4 (metric) / curvature 1 vs ¼.
5. **Hairy-ball stagnation is parity-dependent** (Item 3). Absent on odd stance-spheres (S¹, S³) —
   i.e. for N=3, 5 maximally-opposed stances. Must not be cited as universal.
6. **Circle-vs-interval topology unflagged** (Item 6). Modeling a bipolar stance on S¹ silently welds
   extreme-agree to extreme-disagree.
7. **"Path is information" needs an unstated dynamics** (Item 2). Geodesic IVP is unique; the
   information claim rests on Fork 2's still-unmet governing-law test.

*End of leg — Color. Derivations self-verified: dimensions/constants re-checked (Item 5 factor ¼
re-derived; Item 4 bound `c≥−1/(N−1)` re-derived; Item 3 χ(Sⁿ) parity re-checked; counterexamples in
Items 4 and 8 confirmed to violate the stated claims).*
