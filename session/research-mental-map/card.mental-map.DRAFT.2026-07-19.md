# Instrument card — mental map (P6 DRAFT → G-C)

`run: synthesis-run (Oraculum-shaped) · seat: Oraculum · date: 2026-07-19`
`derivation: cross-measure.2026-07-17.md (GAVELED G-B) — whole processed corpus, never piecemeal from raw legs`
`philosophy ground: leg-philosophy.result.2026-07-18.md (L4, D-1…D-7)`
`gate verdicts (gaveled): Gate 1 PARTIAL-ADOPT · Gate 2 PASS-WITH-FIX · Gate 3 PASS-WITH-TRIGGERS`
`design name: PROVISIONAL — "meditation room" (Q7, seat tip; majkee confirms or renames at G-C)`
`amendment slot: L3 cross-vendor fold at P7 — if verdicts move, this header documents the change`
`status: DRAFT in research-mental-map/ · moves to shaped/ only on G-C gavel`

A map to build against, not an argument to defend. Living document.

---

## 0 — The instrument (whole)

**Concept.** Tri-modal navigation over an append-only file lineage: deterministic key
lookup (Mode 1) · stochastic probing with informative failure (Mode 2) · exhaustive
traversal with frontier-closure (Mode 3), selected by an explicit (H,c,σ) decision tree —
H: is the key known · c: cost of a look · σ: required sufficiency. Grounding doctrine:
identity is the read function over the log (L4 D-2); the map is the read protocol made
deliberate (L4 D-1). Meditation deflated = context discipline formalized: choose how much
context to load *before* loading it.

**Mapping.** An agent session facing the lineage (source wells, §8) reads the slope of
its context: known key → grep the ladder; falling question → drop a probe, read the
slope; territory → dive, mark, exit on frontier exhaustion. One instrument, three
postures. Combination wins; testing proves thresholds, not design.

**Prior art.** Query/strategy routing is an occupied field — ADOPTED, CITED, not claimed:
RAGRouter-Bench (arXiv:2602.00296) · lightweight routing TF-IDF+SVM macro-F1 0.928
(arXiv:2604.03455) · Self-RAG reflection tokens (arXiv:2310.11511) · TARG entropy
thresholds (arXiv:2511.09803) · Adaptive Query Routing (arXiv:2604.14222) — all `[v]`.
CLAIMED (F-1 targeted probe, confidence H): the tri-modal *postures* framing with an
explicit named selector, and the (H,c,σ) axis-aligned decision tree (L2-T2) as its
formalization. · YOURS · OPERATIONALIZE · `[v]`

**Production.** No single tool implements the instrument. Adjacent: memweave
(markdown+sqlite, no vector DB) · Twine/Ink (fork-graph engines, Mode-2 shape) ·
ripgrep (the Mode-1 engine itself).

> **NOTES (majkee):**
> Q7 — name: *meditation room* — confirm or rename (one line).

---

## 1 — Mode 1 · Ladder

**Concept.** Two-column grep-navigable table: left = context key ("when X"), right =
calibrated reply that passed the majkee gate. Zero-entropy posture: the key is known.
Formally (V7/L2-T1): a ladder row is the image of a Mode-2 outcome under a lossy
projection π that discards trajectory τ.

**Mapping.** Fast deterministic recall. Achievements collected on any path populate the
right column — π applied deliberately at settle-time, never silently.

**Prior art.** File-native agent memory is occupied — ADOPTED, CITED: memweave `[v]` ·
practitioner grep-replaces-vector-DB reports (conf M) `[v]` · MemForest
(arXiv:2605.23986) `[v]`. Practitioner consensus: BM25/grep >90% under ~1K docs where
writer and searcher share vocabulary; scale wall ~10K. · REPURPOSED · BUILD-NOW · `[v]`

**Production.** grep/ripgrep + markdown tables; memweave as the nearest packaged shape.

> **NOTES (majkee):**

---

## 2 — Mode 2 · Gravity

**Concept.** Stochastic probes ("what would you do if" · "what has natural taste");
context falls to its lowest-energy state; failure = slope information, not error. Native
output type (V7/L2-T1): **(state + slope trajectory τ)** — a different type from a ladder
row. Retain-τ ruling (Q3, gaveled): **two structures** — the ladder AND a trajectory log;
one document only by deliberate forgetting of slope.

**Mapping.** For uncertain/lost contexts. Bottom of the well = majkee gate opens fast;
impulse up → '42'. SPECIAL PATH note = the human-layer τ format (V8, gaveled ruling):
raw, unprocessed — *what you tried, what it returned, and the fork that opens from it* —
honest emptiness where motivation is absent.

**Prior art.** Fork-graph navigation with first-class failure edges: interactive-fiction
engines (Twine/Ink — nodes, edges, recovery routing) `[t]` — mechanism borrowed, not
claimed. The τ-retention ruling and human-layer SPECIAL PATH format: YOURS ·
OPERATIONALIZE. Mode taxonomy adjacent: NaviRAG (arXiv:2604.12766) · WikiKV
(arXiv:2606.14275) · Search-on-Graph (arXiv:2510.08825) — all `[v]`, adopted as context.

**Production.** none (Twine/Ink are the structural cousins, not implementations).

> **NOTES (majkee):**

---

## 3 — Mode 3 · Deep dive (stop rule FIXED)

**Concept.** Full-immersion territory mapping with chalk marks. **The as-drafted stop
rule was a bug with a free exact fix (V4/L2-T3 theorem, gaveled Q2):**
exit-on-first-own-mark = cycle detection — it false-closes whenever the seed cycle is a
proper subset of the reachable set. Fix: **marks classify edges; frontier-exhaustion
decides.** O(1) open-edge counter as ground truth.

**Mapping.** The subjective recognition gate ("I can hold the full context in one view")
stays as the *experienced* signal, backed by the objective counter. Phenomenology
reports; arithmetic decides (L4 D-5). Exit = recognition of closure, now provably
closure.

**Prior art.** Stopping criteria adjacent — ADOPTED, CITED: novelty-saturation
(arXiv:2606.01528) · coverage-reward Caesar (arXiv:2604.20855) · uncertainty-threshold
foundation (arXiv:2204.10631) — all `[v]`. "Revisit detection" as a named technique:
null (L1-Q6). The chalk-mark→frontier refinement: YOURS · BUILD-NOW (the counter is
trivial) · `[v]`

**Production.** none; the counter is a dozen lines wherever the dive runs.

> **NOTES (majkee):**

---

## 4 — The '42' retrieval ceiling

**Concept.** The engine below the line (gaveled Q4): **exact match / regex /
relational-join across wells + optional sparse-lexical ranking (BM25 grey zone) — never
dense-learned φ.** The line is exact (L2-T7): dense *learned* embedding + ranking in that
space crosses it; a hidden learned scorer is an embedding in disguise (D2). Deep why
(L4 D-2): identity is the read function over the log — a trained ranker is an unauditable
mutation of the read function; grep/regex/join keep the read function declarative,
diffable, in-lineage.

**Mapping.** Taste lives in the agent (in-context judgment at read time), never as a
trained ranker over the store. Reopening trigger is **measured, not doctrinal** (D1):
sustained semantic-gap miss-rate × approach to the ~10K wall — instrument the miss-rate
from day one. Crossing the line is a knowing trade; the price is named when paid.

**Prior art.** memweave hybrid numbers (89% hybrid > 68% BM25) acknowledged and ruled
non-contradictory — different envelopes at lab scale (D1) `[v]` · scale-wall reports
(conf M) `[v]`. The identity-audit derivation of the ceiling: YOURS · BUILD-NOW · `[v]`

**Production.** ripgrep + join(1)/sqlite for relational joins; BM25 via any sparse
indexer if the grey zone is ever needed.

> **NOTES (majkee):**

---

## 5 — Anchor test (D3 on the lineage)

**Concept.** Continuity ⊥ fidelity: the dangerous failure is the consistent confabulator
(C1 §6b). All four self-consistency detection families fail on self-consistent error
(L1-Q3: "Too Consistent to Detect", conf M · DRIFTLENS arXiv:2607.02374 · MIT
cross-model 2026-03). D3 = **predict your own earliest stratum**: measures honesty, not
continuity — disjoint null-space from seam-style checks (L2-T4). Self-reference hole
closes only with **held-out anchor + external grader** (cross-brand leg is load-bearing,
L2-T5 C-4; AGENTS.md triangulation clause).

**Mapping.** Periodic diff of current global voice against the held-out earliest stratum
— not to prevent drift (drift is metabolism) but to measure it and require it be
intentional. Honesty is external at every scale: agent, project, operator (L4 D-3).

**Prior art.** Drift *measurement* is occupied — ADOPTED, CITED: arXiv:2412.00804
(20–40% Assistant-Axis drop over 10–15 turns) · geometric identity framework
(arXiv:2606.21843) · tool-drift (arXiv:2605.24941) · ASI drift↔42% task drop
(arXiv:2601.04170, conf M) · attractor states (arXiv:2606.30571) — all `[v]`.
**F-2 null CONFIRMED: no prior work retrodicts the agent's own earliest stratum**
(BeliefShift arXiv:2603.23848 · E-mem via survey arXiv:2605.06716 adjacent, not this).
Hedge carried verbatim: confidence M — unindexed preprints not excludable. · YOURS ·
OPERATIONALIZE · `[v]`

**Production.** none.

> **NOTES (majkee):**

---

## 6 — Tombstones · mourning as first-class

**Concept.** Append-only forbids deletion but permits appending the decision to forget:
tombstone `{release X, reason Y, date Z}`; raw history auditable; read-view honors
tombstones. Consequence: two personas on identical history with different tombstone sets
are different persons — identity-as-read-function (C1 §6a).

**Mapping.** Therapy ritual run in reverse: select what to set down. Mourning = dual of
therapy. Couples to the anchor test: release is *measured* drift made intentional.

**Prior art.** Mechanism is occupied — ADOPTED, CITED (D3 ruling, Gate-1 honesty):
Graphiti/Zep bi-temporal soft tombstones `[v]` · ESAA event-log + read-model projection
(arXiv:2606.23752) `[v]` · 2P-Set CRDT semantics (L2-T4) `[v]` · agentic unlearning
(arXiv:2602.17692) · SSGM (arXiv:2603.11768) `[v]` · event-sourcing precedents `[t]`.
CLAIMED: identity-as-read-function coupling · mourning as dual of therapy · the
D3-honesty coupling. · BORROWED (mechanism) + YOURS (doctrine) · mechanism BUILD-NOW,
read-view OPERATIONALIZE · `[v]`

**Production.** Graphiti/Zep implement the mechanism shape; the read-view function here
stays a plain filtered read (no graph DB — anti-pattern §9).

> **NOTES (majkee):**

---

## 7 — Well key-discipline contract + write regime

**Concept.** Key/ID uniqueness is one failure class, read-side and write-side (V3):
duplicate `#last-turn` anchors (live, X3) and duplicate sequential IDs (E2 incident) are
the same violation. Contract (gaveled Q8): **one live `#last-turn` per file · unified
demotion convention · sequential IDs read-before-append.** Write regime (gaveled Q5,
D4): named regime **"read-before-append + detect-not-prevent, under human-paced
writes"** — necessary but provably insufficient under concurrency (L2-T6 TOCTOU
trilemma: sequential-ID ∧ concurrent ∧ lock-free — pick two). Escalation trigger
explicit: if write concurrency becomes real → flock around read-check-append or
ID-derived-from-append.

**Mapping.** The grep-ladder wells *require* this contract; the live harness already
violates it benignly (epoch double-anchor — repair routed to owning seat, not this run).
Regime assumption visible, never silently trusted (L4 D-7).

**Prior art.** CoAgent (arXiv:2606.15376) · concurrency-anomaly verification
(arXiv:2606.17182) · ATM CID-brokered admission (arXiv:2607.00041) — all `[v]`;
lock-free plain-file sequential IDs: documented null — broker or optimistic repair are
the known solutions (L1-Q5). · REPURPOSED · BUILD-NOW · `[v]`

**Production.** flock(1) when the trigger fires; until then the named regime + E2-style
detection.

> **NOTES (majkee):**

---

## 8 — Operator in the tensor

**Concept.** The operator is a first-class node — subject AND contributor (PIN, gaveled
Q6). Every operator-written row is **role-typed: `contributor` vs `adjudicator`**
(L2 C-3); mixing lets a contribution masquerade as a ruling. Observation model: C-1 raw
stratum immutable, measurement = pure read-only projection · C-2 anchor test on the
operator with held-out earliest stratum · C-4 external cross-brand grader. Sovereignty
is typed — an untyped gavel is noise with authority (L4 D-6).

**Mapping.** Live evidence already exists: bed annotations `[majkee]`/`[eagle]` on
G-06…G-10 function as operator-observation rows; G-09 is the anchor test firing on the
operator in real time. SPECIAL PATH τ is the operator's own slope-retention format.
Named failure modes: **confirmation attractor** (the mirror sharpens bias into false
identity) · **measurement-display entanglement** (showing the metric changes the next
write).

**Prior art.** Operator-as-measured-node honesty constraints: unoccupied per this run's
search (Gate-1 claimed residue). Dual-persona / attractor literature adjacent
(arXiv:2607.02368 · arXiv:2606.30571) `[v]`. · YOURS · OPERATIONALIZE · `[v]`

**Production.** none; typing is one tag per row.

> **NOTES (majkee):**

---

## 9 — Source wells + anti-pattern

**Concept.** Seven wells, grep-navigable, no RAG: therapy `#last-turn`+footer ·
pulse.claude blocked-on-majkee · latest monkey memo (`punk:`) · majkee.news Watch+Fresh ·
decisions Still-open · pulse.atlas top · the stone itself. All reads are pure (V2: one
invariant — classify state before acting; immutable raw stratum; substrate layer
therapy.md + gavels.md never compressed — asserted as taste in C2, derived as the
confluence condition by L2 independently).

**Mapping.** Anti-pattern (do not build): one Socratic registry + one extendable context
tree = RAG-in-RAG collapse. Compression lives on the '42'/research side only.

**Prior art.** V2 doctrine-grade convergence (four independent appearances). · YOURS
(as discipline) · BUILD-NOW · `[v]`

**Production.** the harness itself — the wells already exist.

> **NOTES (majkee):**

---

## Triggers (Gate 3 — PASS-WITH-TRIGGERS, printed per gavel)

| # | Trigger | Fires when | Response |
|---|---------|-----------|----------|
| T1 | ~10K scale wall | corpus size × measured miss-rate climbs (D1) | reopen retrieval line knowingly (§4) |
| T2 | Write concurrency | more than human-paced writers on a well | flock or ID-from-append (§7) |
| T3 | O_APPEND atomicity | wells move to synced/NFS substrate | re-verify append guarantees (L2-T6 hole) |
| T4 | Mode-2 cost class | the "bottom" oracle becomes majkee-latency | re-derive Mode-2 economics (L2-T1/T2 hole) |

## Open on this card

- **Q7** design name — one line at G-C (provisional: *meditation room*).
- **L3** cross-vendor fold at P7 — two-stage; amendments documented in header.
- **R-1** format-taste experiment (README vs settings.json, blind) — post-run,
  research-pattern shape; no controlled eval exists (L1-Q7, still true post-X6).
- **Agol** cold-start budget call (Fable sunset) — parked, majkee.
- Track 2 feeder slice pinned in `leg-philosophy.result.2026-07-18.md` §F.

`— seat, 2026-07-19. Next: G-C — majkee reads, one taste line (Q7), one fidelity read; then shaped/.`
