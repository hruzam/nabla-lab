# Coin dynamics and session evidence — what survives the later drafts

*2026-11-04 · research synthesis · intake closed; empirical hypotheses parked.*

[Collection](README.md) · [Main mathematical study](study.md) · [Research directions](research-directions.md)

## The useful question

Majkee's edge-space idea asks whether a binary readout hides states with different possible motions or different appropriate actions. This is a worthwhile modeling question. The later drafts explore three routes: a physical coin or cylinder, a geometric observation map, and a session observer. They are not interchangeable proofs of one another.

The source threads and design sketch are preserved in the [source archive](../../../session/research-jev-usage/archived-inputs/README.md). This chapter folds the bounded mathematical and source reviews performed after the first Jev edition; it preserves disagreements rather than silently upgrading analogies into theorems.

## 1. Geometry, symmetry and the state being observed

For a face normal `n` on the unit sphere, the linear readout `ℓ(n)=n_z` vanishes on the equator. The kernel belongs to the linear map on ambient space; its intersection with the sphere is the equator. Changing physical thickness does not thicken that kernel. It can change which initial conditions settle on the side.

The reflection `(nx,ny,nz) → (nx,ny,−nz)` fixes the equator. The antipodal map `n → −n` has no fixed point on the sphere. A claim that "the edge is fixed by the flip" therefore requires the exact flip map. A zero scalar readout need not mean a unique physical state.

A face normal omits rotation about that normal. A model of a moving marked coin may also need full orientation, angular momentum, position, velocity and contact state. Counting dimensions in the normal sphere alone does not count all mechanical degrees of freedom. The original rotation construction in the [main study](study.md) makes a narrower point: two states can have the same scalar confidence and different orientation labels, requiring an additional observable.

## 2. Physical thickness and probability

For an ideal homogeneous right circular cylinder on a plane, diameter `d`, thickness `h`, and normal tilt `α` in `[0,π]`, the proposed gravitational potential is

`U(α) = (mg/2) [h |cos α| + d sin α]`.

For positive `d,h`, the two face positions and the side position are local minima of this constrained potential. Maxima occur at `α*=atan(d/h)` and `π−α*`. Near the side, writing `α=π/2+δ`,

`U/(mg) = d/2 + (h/2)|δ| − (d/4)δ² + O(|δ|³)`.

The cusp matters: a smooth curvature or Hessian test cannot simply be applied there. Under **uniform orientation on the sphere and the stated quasi-static basin assignment**, the side-band probability is `h/sqrt(d²+h²)`. This is a conditional geometric calculation, not a universal toss law. Launch conditions, spin, friction, impacts and bouncing change the outcome distribution. The authors' [coin-toss overview](https://physicstoday.aip.org/quick-study/probability-physics-and-the-coin-toss) explains why the mechanism and initial distribution matter; [Yong and Mahadevan's primary study](https://arxiv.org/abs/1008.4559) develops a dynamical model.

The approximately one-in-6000 nickel number in the draft is not adopted here as a universal empirical frequency. Comparing a static formula with a dynamical model requires matching assumptions and provenance first.

For an explicitly chosen overdamped stochastic model with spherical area as the reference measure, a Gibbs density would be `ρ ∝ exp(−U/κ)`. Its tilt-angle marginal has the additional Jacobian: `q(α) ∝ sin α exp(−U(α)/κ)`. Pointwise density ratios do not equal integrated outcome probabilities. A Kramers approximation also requires its regularity and noise assumptions; smooth-well prefactors cannot be imported unchanged into a cusp model. These are conditional modeling statements, not a calibrated description of a tossed coin.

## 3. Flow, contraction and information loss

Negative divergence measures local volume contraction and does not imply attraction of every direction. For example, `F(x,y)=(−2x,y)` contracts area while the origin is a saddle. Negative-real-part eigenvalues of the equilibrium Jacobian are a sufficient local asymptotic-stability condition under the usual smoothness assumptions, not a necessary one: `x' = −x³` has an attracting origin with zero derivative there.

Finite-time flow invertibility must specify domains of existence. For this same scalar field,

`φ_t(x)=x/sqrt(1+2t x²)` for `t>0`.

Its derivative is positive, but its image is bounded. Thus it is invertible onto its image, not onto all of the real line. The draft's linear positive-semidefinite gradient-flow example does converge to a projection onto the matrix kernel; this does not establish that arbitrary dynamics have such a limit.

Ordinary event logs do not supply a differentiable state flow or its derivatives. FTLE, separatrices and Filippov sliding require a defined dynamical model. The labels Suspect, Wedged or Contended do not by themselves establish crossing, escaping or sliding. Ideal sliding and implementation chatter also need to be distinguished.

## 4. Session evidence: preserve the mechanism without overclaiming

The practical contribution is to preserve observations and derive revisable interpretations. Keep process existence, progress, expected waiting, ownership and freshness as distinguishable axes. A timeout or heartbeat statistic supplies evidence about a timing model; it is not proof of process death. The φ-accrual detector's `−log10(1−F(t))` is a tail-surprise statistic under its fitted distribution, not automatically a posterior probability of failure. [Primary report](https://dspace.jaist.ac.jp/dspace/bitstream/10119/4784/1/IS-RR-2004-010.pdf).

FLP concerns deterministic consensus under specified asynchronous failure assumptions; it is not a blanket theorem that every operational status question is undecidable. [Original paper](https://groups.csail.mit.edu/tds/papers/Lynch/jacm85.pdf). Lease and fencing designs need explicit authority and resource enforcement; a suspicion label does not authorize releasing another process's holdings. [Fencing explanation](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html).

Time spent in a mode measures occupancy. Basin stability concerns the probability of recovery under a specified distribution of perturbations/initial conditions. [Primary basin-stability paper](https://www.pik-potsdam.de/members/kurths/recent-selected-publications/nphys2516.pdf). A simple two-state continuous-time model exposes the difference: with rates `a: R→E` and `b: E→R`, stationary edge occupancy is `a/(a+b)`, while recovery by time `T` from E has probability `1−exp(−bT)`. Scaling both rates preserves occupancy and changes recovery times. A rare failure can also dominate total loss.

Changing a classifier threshold changes the interpretation of evidence. Changing the cylinder's shape changes a physical model. Treat their relationship as an analogy until a correspondence is defined. The [research-directions chapter](research-directions.md) specifies experiments that separate representation loss, history loss and missing observations.

## 5. Hypotheses kept open, with their evidence requirements

| Hypothesis or analogy | What would make it testable? |
|---|---|
| "The edge has different possible moves" | Specify full state, observation map, allowed dynamics and an outcome that distinguishes states sharing one readout. |
| Thickness reallocates outcome probability | Fix geometry, launch/settling protocol and initial distribution; measure outcome frequencies and uncertainty. |
| Session edge states carry most of the practical weight | Measure consequence, detection delay and recovery outcomes as well as occupancy. |
| A third answer symbol changes a logic puzzle | State admissible questions and answer semantics; counting three symbols alone does not construct a valid solution. |
| Wheels or another algebra illuminate the edge | State the algebra and changed laws, then identify an actual task requiring them. No adoption follows from a shared metaphor. |
| A frame-breaking loop has a halting-theorem interpretation | Define a formal reduction and its domain. An informal loop or paradox is not such a proof. |

The last three rows remain research pointers from the source lens, not newly verified prior-art results. Their source references were not exhaustively rechecked in this fold. Boolean, multivalued, geometric and dynamical models should be selected by the decision they support.

## Evidence status

The equations and counterexamples above are bounded derivations checked in the research review. The primary sources support the mechanisms identified beside them. The collection contains synthetic construction checks, not physical toss measurements or Jev/session benchmarks. The earlier read-only math and source helpers informed this synthesis; same-provider review is not cross-vendor triangulation. Original drafts remain byte-preserved and retain their own historical provenance labels.
