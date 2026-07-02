# Instrument card — Choquet Consensus Gate ("which 3 of 5")

`shaped: 2026-07-02 · revised same day per @Janus gate (REVISE-HARD accepted in full: "zero theory gaps" retracted; null-model gate + data-source added)`
`derived from: WHOLE Atlas №1 (I.8, Spine III) + processed №2 (cross-measure C2, B7) per flag lock 3`
`destination: subai.devenv (bus side)`
`status: BUILD-NOW (implementation is small) · ADOPTION-GATED — the null-model gate below must pass before this replaces a plain quorum; if it cannot be run or does not pass, the card parks as OPERATIONALIZE`

## Concept

"Pass when ≥3 of 5, but *which* 3 matters, and 2-of-5 ≠ 1-of-5" is not fuzzy logic (pointwise) — the exact object is a **fuzzy measure (capacity) μ aggregated by the Choquet integral**: μ assigns weight to every *subset*, so `μ({1,3}) ≠ μ({1})+μ({3})` — synergy and redundancy encoded directly. **Which voters matter:** Shapley or Banzhaf values over μ — equal values = identity-blind gate; unequal = identity is load-bearing, quantified. Engineering form: full capacity has `2^N−2` parameters; the **2-additive Möbius restriction** (pairwise synergies only) is the tractable compromise at bus N≤7 (21 parameters at N=5... 6; small either way).

**Theory gap, stated (retraction of the earlier label):** the *mathematics* of Choquet aggregation is settled; whether a non-additive capacity **adds decision value over a weighted quorum on this bus's real verdicts** is an open empirical question, and until μ is learned from data, a hand-set capacity is structured weighted voting — honest name attached.

## Null-model gate (mandatory before adoption — @Janus condition, accepted)

- **Baseline:** a plain weighted-quorum / linear-threshold rule (three lines of code).
- **Test:** pre-registered set of real bus decisions with known outcomes; the Choquet gate must **out-predict the quorum** on held-out cases. Pre-register task, metric, and split before looking.
- **Ruling:** beats quorum → adopt, `BUILD-NOW` stands. Ties or cannot be run for lack of data → park `OPERATIONALIZE`, keep the quorum, keep logging.

**Where the labels come from (the scarce resource, named):** resolved bus decisions — gated verdicts later validated or reverted in session journals, flag ledgers, and post-mortems. This corpus is small and grows slowly; that is precisely why the card starts with a hand-set μ (expert priors, e.g. "two independent legs converging outweigh three correlated ones") in **log-and-learn** mode: every gate decision logs votes + eventual outcome, building the training set the learned capacity needs. No labels, no learned μ — the card does not pretend otherwise.

## Mapping

The consensus gate on bus verdicts: agent votes/confidences in → gated decision + identity-loading (Shapley) readout + audit line (which coalition carried it) out. Second mapping, proven in-house this run: the lab's blind fan-out cross-measure *is* this gate executed manually — heterogeneous legs, subset-dependent trust. The card mechanizes existing temple practice.

**Caveat carried from №2 processing (cross-measure C2):** Dempster–Shafer fusion attaches only in its **Bayesian face**. A general DS mass lives on the simplex over `2^Θ∖∅`; the √p/Fisher–Rao bridge does not transport Dempster's rule or the subset lattice. Do not sell DS+geometry as one object.

## Prior art

- Choquet-integral classifier fusion: Grabisch 1996 and decades of fusion literature. `BORROWED` `[v]`
- LLM application exists: fuzzy Choquet over a non-additive measure for conflicting LLM evidence (arXiv:2506.05675). `[v]`
- Dempster–Shafer decision fusion: established; Bayesian-face restriction per this run. `[v]`

`BORROWED` · exact fit to the phrasing — and exact-fit is a seduction risk (theatre gate), which is what the null-model gate above is for.

## Production

Bespoke capacity code is small; `scikit-fuzzy` partial. Ship: gate function + Shapley readout + audit log + the quorum baseline *in the same module* (the null model is a deliverable, not a footnote). Capacity learning starts only when the log-and-learn corpus exists.

## Upgrade path (pending gate-1 gavel — not a dependency)

№2 Fork 3's Fisher–Rao Bayesian face (B7): vote distributions on the radius-2 sphere orthant (`p↦2√p`, curvature ¼), opposition as arc distance — only if its own pre-registered head-to-head vs cosine/KL shows a win. The gate works fully without it.

> **NOTES (majkee):**
>
