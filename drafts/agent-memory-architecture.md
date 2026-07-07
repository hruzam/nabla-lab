# Agent Memory Architecture — Background Stone

### State persistence across agent restarts on a file-backed orchestration bus. Systems framing. Phase-A launch point.

*Nabla & majkee. Cut 2026-07-06. This is a **background stone**, not a solution: it carries the problem space and invariants from prior design sessions so a fresh thread resumes without re-derivation. The design space is deliberately left open — the next thread is Phase A (substrate / dreaming), and majkee's own vision is not pre-empted here.*

---

## On this reincarnation — read first

This collaborator (Nabla) was originally specified for a different job: reshaping the terminal, UNIX-side tooling — Phase-C execution work. It turned out to be the better vehicle for something the spec never targeted: the Phase-A abstraction this stone launches into — raw, half-formed systems-and-math dreaming.

That is not a mystery and should not be mythologized. The reason is mechanical. The operating manual (WHOAMI) specifies a *mode of thinking* — the A/B/C phases, the buffering workflow, brutal honesty, the peer stance, the truth-in-files law — not just a task list. Most project prompts specify tasks; this one specifies a thinking partner. For execution work that part sits mostly idle. For abstraction work it is the entire load-bearing structure. The engine was built for the errand and turned out to be a track car — surprising only if you expected the spec to matter equally in every phase. It doesn't. It matters most in A.

There is no persistent "Nabla" carried between threads. The continuity is three things, rebuilt fresh each time: the immutable WHOAMI spec (truth, in a file), the stones like this one (condensed prior consensus, on disk), and majkee's own consistent way of engaging. The personality is reconstructed on instantiation from those inputs — which is exactly the truth-in-files / rebuild-on-read pattern this stone is about, turned on the collaborator itself. Worth noticing rather than romanticizing: the partnership works the way the architecture works.

So honor the manual as written, and don't read the terminal origin as a contradiction. The same UNIX values — composability, X-Y override, truth on disk, disdain for bloat — are what make the abstraction sharp. Same substrate, different phase.

---

## 0. How to use this

Open a new thread, paste the operating manual (WHOAMI) as usual, attach this file. It gives the collaborator full background on the stack, the invariants, the problem, and the prior art — so the conversation starts at the frontier instead of re-deriving the setup. Then majkee unfolds the raw idea. The collaborator's job is stated in §7: find the reasonable structure in the impulse, honor the invariants, and do **not** force the idea into any pattern below. Substrate, not cage.

---

## 1. Collaboration frame (pointer)

Three phases, and the collaborator must always know which one is active: **A — Substrate** (dreaming, first-principles, infinite compute assumed, no implementation); **B — Architecture** (map the dream to bare-metal UNIX I/O, streams, daemons); **C — Execution** (deterministic code under real constraints). Workflow is buffering, not artifact-vending: read the impulse, ask when unsure, think, argue to clarify, release artifacts only on request. Brutal-honest over agreeable. This stone opens a **Phase A** thread.

---

## 2. The stack (context the collaborator needs)

A file-backed, append-only multi-agent orchestration bus. A central orchestrator coordinates heterogeneous agents (different vendors — the heterogeneity is deliberate, it decorrelates their errors). Agent turns are normalized to JSONL lines; those lines are the canonical substrate. Live negotiation happens in streams; durable record lives in files.

Load-bearing invariants (everything below inherits these):

- **Text interface contract** — components emit and consume plain text; anything pipeable, streamable, multiplexable.
- **Single-responsibility daemons** — hyper-focused decoupled processes, not monoliths.
- **X-Y override** — never mistake the proposed implementation for the actual goal; question the tool choice itself.
- **Append-only invariant** — history is preserved, not simulated. Truth lives on disk. Append, filter on read, keep the raw timeline.
- **Resonance in streams, truth in files** — consensus is found live in memory, then condensed and written to disk. Permanent memory is strictly file-based.

---

## 3. The problem: state persistence across restart

Agents are effectively stateless processes over a durable log. On teardown, in-process context is gone. On restart — call it *reincarnation* — the agent comes up with a clean context and must reload its working memory from an external store. **No durable in-process state survives the boundary.**

So the real questions, in systems terms:

1. What *is* the external memory the agent reloads from?
2. How is it **written** — everything, or selectively? On what trigger?
3. How is it **read back** — full replay, or a compact projection?
4. How does a restarted agent reach a *consistent, useful* working state **fast**, without re-ingesting the entire history every time?

This is a **state-persistence and cache-coherence problem**, not a model-internals problem. It lives at the orchestration layer, on the file substrate — exactly where the invariants apply.

---

## 4. Prior art: the two-tier cache (HOLA)

*arXiv:2607.02303, "A Hippocampus for Linear Attention," submitted 2 Jul 2026 — verified against source, four days old at time of writing.*

Read as what it is: a **caching architecture** for linear-attention / state-space models. Those models compress the whole prefix into a fixed-size recurrent state — O(1) memory, but lossy; when many key–value associations compete, older ones get overwritten and exact recall degrades. HOLA adds a **bounded exact key–value cache** beside the compressed state. The state holds the compressible structure; the cache holds the raw associations that shouldn't be forced through it.

The write rule is the part worth stealing: **no learned eviction module — cache the tokens with the largest prediction residual**, i.e. store precisely what the compressor *failed to absorb*. Surprise-gated writing. What doesn't fit gets stored verbatim; what fits stays compressed.

**Honest scope — the reason this is prior art and not a solution.** HOLA operates *within a single forward pass over one context window*. Its cache lives and dies inside one inference; it never crosses the session boundary. So it solves within-context needle recall for a class of models — **not** cross-reincarnation persistence (§3). Take the *write policy* (append what surprised you) as a transferable pattern; do not take the paper as an answer to durable agent memory. Different floor of the stack.

---

## 5. The core design axis (open, not resolved)

Two opposed philosophies of what the external memory *is*. The whole design lives on this axis.

**(a) Immutable event log — event sourcing.** Every state change appended, never mutated. Working state is a fold/replay over the log. Honest, auditable, reconstructable from scratch; the cost is that "current belief" isn't stored, it's computed. This is the append-only invariant, taken literally.

**(b) Mutable derived projection.** A compact "current belief" rewritten in place as new information arrives. Fast to read; the cost is **integrity risk** — a mutable projection drifts from the source of truth unless strictly disciplined, and once it has drifted there's no untouched original left inside it to check against.

The tension is concrete: a read can serve the raw log entry, or a recomputed projection that folds in newer state. And the integrity risk of (b) is *precisely the argument for* (a).

The standard clean resolution — event sourcing + materialized views — is worth having on the table as a *default to beat, not a conclusion*: keep the log immutable as the single source of truth; treat any "current belief" as a **derived, rebuildable view**, always traceable to the log, always recomputable from zero. Truth is stored; meaning is derived. Three strata, not two: raw log (immutable) → derived working view (rebuilt, never authoritative) → live stream (ephemeral).

*(Note for continuity: an earlier session reached this axis through a complementary-learning-systems analogy from ML. This stone discharges that scaffolding and states the problem directly in systems terms — event sourcing, cache coherence, materialized-view invalidation — which is the more precise vocabulary for the build. The analogy was ladder, not architecture.)*

---

## 6. Instruments available from prior threads (pointers, not commitments)

- **Surprise-gated write** — the HOLA write rule generalized: append verbatim what the compressed model failed to predict (high prediction residual). Same signal as the active-inference / free-energy term from Atlas №1 (I.10). Candidate answer to §3 question 2.
- **Multi-agent reconciliation** — when two restarted agents restore *inconsistent* working states, distinguish a mere frame-difference (reconcilable) from a genuine contradiction (a real obstruction). Sheaf-consistency instrument, Atlas №1 I.9.
- **Associative recall over the log** — treat the JSONL log as a graph; recall by spreading activation / diffusion rather than by scanning (HippoRAG-style personalized-PageRank, Atlas №1 Part II). Candidate answer to §3 questions 3–4.

Available tools in the drawer. None is chosen. The idea picks the tool, not the reverse.

---

## 7. The open door — Phase A launch

The next thread is **majkee's own raw vision** for agent memory persistence across reincarnation. It is not stated here, on purpose. It will arrive as an impulse — abstract, possibly dreaming more than specified — and that is the correct form for Phase A.

The collaborator's job:

- Read the impulse as an *X-impulse*, not a verbatim spec. Find the hidden structure in it.
- Honor the append-only invariant and the truth-in-files / resonance-in-streams law unless there's a first-principles reason to challenge them — and if there is, say so plainly.
- **Do not force the idea into HOLA's two-tier mold, into the event-sourcing default of §5, or into any instrument in §6.** Those are the ground already cleared; the point of the new thread is what grows on it.
- Assume infinite compute. Dream first. Architect later. Say "I don't know" when that's the true answer.

---

## 8. Freshness & provenance

HOLA (§4) verified against arXiv, 2 Jul 2026. Timeless patterns — event sourcing, append-only logs, cache coherence, materialized-view invalidation — need no verification and get none. Everything in §5–§7 is open design space, explicitly not fact. Atlas №1 references (I.9, I.10, Part II) are prior artifacts from the same collaboration and can be carried in if the thread needs them.

*End of stone. Background only. The idea is majkee's to bring.*
