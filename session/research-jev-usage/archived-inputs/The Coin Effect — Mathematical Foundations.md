# The Coin Effect — Mathematical Foundations

Oct 8, 2026 · @Michal Hrůza

## Scope

The hypothesis splits into two claims that stand or fall separately. One is established mathematics you can borrow outright; the other is a genuine extension with no ready-made theorem behind it.

**Claim A — the group layer.** A decision is taken by an odd-sized group of elements, and the verdict depends on *which* elements carry it, not only on how many. Two specific elements out of five may pass the signal where two others do not.

**Claim B — the element layer.** Each element's own state is not binary. Besides FACE and TAIL there is a third state, EDGE, which is not a gap in knowledge and not a value lying between the other two. It is a distinct state with its own orientation.

Claim A is prior art, recovered independently. Claim B is partly prior art and partly new; the new part is specific and can be stated precisely rather than waved at.

The two claims are not independent. Whether an element's EDGE matters to the group verdict is decided entirely by the group layer, which is what makes the pair worth treating as one object.

## Part A — the group layer is established mathematics

Claim A is a **simple game**, and it was formalised twice independently: once in cooperative game theory, once in threshold logic as a **monotone Boolean function**. The two theories are [isomorphic](https://link.springer.com/article/10.1007/s11238-017-9606-z), so every result on one side transfers to the other.

Formally: a set N of n elements, and a function v mapping each subset to {0,1}, with v(∅)=0, v(N)=1, and monotone — adding an element never turns a passing coalition into a failing one.

Four borrowed results do real work here.

**Minimal winning coalitions.** A coalition that passes the signal but fails if any single member leaves. The set of these characterises the game completely — in Boolean terms they are the [prime implicants](https://www.sciencedirect.com/science/article/pii/S2307187725008752) of the threshold function. "Two specific elements out of five pass the signal" is the statement that those two form a minimal winning coalition.

**Weights are strictly weaker than identity.** A *weighted* voting game assigns each element a number and passes when the sum clears a quota. Not every simple game can be written this way — there are games provably outside the weighted class. This matters directly: if the configurations that pass cannot be reproduced by any assignment of weights, the system is a general simple game and attempts to model it by scoring elements individually will fail as a matter of theorem, not of tuning.

**Banzhaf pivotality.** An element's importance is not its weight but the count of configurations in which it swings the verdict — coalitions that win with it and lose without it. Equivalently, the prime implicants of the Boolean difference of v with respect to that element. This is the formal content of "load-bearing".

**Odd n is not decoration.** With n odd and a majority rule, exactly one of any coalition and its complement wins. No ties, and the game is both proper and strong. The choice of five and seven buys decisiveness.

### What to take

Describe the group layer by listing its minimal winning coalitions, not by assigning weights. Test whether the game is weighted; if it is not, say so and keep the MWC list as the primitive.

## Part B — the element layer is half borrowed, half new

Four existing systems each capture part of EDGE and miss part. Naming which part each one misses is what makes the residue defensible as new rather than merely unfamiliar.

| System | What it offers | Why EDGE is not it |
| --- | --- | --- |
| [Strong Kleene three-valued logic](https://plato.stanford.edu/entries/logic-manyvalued/) | A third value U for undefined output of a partial function | U means *not yet determined*. It resolves to true or false on further information. EDGE does not resolve; it is a state, not a gap |
| [Bochvar / weak Kleene](https://link.springer.com/article/10.1007/s10849-025-09436-w) | A third value that is **infectious** — any compound containing it takes it | Right propagation instinct, wrong trigger. Here EDGE infects the group only conditionally, never automatically (see the next section) |
| Belnap–Dunn four-valued logic, bilattices | Two orthogonal orders at once: a truth axis and an information axis | Closest structural match to the cylinder. But the second axis measures *how much is known*, which is again epistemic, not a property of the element |
| [Ternary voting games](https://link.springer.com/article/10.1007/BF01263275) and [(j,k) simple games](https://link.springer.com/article/10.1007/s00355-003-0212-3) | Exactly a group rule over elements with three input states, with Banzhaf and Shapley–Shubik indices already extended to it | The third state is **abstention, ordered between yes and no**. EDGE is explicitly not between FACE and TAIL |

### The residue

Strip out what is borrowed and one claim is left standing:

> A (3,2) simple game in which the third input level is **not order-embedded** between the other two, but lies on an axis orthogonal to them, carrying an orientation rather than a magnitude.

Every ingredient of that sentence exists in the literature except the conjunction. Freixas and Zwicker's characterisation theorem rests on *grade trade robustness*, which presupposes ordered input levels; remove the order and that theorem does not apply. That is the precise edge of the known terrain.

### On the orientation

EDGE carries a sign — the two rims of the cylinder running to opposite infinities. The sign is a **selector, not a measurement**: it routes which resolution strategy is applied, and its magnitude is never read. Write the two polarities as `EDGE_POS` and `EDGE_NEG`.

This is the one place where the cylinder picture should not be taken literally. An unbounded axis read only for its sign is, formally, a binary label attached to a third state — not a continuum. Keeping that distinction explicit prevents the model from quietly acquiring a real-valued parameter it never needed.

## The propagation result

The two claims meet here, and the meeting produces something neither has alone.

**Proposition.** Let v be a simple game on N, and let a configuration assign each element FACE, TAIL, or EDGE. Let E be the set of EDGE elements. Evaluate v twice: once with every element of E forced to FACE, once with every element of E forced to TAIL.

- If the two evaluations **agree**, the group verdict is that value, and EDGE does not propagate.
- If they **disagree**, the group is itself on its edge.

**Corollary.** The group is EDGE-contaminated if and only if at least one EDGE element is *pivotal* in the current partial configuration — a swing element in the Banzhaf sense, given how the non-EDGE elements have landed.

The proof is immediate from monotonicity: forcing all of E to FACE is the maximal completion, forcing all to TAIL the minimal one, and monotone v is bounded between them. Agreement means no completion changes the outcome.

```latex
v^{-} = v(S_{\mathrm{FACE}}), \qquad v^{+} = v(S_{\mathrm{FACE}} \cup E), \qquad \text{verdict} = \begin{cases} v^{-} & v^{-} = v^{+} \\ \mathrm{EDGE} & v^{-} \neq v^{+} \end{cases}
```

### Why this is the useful result

Three consequences follow, and they are what make the hypothesis implementable rather than ornamental.

**EDGE is not infectious by default.** Weak Kleene would contaminate every compound touching a third value. Here most EDGE elements are simply irrelevant — they sit outside every minimal winning coalition that is still live. The group stays determinate, and the edge stays local.

**It is cheap.** Two evaluations of v, regardless of how many elements are on their edge. No enumeration over completions.

**It tells you where to spend.** Only *pivotal* EDGE elements are worth resolving. Everything else can be left unresolved forever without affecting the answer. This converts the Banzhaf index from a descriptive measure of power into an operational budget rule — which is the main practical payoff of pairing the two claims.

### The open question

The proposition treats EDGE as unresolved-but-completable, which is exactly the Kleene supervaluation move and sits uneasily with Claim B's insistence that EDGE is not a gap.

The defence: the two-completion test is a statement about *what the group rule can see*, not about what the element is. The group rule is binary by construction and can only read FACE or TAIL, so bracketing is the correct way to ask whether it needs to look. The element's own EDGE state and its orientation remain intact and are read by the resolution layer, not by v.

If that defence fails — if the orientation turns out to change the group verdict directly, not merely the resolution strategy — then v must be replaced by a genuine (3,2) rule and the two-completion shortcut is lost. That is the sharpest falsification condition in the whole hypothesis.

## Notation and syntax

The concern is correct and the answer is counterintuitive: **compact symbols are the wrong choice here, precisely because the concept is new.**

### Why glyphs fail on unfamiliar terrain

A symbol is not a blank slate to a language model. ε carries an overwhelming prior as *an arbitrarily small positive quantity*; ○ carries function composition and the Hadamard product; ⊥ carries falsity and bottom. Stipulating a new meaning does not delete the prior — it competes with it, and over a long context the prior wins. A model that has never seen your concept will quietly reinterpret the glyph as the nearest thing it does know.

An unfamiliar **word** has no such pull. It arrives empty and takes a stipulated definition cleanly. So the rule inverts the usual mathematical preference: for a concept with no training data, verbose beats compact, and strange beats elegant.

### The three consumers need three different things

**JEV sees no notation at all.** It takes a predefined typed option set and returns a distribution over it. The option *names* are the entire syntax — and critically, `EDGE` is never one of them. JEV is asked only FACE-or-TAIL; the harness assigns EDGE by reading the distribution. Never ask a two-sided instrument to report a state it has no axis for.

**The LLM needs operational definitions, not analogies.** Define each state by the observable that produces it, in a short contract block prepended to the prompt. The coin, the cylinder, the infinite axis are all excellent for human thinking and actively harmful here — the model will extend the metaphor rather than apply the rule.

**A human reader can have the metaphor**, in prose, in documents like this one. Keep it out of anything a machine parses.

### Recommended tokens

| Concept | Token | Rejected alternative and why |
| --- | --- | --- |
| The two ordinary states | `FACE`, `TAIL` | `TRUE`/`FALSE` — invites classical-logic defaults |
| The third state | `EDGE` | ε — collides with infinitesimals |
| Its orientation | `EDGE_POS`, `EDGE_NEG` | ±∞ — implies a magnitude that is never read |
| The per-element operator | `state_of(x)` | ○x — collides with composition |
| The group rule | `group_verdict(...)` | W — too bare to survive a long context |
| The group's own edge | `GROUP_EDGE` | reusing `EDGE` — hides the layer distinction |

All plain ASCII, all typeable, none colliding with an existing mathematical convention.

### The contract block

This is the prelude that gives a model the terrain. It defines by trigger, not by resemblance.

```markdown
STATE VOCABULARY (stipulated; ignore any prior meaning of these words)

Each element is in exactly one of three states.

FACE  - the measurement concentrated on the first option.
TAIL  - the measurement concentrated on the second option.
EDGE  - the measurement did not concentrate on either option.

EDGE is NOT "unknown", NOT "missing data", NOT "between FACE and TAIL",
and NOT a low-confidence FACE or TAIL. It is a distinct outcome.
Do not resolve an EDGE by guessing which side it would fall on.

An EDGE carries an orientation, EDGE_POS or EDGE_NEG. The orientation
selects which resolution procedure is applied. It is never compared,
summed, or treated as a quantity.

GROUP_EDGE - the group verdict is undetermined because at least one
EDGE element is pivotal. It is not the sum or average of element states.
```

### One formal convention

Write a configuration as an explicit map, never as a vector of symbols:

```latex
\sigma: N \rightarrow \{\mathrm{FACE}, \mathrm{TAIL}, \mathrm{EDGE}\}, \qquad E_\sigma = \sigma^{-1}(\mathrm{EDGE})
```

The map form keeps the three states visibly unordered. A vector notation tempts the reader — and the model — into reading position as rank, which would smuggle back the ordering that Part B spent its effort removing.

## Standing

| Component | Status |
| --- | --- |
| Group rule as a simple game; MWCs as the primitive | Established. Borrow it |
| Identity-sensitivity exceeding what weights can express | Established, and a theorem rather than a tuning problem |
| Pivotality as the measure of load-bearing | Established (Banzhaf) |
| A group rule over three-state elements | Established (ternary voting games, (j,k) simple games) |
| A third state that is **not ordered** between the other two | **New.** No theorem found |
| Orientation as selector rather than magnitude | **New.** Plausible but untested |
| Two-completion test and the pivotality corollary | Derived here. Follows from monotonicity alone, so it is sound given the premises |

The honest summary: the skeleton is borrowed and load-bearing, the graft is one sentence wide, and the graft is where the risk sits. That is a good ratio. A failure of the graft costs the graft, not the structure.

### Falsification conditions

Three ways to find out this is a blind alley, cheapest first.

1. **EDGE collapses into abstention.** If every observed EDGE turns out to sit coherently between FACE and TAIL, drop the orthogonality claim and adopt (j,k) simple games wholesale. Loss: the novelty. Gain: a complete existing theory with power indices already derived.
2. **Orientation never changes anything.** If `EDGE_POS` and `EDGE_NEG` route to resolution procedures that converge on the same answer at a rate indistinguishable from chance, the orientation is decoration. Drop it; keep EDGE as a single unoriented state.
3. **The group rule reads the orientation directly.** If the group verdict depends on the orientation of a pivotal EDGE element and not merely on its eventual resolution, the two-completion test is invalid and the group rule must become a genuine three-input function. This is the expensive failure, and the one worth testing first.

Each is decidable by running the circuit against held-out cases rather than by argument. That is the subject of the companion document.

### Sources

- [On the characterization of weighted simple games](https://link.springer.com/article/10.1007/s11238-017-9606-z) — the threshold-logic / simple-game isomorphism
- [Weighted voting systems: a threshold-Boolean perspective](https://www.sciencedirect.com/science/article/pii/S2307187725008752) — MWCs as prime implicants; Banzhaf via the Boolean difference
- [Felsenthal and Machover, Ternary voting games (1997)](https://link.springer.com/article/10.1007/BF01263275) — three input states, extended power indices
- [Freixas and Zwicker, Weighted voting, abstention, and multiple levels of approval (2003)](https://link.springer.com/article/10.1007/s00355-003-0212-3) — (j,k) simple games; grade trade robustness presupposes ordered levels
- [Many-valued logic](https://plato.stanford.edu/entries/logic-manyvalued/) (Stanford Encyclopedia) — Kleene's U as undefined output of a partial function
- [Classical implication for three-valued logic](https://link.springer.com/article/10.1007/s10849-025-09436-w) — weak Kleene / Bochvar and the infectious third value
