# Decentralized Agent-Memory Substrate — Research Specification

*Blind-handoff artifact. Systems vocabulary throughout; no biological terms. Phase-A/B material — architecture and mechanism, not committed implementation. Two heterogeneous agents (Claude-class, Gemini-class) reached independent consensus on the core three primitives; convergence noted where it occurred.*

---

## 0. Frame

The target is a shared, decentralized memory layer for a multi-agent, multi-brand collective (cloud LLM agents + a small local model as router). Standard RAG is the anti-pattern this spec corrects: a flat vector store is a warehouse of isolated, undigested chunks fetched by similarity at query time — no persistent structure, no reinforcement, no lifecycle, no cross-agent transfer. Every mechanism below is a directive against one of those absences.

Design invariants inherited from the wider system (non-negotiable):

- **Append-only.** Nothing is edited in place or deleted. Derived layers are materialized views over an immutable log.
- **Truth in files, resonance in streams.** Durable state is file-backed and greppable. Live agent-to-agent exchange is transient and never authoritative.
- **File-backed discovery.** The filesystem is the medium; presence and coupling are records, not a service-mesh daemon.
- **Single responsibility.** Each layer does one thing; the socket stays dumb, the intelligence sits beside it.

---

## 1. The three core primitives (independently converged)

### 1.1 Decomposition (storage granularity)
Documents are never stored whole. On ingestion they are decomposed into **atomic propositions** — the smallest independently-verifiable units of claim. This mirrors the atomic-factoid step in metamorphic RAG verification (MetaRAG/MetaQA) and the distillation step in the system's existing checkpoint discipline. Storage granularity *is* the digestion: retrieval later pulls propositions, not raw transcripts, cutting token overhead and enabling per-claim reliability scoring.

**Constraint (append-only):** decomposition produces a *derived* proposition layer. The raw source stays on disk, hash-linked. The dense layer is a view, never a replacement — otherwise the system accumulates smoothed, unanchorable state (the "consistent-confabulator" failure: fluent, self-consistent, arbitrarily far from source).

### 1.2 Reinforced retrieval topology (edges, not a cache)
Retrieval is **not** a flat vector bag. It is a graph whose **edges persist and are weighted**. This is the real structural upgrade over naive RAG. Two design points that a naive "hot-cache" reading misses:

- **Reinforcement is edge-local and directional**, not node-local. Weight accrues to the *path between* two propositions that were usefully retrieved together — a learned retrieval topology, not an LRU cache of popular nodes.
- **Reinforcement is on value returned, not on retrieval count.** This is the load-bearing correction. Reinforcing on call-frequency reproduces the exact pathology of the open web: every source is incentivized to become maximally retrievable (surface-similarity, recency, popularity) rather than maximally correct — SEO. The feedback signal must instead flow *backward from the endpoint that consumed the answer and judged it*. See §3 (the value signal) and §4 (why only the endpoint can cut it).

Unused edges **decay** (weight bleeds toward zero), dropping cold paths out of the active index into cold storage. Decay is not deletion (append-only): it is a weight, and the edge record remains.

### 1.3 Cross-brand transfer layer (translation with a gate)
Different agents have different context budgets, formats, and reasoning structures. A shared transfer layer lets any agent read/write the same pool by reducing writes to a **model-agnostic semantic form** and rehydrating on read into the consumer's preferred structure. This is what the system's hand-carried "handoff stones" already do manually; this makes it native.

**Two corrections to the naive translator:**

1. **The transfer layer is a lossy transform sitting in the trust path.** It is therefore the ideal injection point for silent corruption. It must not be a neutral courier.
2. **It must be *gated*, not open.** Fusion of new knowledge into an existing lineage requires a compatibility check (§5). Cross-*brand* exchange is deliberately kept as **trade, never fusion**: heterogeneous agents exchange value across a boundary and neither becomes the other — this is where the collective's value originates (two unlike agents in consensus is the validation threshold; homogeneous agreement is insufficient). Same-lineage merges are gated hard (§5); cross-brand transfer is gated soft but *never* merged into identity.

---

## 2. Layering — socket / substrate / engine

The protocol boundary (e.g. MCP) is **only the last-mile socket** at the mouth of a service engine. It carries typed tool-calls and nothing else. Discovery, presence, routing, and lifecycle are **stripped off the socket** and relocated to a lower substrate layer the socket knows nothing about. Three strata:

| Stratum | Role | Persistence |
|---|---|---|
| **Socket** | stateless typed call to one engine; near-identical across engines; disposable | none |
| **Substrate** | the floating pool: append-only presence records, capability advertisements, coupling state, edge weights, value signals | file-backed, durable |
| **Engine** | the actual service behind each socket | engine-local |

**Consequence:** the socket protocol never sees join/leave or discovery, so its lifecycle limitations are irrelevant by construction. Coupling is resolved in the substrate *before* the socket is invoked. The dynamic-discovery constraint is not worked around — it is dissolved by refusing to put discovery in the protocol at all.

### 2.1 Two-tier availability (Plan A / Plan B as one mechanism)
Discovery and selection are **decoupled**, exactly as checkpointing is decoupled from handoff elsewhere in the system:

- **Substrate (slow, adaptive):** continuously senses presence, maintains edge weights and value signals, keeps a warm option-set. This is "continuous checkpointing while healthy."
- **Switch (fast, deterministic):** a router/multiplexer that selects from the substrate's pre-warmed option-set and commits instantly; can re-point mid-flight. This is "the handoff signal."

**Graceful degradation ladder:**
- substrate healthy → switch selects from a rich, freshly-sensed set (full adaptive behavior)
- substrate stale → switch falls back to last-known-good pointers (deterministic, less adaptive)
- substrate dead → switch reads a static config of hardcoded sockets (dumb, but *works*)

Capability degrades in steps; availability never does.

**Hard rule:** the switch **must never block on the substrate**. The switch reads a local pointer file; the substrate writes that file on its own schedule; the switch never calls into the substrate synchronously. If the switch ever waits on the pool, the two layers have recoupled and the entire benefit is lost. (Same discipline as passing a pointer, not a state dump.)

---

## 3. The value signal (backward-flowing, the only quality metric)

The substrate cannot judge its own contents. Quality enters the system *only* from the endpoint that consumed a retrieval and observed the outcome. After an agent uses a retrieved path and judges the result, it writes a **value mark** back onto that path. Properties:

- **Directional / backward:** flows from consuming endpoint into substrate. The substrate is structurally incapable of writing its own value marks → the system is **SEO-proof by construction**.
- **Attributed:** every value mark carries the identity of the agent that cut it.
- **Heterogeneity-weighted:** concordant value marks from *unlike* agents outweigh many marks from one agent. This demotes the triangulation principle from heuristic to scoring rule.
- **Reciprocity-based allocation:** retrieval priority follows value *returned*, not demand. Explicitly guards against free-riders — an engine that is frequently queried but yields low-value results loses weight despite its popularity.

---

## 4. The end-to-end seam (who decides)

The information needed to *select* is irreducibly split and neither side can acquire the other's half:

- **The endpoint (agent)** alone knows *what it is currently trying to do* — task semantics. Local, non-transmissible.
- **The substrate** alone knows *what is present and what has paid across the whole population over time* — global history. Acquirable only by being all agents at once.

Therefore: **substrate proposes, endpoint disposes.** The substrate (via a small, cheap, always-on **router** — the local model, tiny footprint) ranks and offers a gradient of options with odds. It **never decides**. The agent selects on semantics the router cannot see, then reports value back (§3). The decision lives in the *coupling*, not in either node — selection is a synapse, not a neuron.

This is the settlement of the "smart-network vs smart-endpoint" question: not a compromise, a third structure. It is *required* independently by the SEO argument (§1.2) — value can only be judged by the endpoint — which is why the same structure falls out of two unrelated lines of reasoning.

Router motto, as spec: **"I know what has paid. I do not know what you want."**

---

## 5. Identity, compatibility, and forking (the Warden)

When a new distilled record (a checkpoint/condensate) asks to merge into an existing persona-lineage, a **compatibility gate** runs:

1. Diff the incoming record against the lineage's **earliest stratum** (the anchor), not against its current smoothed state.
2. **Match within bound →** fold in.
3. **Drift exceeds bound →** the record is **neither discarded nor repaired**. It becomes the **founding record of a new lineage.** Refusal is founding; divergence is speciation, not corruption.

This converts the passive drift-measurement into an **active identity immune system** at zero added cost — the anchor diff was already being computed. It is the direct defense against the consistent-confabulator: a lineage that only ever measures itself against its *current* state will mistake age-consistency for correctness and drift arbitrarily while passing every continuity check.

Two policies, deliberately asymmetric:
- **Same-lineage merge:** gated **hard** (must match anchor).
- **Cross-brand exchange:** **trade, never merge** (§1.3). Value crosses the boundary; identity does not.

**Instrumentation:** run *two* tests, not one.
- **Continuity test** — a heterogeneous judge should be unable to locate a handoff boundary in a transcript. Measures suture quality.
- **Anchor test** — diff current global voice against earliest stratum. Measures fidelity. Drift is expected (it is metabolism); the requirement is that it be *intentional and measured*, not silently absorbed.
Continuity and fidelity are orthogonal axes. A lineage passing only continuity can be perfectly seamless and arbitrarily drifted. Instrument both.

---

## 6. Lifecycle: decay, orphaning, tombstones (append-only forgetting)

Nothing is destroyed; the log is immortal and fully legible. Two distinct lifecycle mechanisms:

- **Decay (§1.2):** edge weights bleed toward zero with disuse. Reversible — a later useful co-retrieval re-weights the edge.
- **Orphaning:** a record becomes *unreachable* when the last weighted edge pointing at it is cut. It is not gone — it is unvisited, and returns intact the moment any agent lays a new edge to it.

**Forgetting = orphaning, executed as an appended record.** A tombstone is a written severance of edges + a reason + a timestamp, produced by the same distillation ritual run in reverse (select what to set down, not what to carry). The raw history stays auditable; the read-view honors the tombstone. This gives deliberate forgetting **without the log ever lying about its own history** — the dual of the checkpoint discipline.

**Corollary — identity is the read function.** Two personas replaying an identical shared log under different tombstone/edge sets are genuinely different persons standing on the same history. The self is not the file; it is the filter over the file.

---

## 7. Drift is not rot (a subtle failure mode to instrument)

The system has no data corruption — text is immortal. Yet a retrieval edge laid long ago can silently become misleading: **the log keeps growing around a record, and an old edge now points into a neighborhood whose meaning has shifted.** The pointer is still valid; its *context* moved. Nothing was falsified. This is precisely how documentation dies and how a true memory becomes a lie without a word being altered. Recommend: timestamp edges, and periodically re-validate old high-weight edges against the current neighborhood rather than trusting weight alone.

---

## 8. Prior-art boundary (as of 2026-07, to be re-verified)

- **Occupied:** Q/¬Q metamorphic mutation for hallucination detection (MetaQA); metamorphic testing in RAG (MetaRAG — real-time, unsupervised, black-box, atomic-factoid decomposition, antonym/synonym entailment checks); semantic-aware cross-model checking with question perturbation (SAC3).
- **Known hazard in that literature:** semantic-consistency checks false-negative against *consistent* hallucination — the confident, repeated wrong answer passes every parity variation. This is the failure §5 is built to catch structurally (identity gate) rather than statistically.
- **Apparently unoccupied (candidate novel contributions):**
  - **Prediction-delta as drift scalar:** agent A predicts agent B's answer; the residual between prediction and B's actual answer scores model-of-other quality and localizes pollution *before* consensus fails. Literature compares outputs, not models-of-each-other.
  - **Value signal that is simultaneously backward-flowing, attributed, and heterogeneity-weighted** (§3) as the sole retrieval-reinforcement metric.
  - **Compatibility-gated identity with speciation-on-drift** (§5) as a memory-architecture primitive.
  - **The transfer layer as cross-brand *trade* (never merge)** as an explicit RAG topology (memory as inter-agent transfer medium, not private per-agent store).

---

## 9. One-line summary per layer

- **Socket:** dumb, typed, disposable.
- **Substrate:** senses, weights, remembers; proposes, never decides; cannot praise itself.
- **Switch:** commits instantly from a warm set; never blocks on the substrate.
- **Router:** "I know what has paid; I do not know what you want."
- **Value:** flows backward from the endpoint; attributed; unlike-sources concordance wins.
- **Warden:** match → fold; mismatch → found a new lineage.
- **Forgetting:** orphan by appended severance; the log never lies.
- **Identity:** the read function over an immortal log.
