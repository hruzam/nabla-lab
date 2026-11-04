# thread · edge-space — the coin's edge is a different space

_v1 · released 2026-09-29 · Phase A lens. Majkee's framing: an in-engine joke, "part of Laterna Magica, living inside the engine"; its practical target is `design.edge-first-session-state.2026-09-29.md`. Math background (vector fields, projection, coin landscape): `thread.nabla-coin.2026-09-29.md`._

**Provenance**
- `[buffer]` voice buffer, Majkee × Nabla, 2026-09-29. Two-party, not triangulated. **(M)** marks Majkee's own formulation.
- `[NABLA]` single-agent addition at release. `[NABLA · corrects]` changes or narrows a voice claim.
- `[world ✓]` literature checked by search in this session · `[world ~]` literature from recall, not re-fetched.
- Each anchor is typed by the bounded-validity rule: **homology** (same structure) · **adjacent** (overlapping problem) · **collision** (shared word only).
- v1. The math this leans on is carried from `thread.nabla-coin` v1 by reference, not copied.

---

## 0 · The lens on one screen

1. `[buffer]` **(M)** The coin is a way of thinking. Heads/tails is ordinary work inside a frame; the edge is a different kind of understanding.
2. `[buffer]` **(M)** The edge lives in a completely different space. It is not null, NaN or undefined — "that is system failure, not what I'm targeting."
3. `[buffer]` **(M)** Twins: the frame ("one always tells the truth, one always lies") defines the process. The interesting move is not to solve inside it but to drive the actors into a loop until the frame collapses.
4. `[buffer]` **(M)** In deterministic systems the edge is negligible; in agent sessions it is the main road.
5. `[buffer]` **(M)** Stretch the coin into a cylinder and the probability flows from the faces to the side — the shape is elastic; landing on a cap then takes specific rolls.
6. `[NABLA]` The lens holds up. It can be made exact four ways — dimension (§1), information (§2), algebra (§3), dynamics (§4) — plus the deformation itself (§5). §6 separates what is adjacent from what only shares a word.

---

## 1 · Dimension — the edge is a different shape of state
`[NABLA]` · homology

- Describe the coin by the direction of its normal, n ∈ S². Heads is the north pole, tails the south pole — **points**. The edge is the equator — **a circle**. The edge set has one more dimension than either face set.
- Mechanically: a coin lying on a face can only turn about the vertical. A coin on its edge can also **roll** — a degree of freedom that does not exist on a face. The edge has different *moves*, not just a different probability. "A different game", made literal.
- **(M)** On the long rod: "this is the whole line." One reading `[NABLA]`: a rod lying on its side rolls freely, so the side state is not a point but a continuous family (every roll angle) — a *manifold of equilibria* with a neutral direction.
- Terms to study: manifold of equilibria, neutral stability.

## 2 · Information — the non-answer is a symbol
`[world ✓]` · homology

- The twins are Smullyan's knights and knaves `[world ~]`. The frame's edge shows up as a sentence nobody on the island can say: "I am a knave." Not false — unsayable.
- Boolos (1996) built "the hardest logic puzzle ever" on that island: gods True, False and Random, answering "da"/"ja" of unknown meaning `[world ✓]`. Rabern & Rabern (2008) used questions a god cannot consistently answer — the god's head "explodes" — and solved the original in two questions instead of three `[world ✓]`. **(M)**'s loop-until-collapse is this move.
- Why it works, in bits `[NABLA]`: three gods have 3! = 6 possible identities, log₂6 ≈ 2.58 bits. A yes/no answer carries at most 1 bit, so three questions are needed. Admit the non-answer as a third symbol and each answer carries up to log₂3 ≈ 1.58 bits; two questions give 3² = 9 ≥ 6 outcomes.
- The debate *is* the lens. Wheeler & Barahona (2012) showed that Uzquiano's harder variant cannot be solved in fewer than three questions; an axiomatic paper (arXiv:1804.05677) argues Boolos' original needs three when only admissible yes/no questions are allowed `[world ✓]`. Nobody disputes the arithmetic. They disagree about *which space the puzzle lives in* — a two-symbol game or a three-symbol one. **(M)**: "completely different space."

## 3 · Algebra — undefined here, ordinary there
`[world ✓]` · homology

- In the reals 1/0 has no value. On the projective line — the number line closed into a circle — it is the point ∞, as ordinary as any other `[world ~]`.
- Carlström's **wheels** (2004) go further: an algebra where division is always defined. 1/0 is an unsigned ∞; 0/0 is a separate element ⊥ that absorbs addition (x + 0/0 = 0/0); and 0·x = 0 no longer holds in general. The elements that do satisfy 0·x = 0 form an ordinary ring `[world ✓]`. The name is the picture: the projective circle plus one extra point.
- Lens reading `[NABLA]`: giving the edge citizenship changes **the laws**, not just the list of values. The exceptional elements obey their own identities. That is why **(M)** rejected null: null bolted onto booleans keeps the old laws; a wheel does not. It also answers the voice question "is 1/0 in the same group as 0 and 1?" — in a wheel it is an element, but it does not obey the same identities.
- Computing precedent: Bergstra & Tucker treat the wheel of rationals as an abstract datatype; Bergstra's survey maps the options for division by zero `[world ✓]`.

## 4 · Dynamics — three things a boundary can be
`[world ✓]` · homology

Filippov's theory of piecewise-smooth systems (vector fields that jump across a switching surface Σ) separates three behaviors at the boundary `[world ✓]`:

| at Σ | the two sides… | the state… | coin / session reading `[NABLA]` |
|---|---|---|---|
| crossing | push the same way | passes through instantly | the frame working: H or T, a clean state change |
| escaping | push away from Σ | may have more than one future | the thin-coin edge: undecided, "where the dynamics decide" |
| sliding | push toward Σ | stays on Σ, moving by its own rule (a weighted blend of both sides) | the edge as a place to live, with its own rules — **(M)**'s different game |

- Sliding is not a curiosity: stick-slip friction is sliding, and sliding-mode control deliberately keeps a system on the switching surface `[world ✓]`. Engineering already treats the edge as a main road.
- Real sliding chatters — rapid back-and-forth across Σ. The practical cure is hysteresis: separate thresholds for each direction (circuit breakers; `study-two.technical.2026-07-13.md` §6).
- `[NABLA · corrects]` This replaces my voice-session split "rest state vs non-termination". The rest state with its own rules is *sliding*; the undecided state is *escaping*; *crossing* is the frame doing its job.

## 5 · Deformation — the elastic knob
`[NABLA]` + `[world ✓]` · homology

- Landscape (derived in `thread.nabla-coin` §3): U(α) = m·g·[(h/2)·|cos α| + (d/2)·sin α]. It is symmetric under h ↔ d with α ↔ π/2 − α: **the coin and the rod are the same landscape with face and side swapped.** `[NABLA]`
- Static basins (uniform random orientation): Pr(side) = h / √(d² + h²). It slides continuously from 0 (thin coin) to 1 (long rod); equal thirds at h = d/√8 `[NABLA]`. Yong & Mahadevan (2011) did the dynamic version — spin, precession, landing without bounce — and derived the aspect ratio that gives any prescribed face-vs-side frequency, checked against tosses of coins with different aspect ratios `[world ✓]`.
- Two kinds of stability `[world ✓]`. *Linear* stability asks whether a small nudge returns (local curvature). *Basin stability* (Menck et al. 2013) asks whether a large kick returns, measured by basin volume. They can disagree: a state can be deep but small (Zhang et al. 2024).
- `[NABLA · corrects]` In voice I said stretching turns the caps into saddles. Not quite: on a long rod the caps remain local minima — a tall can does stand upright — but their basins shrink toward zero. What swaps between coin and rod is **basin stability**, not linear stability; caps become true ridges only in the needle limit. **(M)**'s "specific rolls" is small basin stability, exactly.
- The readable probabilities are themselves limits of the flow. Keller's thin coin tends to ½ as spin and speed grow; the method of arbitrary functions (Poincaré, Hopf) explains why smooth spreads of initial conditions produce stable frequencies `[world ✓]`.

## 6 · The frame — adjacent, homology, collision
`[NABLA]`

- **Adjacent** — the frame problem (McCarthy & Hayes 1969): how a finite formal description copes with everything it does not say `[world ✓]`. Same family (limits of finite frames), different problem.
- **Homology** — undecidability. Turing (1936): no program decides halting for all programs; Rice (1953): no non-trivial semantic property of programs is decidable `[world ~]`. The twins-loop is the halting pattern in miniature: an input the answerer cannot finish.
- **Collision** — "frame" in locale theory is a lattice of open regions `[world ✓]`. Shared word only. The *stance* does rhyme with the cylinder picture: in pointless topology regions come first and points are derived (Johnstone 1983) `[world ~]`.
- **Not the idea** (rejected by **(M)**, kept for contrast): three-valued logics (Kleene, Łukasiewicz), SQL NULL, Belnap's four values, domain theory's ⊥ `[world ~]`. Each adds a value and keeps the old frame and its laws.

## 7 · Corrections to the voice session
`[NABLA · corrects]`

- I cited "a 2025 result, via Rice's theorem, that frame adequacy is undecidable from inside." Overstated: it is a self-published claim (Schlereth, on PhilPapers), not an established result. The established anchors are Turing 1936 and Rice 1953 (§6).
- "The frame problem is exactly this" → adjacent (§6).
- "Locale/frame theory is the reframe, precisely" → a collision on the word; the parallel is stance-level only (§6).
- "Caps become saddles" → basin stability shrinks; linear stability stays (§5).
- "Two escapes: rest state vs non-termination" → Filippov's three boundary behaviors (§4).

## 8 · Study path — for a physicist who codes
`[NABLA]` — intuition first, formalism later.

1. Mahadevan & Yong, *Probability, physics, and the coin toss*, Physics Today 64(7), 2011 — the whole coin in a few pages.
2. Scholarpedia, *Basin of attraction* — the double-well example (everything except the saddle's stable manifold falls to one of two attractors), then fractal and riddled basins.
3. Strogatz, *Nonlinear Dynamics and Chaos* — flows on the line and circle, bifurcations, phase plane `[world ~]`.
4. Menck et al., *How basin stability complements the linear-stability paradigm*, Nature Physics 2013 — four pages.
5. Rabern & Rabern 2008, then Wheeler & Barahona 2012 — the twins, formally.
6. Filippov-type systems: an overview paper (e.g. arXiv:1310.8328), then di Bernardo et al., *Piecewise-smooth Dynamical Systems* (Springer 2008) `[world ~]`.
7. Carlström 2004 — sections 1–2 for the idea; Bergstra 2019 for the map of options.
8. Smullyan, *What Is the Name of This Book?* (1978) → *Forever Undecided* (1987) — from knights and knaves to Gödel `[world ~]`.

---

## References

Checked in this session `[world ✓]`:
- G. Boolos, *The hardest logic puzzle ever*, Harvard Review of Philosophy 6 (1996) — overview: https://en.wikipedia.org/wiki/The_Hardest_Logic_Puzzle_Ever
- B. Rabern, L. Rabern, *A simple solution to the hardest logic puzzle ever*, Analysis 68(2) (2008) 105–112, doi:10.1093/analys/68.2.105
- G. Wheeler, P. Barahona, *Why the hardest logic puzzle ever cannot be solved in less than three questions*, J. Philos. Logic 41(2) (2012) 493–503 — preprint: https://philsci-archive.pitt.edu/9490
- *Boolos' Hardest Logic Puzzle Ever can be solved in no less than three admissible questions*, arXiv:1804.05677
- J. Carlström, *Wheels — on division by zero*, Math. Struct. Comput. Sci. 14(1) (2004) 143–184, doi:10.1017/S0960129503004110
- J. A. Bergstra, *Division by zero, a survey of options*, Transmathematica (2019), doi:10.36285/tm.v0i0.17
- J. A. Bergstra, J. V. Tucker, *The wheel of rational numbers as an abstract data type*, WADT 2020, LNCS 12669 (2021) 13–30
- Piecewise-smooth / Filippov overviews: arXiv:1310.8328; arXiv:2608.19785; D. J. W. Simpson, arXiv:2602.08536
- P. J. Menck, J. Heitzig, N. Marwan, J. Kurths, *How basin stability complements the linear-stability paradigm*, Nature Physics 9 (2013) 89–92, doi:10.1038/nphys2516
- Y. Zhang, P. S. Skardal, F. Battiston, G. Petri, M. Lucas, *Deeper but smaller: higher-order interactions increase linear stability but shrink basins*, Science Advances 10 (2024) eado8049
- E. H. Yong, L. Mahadevan, *Probability, geometry, and dynamics in the toss of a thick coin*, Am. J. Phys. 79 (2011) 1195–1201, arXiv:1008.4559
- L. Mahadevan, E. H. Yong, *Probability, physics, and the coin toss*, Physics Today 64(7) (2011), doi:10.1063/PT.3.1178
- D. B. Murray, S. W. Teare, *Probability of a tossed coin landing on edge*, Phys. Rev. E 48 (1993) 2547–2552
- J. B. Keller, *The probability of heads*, Amer. Math. Monthly 93 (1986) 191–197, doi:10.2307/2323340
- Scholarpedia, *Basin of attraction*: http://www.scholarpedia.org/article/Basin_of_attraction
- Stanford Encyclopedia of Philosophy, *The Frame Problem*: https://plato.stanford.edu/entries/frame-problem/
- nLab, *frame*: https://ncatlab.org/nlab/show/frame

From recall, not re-fetched `[world ~]`: Turing 1936; Rice 1953; McCarthy & Hayes 1969; Smullyan 1978, 1987; Kleene; Łukasiewicz; Belnap 1977; P. T. Johnstone, *The point of pointless topology* (1983); Strogatz, *Nonlinear Dynamics and Chaos*; A. F. Filippov, *Differential Equations with Discontinuous Righthand Sides* (1988); di Bernardo et al. (2008).
