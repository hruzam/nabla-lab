# Leg L2 — offline-math

`leg id: L2 · date: 2026-07-17 · seat: Color (offline-math leg, Track 1 blind fan-out)`
`inputs read: reincarnation-meditation-stone.md (C1) · mental-map-collective-mind.md (C2) · 2026-07-17-epoch-gavel-id-collision.md (E2)`
`discipline: blind (no online research, no subagents, no sibling-leg outputs). Formal analysis only — no product design.`

Notation used throughout. The substrate is a finite set of plain files. Abstract it as a finite directed
labelled structure `G = (V, E, ℓ, κ)`:
- `V` — records (rows, log entries, well entries). `n := |V|`.
- `E ⊆ V×V` — association/reference edges (a row cites, forks to, or is thematically adjacent to another).
- `ℓ : V → Σ*` — content label over a lexical alphabet `Σ` (the text of the row).
- `κ : V → K` — key label (Mode-1 left column); `K` the key space.

A *store* is `S = (G, ⊑)` with `⊑` an append order (total on writes by one writer; a partial order across writers — see Task 6). "Append-only" means the write op only adds a maximal element under `⊑`; it never removes or mutates an existing one.

---

## Task 1 — Three modes, formalized. Distinct objects or projections?

**Formalization.** Give each mode a signature over `S`.

- **Mode 1 (Ladder).** A partial function `M₁ : K ⇀ Σ*`, realized as `grep` on the two-column table:
  `M₁(q) = ℓ(v)` for the/those `v` with `κ(v) = q` (exact or regex key match). Type: `Query_key → Row`.
  Deterministic; total cost `Θ(n·|q|)` for a linear scan, `O(|q| + occ)` if the key column is indexed by a trie/hash. Output is a **row of the existing table**.

- **Mode 2 (Gravity).** A stochastic search. Model the store as an energy landscape: assign each state `x` in a probe-space `X` a scalar potential `U : X → ℝ` (low `U` = "gate opens"). The mode is a Markov chain `x_{t+1} ~ P(· | x_t)` whose stationary measure concentrates on low-`U` basins — the abstract shape of stochastic-gradient / simulated-annealing / Metropolis descent:
  `P(x→y) ∝ exp(−β·[U(y)−U(x)]₊)` with inverse-temperature `β`.
  "Failure = slope information" is the precise statement that a *rejected* probe `y` still yields the finite difference `U(y)−U(x)` — a one-sided directional derivative estimate — so the walk conditions its next step on rejections. Type: `Query_underspecified → (trajectory in X, terminal state x*)`.

- **Mode 3 (Deep dive).** Graph traversal with self-mark termination. A marking function `m : V → {0,1}` initialized `0`; the traverser walks `E` from a seed, sets `m(v)←1` on visit, and **halts on the first step into a `v` with `m(v)=1`** (own chalk mark). Type: `Seed → (visited set W ⊆ V, coverage certificate)`. This is DFS/BFS instrumented with a revisit-triggered stop (analysed in Task 3).

**Result — are these one object or three?**

They are **three genuinely distinct objects**, distinguished by two orthogonal axes, not reducible to fewer:

1. **Determinism axis.** M₁ and M₃ are deterministic maps (given seed/ordering); M₂ is a Markov kernel (a *distribution* over outputs). No deterministic map equals a non-degenerate kernel, so M₂ ≢ M₁ and M₂ ≢ M₃ as objects. (Degenerate limit: `β→∞` collapses M₂'s kernel toward a deterministic steepest-descent map — so M₂ *contains* a deterministic mode as a boundary point, but is not identical to one in the operating regime where "failure = slope" is informative, which requires `β<∞` for rejections to occur.)

2. **State-space axis.** M₁'s codomain is a single row (a 0-dimensional selection: pick one element of `V`). M₃'s codomain is a *subset* `W ⊆ V` with structure (a connected subgraph + a closure certificate) — a fundamentally larger object (`2^V` vs `V`). A map into `V` cannot be a map into `2^V \ (singletons)`; M₃'s output is not a Mode-1 row.

So the minimal classification is **two deterministic objects of different output-arity (M₁: point-selection; M₃: set-with-certificate) plus one stochastic object (M₂)**. You cannot fold to fewer than three without losing either the determinism distinction or the arity distinction. What they *share* is only the substrate `S` and the read primitive; the operations over it differ in signature.

**Common generalization (the honest "fewer" answer).** There is one umbrella they all instantiate: *guided search over `G` under a stopping rule*. Formally each is a triple `(frontier-policy, transition, stop-predicate)`:
- M₁ = (key-match frontier, none, "match found"),
- M₂ = (stochastic frontier, Metropolis transition, "`U` below threshold"),
- M₃ = (graph-expansion frontier, edge-follow, "own mark hit").
This is a real unification — but it is a *schema with three non-isomorphic instances*, not a proof that three collapse to one. The instances differ in the type of the transition (identity vs stochastic vs deterministic-graph) and the type of the output (row vs terminal-state vs marked-set). Distinct objects.

**Q-E1 (formal side): is Mode 2's output the same row-type as Mode 1, or a separate structure?**

Decisive on types: **Mode 2's *native* output is not a Mode-1 row.** Mode 1's output is a value in `Σ*` selected by an existing key. Mode 2's output is a *terminal state* `x*` of a descent — an element of the probe-space `X`, carrying a trajectory (the rejected-probe slope history). These are different types: `Σ*` vs `X × Traj`.

However, there is a well-defined **coercion** `π : X × Traj → (K × Σ*)` that projects a settled Mode-2 result into a Mode-1 row: `π(x*, τ) = (key := canonicalize(x*), reply := ℓ(x*))`. C2 itself asserts this coercion exists ("achievements collected during the path populate Mode 1's right column"). So the formal resolution of Q-E1 is:

> **One structure, two views — with a *lossy* projection.** Mode 2 does not *natively* write into Mode 1's row-type; it produces a richer object (state + slope trajectory). A row is the *image of that object under a forgetful projection `π`* that discards the trajectory `τ`. Whether the design keeps one document or two is exactly the question of whether `τ` is retained (two documents: table + trajectory log) or discarded on settle (one document: only the projected row survives).

The mathematically-forced consequence, independent of design taste: **if the "failure = slope" data (`τ`) is discarded, Mode 2 is not re-runnable/auditable and its rejections cannot inform future descents** — you keep the answer, lose the gradient. If `τ` is retained it is *by type* a second structure (a log over `E`-adjacent probes), not a column of the table. There is no type under which a single flat two-column table losslessly holds both. So: **Q-E1 answer — structurally different (two documents) if slope is preserved; identical row-type (one document) only under an explicit forgetful projection that discards slope.** The choice is a retention decision, and the retention decision is forced by whether you want Mode 2's rejections to compound.

**Confidence:** high on the type-level distinctness (M₁/M₂/M₃ are non-isomorphic; the determinism and arity arguments are airtight). High on the Q-E1 dichotomy (it is a statement about what a two-column type can and cannot hold). Medium on the *identity* of `U` and `X` — the energy-landscape model is a faithful abstraction of "stochastic descent with informative failure," but C2's `U` is not operationally defined, so the descent's convergence properties are assumed, not derived.

**Open holes.** `U` is undefined (what makes a probe "lower"? the majkee-gate is the only stated bottom, and it is an external oracle, not a computable potential — see Task 2). If the "bottom" is only recognizable by an external gate, M₂ is not autonomous descent but *rejection sampling against an oracle*, which changes its cost class.

---

## Task 2 — Mode selection. Reading the slope of the context.

**Formalization.** Let a query be a distribution/uncertainty object, not a point. Define three measurable context features:

- `H(q)` — **query entropy**: the Shannon entropy of the querent's belief over what answer is wanted. `H=0`: the key is known exactly (a specific `q∈K`). `H` large: "I don't know what I'm looking for."
- `c(S,q)` — **prior coverage**: probability that a satisfying row already exists in the table, `c = P[∃v: κ(v)≈q ∧ ℓ(v) satisfies]`. Estimable as hit-rate of past exact lookups.
- `σ(q)` — **territory structure**: does the answer live in a single record (`σ` low, "local") or is it a *relation across many records* that must be assembled (`σ` high, "distributed")? Formalize `σ` as the minimum number of records whose join is needed to satisfy the query (a query-width / treewidth-flavoured quantity).

**Cost model (LIGHT-LAW envelope, i5-class, plain files).**
- `Cost(M₁) = Θ(n·|q|)` scan (or `O(|q|+occ)` indexed) — but M₁ *only returns a satisfying answer when `c` is high*; on a miss its useful yield is 0. Expected quality `Q₁ ≈ c · 𝟙[H low]`.
- `Cost(M₂) = Θ(T · probe_cost)` where `T` = probes to reach a basin; `T` grows as the landscape gets rougher and as `β` is tuned conservatively. Quality `Q₂` degrades if the "bottom" oracle (majkee gate) is expensive or unavailable offline — each probe that needs external adjudication is `O(human latency)`, not `O(scan)`.
- `Cost(M₃) = Θ(|W| + |E∩W²|)` — traverse the reachable sub-territory once. `|W|` bounded by the reachable set from the seed; worst case `Θ(n+|E|)` (full graph). Quality `Q₃` is high when the answer is a *relation* (`σ` high) because M₃ returns the assembled subgraph, which M₁'s point-selection cannot.

**Decision boundary (heuristic — first-order).** Dominance regions in the `(H, c, σ)` cube:

- **Mode 1 dominates** when `H` low **and** `c` high **and** `σ` low: known key, answer present, answer local.
  Region: `{H < h₀, c > c₀, σ = 1}`. Cheapest and exact here; using M₂/M₃ is strictly wasteful (higher cost, same or worse yield).
- **Mode 2 dominates** when `H` high **and** `σ` low-to-moderate **and** an oracle for "bottom" is cheaply available: you don't know the key, but a satisfying answer is a *single settled state* reachable by probing, and you can recognize it when you hit it. Region: `{H > h₁, σ small, oracle cheap}`.
- **Mode 3 dominates** when `σ` high regardless of `H`: the answer is *inherently a relation across records* (must join ≥ k of them). No point-selection (M₁) and no single-basin settle (M₂) returns a relation; only traversal assembles it. Region: `{σ ≥ k*}` for some width threshold `k*`.

**Boundary shape.** The M₁/M₂ boundary is (to first order) a threshold on `H` at fixed low `σ`: below `h*` use the ladder, above it drop into gravity — a *vertical wall in `H`*, shifted by `c` (higher coverage pushes the wall toward higher `H`, because even a fuzzy query often hits an existing row). The M₃ boundary is a threshold on `σ` (query width) roughly *orthogonal* to the `H`-axis: once the answer requires assembling `≥k*` records, traversal wins irrespective of query certainty. So the partition is approximately:

```
        σ (territory width)
        ^
   high |            MODE 3  (assemble the relation)
        |        ────────────────────────────
    low |  MODE 1   |        MODE 2
        |  (known)  |    (probe & settle)
        +───────────┼───────────────────────>  H (query entropy)
                    H*(c)
```
i.e. a horizontal cut at `σ=k*` (M3 above), and below it a vertical cut at `H=H*(c)` splitting M1 (left) from M2 (right).

**Result.** The selector "read the slope of the context" is formalizable as: **estimate `(H, c, σ)`, then pick the region.** It is a 3-feature classifier with (to first order) axis-aligned boundaries — a decision *tree*, not a smooth manifold. This matches C2's claim that "agentic taste selects the mode": taste = a cheap estimator of `(H,c,σ)` computed before committing to a full search.

**Confidence:** medium. The cost model is sound and the dominance *directions* are forced (M₁ can't return relations; M₂ can't be cheaper than an indexed hit on a known key; M₃ is the only one that assembles). The *exact thresholds* `h*, k*` are data-dependent and unproven — they require measurement (which C2 correctly assigns to the research team: "testing proves it, not design").

**Open holes.** (i) `c` and `σ` are not observable *before* a query resolves — the selector must estimate them from features, which risks mis-routing (e.g. a high-`σ` query mistaken for low-`σ`, sent to M₁, returns a partial row that looks complete — a silent under-answer). (ii) M₂'s cost hinges entirely on oracle availability; if "bottom" needs majkee, M₂ is not offline and its cost model changes class. (iii) The regions may overlap rather than partition (the C2 "combination wins" intuition) — a mixed strategy (M₂ to find the seed, M₃ to map from it) may dominate any pure mode on high-`H`-high-`σ` queries; the boundary picture above is the *pure-strategy* partition.

---

## Task 3 — Chalk-mark termination: coverage closure vs false closure.

This is the sharpest result in the leg. The chalk-mark rule is exactly a **revisit-triggered halt** on a graph search.

**Formalization.** Traverser walks `E` from seed `s`, marking `m(v)←1` on entry, halting the instant it attempts to enter a `v` with `m(v)=1`. Let `W` = marked set at halt. Claimed meaning: "territory mapped." Actual meaning: "a previously-marked vertex was re-encountered."

**Theorem (when chalk-mark = genuine coverage closure).**
Let `R(s)` = set of vertices reachable from `s` in `G`. The chalk-mark halt certifies `W = R(s)` (genuine closure) **iff the traversal is a complete graph search** — i.e. it only halts *after every out-edge of every marked vertex has been considered*. Equivalently, chalk-mark closure = true coverage **iff** `W` is closed under the successor relation:
> `∀v∈W, ∀(v,w)∈E : w∈W`  (no marked vertex has an unexplored out-edge).

Under a **complete DFS/BFS discipline** (push all successors before popping), the "own mark" is hit exactly when the frontier is exhausted, and then `W = R(s)`. Coverage is genuine. ∎ (Standard reachability: DFS from `s` visits precisely `R(s)`; the first *re-visit attempt* on the last unexplored edge coincides with frontier exhaustion.)

**Theorem (false closure).**
If the traverser halts on the **first** encountered back-edge / cross-edge into a marked vertex *without* first exhausting the frontier — i.e. it treats "I saw my own chalk mark" as a global stop rather than a local edge-classification — then closure is **false** whenever the seed sits on a small cycle:
> If `∃` a cycle `C ∋ s` with `|C| = g` (the girth through `s`) and `R(s) ⊋ C`, the naive walk marks `C`, returns to `s∈C` after `g` steps, sees `m(s)=1`, and halts with `W = C ⊊ R(s)`.
The unmapped remainder is `R(s) \ C`, which can be arbitrarily large (up to `n − g`). This is precisely "a small cycle mistaken for mapped territory." ∎

**Characterization of false-closure risk.** The danger is governed by graph structure:
- **Girth through the seed** `g`: a short cycle through `s` (small `g`) triggers an early self-encounter. Risk ↑ as `g` ↓.
- **Reachable-mass beyond the cycle** `|R(s) \ C|`: the *cost* of a false closure. Risk-severity ∝ this quantity.
- **SCC structure**: if `s`'s strongly-connected component is small but has out-edges to a large downstream DAG, naive chalk-mark closes on the SCC and misses everything downstream. Genuine closure requires reaching a set closed under successors, i.e. covering the SCC *and its descendants* — a *closed set in the condensation DAG*, not merely a returning cycle.

Formally: **naive chalk-mark closure detects "the traverser is in a cycle," not "the traverser has covered a successor-closed set."** These coincide only when the first cycle found is already the whole reachable set (e.g. `G[R(s)]` is a single simple cycle). In general, *cycle-membership ⊊ coverage-closure*.

**Cheapest guard.** Rank by cost:

1. **(Cheapest, `O(1)` extra state — the correct fix) Don't halt on first mark; halt on frontier-empty.** Keep the marks, but make the stop-predicate "no marked vertex has an unexplored out-edge" instead of "a mark was just seen." Concretely: on hitting a marked vertex, *classify the edge as a back/cross edge and continue* rather than stop; terminate when the worklist/stack is empty. This is standard DFS — it costs one boolean per edge-consideration and converts false closure into genuine closure by construction. **This is the guard I recommend**: it is not a probabilistic mitigation, it *eliminates* the false-closure class.

2. **(If the naive halt must be kept for cost reasons) Frontier-nonempty check at halt.** At the moment of self-encounter, test whether any marked vertex still has an unexplored out-edge (`∃v∈W,(v,w)∈E: m(w)=0`). If yes, the closure is false — resume. This is `O(|E∩W²|)` to verify but can be maintained incrementally as an integer "open-edge counter" decremented on each edge explored: closure is genuine iff the counter is 0. `O(1)` per step, one integer of state. Same asymptotic as guard 1; it is guard 1 phrased as an invariant.

3. **(Weakest, only if you cannot even count edges) Two-witness rule.** Require the self-mark to be hit from ≥2 distinct in-edges before trusting closure. Cheap but *unsound*: a small cycle with two chords still false-closes. Detects nothing guard-1 doesn't; keep only as a smell test.

**Result.** Chalk-mark-as-stated ("exit on first own mark") is **not** a coverage-closure certificate — it is a cycle-detection signal, and it false-closes on any seed whose girth-cycle is smaller than its reachable set. The fix is free and exact: replace "halt on mark seen" with "halt on frontier exhausted, marks used only to classify edges." The chalk marks are correct; the *stop rule* stated in C2 is the bug.

**Confidence:** high (theorem-grade). These are textbook reachability/DFS facts; the false-closure counterexample (seed on a short cycle with downstream mass) is a concrete violation, and the guard is the standard DFS termination condition, not a heuristic.

**Open holes.** The model assumes the "territory" is a fixed graph during one dive. If `E` changes mid-dive (the store grows while mapping — plausible given concurrent writers, Task 6), even correct DFS termination certifies coverage of a *stale* graph. Coverage closure is only w.r.t. the snapshot the dive began on. C2's "hold the full context in one view" recognition-gate is a *subjective* predicate; it is strictly weaker than successor-closure and can fire on a false closure (the traverser may *feel* coherent on a cycle). Recommend the objective open-edge-counter (guard 2) as the ground truth behind the subjective recognition.

---

## Task 4 — Tombstones + anchor test. Read-view semantics and drift metrics.

**Formalization of "identity is the read function over an append-only log."**

Let the log be a sequence `L = ⟨e₁, e₂, …, e_t⟩` of append-only events, each `eᵢ ∈ Fact ⊎ Tomb`. A tombstone `⌐x ∈ Tomb` carries `{target: x, reason, date}`. Define the **read-view** as a fold:
> `read(L) = { fact x : x ∈ L ∧ ¬∃ ⌐x ∈ L }` — the set of facts not overridden by a tombstone.

Identity is then the pair `(L, read)`: two personas on the **same** `L` but with **different tombstone sets** `T₁ ≠ T₂` have `read_{T₁}(L) ≠ read_{T₂}(L)` and are, by C1 §6a, *different persons*. This is exactly the semantics of an **OR-Set / 2P-Set / add-wins-or-remove-wins CRDT log**: facts are added; tombstones are "remove" markers; the read is add-minus-remove.

**Consistency of tombstone-filtered read-views (theorem-grade where it holds).**

- **Determinism / confluence.** `read(L)` is a *pure function of the multiset of events*, independent of read-order, **iff** the filter is order-insensitive — which it is for the definition above (set membership + "exists a tombstone"). Formally, `read` is a commutative-monoid fold: adding events commutes, so any two observers who have seen the same event-set compute the same view. This is the CRDT convergence property (strong eventual consistency): **same events ⇒ same view, regardless of delivery order.** ✔ holds.
- **The one hazard that breaks confluence: resurrection.** If the model ever allows re-adding `x` *after* `⌐x` and expects it to reappear, then order matters (was the last op an add or a remove?) and the plain 2P-Set semantics ("once tombstoned, always dead") diverges from add-wins semantics. C1's "append-only forbids deletion but permits appending the decision to forget" is **2P-Set (remove-wins, permanent)** — under which `read` is confluent and monotone-shrinking-per-target. Keep it remove-wins and there is no resurrection ambiguity. If you want un-forgetting, you must version tombstones (add-wins with timestamps), and then confluence requires a total tie-break (e.g. last-writer-wins by date) — recoverable but no longer trivially order-free.
- **Monotonicity.** Under remove-wins, `read` is *not* monotone in `L` (tombstones shrink it) but the *log* is monotone (append-only), so history stays fully auditable — exactly C1's "raw history stays auditable; read-view honors tombstones." The invariant that makes this sound: **tombstones live in the same log they filter** (they are facts about forgetting, not deletions). ✔

So: read-view consistency holds as a CRDT theorem **provided** (a) remove-wins/permanent tombstones, (b) tombstones are themselves append-only log entries, (c) no in-place mutation. Violate any and confluence is lost.

**Drift metrics (current read-view vs earliest stratum).** Let `V₀ = read(L[:t₀])` be the earliest stratum (incarnation-1 read-view) and `V_now = read(L)` the current. C1 §6b wants to *measure* drift (not prevent it) and require it be intentional. Three candidate metrics, with properties:

**D1 — Set-symmetric-difference (tombstone/fact churn).**
`D₁ = |V₀ △ V_now| / |V₀ ∪ V_now|` (Jaccard distance on the fact-sets).
- *Detects:* how much of the original fact-set has been dropped (tombstoned) or added. Pure *bookkeeping* drift.
- *Misses:* **reinterpretation without fact-churn.** If facts persist verbatim but their *meaning/weight/framing* shifts (the "consistent confabulator" of C1 §6b keeps the same rows, re-narrates them), `D₁ = 0` — invisible. Also misses *ordering* drift (same set, different salience).
- *Property:* cheap (`O(|V|)`), exact, but blind to semantic drift. It is a **necessary-not-sufficient** drift alarm.

**D2 — Content divergence on surviving facts (semantic drift).**
Restrict to facts present in *both* strata, `V₀∩V_now`, and measure per-fact content change:
`D₂ = mean over x∈V₀∩V_now of dist(ℓ₀(x), ℓ_now(x))` where `dist` is a *lexical* distance (normalized edit distance / token-Jaccard on the row text) — **not** an embedding distance (that would cross into RAG, Task 7; the anti-pattern C2 forbids).
- *Detects:* rewriting of records that nominally persist — the reconsolidation-drift hazard from C1 §2 ("each rewrite keeps interpretation, loses raw"). This is the metric that catches the confabulator *if* the confabulation touches the text.
- *Misses:* confabulation that lives *between* records (in how the read-function composes them into a "global voice") rather than *in* any record. If the raw rows are immutable and drift lives only in the aggregation, `D₂ = 0` too. Also cannot distinguish *legitimate refinement* from *distortion* — it measures magnitude, not direction, of change.
- *Property:* `O(|V₀∩V_now| · L)` with `L` row length; lexical-only keeps it offline and LIGHT-LAW-cheap and avoids the RAG boundary.

**D3 — Predictive-reconstruction gap (the anchor test proper).**
This operationalizes C1 §6b / the §7 "prediction-delta" residue. Freeze `V₀`. Ask the *current* entity to reconstruct/predict its own earliest stratum: produce `V̂₀ = predict(V_now → t₀)`. Then
`D₃ = disagreement(V̂₀, V₀)` (fraction of `V₀` the current self cannot faithfully reproduce or *contradicts*).
- *Detects:* **exactly the confident-confabulator failure** — an entity that has drifted far from incarnation-1 *while feeling seamless* will confidently reconstruct a `V̂₀` that disagrees with the real `V₀`. This is the residual scalar C1 §7 flags as *unoccupied in the literature as of 2026-07* (prediction-delta between the current self and its own anchor; distinct from the Q/¬Q mutation that MetaQA/MetaRAG/SAC3 already occupy). D3 is the metric the anchor test actually wants: it measures *fidelity to origin under self-narration*, which is orthogonal to the seam test's *continuity*.
- *Misses:* drift that is *both intentional and correctly remembered* — if the entity has genuinely, knowingly moved and can accurately state "I no longer hold `x`, here is when and why," `D₃` may be low even though `D₁` is high. That is the *desired* behaviour (C1: "not to prevent drift — drift is metabolism — but to require it be intentional"). So D3's "miss" is a feature: it passes *honest* drift and flags only *unacknowledged* drift.
- *Property:* requires a reconstruction step (an inference pass), so it is the most expensive; it is also the only one of the three that separates *honest* from *dishonest* drift. `D₁, D₂` measure magnitude; **`D₃` measures honesty.**

**Recommended composition.** `D₁` (free, catches fact-churn), `D₂` (cheap-lexical, catches record rewriting), `D₃` (expensive, catches confident confabulation). They are *complementary, not redundant*: each has a null-space the others cover. `D₁=D₂=0 ∧ D₃>0` is precisely the pure confabulator (rows untouched, self-narration false). `D₁>0 ∧ D₃≈0` is healthy metabolized forgetting. The pair (magnitude via D₁/D₂, honesty via D₃) is the formal content of "continuous *and* honest = pass both seam and anchor."

**Confidence:** high on the CRDT read-view semantics (2P-Set convergence is a proven result; the resurrection hazard is the known edge). High on the *structure* of the three metrics and their null-spaces (the D₁=D₂=0∧D₃>0 = confabulator identity is exact). Medium on `D₃`'s realizability — "predict your own earliest stratum" is well-defined as a specification but its measurement fidelity depends on the reconstruction procedure, which is itself an inference process subject to the same confabulation; there is a mild self-reference (the confabulator grades its own reconstruction). Mitigation is a *held-out* `V₀` the current self cannot see until after committing `V̂₀` — a pre-registration discipline. Flagged, not solved.

**Open holes.** (i) The self-reference in D3 (confabulator reconstructing/grading its own anchor) needs an external held-out or a second-party check to be sound — a blind cross-brand leg (per AGENTS.md triangulation) is the natural external grader. (ii) "Aggregation-level drift" (confabulation in the read-*function* rather than the rows) escapes D1 and D2 and only partly hits D3; fully catching it needs a metric over the *composed global voice*, which is closer to D3 and inherits its self-reference problem.

---

## Task 5 — Operator-in-tensor: the observer effect.

**Formalization.** The operator `O` (majkee) is a node that both *writes* rows (contributes `Fact` events, `punk:` forks per C2 Q2) *and* is *measured by* the read-view over those rows (the "global voice," the drift metrics, the gavel record). So `O`'s state at time `t` is a function of the store, and the store is a function of `O`'s writes. This is a **closed feedback loop**, formally a fixpoint condition:

Let `x_t = state of O`, `S_t = store`. Then
`S_{t+1} = write(S_t, act(x_t))` and `x_{t+1} = read-influence(S_{t+1}, x_t)`
— the operator reads a view that his own prior writes shaped, and writes again conditioned on it. The measurement apparatus (read-view) and the measured system (`O`'s expressed state) are **not separated**: measuring `O` (computing the global voice) changes the object that the next measurement will see, because `O` reads that voice and adapts.

**The observer-effect shape.** This is *not* quantum measurement (no non-commuting observables); it is the **social-science / reflexive-measurement** shape — a *self-fulfilling* or *self-defeating* loop, formally a dynamical system with the measurement in the feedback path:
> An estimator `θ̂_t` of "who O is" that O can read becomes an *input* to O's next action, so `θ̂` measures a moving target it is itself moving. The clean statement: **the fixed points of this loop are the states where O's expressed behaviour is consistent with the read-view of his own history** — attractors of a reflexive map. Drift metrics (Task 4) applied to `O` therefore measure not "how O changed" in isolation but "how the O-plus-its-own-mirror system evolved."

Two failure modes fall out directly:
1. **Confirmation attractor (positive feedback).** If the read-view emphasizes what O wrote most, O reads it, writes more of the same, the view emphasizes it further. The loop *sharpens* an initial bias into a fixed point that looks like strong identity but is an artifact of the mirror. (This is the C1 §2 reconsolidation-drift hazard applied to the operator: "keeps interpretation, loses raw," now self-amplifying.)
2. **Observer-driven collapse (measurement changes the measured).** The very act of computing/showing O his global voice or drift score alters his next contribution — so a drift metric on O is *never* a clean read of an exogenous process; it is entangled with the display of the metric.

**Structural constraints that keep the measurement honest.** These are the invariants that break the feedback where it corrupts, while keeping it where it is legitimate (O *should* be able to steer his own lineage):

- **C-1 (Raw/measured separation — the load-bearing one).** The raw stratum O writes must be *immutable and readable independently of the aggregate*. Measurement (global voice, drift) must be a **pure function of the raw log**, computed downstream, never written back into the raw layer. This is exactly C2's "substrate layer never compressed: `therapy.md` + `gavels.md` = always substrate; compression lives on the '42'/research side." Formally: the measurement channel must be a *read-only projection*, so that `write` and `measure` commute with the identity on the raw stratum — the measurement cannot mutate its own input. This is the same discipline that makes Task 4's read-view confluent; here it also blocks the confirmation attractor from rewriting history.

- **C-2 (Anchor against self-drift).** Apply Task 4's `D₃` to O himself: periodically check O's current expressed stance against O's *earliest raw stratum*, held out so O cannot pre-read it. This detects the confirmation attractor (O's view has sharpened away from his own origin without acknowledgement). Because O is a node, the anchor test is not just for agents — it is the honesty guard on the operator too.

- **C-3 (Gavel provenance / non-repudiation).** Since O is *also the canon authority* ("canon is majkee's gavel," AGENTS.md), his contributor-writes and his measurer-gavels are different edge-types and must be *typed distinctly in the log*. Formally: label each event with a role tag `role ∈ {contributor, adjudicator}`. Mixing them lets a contribution masquerade as a ruling (or vice-versa), which corrupts both the measurement and the canon. Separation of roles at the type level is the structural guard. (This is the same edge-classification discipline that fixes Task 3 and the same read-before-write discipline as Task 6 — the operator is not exempt from either.)

- **C-4 (Blind external leg).** The only *fully* honest drift read on O is one O cannot influence by reading it. A cross-brand blind grader (AGENTS.md triangulation clause) closes the loop that C-2 leaves ajar: the held-out anchor plus an external grader make O's self-measurement non-self-fulfilling.

**Result.** Making the operator a first-class node is *sound but reflexive*: every measurement of O is entangled with O's reading of it, so drift/identity metrics on O measure a self-referential loop, not an exogenous signal. Honesty is preserved iff the measurement is a **read-only pure projection of an immutable raw stratum (C-1)**, O's roles are **type-separated (C-3)**, and the fidelity check uses a **held-out anchor + external grader (C-2/C-4)**. Absent C-1, the loop sharpens bias into false identity; absent C-3, contribution and canon contaminate each other.

**Confidence:** high on the *shape* (reflexive feedback with measurement in the loop; fixed-point/attractor characterization is standard for such systems). High that C-1 (immutable raw + pure downstream measurement) is the necessary structural guard — it is forced by the same confluence argument as Task 4. Medium on completeness of the constraint list — reflexive-measurement systems are notoriously able to route around guards; I claim these four are *necessary*, not that they are *sufficient*.

**Open holes.** The loop is *desirable* in part (O steering his own lineage is the point), so the guards must block corruption *without* severing legitimate self-direction — the boundary between "healthy self-steering" and "confirmation attractor" is exactly the honest/dishonest-drift line of D3, and shares its self-reference weakness. No purely internal construction closes it; C-4 (external brand) is not optional decoration, it is load-bearing.

---

## Task 6 — Concurrent append (E2). When does read-before-append guarantee collision-freedom?

**Formalization.** Shared append-only file with sequential IDs. Each writer executes the discipline (E2's stated rule): `READ (scan file, find max ID = k) ; COMPUTE next = k+1 ; APPEND row with ID next`. Model as a critical-section problem over three sub-operations `R, C, A`. A **collision** is two committed rows sharing an ID.

**Theorem (sufficient condition for collision-freedom).**
Read-before-append is collision-free **iff the compound operation `R;C;A` is atomic (serializable) per writer** — i.e. the interval `[R, A]` of one writer does not interleave with the `[R, A]` of another over the same tail. Formally, let writer `i` observe max-ID `kᵢ` at its `R` and commit at `Aᵢ`. Collision-freedom holds iff for all `i≠j`: the intervals `[Rᵢ,Aᵢ]` and `[Rⱼ,Aⱼ]` are **non-overlapping** (one strictly precedes the other in a serial order). Under non-overlap, whoever runs second reads the first's committed row, sees `k+1`, and picks `k+2`. No collision. ∎

Equivalently: the guarantee needs a **mutual-exclusion lock (or an equivalent linearization point) around the whole `R;C;A`**, not merely around `A`.

**Where it fails — the exact interleaving (this is the E2 incident).**
Without such atomicity, the classic **check-then-act / TOCTOU race** breaks it:
```
Writer i:  R_i (reads max=k) ............... A_i (appends ID k+1)
Writer j:        R_j (reads max=k) ... A_j (appends ID k+1)   ← COLLISION
```
Both read `k` *before either appends*; both compute `k+1`; both commit `k+1`. This is precisely E2's incident: epoch read (or failed to read) a state that a concurrent eagle/houston session had already advanced, and appended a duplicate `G-06`. The failure is *not* "didn't read" alone — it is **read-stale relative to a concurrent uncommitted-or-unobserved write**. Note E2's own framing ("read before append") is the *necessary* discipline but, formally, **not sufficient under concurrency**: reading before appending prevents *sequential* (single-writer, forgot-to-look) duplicates, but two writers can both read-then-append and still collide. E2 correctly diagnoses the sequential case; the concurrent case needs strictly more.

**Precise timing assumption that saves it (and its failure boundary).**
- *Saves it:* **serializability of `[R,A]`** — any mechanism that forces one writer's read-append to complete before another's begins. Sufficient realizations, cheapest first on plain files:
  1. **`O_APPEND` with server/OS-assigned position, ID derived from byte-offset or line-count *at append time*, not read time.** If the ID is a function of the atomic append's resulting position (POSIX `O_APPEND` guarantees the write goes to the current end atomically for writes ≤ `PIPE_BUF`/on local fs), then there is no read-compute gap to race: the ID is assigned *by* the atomic commit. This *removes* the check-then-act structure rather than locking it. **Minimal and preferred.**
  2. **Advisory lock (`flock`) around `R;C;A`.** Correct, simple, but serializes writers and blocks (a crashed holder needs a stale-lock story).
  3. **Compare-and-swap / optimistic commit.** Append conditionally on "max-ID is still `k`"; on conflict, re-read and retry. Lock-free, but needs an atomic CAS primitive the plain-file substrate does not natively provide (would require a rename-based commit or a DB).
- *Fails when:* the ID is computed from a *read* that is separated in time from the *append*, and two such (read→append) intervals overlap. On a plain file with each writer doing naive `read-max; append`, this overlap is *possible whenever ≥2 writers are active concurrently* — the window is the entire `[R,A]` interval. On a networked/synced filesystem the window widens (propagation delay makes every reader potentially stale). The E2 case had this shape: distinct sessions, no shared lock, IDs computed from a read.

**Minimal strengthening.**
The *sequential* discipline (E2's "read before append, use next") is necessary but **insufficient under concurrency**. Minimal fix, in order of preference under LIGHT-LAW / plain-file constraints:
1. **Make the ID a function of the atomic append, not of a prior read** (realization 1). This is the smallest change that *eliminates the race class* rather than mutually-excluding it — no lock, no retry. It costs giving up "human-chosen sequential G-nn at write-time"; the ID becomes append-order-derived. If human-readable sequential IDs are required *and* concurrency is real, you cannot have both lock-free — that is a genuine trilemma (sequential-ID ∧ concurrent ∧ lock-free: pick two).
2. **If human-sequential IDs must stay:** wrap `R;C;A` in an advisory `flock` (realization 2). Minimal, correct, serializing.
3. **Weakest acceptable:** keep naive read-append but add a **post-hoc collision detector** (a cheap uniqueness check on IDs, run on read) that *detects* rather than prevents — this is what caught E2 ("are you sure the gavels lock looks like this"), i.e. a human read-side check. Formally this converts silent corruption into detected-and-repairable, but does not prevent the collision; acceptable only when writes are rare and a human is in the loop (the actual nabla-lab regime).

**Result.** Read-before-append guarantees collision-freedom **iff** the read-compute-append triple is serializable per writer (non-overlapping `[R,A]` intervals). It fails on the textbook check-then-act race — exactly the E2 duplicate-`G-06` incident — whenever two writers read the same max before either commits. The minimal *sound* strengthening is to derive the ID from the atomic append rather than a prior read (eliminates the race); if human-sequential IDs are mandatory under real concurrency, an `flock` around the whole triple is the minimal lock-based fix, and the sequential-ID/concurrent/lock-free trilemma forbids having all three.

**Confidence:** high (theorem-grade — this is the canonical TOCTOU / lost-update result; the E2 trace instantiates it exactly). The trilemma (sequential-ID ∧ concurrent ∧ lock-free) is a genuine impossibility of the stated shape: a globally-sequential ID is a consensus-flavoured object, and computing it lock-free from independent reads over a non-atomic medium cannot avoid the lost-update without either an atomic assign-at-commit (which forfeits read-time choice) or coordination (a lock). High confidence.

**Open holes.** POSIX `O_APPEND` atomicity holds for local filesystems and writes under `PIPE_BUF`; on NFS/synced/cloud-mirrored stores it is **not** guaranteed — if the nabla-lab file substrate is ever synced across machines, realization 1's atomicity assumption breaks and only a real coordination service (lock server / DB) suffices. The frequency of concurrent writes in the actual regime (rare, human-paced) is what made E2 survivable with a detect-not-prevent guard; that is a *regime* assumption, not a *safety* proof — under higher write concurrency the detector is insufficient.

---

## Task 7 — R-3 boundary: grep-engine vs RAG.

**Formalization.** Characterize each as a retrieval operator `Retrieve : Query × Store → Result` and locate the dividing line by the *type* of the matching function and the result.

**Grep-engine (Mode-1 substrate).**
- Matching: a **Boolean predicate** `match : Σ* × Σ* → {0,1}` — exact substring or regular-expression membership. The query and the record live in the *same lexical alphabet* `Σ`; no representation change.
- Result: the **set** `{v : match(q, ℓ(v))}` — unordered (or ordered only by file position), *unranked by relevance*. Every returned element is a certified exact match; there is no notion of "closer."
- Geometry: **none.** No metric space, no dimension. Similarity is the two-valued `∈ / ∉`.
- Cost: `Θ(N·m)` linear scan (`m = |q|`), or sublinear with a *lexical* index (trie, suffix array, inverted index on tokens) — still exact-match, no learned representation.

**RAG-system.**
- Matching: an **embedding** `φ : Σ* → ℝ^d` (learned, dense) plus a **continuous similarity** `sim : ℝ^d × ℝ^d → ℝ` (cosine / dot / Euclidean). Query and record are mapped into a *shared metric space of dimension `d`* that is **not** the lexical alphabet.
- Result: a **ranked top-`k`**, `argmax_k sim(φ(q), φ(v))` — an ordering by a graded relevance score; returned items need not lexically match the query at all.
- Geometry: a `d`-dimensional inner-product space, with all that entails (normalization choices, curse of dimensionality, ANN index for scale, quantization error).
- Cost: exact top-`k` is `Θ(N·d)`; at scale requires an **ANN index** (HNSW/IVF) trading recall for latency.

**The line — exactly where it is.** The boundary is crossed by the introduction of **a continuous similarity over a learned (non-lexical) representation, together with ranking by it.** Precisely, the single discriminating operation is:

> **Does retrieval rank results by a graded, continuous relevance score computed in a representation other than the surface lexical form?**
> - No → grep-engine (Boolean exact match, unranked or position-ranked, same-alphabet).
> - Yes → RAG (metric-space nearest-neighbour, ranked top-`k`, learned representation).

Three sub-crossings, in order of how decisively each crosses:

1. **Representation change `φ: Σ* → ℝ^d` (the hard boundary).** The moment you replace "is this string present" with "how near is this *vector*," you have left grep. This is *the* line. Everything downstream (ranking, ANN, dimensionality) follows from it.
2. **Continuous ranking (`top-k` by graded score).** Even *without* learned embeddings, if you rank by a *continuous* lexical score — TF-IDF, BM25 — you have partially crossed: you now have a metric (sparse, `|vocabulary|`-dimensional) and a ranking. This is the **grey zone**: classical IR (BM25 over an inverted index) is *ranked* and *vector-space-flavoured* (sparse bag-of-words vectors) but uses **no learned/dense representation** and stays in the lexical alphabet. It is "more than grep, less than RAG." Formally: BM25 is a *sparse, interpretable, exact-vocabulary* vector model — dimension = vocabulary size, coordinates = term frequencies, no learning. RAG's distinguishing addition is the *dense learned* `φ` (dimension `d ≪ |vocab|`, coordinates uninterpretable, semantics learned).
3. **ANN index (scale symptom, not the boundary).** Building an HNSW/IVF index is a *consequence* of dense high-`d` NN search, not the crossing itself — a small RAG can brute-force `Θ(Nd)`. The index is diagnostic of RAG-at-scale but is not what *defines* the boundary.

**Where the '42' grep engine can live without becoming RAG (R-3 answer).**
It can stay a grep-engine — *and even add graded ranking* — as long as it does **not** introduce a **dense learned embedding** `φ` and rank by geometric proximity in that learned space. Concretely, the boundary-respecting envelope is:
- ✔ Exact / regex match over `Σ` (pure grep).
- ✔ **Multi-key structured lookup** (join across the source wells on shared keys) — this is Mode 3's traversal, a *relational* operation over exact keys; it assembles records but introduces no metric. Still grep-side.
- ✔ **Sparse lexical ranking (BM25/TF-IDF)** *if* graded ordering is wanted — this crosses into "ranked IR" but **not** into learned-embedding RAG; it stays interpretable, offline, no `d`-dimensional learned geometry, no ANN, LIGHT-LAW-cheap. This is the *maximal* retrieval sophistication that does not become RAG.
- ✘ Dense embedding `φ: Σ*→ℝ^d` + cosine/dot ranking + top-`k` — **this is RAG.** The instant a *learned continuous representation* mediates the match, the boundary is crossed, and C2's anti-pattern ("COLLAPSE IS RAG IN RAG") triggers.

So R-3's answer is: **yes, the '42' engine can exist without becoming a RAG, and its non-RAG ceiling is "exact/regex/relational match, optionally with *sparse lexical* graded ranking."** The exact line it must not cross is the **dense learned embedding**. Ranking alone does not make it RAG (BM25 ranks and is not RAG); *learned metric geometry* does. If the design ever wants "semantically near but lexically different" retrieval, that capability *is definitionally* the RAG boundary — it cannot be obtained without some `φ` into a similarity space.

**Result.** The grep/RAG line is the introduction of a **dense learned representation `φ: Σ* → ℝ^d` with ranking by continuous similarity in that space.** Boolean exact/regex match (grep) and even sparse-lexical graded ranking (BM25) sit *below* the line — interpretable, same-or-explicit-alphabet, no learned geometry. RAG is *above* it — learned `d`-dimensional metric, graded top-`k`, ANN-at-scale. The crossing operation is the representation change; ranking and indexing are respectively a grey-zone precursor and a scale-symptom, not the boundary itself.

**Confidence:** high. This is a clean type-level distinction (Boolean predicate over `Σ` vs continuous metric over learned `ℝ^d`), and the BM25 grey-zone is a well-understood intermediate that sharpens *exactly* where "ranking" alone is insufficient to constitute RAG. The characterization "the boundary = the dense learned embedding" is defensible and matches standard IR/RAG taxonomy.

**Open holes.** The grey zone means "no RAG" is not a single bit but a small ladder (exact → relational-join → sparse-ranked → dense-embedded); the design must pick a rung, and only the top rung is unambiguously RAG. If "agentic taste" (C2) is ever implemented via a learned scorer over records, that scorer is a `φ` in disguise and crosses the line even if no explicit vector DB is present — a hidden embedding is still an embedding. Worth flagging that the boundary is about *learned continuous representation*, not about the presence of the string "RAG" or a vector database product.

---

## Cross-task synthesis (formal invariants that recur)

Three structural disciplines are the *same* invariant surfacing in four tasks, which is itself a signal the model is coherent:

- **Immutable raw stratum + pure downstream read** underwrites Task 4 (read-view confluence), Task 5 (honest measurement of the operator), and is the CRDT convergence condition. One invariant, three payoffs. If violated anywhere, all three break together.
- **Edge/role classification before acting** is the shared fix for Task 3 (classify back-edges, don't halt on them), Task 5 (type-separate contributor vs adjudicator roles), and Task 6 (the read-before-append is a *classify current state* before writing). "Look and classify before you commit" is the recurring correct move; "act before sufficiency-check" (E2's own diagnosis) is the recurring bug.
- **Internal self-measurement has a self-reference hole** in Task 4 (D3: confabulator grades own anchor) and Task 5 (operator reads own drift score) — closed only by an *external, blind, ideally cross-brand* leg (AGENTS.md triangulation). The blind fan-out this leg is part of is itself an instance of the guard the analysis recommends.

## Confidence ledger (per task)

| Task | Result | Confidence | Grade |
|------|--------|-----------|-------|
| 1 | Three distinct objects (determinism × arity); Q-E1 = two docs iff slope kept | high on distinctness/Q-E1; med on `U`-identity | theorem (distinctness) + reasoned (energy model) |
| 2 | 3-feature axis-aligned decision tree over `(H,c,σ)` | medium | heuristic (directions forced, thresholds empirical) |
| 3 | Chalk-mark = cycle-detect ≠ coverage; false-closes on short seed-cycle; free exact fix | high | theorem-grade |
| 4 | 2P-Set read-view confluent under remove-wins; D1/D2/D3 with disjoint null-spaces | high on semantics + metric structure; med on D3 realizability | theorem (CRDT) + reasoned (metrics) |
| 5 | Reflexive feedback; honest iff pure-projection + role-separation + held-out anchor + external grader | high on shape/C-1; med on sufficiency | reasoned (fixpoint) |
| 6 | Collision-free iff `[R,A]` serializable; fails on TOCTOU (=E2); ID-from-append eliminates race; sequential∧concurrent∧lock-free trilemma | high | theorem-grade |
| 7 | Line = dense learned embedding + ranked similarity; BM25 = grey zone below line | high | reasoned (IR/RAG taxonomy) |

---
`— L2 (Color), offline-math leg, 2026-07-17. Blind: no online sources, no subagents, no sibling legs consulted. Formal analysis only; no product design offered.`
