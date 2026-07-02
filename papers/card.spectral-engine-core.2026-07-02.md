# Instrument card — Spectral Engine Core (dual-face)

`shaped: 2026-07-02 · revised same day per @Janus gate (REVISE-LIGHT: edge rule named) + P4 mount findings (sibling fence honored)`
`derived from: WHOLE Atlas №1 (esp. Part II, I.1) + processed №2 (cross-measure.2026-07-02) per flag lock 3`
`destinations: subai.devenv (Face A, diagnostics) + reposoma.devenv (Face B, retrieval core) — ownership split per lock 4, boundary per the sibling fence (Hypatia 2026-06-24)`
`status: BUILD-NOW (core) · OPERATIONALIZE (crossover scale, cross-vendor face) · delivery per lock 5`

## Concept

Truth lives in files: agent outputs are normalized JSONL lines, one per turn — **the line is canonical**; vectors are a derived coordinate, not the source of truth; **the association graph over the lines is the brain** (the substrate inversion, II.1 — `YOURS`). Retrieval is field dynamics realized: seed activation on query-matched nodes, spread by the heat kernel `exp(−tL)` — two units are close when many short associative paths connect them (diffusion distance, Coifman–Lafon 2006). Spectral clustering (Fiedler + first k eigenvectors) retrieves *coherent connected neighborhoods*, curing top-k cosine's mutual-incoherence failure. Laplacian eigenmap gives connectivity-derived coordinates; low-rank sparsification denoises spurious edges and reports intrinsic dimensionality.

**Hybrid boundary (honest):** pure-associative does not beat good embeddings on single-hop; it wins on multi-hop and coherence. Vectors demoted to cheap first-hop candidate generation; diffusion does expansion (II.6). Note: reposoma's charter takes a *stronger* stance (dense-embedding search "optional and downstream, never the substrate") — at small corpus scale the stronger stance holds; the hybrid is the scale hedge, not a disagreement.

**Append-only reconciliation (II.7):** eigendecomposition is O(n³) and non-incremental — two paths. *Runtime (append-safe):* per-query diffusion via Chebyshev polynomial filters / Lanczos bottom-k, no global precompute. *Batch (scheduled):* global embedding/clustering on a cadence, tolerating staleness. Do not build the runtime path before the corpus size demands it — dense `eigh` at current sibling scales is correct.

## Edge rule (named — this was the card's silent step, flagged by @Janus)

The graph is a **layered edge stack**; each layer is separately weighted, logged, and density-measured at calibration:

- **L0 — structural (always present, ground truth):** same-session turn adjacency (t→t+1), explicit reply/quote edges, citation/wikilink edges. Sparse, cheap, honest. The ρ monitor's cascade graph is exactly this layer.
- **L1 — co-occurrence:** shared anchors/tags/registry terms/salient entities. This is the shape reposoma's H-spatial hemisphere already implements (wikilinks/tags/registry co-occurrence) — the layer exists in production form there.
- **L2 — embedding-kNN (enrichment only, weighted lowest):** single embedder per graph (see gap 1); adds recall the structural layers miss.

**Circularity, acknowledged rather than hidden:** if L2 contributes edges, vectors participate in graph *construction*. The demotion claim is about retrieval *semantics* — ranking, expansion, and coherence are graph-native operations — not about vector absence. A graph built from L0+L1 alone is fully functional at reduced recall; L2 is optional enrichment. **First build measurement: edge density and component count per layer** — if L0+L1 is "too sparse to cluster," that is a *finding, not a failure* (it matches reposoma's own P2 gate philosophy).

## Face A — subai.devenv: diagnostics face (re-aimed per the sibling fence)

The fence (Hypatia, 2026-06-24, subai canon): *"knowledge-corpus RAG is reposoma's sovereign role — subai's L2 spectral stays scoped to live-medium lane telemetry. Two engines, two graphs, no overlap."* subai already rents knowledge recall from reposoma over MCP (`recall_lighthouse`). This card **honors the fence**: Face A supplies no retrieval.

- subai's locked brick (spectral-engine.decision.2026-06-17: out-of-process MCP numerics brick, **scalar spectrum returns only**, dependency firewall, read-triggered debounced cadence) is the correct mounting flange — this card *extends its read menu*, it does not compete: first reads already live (k = component count, λ₂ = Fiedler fragility on the lane graph); candidate next reads from Atlas №1: signal-view drift/loop spectrum (I.1), spectral radius ρ_op of the excitation kernel (feeds the ρ monitor card), the aggregated health scalar (Part III).
- Their build lessons transfer downstream and are adopted here as card doctrine: stdout tripwire (numerics warnings corrupt stdio JSON-RPC — route to stderr), structured `ArpackNoConvergence` errors, shift-invert with small positive σ, largest-connected-component discipline.

## Face B — reposoma.devenv: retrieval core (the sovereign RAG face)

- The charter's pillar 1 **is** this card's batch path, independently derived: `B → D → L_sym = I − D^(−½)BD^(−½) → eigsh → (λ,U) → KMeans → clusters + centrality`, with "truth-lives-in-files" as standing LAW — the substrate inversion is their law and our card, convergent. The card adds what the charter defers: diffusion retrieval as the *query-time* mechanism (heat kernel over the same L_sym), the append-only reconciliation for scale, sparsification as denoise + intrinsic-dimension readout, and the honest hybrid boundary for when the corpus outgrows structural recall.
- Episode→fact provenance (Zep/Graphiti pattern) maps onto their registry/trace spine as-is.

## Prior art

| Element | Nearest | Relation | Tag |
|---|---|---|---|
| Diffusion/PPR recall | HippoRAG 1/2 (arXiv:2405.14831, 2502.14802) | same mechanism family; they do doc-QA, this does agent-log metabolism | `BORROWED`/`YOURS` `[v]` |
| Graph-RAG heavy | GraphRAG, LightRAG, PathRAG | mature, heavier ingestion than lean target | `[v]` |
| Episode provenance | Zep/Graphiti (arXiv:2501.13956) | closest to truth-in-files discipline; OSS | `[v]` |
| Line-as-node | SGMem (2025); A-MEM (2025) | JSONL-line granularity lineage | `[t]` |
| Diffusion distance | Coifman–Lafon 2006 | the math under the core | `[v]` |
| Eigenmaps | Belkin–Niyogi 2003, Neural Comp. 15(6) | **upgraded `[t]`→`[v]` this run** | `[v]` |
| Sparsification | Spielman–Teng lineage (arXiv:0808.4134 → Batson–Spielman–Srivastava) | **upgraded `[t]`→`[v]` this run** | `[v]` |

`BORROWED` (mechanism) / `YOURS` (file-canonical inversion + agent-log application + append-only reconciliation + layered edge stack as named doctrine).

## Production

`scipy` (dense `eigh` now; `sparse.linalg`/Lanczos at scale), `networkx`, `scikit-learn`; Chebyshev filter ≈ ChebNet trick when runtime path is earned. Honest testing: LongMemEval, LOCOMO, BEAM — plus the sibling projects' own no-LLM golden fixtures (reposoma Batch B) as the correctness oracle. No product exposes the spectrum as a feature — the gap remains real and ours.

## Explicit gaps and flags

1. **Cross-vendor face is NOT buildable-as-assumed.** vec2vec (arXiv:2505.12540) gives >0.9 *retrieval* fidelity unpaired, but global **directional** alignment is unsolved (arXiv:2602.14486, Feb 2026). One embedder per graph is the design rule; cross-vendor comparison is research item B9, not a feature.
2. **Crossover scale unmeasured** (II.7): measure before promising latency; do not pre-build the runtime path.
3. **Edge-stack calibration is the first build decision** (per @Janus): weights and density thresholds per layer are unset until measured on a real corpus.
4. **Lock-4 "shared spectral anchor" — reality delta, majkee's gavel pending:** project-side reality is "two engines, two graphs" + MCP rental, not one shared engine. Recommended reading: the shared anchor is the shared *mathematical toolkit* (this card + fixtures + build doctrine), mounted twice.

## Upgrade path (pending gate-1 gavel — not commitments)

- Stance-geometry diagnostics at a second scale (№2 Fork 2; Kuramoto-on-sphere law, Automatica 2024) over the *agent-stance configuration*, distinct from the content graph.
- Heterogeneous-frame consistency via the O(d)-synchronization sheaf program (B8): math BORROWED (Singer–Wu × Hansen–Ghrist), application OPEN.

> **NOTES (majkee):**
>
