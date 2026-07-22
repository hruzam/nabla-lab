# @Epoch Research Report — Leg L1

**Leg ID:** L1 (online-depth, blind fan-out, Track 1)
**Model:** claude-sonnet-4-6
**Run date:** 2026-07-17
**Calibration note:** Training cutoff August 2025. All version strings, paper IDs, and claim dates below were live-verified via web search on 2026-07-17. Claims marked [TRAIN] could not be confirmed against a live source this run.

---

## Q1 — File-Native Agent Memory (plain files + grep, no vector DB)

### Prior art and known systems

**memweave** (open-source Python library, active as of 2026-07-17)
- Stores agent memory as plain Markdown files, indexed by SQLite FTS5 (BM25) + sqlite-vec (cosine)
- Hybrid retrieval: `merged_score = 0.7 × vector_score + 0.3 × bm25_score`; 0.35 minimum threshold
- Benchmark on their own test set: 89% recall (hybrid) vs 76% (vector-only) vs 68% (BM25-only)
- No server, no Docker; entire store is a single SQLite file alongside Markdown
- Source: [Towards Data Science / memweave](https://towardsdatascience.com/memweave-zero-infra-ai-agent-memory-with-markdown-and-sqlite-no-vector-database-required/) · [GitHub](https://github.com/sachinsharma9780/memweave) | Confidence: H

**Practitioner consensus (DEV community, 2025–2026)**
- Multiple practitioner reports of replacing vector DBs with grep/ripgrep for agent memory under ~1,000 documents
- Rationale: "At under 1,000 documents, BM25 keyword matching finds the right document over 90% of the time because when you write memory, you use the same words you'd search for later — the semantic gap barely exists."
- Source: [DEV Community — grep replacement](https://dev.to/kuro_agent/why-i-replaced-my-ai-agents-vector-database-with-grep-59mm) · [voxos.ai](https://voxos.ai/blog/how-to-give-ai-coding-agents-long-term-m/index.html) | Confidence: M

**Claude Code, Manus, and similar production coding agents** [TRAIN / partially confirmed]
- Reported to use Markdown files as primary memory substrate in 60,000+ projects
- Source: [DEV Community — flat files](https://dev.to/mindon/i-built-3-agent-systems-all-of-them-use-flat-files-heres-why-your-vector-db-is-overkill-5f31) — practitioner report, not official vendor confirmation | Confidence: M

**MemForest** (arXiv:2605.23986, 2026)
- Hierarchical temporal indexing over persistent agent memory
- Not purely file-native but relevant to the navigation layer over flat stores
- Source: [arXiv:2605.23986](https://arxiv.org/pdf/2605.23986) | Confidence: H

### Comparison vs RAG / vector stores (2026 state)

| Dimension | File-native + BM25 | RAG / Vector DB |
|---|---|---|
| Temporal reasoning | Strong (timestamps in filenames/frontmatter) | Weak by default; no timestamp weighting in embedding distance |
| Recall at < 1,000 docs | ~90% BM25 (practitioner reports) | ~76–85% (benchmarks vary) |
| Infrastructure cost | Near-zero; single SQLite file | $0.23/GB/month managed (AWS OpenSearch, 2024 [TRAIN]) |
| Multi-hop reasoning | Weak without graph overlay | Weak for pure vector; graph RAG stronger |
| Auditability | Excellent (git-diffable Markdown) | Poor (opaque embedding space) |
| Scaling wall | Degrades past ~10,000 docs; raw logs don't rank | Scales with index; degrades on stale facts |

Source: [Atlan — Agentic AI Memory vs Vector DB](https://atlan.com/know/agentic-ai-memory-vs-vector-database/) · [sparkco.ai](https://sparkco.ai/blog/ai-agent-memory-in-2026-comparing-rag-vector-stores-and-graph-based-approaches) | Confidence: M

### Known failure modes (file-native)

1. **Scale wall**: Raw append-only Markdown logs degrade retrieval quality past ~10K entries; BM25 keyword clutter grows
2. **Silent staleness**: Old and new versions of a fact coexist; agent cannot distinguish recency without explicit timestamps or filtering logic
3. **No semantic gap bridging**: Grep/BM25 fails when the query uses different vocabulary than the stored memory (mitigated by hybrid with sqlite-vec)
4. **Concurrent write corruption**: Multi-writer scenarios require coordination (see Q5)

Source: [DEV Community — AI Agent Memory Management](https://dev.to/imaginex/ai-agent-memory-management-when-markdown-files-are-all-you-need-5ekk) · [Medium — Scaling Wall](https://volodymyrpavlyshyn.medium.com/the-scaling-wall-moving-beyond-md-files-in-multi-agent-systems-da413f9d33e3) | Confidence: M

---

## Q2 — Deliberate Forgetting in Append-Only Knowledge Stores

### Who has built this

**Graphiti** (Zep AI, open-sourced January 2025)
- Temporally aware knowledge graph engine with bi-temporal model: every graph edge carries `valid_from` / `valid_to` timestamps plus ingestion timestamp
- When information is superseded, old edges are **invalidated, not deleted** — soft tombstone pattern
- Read-view filtering: "a query for 'what was true on 2025-12-01' filters to edges whose valid-from/valid-to window contains that date"
- Source: [Zep — Temporal Knowledge Graph](https://www.getzep.com/ai-agents/temporal-knowledge-graph/) · [Callsphere / Graphiti](https://callsphere.ai/blog/graphiti-temporal-knowledge-graph-ai-agents-2026) | Confidence: H

**ESAA-Conversational** (arXiv:2606.23752, 2026)
- Event-sourced memory layer for LLM coding agents
- `activity.jsonl`: append-only log of turns, decisions, tasks
- Read models (`state.md`, `handoff.md`): compact summaries derived from the event log
- Explicit separation of the write path (immutable event log) from read views (mutable projections)
- Source: [arXiv:2606.23752](https://arxiv.org/pdf/2606.23752) | Confidence: H

**Agentic Unlearning / SBU** (arXiv:2602.17692, Feb 2026)
- "Synchronized Backflow Unlearning" — removes targeted information from both model parameters AND persistent memory
- Problem identified: parameter-memory backflow — retrieval reactivates parametric remnants even after memory deletion
- Memory pathway: dependency closure-based pruning + logical invalidation of shared artifacts
- Source: [arXiv:2602.17692](https://arxiv.org/abs/2602.17692) | Confidence: H

**SSGM Framework** (arXiv:2603.11768, 2026)
- "Stability and Safety Governed Memory" — bounded, budget-aware forgetting policies
- Forgetting taxonomy: time-based, frequency-based, importance-driven (Priority Decay)
- Claim: reduces computational cost while preserving narrative coherence and privacy
- Source: [arXiv:2603.11768](https://arxiv.org/pdf/2603.11768) | Confidence: H

### Database / event-sourcing precedents [TRAIN — not live-verified this run]

- **Apache Kafka log compaction**: keeps only the latest value per key; earlier values are tombstoned. Standard tombstone = record with null value and same key. Known issue: compaction does not run continuously; consumers may see deleted entries in the window before compaction.
- **Apache Cassandra TTL + tombstones**: time-to-live on cells; expired cells become tombstones; tombstones themselves are garbage-collected after `gc_grace_seconds`. Known failure: tombstone accumulation causes read performance degradation ("tombstone storm") on high-churn workloads.
- These patterns are referenced but not currently documented in agent-specific literature as adopted patterns. Confidence: L (training-era knowledge, not live-verified)

### What broke

- **Coexistence problem**: append-only stores without read-view projection force the agent to guess which version of a fact is current — identified as the dominant failure mode in multiple 2025 surveys
- **"Most fail conspicuously on selective forgetting"** — direct quote from benchmark evaluation in the agent memory survey landscape (2025–2026); selective forgetting is explicitly called an active research frontier
- **Backflow after unlearning** (SBU paper): deleting from memory without also suppressing parametric memory leads to recontamination; a finding with no prior-art solution until SBU
- Source: [Nuanced Perspective Substack — Agentic Memory 2026](https://thenuancedperspective.substack.com/p/designing-agentic-memory-in-2026) · [arXiv:2603.11768](https://arxiv.org/pdf/2603.11768) | Confidence: H

---

## Q3 — Identity Drift: Measurement, Not Prevention

### Measurement frameworks (2025–2026)

**Examining Identity Drift in Conversations of LLM Agents** (arXiv:2412.00804, Dec 2024)
- Defines drift as systematic decrease in projection along the "Assistant Axis" in activation space
- Formal identity metrics: Identifiability, Continuity, Persistence, Consistency, Recovery
- Black-box, trait-agnostic, multi-turn aware
- Source: [arXiv:2412.00804](https://arxiv.org/abs/2412.00804) | Confidence: H

**Measuring What Persists: Geometric Framework for AI Agent Identity** (arXiv:2606.21843, June 2026)
- "Magnitude-homology fingerprint" as instrumentation of Persistence and Consistency metrics
- Conditions identity measurement on conversation trajectory geometry
- Source: [arXiv:2606.21843](https://arxiv.org/html/2606.21843) | Confidence: H

**DRIFTLENS** (arXiv:2607.02374, July 2026, Amazon)
- Ground-truth-free framework; maps reasoning steps to value categories; measures divergence between no-memory and memory-injected trajectories
- Tested across 4 LLMs, 10 user-attribute categories (age, occupation, disability, etc.)
- Finding: user-attribute memory induces medium-to-large reasoning drift **even when final answers remain fluent, on-topic, and plausible** — the visible surface is stable; the reasoning path has shifted
- Mitigation tested: GRPO and DPO post-training reduce drift but neither uniformly preserves downstream capability
- Source: [arXiv:2607.02374](https://arxiv.org/abs/2607.02374) | Confidence: H

**Memory-Induced Tool-Drift in LLM Agents** (arXiv:2605.24941, 2026)
- Specifically measures how persisted user context reshapes tool-calling behavior, not just text output
- Source: [arXiv:2605.24941](https://arxiv.org/pdf/2605.24941) | Confidence: H

**Quantifying Agent Drift in Multi-Agent LLMs** (arXiv:2601.04170, 2026)
- 12-dimensional Agent Stability Index (ASI)
- 800+ simulation workflows; 42% drop in task success rates correlated with drift; 3.2x increase in human interventions
- Source: [emergentmind.com — Quantifying Agent Drift](https://www.emergentmind.com/papers/2601.04170) | Confidence: M (emergentmind summary, not direct paper read)

**The Dual Nature of LLM Persona** (arXiv:2607.02368, July 2026)
- Frame-dependent geometry: persona expressed depends on the conversational frame, not solely on the model's weights
- Source: [arXiv:2607.02368](https://arxiv.org/abs/2607.02368) | Confidence: H

**Attractor States Emerge in Multi-Turn LLM Conversations** (arXiv:2606.30571, June 2026)
- Persona convergence to training-reinforced modes in the absence of human correction
- Source: [arXiv:2606.30571](https://arxiv.org/pdf/2606.30571) | Confidence: H

### Self-consistency false negatives (confident repeated error)

"Too Consistent to Detect: A Study of Self-Consistent Errors in LLMs" (ResearchGate, 2025)
- Self-consistent errors: LLM repeatedly generates the same wrong answer across multiple stochastic samples
- Key finding: unlike random errors (which decrease with model scale), self-consistent errors remain stable or **increase** with scale
- "All four types of detection methods significantly struggle to detect self-consistent errors"
- Mechanism: systematic training-time bias means the wrong answer wins the majority vote every time; self-consistency voting catches variance but not systematic bias
- Source: [ResearchGate](https://www.researchgate.net/publication/392085012_Too_Consistent_to_Detect_A_Study_of_Self-Consistent_Errors_in_LLMs) | Confidence: M (summary level; paper not directly read)

MIT method (2026): cross-model disagreement measurement; comparing target model against a group of similar LLMs outperforms single-model self-consistency for uncertainty detection
- Source: [MIT News, March 2026](https://news.mit.edu/2026/better-method-identifying-overconfident-large-language-models-0319) | Confidence: H

### Quantified drift numbers (live-verified)

- 20–40% drop in Assistant Axis projection over 10–15 turns in therapy/philosophy conversation domains (arXiv:2412.00804)
- 42% task success rate drop correlated with ASI-measured drift (arXiv:2601.04170)
- Reasoning drift detected even with stable surface output (DRIFTLENS, arXiv:2607.02374)

---

## Q4 — Navigation Modes Over Knowledge Stores

### Literature on mode types and selection

**NaviRAG** (arXiv:2604.12766, April 2026, Tsinghua / Nanjing / Northeastern)
- Shifts from flat passive retrieval to active hierarchical navigation
- Organizes documents into coarse-to-fine hierarchy; LLM agent actively navigates, iteratively identifying information gaps, choosing granularity level
- Beats conventional RAG baselines on long-document QA benchmarks
- Most relevant to **mode selection**: the agent's navigation mode (flat vs. hierarchical descent) is selected dynamically based on identified gaps
- Source: [arXiv:2604.12766](https://arxiv.org/abs/2604.12766) | Confidence: H

**WikiKV** (arXiv:2606.14275, June 2026, WeChat/Tencent)
- Path-indexed storage for hierarchical wiki-shaped knowledge bases
- Budgeted navigation operator: "search-accelerated routing reduces expected LLM-assisted descent steps from d to O(1) while preserving anytime semantics with progressively refined answers"
- Three query operators: path lookup (deterministic), tree traversal (exhaustive), budgeted navigation (hybrid)
- Deployed in production: WeChat Official Account AI Assistant; 63.2% end-to-end answer correctness, exceeds RAG baselines
- Source: [arXiv:2606.14275](https://arxiv.org/pdf/2606.14275) | Confidence: H

**Search-on-Graph** (arXiv:2510.08825, 2025)
- Iterative informed navigation for LLM reasoning on knowledge graphs
- Mode selection based on hop distance and confidence at current node
- Source: [arXiv:2510.08825](https://arxiv.org/pdf/2510.08825) | Confidence: H

### Mode taxonomy from gathered evidence

| Mode | Trigger condition (from literature) | Failure mode |
|---|---|---|
| Deterministic key lookup | Known exact address; closed-domain; structured KV | Fails on semantic queries; brittle to key format changes |
| Hierarchical descent (NaviRAG/WikiKV) | Structured corpora; multi-granularity queries | Overhead for simple lookups; hierarchy must be maintained |
| Stochastic probing / sampling | Open-domain; ambiguous queries; creative synthesis | High variance; no convergence guarantee |
| Exhaustive traversal | Coverage required; audit/compliance queries | Cost scales linearly with corpus; not viable at scale |

### Mode SELECTION literature — honest null

No paper directly titled "when to select navigation mode" was found. WikiKV's budgeted operator is the closest: it starts with O(1) routing and falls back to deeper traversal when the routing estimate is low-confidence. NaviRAG's agent selects granularity level per gap, but the selection policy is learned implicitly, not formalized as a separate decision procedure. This sub-question (explicit mode-selection policy) is **not yet formally addressed in the literature as of 2026-07-17**. Confidence: M (absence of evidence, not evidence of absence)

---

## Q5 — Concurrent Append: Multi-Writer Files, Sequential IDs, No Locking

### CoAgent (arXiv:2606.15376, June 2026, Shanghai Jiao Tong University)

Most directly relevant paper found.

- Problem: agent transactions span minutes of inference with broad, opaque read sets; classical locking blocks long inference; OCC abort-and-retry discards minutes of work per conflict
- Solution: **MTPO (Monotonic Trajectory Pre-Order)** — fixes serialization order at launch; serves each read an order-filtered value; applies writes speculatively in place; one-way notification asks affected readers to re-judge and patch their plan
- Key insight: the LLM inside each agent can judge whether a conflicting write actually invalidates its plan — control becomes advisory, not blocking
- Does NOT address sequential IDs specifically; addresses write-set conflicts generally
- Source: [arXiv:2606.15376](https://arxiv.org/abs/2606.15376) | Confidence: H

**Verified Detection and Prevention of Concurrency Anomalies** (arXiv:2606.17182, 2026)
- Formal verification of concurrency anomalies in multi-agent LLM systems
- Source: [arXiv:2606.17182](https://arxiv.org/pdf/2606.17182) | Confidence: H

**ATM: CID-Brokered Pre-Write Admission** (arXiv:2607.00041, July 2026)
- Pre-write admission control via a central ID broker before any agent commits
- Most relevant to sequential ID coordination: a broker assigns IDs before write, preventing collision
- Source: [arXiv:2607.00041](https://arxiv.org/pdf/2607.00041) | Confidence: H

### Known coordination disciplines (current practice, 2025–2026)

1. **Sequential execution** — one agent writes at a time; loses concurrency benefit entirely
2. **Static write-set partitioning** — agents have non-overlapping write domains assigned at launch; brittle when plans emerge during execution
3. **Fork-and-merge** — agents fork shared state, execute, merge; weak isolation (read-committed equivalent); merge conflicts still require resolution
4. **Lock acquisition via platform API** (e.g., Fastio) — explicit lock/release; introduces contention and failure recovery complexity
5. **CRDTs** — referenced as a direction in CoAgent paper but no agent-specific CRDT implementation found in the literature as of this run

Source: [Amplify Partners — File systems for agents](https://www.amplifypartners.com/blog-posts/file-systems-for-agents) · [CoAgent paper](https://arxiv.org/html/2606.15376) | Confidence: H

### On "no locking" specifically

"Without locking, concurrent writes silently lose entries — resulting in corrupted data." This framing appears consistently across practitioner sources. The CoAgent MTPO approach is the closest to lock-free coordination but still requires a notification/re-judge cycle; it is optimistic, not lock-free in the strict sense. True lock-free sequential ID generation over plain files is **not documented as a solved pattern in agent memory literature** as of 2026-07-17. The ATM CID-broker approach (arXiv:2607.00041) solves the ID collision problem but introduces a broker as a coordination point.

---

## Q6 — Self-Termination in Agentic Exploration

### Research found (2024–2026)

**Joint Agent Memory and Exploration Learning via Novelty Signals** (arXiv:2606.01528, June 2026)
- Novelty-based intrinsic reward: binary signal — action produced genuinely new experience relative to accumulated history
- Once a state is visited, it must never register as novel again (persistent novelty memory)
- GUI domain proxy: code coverage as deterministic novelty — a step is novel iff it triggers at least one previously unexecuted code path
- Source: [arXiv:2606.01528](https://arxiv.org/html/2606.01528) | Confidence: H

**Caesar: Deep Agentic Web Exploration for Creative Answer Synthesis** (arXiv:2604.20855, 2026)
- Cumulative coverage reward for web agents measuring exploration breadth
- Termination implicitly tied to coverage saturation
- Source: [arXiv:2604.20855](https://arxiv.org/pdf/2604.20855) | Confidence: H

**Enough is Enough: Autonomous Uncertainty-driven Stopping Criteria** (arXiv:2204.10631, 2022 — foundational)
- Uncertainty-driven stopping; agent terminates when uncertainty estimate falls below threshold
- Foundational paper; still cited in 2025–2026 agent literature
- Source: [arXiv:2204.10631](https://arxiv.org/pdf/2204.10631) | Confidence: H

**Causaly / R&D termination conditions** (2026)
- Termination as function of: coverage saturation, diminishing returns, decision risk, artifact completeness (evidence tables, assumptions, provenance)
- Practitioner framing, not formal paper
- Source: [Causaly blog](https://www.causaly.com/blog/how-termination-conditions-strengthen-agentic-systems-in-r-d) | Confidence: M

**SLAM-based robotic exploration stopping** [TRAIN — referenced in search summaries but not directly verified]
- TOED-based criterion: exploration terminates when information gain to the SLAM map falls below threshold
- Analogy to knowledge-store exploration: "done" when new traversal adds no new map content
- Confidence: L (not live-verified; mentioned in search result summary only)

### State of the art summary

| Stopping mechanism | Status in 2026 | Source |
|---|---|---|
| Budget exhaustion (token/step limit) | Default; widely used | Implicit across agent frameworks |
| Novelty saturation (visited state memory) | Active research; code coverage proxy working in GUI agents | arXiv:2606.01528 |
| Uncertainty threshold | Established (2022 paper); not yet standard practice | arXiv:2204.10631 |
| Coverage-based (explicit reward) | Active research; web agent domain | arXiv:2604.20855 |
| Revisit detection | Referenced but no dedicated paper found in this run | Null result |
| Artifact completeness checking | Practitioner only; not formally benchmarked | Causaly blog |

Honest null: "revisit detection" as a named distinct technique with its own paper did not surface. The novelty-signal papers cover overlapping ground but frame it as reward, not as termination logic.

---

## Q7 — Agent Factory Taste: File Format / Convention Preferences

### AGENTS.md ecosystem (2026 state)

- AGENTS.md is stewarded by the **Agentic AI Foundation under the Linux Foundation**, originally driven by OpenAI, Amp, Google (Jules), Cursor, and Factory
- Read by 30+ agents across 60,000+ repositories (as of 2026)
- Format: plain Markdown, no required fields, no YAML frontmatter, no special syntax
- "Think of AGENTS.md as a README file, but for machines"; CLAUDE.md = "configuration file for one specific agent"
- Source: [morphllm.com — AGENTS.md Spec 2026](https://www.morphllm.com/agents-md-guide) · [agents.md official](https://agents.md/) | Confidence: H

### Is "agents follow README-style conventions better than bespoke formats" supported by evals?

**Partially supported, with important nuance:**

A 2025 benchmark on AGENTS.md files found:
- **LLM-generated AGENTS.md files reduced success rates by 2% and increased cost by 23%** — primarily because they duplicated content already available in the repository
- **Human-written minimal AGENTS.md files** with only three content categories (coding conventions, architecture, project description) **reduced median wall-clock time by 28% and output tokens by 16%**
- The key is information density: "Every line should contain information the agent cannot get from reading your code, package manifests, or existing documentation"

Source: [morphllm.com — AGENTS.md Spec](https://www.morphllm.com/agents-md-guide) · [builder.io — AGENTS.md](https://www.builder.io/blog/agents-md) | Confidence: M (the specific benchmark percentages appear in the morphllm.com summary; the underlying study was not directly accessed)

### What the evidence supports vs. what is folklore

| Claim | Evidence status |
|---|---|
| Agents read and act on AGENTS.md / CLAUDE.md | H — confirmed by ecosystem adoption (30+ agents, 60K+ repos) |
| README-style Markdown outperforms bespoke format | M — implied by adoption and one benchmark; no head-to-head format comparison study found |
| More content in AGENTS.md = better agent performance | Contradicted — LLM-generated verbosity reduces performance |
| Convention-following (README pattern) is innate to LLMs | Unverified — no controlled experiment isolating format vs. content effect found in this run |

**Honest null**: No peer-reviewed paper directly comparing README.md vs. settings.json vs. AGENTS.md as instruction formats for LLM agent behavior was found. The AGENTS.md benchmark above is the closest evidence. The claim "agents follow README-style conventions better than bespoke formats" has practitioner support and ecosystem momentum, but is not formally proven in a controlled eval as of 2026-07-17.

---

## Q8 — Name-Collision Check

### "SML" / "small mind model"

- **"SML"** is **not occupied** as a distinct AI/agent tooling term as of 2026-07-17. Searches return only "SLM" (Small Language Models), which is a heavily occupied term (Microsoft Phi, Meta Llama 3.2, Mistral Ministral, Google Gemma, Alibaba Qwen product families)
- **"small mind model"** as a specific named concept: no results found. Not an occupied term.
- **Risk**: "SLM" is the dominant adjacent term; naming anything "SML" risks confusion with SLM in verbal communication. In text it is distinguishable.
- Source: [futureagi.com — SLM 2026](https://futureagi.com/blog/small-language-models-agentic-ai-2025/) | Confidence: H (null confirmed by search; absence is meaningful here)

### "meditation room" (as a named technique/tool in AI/agent contexts)

- No result found for "meditation room" as a named AI agent technique, method, or tool
- Results returned only: AI-powered wellness apps, mindfulness chatbots, VR meditation tools
- One edge result: "structured rest" concept involving a meditation cron job — this is a practitioner blog pattern, not a named technique with a paper or tooling entry
- **Not occupied** as a named agent technique as of 2026-07-17
- Source: search conducted 2026-07-17 | Confidence: H (null confirmed)

### "SUPER-README"

- No result found for "SUPER-README" as a named tool, technique, or ecosystem concept
- Closest results: AGENTS.md described as "the README for AI agents"; readme-ai (generator); ReadMe.com's AI agent documentation assistant
- **Not occupied** as a named concept as of 2026-07-17
- Source: search conducted 2026-07-17 | Confidence: H (null confirmed)

---

## Summary Table

| Q | Core finding | Confidence | Null result? |
|---|---|---|---|
| Q1 File-native memory | memweave (live, active); practitioner consensus BM25 < 1K docs; RAG comparison documented; failure modes clear | H/M | No |
| Q2 Deliberate forgetting | Graphiti bi-temporal (H); ESAA event-sourced (H); SBU agentic unlearning (H); tombstone DB patterns (L, training-era) | H | Partial — DB tombstone precedents unverified |
| Q3 Identity drift measurement | DRIFTLENS (July 2026, Amazon); geometric framework (arXiv:2606.21843); self-consistent errors confirmed (ResearchGate 2025); MIT cross-model method (March 2026) | H | No |
| Q4 Navigation mode selection | WikiKV budgeted operator; NaviRAG; mode taxonomy assembled; explicit mode-SELECTION policy paper: null | H | Partial — mode selection as explicit decision procedure not found |
| Q5 Concurrent append | CoAgent MTPO (June 2026); ATM CID-broker (July 2026); lock-free sequential IDs over plain files: null | H | Partial — no lock-free plain-file ID discipline found |
| Q6 Self-termination | Novelty signals (arXiv:2606.01528); coverage reward (Caesar); uncertainty threshold (2022 foundation); revisit detection as named technique: null | H | Partial — revisit detection paper not found |
| Q7 Agent format taste | AGENTS.md ecosystem confirmed (H); LLM-generated verbosity reduces perf (M); head-to-head format eval: null | H/M | Partial — no controlled format comparison study |
| Q8 Name collisions | SML: not occupied (SLM is); meditation room: not occupied; SUPER-README: not occupied | H | (all three are clean) |

---

## Sections to refresh

- Q4 navigation mode selection: search specifically for "adaptive retrieval strategy selection" and "query routing" literature — the gap is real but may be partially filled under different terminology
- Q5 lock-free sequential IDs: search database literature (HBase WAL, Cassandra commit log) for analogous patterns; the agent-specific literature is sparse
- Q7 controlled format eval: monitor AGENTS.md Foundation publications and any Anthropic/OpenAI evals on instruction-file format sensitivity
- Q2 tombstone DB precedents: live-verify Kafka log compaction and Cassandra TTL behavior against current docs (currently only training-era knowledge)
- Q3 self-consistent errors paper: direct read of the ResearchGate paper if accessible — currently only summary-level

---

## Follow-up round 1 (2026-07-17, F-leg)

**Run date:** 2026-07-17 | **Model:** claude-sonnet-4-6 | **Scope:** Two bounded null-verification passes (F-1, F-2)

---

### F-1 — Mode-Selection Null: OVERTURNED (partial)

The Q4 null ("no explicit formalized mode-selection policy") does not fully hold under alternative terminology. The field is active and named.

**RAGRouter-Bench** (arXiv:2602.00296, Feb 2026) + **Lightweight Query Routing for Adaptive RAG** (arXiv:2604.03455, Apr 2026)
- RAGRouter-Bench: 7,727 queries across four knowledge domains, each annotated with one of three retrieval strategy classes (factual / reasoning / summarization). Provides the first dedicated benchmark for adaptive RAG routing.
- Companion paper (arXiv:2604.03455): evaluates lightweight classifier-based routing — TF-IDF + SVM achieves macro-F1 0.928, 93.2% accuracy, 28.1% token savings vs. always-expensive baseline.
- This is a formalized selection procedure: a trained classifier decides which retrieval strategy to invoke per query.
- Source: [arXiv:2602.00296](https://arxiv.org/abs/2602.00296) · [arXiv:2604.03455](https://arxiv.org/abs/2604.03455) | Confidence: H

**Self-RAG** (arXiv:2310.11511, 2023 — foundational) + **TARG** (arXiv:2511.09803, Nov 2025)
- Self-RAG: trains reflection tokens ([Retrieval] / [No Retrieval]) into the LM itself; retrieval is triggered by token prediction, not a separate classifier. Formally: a trained binary gate, not a multi-strategy router.
- TARG (Training-Free Adaptive Retrieval Gating): single-shot policy using token entropy or logit-gap margin to gate retrieval. Threshold-based; no routing between multiple strategies — only retrieve vs. skip.
- Source: [arXiv:2310.11511](https://arxiv.org/html/2310.11511v1) · [arXiv:2511.09803](https://arxiv.org/abs/2511.09803) | Confidence: H

**Adaptive Query Routing** (arXiv:2604.14222, Apr 2026)
- Tier-based routing across financial, legal, and medical documents; classifies queries and routes to domain-specialized retrievers.
- Frames routing as an explicit decision policy, not implicit learning.
- Source: [arXiv:2604.14222](https://arxiv.org/html/2604.14222v1) | Confidence: H

**Verdict on F-1:** The null is overturned for "retrieve vs. skip" (Self-RAG, TARG: formalized) and for "which retrieval strategy" (RAGRouter-Bench, arXiv:2604.14222: formalized classifier). The specific gap that remains: no paper formalizes the tri-modal selection among deterministic key lookup / stochastic probing / exhaustive traversal as named categories in that vocabulary. The territory the downstream artifact claims — that specific tri-modal framing — remains unoccupied. The broader "query routing" space is occupied. Confidence: H

---

### F-2 — Anchor-Reconstruction Null: CONFIRMED

Probe terms: "retrospective self-prediction," "memory fidelity to origin," "self-consistency with historical self," "reconstruction-based drift detection," "pre-registration anchor for agent identity."

**Adjacent work found — none of it is the target:**

**BeliefShift** (arXiv:2603.23848, 2026)
- Benchmarks temporal belief consistency and opinion drift across multi-session interactions.
- Tracks whether beliefs change over time; does NOT ask the agent to reconstruct or predict its own earliest state, nor score that reconstruction as a honesty/fidelity metric.
- Source: [arXiv:2603.23848](https://arxiv.org/abs/2603.23848v1) | Confidence: H

**E-mem / Episodic Context Reconstruction** (Wang et al., 2026, referenced in survey arXiv:2605.06716)
- Reconstructs context from fragmented traces for higher retrieval fidelity.
- This is reconstruction of PAST CONTEXT for use in current inference — not an agent predicting its own initial state and scoring disagreement as a self-honesty metric.
- Source: [arXiv:2605.06716](https://arxiv.org/html/2605.06716v1) | Confidence: M (survey reference, not direct paper read)

**MEMPROBE** (referenced in 2026 agent eval literature)
- Reconstructs hidden user-state dimensions from memory store to audit memory completeness.
- Subject of reconstruction is user state, not the agent's own earliest self-state. Honesty metric is about memory completeness, not origin-fidelity.
- Confidence: M (search summary only; no direct arXiv ID confirmed this run)

**What was NOT found:** No paper constructs a held-out anchor of the agent's earliest recorded state, asks the agent to predict/reconstruct that state after N turns, and scores the reconstruction disagreement as a fidelity or honesty metric. The specific design — pre-registration of origin state, retrospective self-prediction, disagreement score as honesty signal — is absent from the literature as of 2026-07-17.

**Verdict on F-2:** Null confirmed. The anchor-reconstruction-as-honesty-metric concept is not documented in existing work. Adjacent territory (belief drift benchmarks, episodic reconstruction for retrieval, memory completeness auditing) is occupied but structurally distinct from the proposed design. Confidence: M (absence confirmed by targeted probing across multiple probe terms; cannot rule out an obscure pre-print not indexed by search).
