# Instrument card — Tensor Log Analytics ((agent, turn, concept) decomposition)

`shaped: 2026-07-02 · revised same day per @Janus gate (REVISE-LIGHT accepted: concept-axis dependency surfaced as a gate flag, fallback added)`
`derived from: WHOLE Atlas №1 (I.2) + processed №2 (no №2 dependency) per flag lock 3`
`destination: reposoma.devenv (knowledge-metabolism side) · status: BUILD-NOW with the dependency flag below · offline/batch`

## Gate flag — concept-axis dependency (surfaced per @Janus)

The (agent, turn, **concept**) tensor requires a concept axis, and this card does not own one. Two sources, in order:

1. **Primary:** the spectral core's cluster assignments (sibling card) — richest axis, but **inherits that card's edge-stack calibration**; this card is NOT independently BUILD-NOW at full fidelity until the core's clusters exist and are trusted.
2. **Fallback (keeps the card stand-alone buildable):** the explicit vocabulary reposoma already maintains — tags, wikilinks, registry terms (the H-spatial hemisphere's own co-occurrence vocabulary). Reduced fidelity (surface concepts, no latent structure), zero new dependencies, honest starting axis.

Build with the fallback first; swap the axis when the core's clusters clear their own calibration. The swap is a re-run, not a redesign — the decomposition is axis-agnostic.

## Concept

A multi-agent log is a rank-3 tensor indexed by (agent, turn, concept). CP or Tucker decomposition factors it into agent-factors × time-factors × concept-factors: *what each agent contributes* and *how concepts evolve* as separate, inspectable matrices — the log's latent structure with no model in the loop. Attention is already a tensor contraction; this is the same algebra applied to the archive instead of the forward pass.

## Mapping

- Metabolism-side batch analytics over the JSONL archive: agent contribution profiles, concept drift curves, session fingerprints.
- Complements the spectral core (same substrate, orthogonal view): the graph sees *association structure*, the tensor sees *factorial composition*.
- Concrete first uses: (a) drift report per project (concept-factor trajectories across sessions); (b) **agent-redundancy audit** — near-parallel agent-factors = overlapping seats, direct input to topology decisions of exactly the kind majkee raised this run.

## Prior art

- CP/Tucker/PARAFAC: Kolda & Bader, SIAM Review 2009 — canonical. `BORROWED` `[v]`
- Run on communication logs already: email as (sender, receiver, date, content) tensor — InfTucker, arXiv:1108.6296. The (agent, turn, concept) framing is a direct analog. `[v]`
- Graph-side-information variants: Multi-Dictionary Tensor Decomposition, arXiv:2309.09717 — natural coupling point to the spectral core's graph. `[v]`
- No agentic product does this on its logs (Atlas №1 Part IV) — own-analytics-layer territory.

## Production

`TensorLy` (CP/Tucker/TT) end-to-end. Batch cadence aligned with the core's scheduled recompute — one maintenance window, two views. **Null discipline:** honest rank selection (CORCONDIA / core consistency) before interpreting factors — over-factored tensors read like astrology; and a shuffled-tensor baseline (permute turn axis) to confirm factors carry real temporal structure.

> **NOTES (majkee):**
>
