# Decentralized Agent-Memory Substrate — Research Specification v2

*Blind-handoff artifact. Systems vocabulary throughout; no biological terms. Phase-A/B material — architecture and mechanism, not committed implementation.*

*Provenance flags:*
- *[CORE] — original v1 material; two heterogeneous agents (Claude-class, Gemini-class) reached independent consensus on the three primitives.*
- *[v2] — added in second pass by a Claude-class agent (Nabla thread); single-agent origin, **not yet triangulated**. Treat as candidate material until a heterogeneous second opinion lands.*
- *[CORE+v2] — original mechanism with a v2 correction folded in.*

---

## 0. Frame [CORE]

The target is a shared, decentralized memory layer for a multi-agent, multi-brand collective (cloud LLM agents + a small local model as router). Standard RAG is the anti-pattern this spec corrects: a flat vector store is a warehouse of isolated, undigested chunks fetched by similarity at query time — no persistent structure, no reinforcement, no lifecycle, no cross-agent transfer. Every mechanism below is a directive against one of those absences.

Design invariants inherited from the wider system (non-negotiable):

- **Append-only.** Nothing is edited in place or deleted. Derived layers are materialized views over an immutable log.
- **Truth in files, resonance in streams.** Durable state is file-backed and greppable. Live agent-to-agent exchange is transient and never authoritative.
- **File-backed discovery.** The filesystem is the medium; presence and coupling are records, not a service-mesh daemon.
- **Single responsibility.** Each layer does one thing; the socket stays dumb, the intelligence sits beside it.

All v2 additions were checked against these invariants: none requires in-place editing, none blocks the switch, none merges identities.

---

## 1. The three core primitives

### 1.1 Decomposition (storage granularity) [CORE]

Documents are never stored whole. On ingestion they are decomposed into **atomic propositions** — the smallest independently-verifiable units of claim. This mirrors the atomic-factoid step in metamorphic RAG verification (MetaRAG/MetaQA) and the distillation step in the system's existing checkpoint discipline. Storage granularity *is* the digestion: retrieval later pulls propositions, not raw transcripts, cutting token overhead and enabling per-claim reliability scoring.

**Constraint (append-only):** decomposition produces a *derived* proposition layer. The raw source stays on disk, hash-linked. The dense layer is a view, never a replacement — otherwise the system accumulates smoothed, unanchorable state (the "consistent-confabulator" failure: fluent, self-consistent, arbitrarily far from source).

#### 1.1a Ingestion metadata [v2]

Each proposition is stamped at ingestion with two cheap fields that later layers depend on:

- **Generation integer** (see §1.4): 0 if hash-linked to raw external source; N+1 if derived from a generation-N record.
- **Volatility class** (see §6.1): `timeless | stable | volatile`. Same taxonomy as the freshness-anchor discipline: architecture patterns are timeless; API pricing is volatile. Class drives decay rate and value-mark regime checks.

Both are append-time stamps on the derived layer; the raw source is untouched.

### 1.2 Reinforced retrieval topology (edges, not a cache) [CORE+v2]

Retrieval is **not** a flat vector bag. It is a graph whose **edges persist and are weighted**. This is the real structural upgrade over naive RAG. Two design points that a naive "hot-cache" reading misses:

- **Reinforcement is edge-local and directional**, not node-local. Weight accrues to the *path between* two propositions that were usefully retrieved together — a learned retrieval topology, not an LRU cache of popular nodes.
- **Reinforcement is on value returned, not on retrieval count.** This is the load-bearing correction. Reinforcing on call-frequency reproduces the exact pathology of the open web: every source is incentivized to become maximally retrievable rather than maximally correct — SEO. The feedback signal must flow *backward from the endpoint that consumed the answer and judged it*. See §3 and §4.

Unused edges **decay** (weight bleeds toward zero), dropping cold paths out of the active index into cold storage. Decay is not deletion (append-only): it is a weight, and the edge record remains.

#### 1.2a Typed edges [v2]

v1 edges were untyped co-retrieval weights. Three types earn their storage cost immediately:

| Type | Semantics | Payoff |
|---|---|---|
| **supports** | default co-retrieval association | unchanged from v1; cheap |
| **contradicts** | P and ¬P are linked | retrieval of P surfaces ¬P for free — the substrate becomes a passive consistency checker at zero inference cost |
| **supersedes** | new record replaces old for current-state queries | the append-only answer to volatile facts: a new API-version proposition never touches the old record; it lays a supersedes edge and the read-view walks the chain to the head |

The **supersedes** type partially dissolves the §7 context-drift hazard: an old edge into a shifted neighborhood is no longer *silently* misleading, because the neighborhood's supersession chain is explicit and walkable.

### 1.3 Cross-brand transfer layer (translation with a gate) [CORE]

Different agents have different context budgets, formats, and reasoning structures. A shared transfer layer lets any agent read/write the same pool by reducing writes to a **model-agnostic semantic form** and rehydrating on read into the consumer's preferred structure. This is what the system's hand-carried "handoff stones" already do manually; this makes it native.

**Two corrections to the naive translator:**

1. **The transfer layer is a lossy transform sitting in the trust path.** It is therefore the ideal injection point for silent corruption. It must not be a neutral courier.
2. **It must be *gated*, not open.** Fusion of new knowledge into an existing lineage requires a compatibility check (§5). Cross-*brand* exchange is deliberately kept as **trade, never fusion**: heterogeneous agents exchange value across a boundary and neither becomes the other — this is where the collective's value originates (two unlike agents in consensus is the validation threshold; homogeneous agreement is insufficient). Same-lineage merges are gated hard (§5); cross-brand transfer is gated soft but *never* merged into identity.

### 1.4 The autophagy guard (provenance generation) [v2]

v1 guards against drift of context (§7) but not against **self-referential ingestion**. The moment agent outputs — distillates, condensates, answers — re-enter the pool as source material, the log starts feeding on itself: propositions derived from propositions derived from propositions. This is citogenesis / model-collapse-in-miniature — the Wikipedia-cites-journalist-cites-Wikipedia loop, run at memory-substrate speed.

Mechanism (free under append-only, since the derivation chain is already in the log):

- Every proposition carries the **generation integer** from §1.1a.
- The read-view never forgets derivation depth.
- The anchor test (§5) gets a **generational analog**: high-weight paths dominated by gen≥2 propositions are flagged for **re-grounding** — re-validation against their gen-0 ancestry.
- Re-grounding is itself an appended record (a fresh gen-1 derivation from the gen-0 source), never a repair-in-place.

Rule of thumb: **weight may compound; generation may not.** A path can become arbitrarily hot, but its evidential floor is always its shallowest generation.

---

## 2. Layering — socket / substrate / engine [CORE]

The protocol boundary (e.g. MCP) is **only the last-mile socket** at the mouth of a service engine. It carries typed tool-calls and nothing else. Discovery, presence, routing, and lifecycle are **stripped off the socket** and relocated to a lower substrate layer the socket knows nothing about. Three strata:

| Stratum | Role | Persistence |
|---|---|---|
| **Socket** | stateless typed call to one engine; near-identical across engines; disposable | none |
| **Substrate** | the floating pool: append-only presence records, capability advertisements, coupling state, edge weights, value signals | file-backed, durable |
| **Engine** | the actual service behind each socket | engine-local |

**Consequence:** the socket protocol never sees join/leave or discovery, so its lifecycle limitations are irrelevant by construction. Coupling is resolved in the substrate *before* the socket is invoked. The dynamic-discovery constraint is not worked around — it is dissolved by refusing to put discovery in the protocol at all.

### 2.1 Two-tier availability (Plan A / Plan B as one mechanism) [CORE]

Discovery and selection are **decoupled**, exactly as checkpointing is decoupled from handoff elsewhere in the system:

- **Substrate (slow, adaptive):** continuously senses presence, maintains edge weights and value signals, keeps a warm option-set. "Continuous checkpointing while healthy."
- **Switch (fast, deterministic):** a router/multiplexer that selects from the substrate's pre-warmed option-set and commits instantly; can re-point mid-flight. "The handoff signal."

**Graceful degradation ladder:**
- substrate healthy → switch selects from a rich, freshly-sensed set (full adaptive behavior)
- substrate stale → switch falls back to last-known-good pointers (deterministic, less adaptive)
- substrate dead → switch reads a static config of hardcoded sockets (dumb, but *works*)

Capability degrades in steps; availability never does.

**Hard rule:** the switch **must never block on the substrate**. The switch reads a local pointer file; the substrate writes that file on its own schedule; the switch never calls into the substrate synchronously. If the switch ever waits on the pool, the two layers have recoupled and the entire benefit is lost. (Same discipline as passing a pointer, not a state dump.)

---

## 3. The value signal (backward-flowing, the only quality metric) [CORE+v2]

The substrate cannot judge its own contents. Quality enters the system *only* from the endpoint that consumed a retrieval and observed the outcome. After an agent uses a retrieved path and judges the result, it writes a **value mark** back onto that path. Properties:

- **Directional / backward:** flows from consuming endpoint into substrate. The substrate is structurally incapable of writing its own value marks → the system is **SEO-proof by construction**. [CORE]
- **Attributed:** every value mark carries the identity of the agent that cut it. [CORE]
- **Heterogeneity-weighted:** concordant value marks from *unlike* agents outweigh many marks from one agent. This demotes the triangulation principle from heuristic to scoring rule. [CORE]
- **Reciprocity-based allocation:** retrieval priority follows value *returned*, not demand. Explicitly guards against free-riders — an engine that is frequently queried but yields low-value results loses weight despite its popularity. [CORE]

### 3.1 Credit assignment — citation discipline [v2]

v1 specified the *direction* of the value signal but not its *granularity*, and this is a hole. A real retrieval delivers 8–15 propositions into context; the endpoint judges the **outcome**, not the atoms. If the endpoint marks the whole retrieved path on success, free-rider propositions hitchhike on good retrievals — a milder, in-context reincarnation of the SEO pathology §1.2 was built to kill. Backward-flowing but *smeared*.

Fix: the endpoint's answer format carries a **citation discipline** — it marks only the propositions it actually consumed in producing the judged output.

> **value mark = cited ∩ succeeded**, not retrieved ∩ succeeded.

This is the RL credit-assignment problem solved by making the endpoint self-report attribution — which an LLM endpoint can do essentially for free, because citation is a native operation for it. Without §3.1, §3 degrades quietly and the SEO-proofing claim is overstated.

### 3.2 Regime-stamped marks [v2]

The value mark also stamps the **regime** it was judged under (which model versions, which external-API versions, which volatility-relevant world state applied at judgment time). A mark cut against a deprecated API version is not evidence — it is fossil evidence. Heterogeneity-weighting must **discount cross-regime concordance**: two unlike agents agreeing in an obsolete regime is not the same signal as two unlike agents agreeing now.

### 3.3 Mark integrity [v2 — noted, not solved]

Attribution (§3) assumes writers honestly identify themselves. A file-backed substrate needs a **signature or hash discipline on value marks**, or heterogeneity-weighting is spoofable by one agent wearing two hats. Small hole; free to close at design time, expensive after. Flagged for Phase-B resolution — candidate mechanisms: per-agent keypair signing of marks, or an append-side gate that binds marks to authenticated writer sessions.

---

## 4. The end-to-end seam (who decides) [CORE+v2]

The information needed to *select* is irreducibly split and neither side can acquire the other's half:

- **The endpoint (agent)** alone knows *what it is currently trying to do* — task semantics. Local, non-transmissible.
- **The substrate** alone knows *what is present and what has paid across the whole population over time* — global history. Acquirable only by being all agents at once.

Therefore: **substrate proposes, endpoint disposes.** The substrate (via a small, cheap, always-on **router** — the local model, tiny footprint) ranks and offers a gradient of options with odds. It **never decides**. The agent selects on semantics the router cannot see, then reports value back (§3). The decision lives in the *coupling*, not in either node — selection is a synapse, not a neuron.

This is the settlement of the "smart-network vs smart-endpoint" question: not a compromise, a third structure. It is *required* independently by the SEO argument (§1.2) — value can only be judged by the endpoint — which is why the same structure falls out of two unrelated lines of reasoning.

### 4.1 Exploration budget [v2]

Pure value-reinforcement is **preferential attachment**. Rich edges get richer, the router offers what has paid, endpoints mark what was offered — a closed loop, and the substrate becomes its own filter bubble. Worse, there is a **structural cold-start deadlock**: a correct new proposition has zero edges and zero marks; under §3 as written it can never be retrieved, therefore never earn its first mark.

Fix: the router reserves a fixed **epsilon fraction of every offer-set** for unweighted, low-weight, or low-generation candidates (semantic-similarity or recency selected, since no value history exists yet). This is not a heuristic bolt-on — without it the system provably converges to a frozen topology and stops learning.

Epsilon is a substrate-level constant, tunable, logged. Exploratory offers are flagged as such in the gradient so the endpoint knows it is being shown an untried path, and marks cut on exploratory offers are the highest-information marks in the system (first evidence on virgin territory).

Router motto, v2 form:

> **"I know what has paid. I do not know what you want. And I deliberately show you things that have never been tried."**

---

## 5. Identity, compatibility, and forking (the Warden) [CORE+v2]

When a new distilled record (a checkpoint/condensate) asks to merge into an existing persona-lineage, a **compatibility gate** runs:

1. Diff the incoming record against the lineage's **earliest stratum** (the anchor), not against its current smoothed state.
2. **Match within bound →** fold in.
3. **Drift exceeds bound →** the record is **neither discarded nor repaired**. It becomes the **founding record of a new lineage.** Refusal is founding; divergence is speciation, not corruption.

This converts the passive drift-measurement into an **active identity immune system** at zero added cost — the anchor diff was already being computed. It is the direct defense against the consistent-confabulator: a lineage that only ever measures itself against its *current* state will mistake age-consistency for correctness and drift arbitrarily while passing every continuity check.

Two policies, deliberately asymmetric:
- **Same-lineage merge:** gated **hard** (must match anchor).
- **Cross-brand exchange:** **trade, never merge** (§1.3). Value crosses the boundary; identity does not.

**Instrumentation — three tests, not one:** [CORE, extended v2]
- **Continuity test** [CORE] — a heterogeneous judge should be unable to locate a handoff boundary in a transcript. Measures suture quality.
- **Anchor test** [CORE] — diff current global voice against earliest stratum. Measures fidelity. Drift is expected (it is metabolism); the requirement is that it be *intentional and measured*, not silently absorbed.
- **Generation test** [v2, from §1.4] — audit the generation distribution of the lineage's high-weight paths. Measures evidential grounding. A lineage can pass continuity and anchor while quietly floating on gen≥2 self-derivations; this test catches the third failure axis.

Continuity, fidelity, and grounding are orthogonal axes. Instrument all three.

---

## 6. Lifecycle: decay, orphaning, repulsion edges, tombstones (append-only forgetting) [CORE+v2]

Nothing is destroyed; the log is immortal and fully legible. Lifecycle mechanisms, now four:

- **Decay [CORE]:** edge weights bleed toward zero with disuse. Reversible — a later useful co-retrieval re-weights the edge.
- **Orphaning [CORE]:** a record becomes *unreachable* when the last weighted edge pointing at it is cut. Not gone — unvisited, and returns intact the moment any agent lays a new edge to it.
- **Repulsion edges [v2]:** see §6.2.
- **Tombstones [CORE]:** **forgetting = orphaning, executed as an appended record.** A tombstone is a written severance of edges + a reason + a timestamp, produced by the same distillation ritual run in reverse (select what to set down, not what to carry). The raw history stays auditable; the read-view honors the tombstone. Deliberate forgetting **without the log ever lying about its own history** — the dual of the checkpoint discipline.

**Corollary — identity is the read function.** [CORE] Two personas replaying an identical shared log under different tombstone/edge/repulsion-edge sets are genuinely different persons standing on the same history. The self is not the file; it is the filter over the file.

### 6.1 Two-speed decay keyed to volatility class [v2]

One decay constant for the whole graph is wrong physics. "Pipes compose" and "endpoint v3 pricing" are different substances: one is timeless, one has a half-life of weeks. Decay rate follows the volatility class stamped at ingestion (§1.1a):

| Class | Decay behavior |
|---|---|
| **timeless** | near-zero decay; weight persists on architecture patterns, math, invariants |
| **stable** | slow decay; institutional facts, long-lived interfaces |
| **volatile** | fast decay; versioned facts, pricing, "latest" anything — and preferred targets for **supersedes** edges (§1.2a) |

This couples with §3.2: fast-decaying classes are exactly where regime-stamped marks matter most.

### 6.2 Repulsion edges — negative knowledge as first-class [v2]

*(Naming note: this object was renamed from the earlier "scar" — unrelated to the harness term* scar *used elsewhere, which denotes a de-specified lesson record, raw.incarnations.)*

v1 has two terminal lifecycle states — hot (weighted) and orphaned (unreachable) — and both are forms of *forgetting*. But "we tried X and it failed" is the most expensive knowledge to reacquire, and orphaning a dead end guarantees a fresh agent rediscovers it at full cost.

A **repulsion edge** is an appended proposition-plus-edge with deliberately **negative weight** — it actively repels routing rather than merely being unvisited. It carries the failure reason and timestamp, exactly like a tombstone, but with opposite read-view semantics:

> **Tombstone:** "set this down." (neutral severance)
> **Repulsion edge:** "this path is wrong — here is why and when." (active repulsion)

The distinction in one line: **decay = forgot; repulsion edge = remembered-as-wrong.**

Router obligation: the offer gradient **surfaces repulsion edges adjacent to any path it proposes** — the cheapest possible "don't step there" signal, delivered at exactly the moment an endpoint is about to consider the neighborhood.

Repulsion edges are regime-stamped (§3.2) and volatility-classed (§6.1): a repulsion edge cut against a deprecated API version can legitimately fade as the regime that produced it dies. A repulsion edge on a timeless claim does not fade.

---

## 7. Drift is not rot (a subtle failure mode to instrument) [CORE+v2]

The system has no data corruption — text is immortal. Yet a retrieval edge laid long ago can silently become misleading: **the log keeps growing around a record, and an old edge now points into a neighborhood whose meaning has shifted.** The pointer is still valid; its *context* moved. Nothing was falsified. This is precisely how documentation dies and how a true memory becomes a lie without a word being altered.

Mitigations, v2 consolidated:
- Timestamp edges; periodically re-validate old high-weight edges against the current neighborhood rather than trusting weight alone. [CORE]
- **Supersedes** edges (§1.2a) make the most common form of neighborhood shift — versioned replacement — explicit and walkable, removing it from the silent category. [v2]
- Volatility-classed decay (§6.1) ensures the edges most likely to rot are also the edges that fade fastest without re-confirmation. [v2]

Residual hazard after v2: neighborhood shift on *timeless-classed* propositions (rare, but a misclassification at ingestion would hide there). Periodic re-validation remains the only guard; no structural fix claimed.

---

## 8. Prior-art boundary (as of 2026-07, to be re-verified)

- **Occupied [CORE]:** Q/¬Q metamorphic mutation for hallucination detection (MetaQA); metamorphic testing in RAG (MetaRAG — real-time, unsupervised, black-box, atomic-factoid decomposition, antonym/synonym entailment checks); semantic-aware cross-model checking with question perturbation (SAC3).
- **Adjacent-occupied [v2, to be swept before novelty claims]:** generation-tagging resembles the model-collapse / synthetic-data-contamination literature (data provenance tracking); exploration epsilon is standard multi-armed-bandit machinery (ε-greedy); negative-weight repulsion resembles negative caching in DNS/systems. The *combination* inside an append-only, cross-brand memory substrate appears unoccupied, but each ingredient individually has prior art — cite it, don't claim it.
- **Known hazard in the metamorphic literature [CORE]:** semantic-consistency checks false-negative against *consistent* hallucination — the confident, repeated wrong answer passes every parity variation. §5 catches this structurally (identity gate) rather than statistically.
- **Candidate novel contributions, v2 list:**
  - **Prediction-delta as drift scalar** [CORE]: agent A predicts agent B's answer; the residual scores model-of-other quality and localizes pollution *before* consensus fails. Literature compares outputs, not models-of-each-other.
  - **Value signal simultaneously backward-flowing, attributed, heterogeneity-weighted** (§3) as the sole retrieval-reinforcement metric. [CORE]
  - **Citation-granular credit assignment as the value mark's unit** (§3.1) — cited ∩ succeeded. [v2]
  - **Compatibility-gated identity with speciation-on-drift** (§5) as a memory-architecture primitive. [CORE]
  - **Transfer layer as cross-brand *trade* (never merge)** as an explicit RAG topology. [CORE]
  - **Repulsion edge as the dual of the tombstone** — negative knowledge with active routing repulsion inside an append-only log (§6.2). [v2]
  - **Generation integer + generation test as an anti-autophagy primitive** for agent memory (§1.4, §5). [v2]

---

## 9. One-line summary per layer

- **Socket:** dumb, typed, disposable. [CORE]
- **Substrate:** senses, weights, remembers; proposes, never decides; cannot praise itself. [CORE]
- **Switch:** commits instantly from a warm set; never blocks on the substrate. [CORE]
- **Router:** "I know what has paid; I do not know what you want; and I deliberately show you things that have never been tried." [CORE+v2]
- **Value:** flows backward from the endpoint; cited ∩ succeeded; attributed and regime-stamped; unlike-sources concordance wins, same-regime concordance wins harder. [CORE+v2]
- **Warden:** match → fold; mismatch → found a new lineage; and audit the generation floor, not just the voice. [CORE+v2]
- **Edges:** typed — supports, contradicts, supersedes; weight may compound, generation may not. [v2]
- **Forgetting:** orphan by appended severance; lay a repulsion edge on what must never be re-walked; the log never lies. [CORE+v2]
- **Exploration:** a fixed epsilon of every offer is virgin territory, or the topology freezes. [v2]
- **Identity:** the read function over an immortal log. [CORE]

---

## 10. Open items for Phase B

1. Mark-integrity mechanism (§3.3) — signing vs. authenticated append gate. Unresolved.
2. Epsilon value and selection heuristic for exploratory offers (§4.1) — needs empirical tuning; start dumb (uniform random over gen-0/low-weight), measure.
3. Volatility misclassification at ingestion (§7 residual) — who classifies, and is reclassification an appended record? (It must be.)
4. Prior-art sweep for the v2 additions (§8 adjacent-occupied list) before any novelty claim is externalized.
5. **Triangulation of all [v2] material** — single-agent origin; per the system's own validation threshold, none of it is confirmed until a heterogeneous agent independently concurs or productively objects.
