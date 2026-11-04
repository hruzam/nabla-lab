# thread · nabla ↔ coin — operators, convergence, projection, the edge

_v1 · released 2026-09-29 · Phase A. Origin: a voice buffer (Majkee × Nabla) that started from "is convergence a fourth ∇ operator?" and ran through asymptotes and projection to the edge of a tossed coin._

**Provenance**
- `[buffer]` reached in the voice buffer, Majkee × Nabla. Two-party, not triangulated.
- `[release]` single-agent addition by Nabla at release: math, worked examples. Not yet reviewed by Majkee.
- `[release · corrects]` a release addition that changes or narrows a `[buffer]` claim.
- v1: all new, nothing carried from prior versions.

_Notation: Unicode, readable raw. (∇F)ᵢⱼ = ∂Fᵢ/∂xⱼ. φₜ = time-t flow map of ẋ = F(x). φ∞ = lim φₜ as t → ∞._

---

## 0 · The thread on one screen

1. `[buffer]` ∇ builds grad, div, curl. On a vector field, div and curl are compressions of one rank-2 object, the Jacobian ∇F: its trace and its antisymmetric part. The rest is shear. → §1
2. `[buffer]` "Convergence" is not a fourth operator. Locally it is −∇·F; globally it is the t → ∞ limit of the flow, which acts as a projection only in the limit. `[release · corrects]` Negative divergence is not attraction. → §2
3. `[buffer]` Heads/tails is one axis with two signs. The edge is orthogonal to it; the binary model projects the edge away, and the edge case is the projection leaking. `[release]` Precisely: the edge is the kernel of the readout and the fixed point of the H↔T symmetry. → §3
4. `[release · corrects]` The edge is a ridge (separatrix, probability 0) only for a zero-thickness coin. Thickness splits the ridge into a narrow valley between two ridges. The non-zero probability lives in that valley, and its size is set by the dynamics, not the geometry. → §3
5. `[release]` One 2-D field carries all of it. → §4

---

## 1 · One tensor, three operators

`[buffer]` Divergence and curl are the trace and the spin of one tensor; gradient is its rank-one shadow.

`[release]` For F: ℝ³ → ℝ³ the Jacobian ∇F — 9 numbers — is everything F does to first order: F(x + δ) ≈ F(x) + ∇F·δ. It splits uniquely:

```
∇F = (∇·F / 3)·I  +  D  +  W

(∇·F / 3)·I                      isotropic expansion   1 number
D = ½(∇F + ∇Fᵀ) − (∇·F / 3)·I    shear, traceless      5 numbers
W = ½(∇F − ∇Fᵀ)                  rigid rotation        3 numbers
    W·v = ½(∇×F) × v
```

9 = 1 + 5 + 3. The split is canonical, not a choice: these are the only pieces that don't mix under rotations (3 ⊗ 3 = 1 ⊕ 3 ⊕ 5).

Example — F(x, y, z) = (x + 2y, y, z):

```
| 1 2 0 |   | 1 0 0 |   | 0 1 0 |   |  0 1 0 |
| 0 1 0 | = | 0 1 0 | + | 1 0 0 | + | -1 0 0 |
| 0 0 1 |   | 0 0 1 |   | 0 0 0 |   |  0 0 0 |
   ∇F       expansion     shear      rotation
            ∇·F = 3                 ∇×F = (0,0,−2)
```

A small cube is inflated uniformly, stretched along x = y, squeezed along x = −y, and turned clockwise about z at 1 rad per unit time. Simple shear = pure shear + rotation.

Second lens: grad, curl, div are one operator — the exterior derivative d acting on 0-, 1- and 2-forms in ℝ³. The identities ∇×∇f = 0 and ∇·(∇×F) = 0 are one identity: d∘d = 0.

`[release · corrects]`
- "Rank-one shadow" was loose. ∇ raises rank by one; div and curl then compress back down (trace → scalar; antisymmetric part → vector, via ε). Gradient is ∇ on a scalar with no compression — not a piece of ∇F. Point the lens at a gradient field instead: ∇(∇f) = Hess f is symmetric, so W = 0, i.e. ∇×∇f = 0, and its trace is ∇²f, the Laplacian.
- Curl as a *vector* is a 3-D coincidence. An antisymmetric N×N matrix has N(N−1)/2 components, equal to N only for N = 3. In 2-D curl is a scalar; in 4-D it has 6 components. The invariant object is W.

---

## 2 · Convergence is not a fourth operator

`[buffer]` Locally, convergence is negative divergence — a sink. Globally, it is the limit of the flow: an attractor that acts as a projection, but asymptotically — not idempotent along the way.

`[release]` **Local.** Meteorology names it: convergence := −∇·v. A sign convention, not an operator. What divergence measures, exactly (Liouville's formula):

```
det ∇φₜ(x) = exp ∫₀ᵗ (∇·F)(φₛ(x)) ds
```

∇·F is the instantaneous log-rate at which a blob of states changes volume.

**Global — example.** F(x, y) = (−x, 0) = −∇V, V = ½x².
- ∇F = diag(−1, 0), symmetric (it is −Hess V). ∇·F = −1, ∇×F = 0.
- Flow: φₜ = diag(e⁻ᵗ, 1); det = e⁻ᵗ — Liouville, exactly.
- Limit: φ∞ = diag(0, 1), and φ∞² = φ∞ — the orthogonal projection onto the y-axis. x is forgotten; y is the readable result.

**General.** Every linear gradient flow ẋ = −Ax with A = Aᵀ ⪰ 0 ends in an orthogonal projection:

```
e^(−tA) = Σᵢ e^(−λᵢt)·vᵢvᵢᵀ   →   Σ_(λᵢ=0) vᵢvᵢᵀ = P_ker(A)      (t → ∞)
```

`[release · corrects]`
- "Only in the limit" is a theorem, not a hedge. det ∇φₜ = exp(…) > 0 at every finite t, so φₜ is invertible at every finite time: volume shrinks toward zero, never to it. Rank can drop only at t = ∞.
- Negative divergence is not attraction. F = (−2x, y): ∇·F = −1 everywhere, yet the origin is a saddle, φₜ = diag(e⁻²ᵗ, eᵗ). Area shrinks; points are squashed onto the y-axis and thrown out along it. Divergence is a trace — it sees the *sum* of the eigenvalues, while convergence to a point needs *each* of them with negative real part. At a stable point trace ≤ 0 is necessary; from 2-D up it is not sufficient. "Sink" carries the same collision "convergence" did: ∇·F < 0 in vector calculus, attracting fixed point in dynamics.
- Rotation can block the limit. ẋ = −y, ẏ = x: pure curl, circles forever; lim φₜ does not exist. On a limit cycle the orbit converges but the point keeps moving — there the idempotent map is the asymptotic phase (each point ↦ the cycle point it synchronizes with), not lim φₜ.

---

## 3 · The coin: one axis, and the edge

`[buffer]` Heads and tails are one axis — the same state, ± direction. The edge is an orthogonal dimension the two-state model projects away: a separatrix, the unstable ridge. Probability near zero (Nabla), but non-zero (Majkee). The edge case is where the projection leaks.

`[release]` **The readout is a projection.** State: the unit normal n ∈ S² of the heads face.

```
r(n) = sign(ℓ(n)),     ℓ(n) = n·ẑ
```

ℓ projects onto the vertical axis and discards the in-plane part; sign discards magnitude. Edge: ℓ(n) = 0 — the state lies entirely in ẑ⊥, the kernel of ℓ. ℓ returns 0, and 0 is not in the alphabet {+1, −1}. That is "orthogonal", exactly.

**Why E relates differently than H–T** (formalizes Majkee's "no same relation"). The flip symmetry σ: ℓ ↦ −ℓ swaps H and T — one orbit, the same state up to symmetry. The edge is σ's fixed point: it has no partner. The edge is the symmetric, undecided state; every readable result is a broken symmetry.

**Between, or orthogonal? Both.** In the tilt angle α between n and ẑ: H = 0, T = π, E = π/2 — halfway. As a vector in the tilt plane, n = (sin α, cos α): H = (0, 1), T = (0, −1), E = (1, 0) — perpendicular. π/2 is both; two coordinates, one fact.

`[release · corrects]` **Landscape.** Coin of diameter d and thickness h, resting on a table. Height of the center of mass vs tilt:

```
U(α) = m·g·[ (h/2)·|cos α| + (d/2)·sin α ],     α ∈ [0, π]

minima:  α = 0 (H),   π/2 (E),   π (T)
maxima:  α* = arctan(d/h)   and   π − α*     (a rim corner directly under the center)
```

- h → 0: the two maxima merge at π/2 and the edge is a single ridge — a separatrix, probability 0. The buffer picture, exact only for a zero-thickness coin.
- h > 0: the ridge splits into a narrow valley (E) between two ridges. The kernel of the readout thickens into a band.
- This settles the buffer's open tension: "separatrix" and "non-zero probability" contradict each other, because a separatrix has measure zero. The non-zero probability lives in the valley that thickness creates.

`[release]` **Probability: two numbers that disagree.**
- Static — uniform random orientation, quasi-static settling. ℓ(n) is uniform on [−1, 1] (Archimedes' hat-box theorem), so Pr(E) = cos α* = h / √(d² + h²). A ⅓ chance needs h = d/√8 ≈ 0.354·d. US nickel (d = 21.21 mm, h = 1.95 mm): ≈ 0.092, about 1 in 11.
- Dynamic — tossed, landing on a hard surface: ≈ 1 in 6000 for a nickel (Murray & Teare 1993).
- The ~500× gap is dynamics. The edge valley is wide in angle (≈ 10.5° for a nickel) but shallow in energy: leaving E costs m·g·(√(d² + h²) − d)/2 ≈ m·g·h²/(4d), a 0.045 mm lift of the center of mass; leaving a face costs ≈ 9.7 mm. About 200× shallower — a little leftover kinetic energy empties it.
- For a toss, the probability of a readable result lives in phase space (basins of the flow), not in configuration space (valleys of the shape).

**Phase space: Keller's thin coin.** Upward speed u, spin ω about a horizontal diameter, caught at launch height after t = 2u/g. Rotation θ = 2uω/g; starting heads-up, heads iff cos θ > 0.
- Edge set: cos θ = 0 ⇔ u·ω = (2k + 1)·gπ/4, k = 0, 1, 2, … — a family of hyperbolas, the separatrices between heads-bands and tails-bands in the (u, ω) plane. Measure zero.
- For vigorous tosses the bands crowd together and Pr(H) → ½ for any smooth spread of tosses (Keller 1986). The readable ½ is itself a limit.
- Thickness fattens each hyperbola into a thin band (landing and bouncing reshape it); that band's measure is the edge probability.
- Aside: every hyperbola has both axes as asymptotes. Zero spin or zero flight never reaches the edge; the less of one, the more of the other it takes, without bound. The asymptote from the start of the thread, literally — a property of this model, not a law.

**The binary model leaks elsewhere too.** It also discards the starting face. Precession gives a same-side bias ≈ 0.51 (Diaconis, Holmes & Montgomery 2007); 350,757 hand flips measured ≈ 0.508 (Bartoš et al. 2023). The discarded variable there is the initial condition.

**Statistics: the field behind the sequence.** A sequence of outcomes is not a field; its statistics are. Probability obeys a continuity law, and divergence is back:

```
∂ₜp + ∇·J = 0,      J = −p·∇U − κ·∇p      (overdamped drift, noise strength κ)
J = 0   ⇒   p* ∝ exp(−U/κ)
```

∇·J is the rate at which probability drains from a point. Model, not a toss: shake a resting coin. On U(α), p* has three peaks (H, E, T) and troughs at the two ridges; the edge-to-face density ratio is exp(−m·g·(d − h)/(2κ)) — present, exponentially small. Kramers: residence time in a valley ∝ exp(barrier/κ), so the shallow edge valley empties exponentially faster than a face. Readable results = peaks of p* = attractors of the drift.

---

## 4 · One field that carries the whole thread

`[release]`

```
F(x, y) = (−2x,  y − y³) = −∇V,      V = x² − y²/2 + y⁴/4
```

- ∇·F = −1 − 3y² < 0 everywhere: a sink at every point, by the operator. ∇×F = 0.
- (0, ±1): attractors, ∇F = diag(−2, −2) — H and T. (0, 0): saddle, ∇F = diag(−2, 1) — the balanced coin.
- φ∞(x, y) = (0, sign y), and φ∞∘φ∞ = φ∞: a projection onto the readable set {H, E, T}.
- Readout sign(y): one axis, two signs. The symmetry y ↦ −y swaps H and T and fixes the x-axis.
- Edge = {y = 0}: the saddle's stable manifold — separatrix, kernel of the readout, orthogonal to the readout axis, measure zero, and exactly where φ∞ is discontinuous. Only there do states converge to the balanced coin.
- Thickness: replace y − y³ by −y(y² − ε²)(y² − 1). The origin becomes a shallow valley |y| < ε between ridges at ±ε; for uniform starts on (−1, 1), Pr(E) = ε.

A sink by divergence, a coin by dynamics.

---

## 5 · Open — pointers, not conclusions

- `[release]` **The edge detector is ∇ again.** Forward finite-time Lyapunov exponent: Λₜ(x) = (1/t)·ln ‖∇φₜ(x)‖₂. Its ridges mark repelling separatrices (Lagrangian coherent structures); in §4 the ridge sits on y = 0. By Liouville, ∫∇·F is the *sum* of the log-stretches of ∇φₜ — blind to the saddle (§2). Λₜ keeps the *largest* one alone, and sees the edge. Caveat: not every FTLE ridge is a coherent structure (Haller).

---

## References

- J. B. Keller, *The probability of heads*, Amer. Math. Monthly 93 (1986), 191–197.
- D. B. Murray, S. W. Teare, *Probability of a tossed coin landing on edge*, Phys. Rev. E 48 (1993), 2547.
- P. Diaconis, S. Holmes, R. Montgomery, *Dynamical bias in the coin toss*, SIAM Review 49 (2007), 211–235.
- F. Bartoš et al., *Fair coins tend to land on the same side they started: evidence from 350,757 flips*, arXiv:2310.04153 (2023).
- H. A. Kramers, *Brownian motion in a field of force and the diffusion model of chemical reactions*, Physica 7 (1940), 284–304.
- Liouville's formula, Archimedes' hat-box theorem, exterior calculus, FTLE/LCS (Haller; Shadden, Lekien & Marsden 2005): standard sources.

_Citations from recall, not re-fetched at release._
