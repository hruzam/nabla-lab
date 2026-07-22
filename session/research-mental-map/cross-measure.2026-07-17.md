# Track 1 — cross-measure (P4, seat's own work)

`run: synthesis-run (Oraculum-shaped) · seat: Oraculum · date: 2026-07-17`
`amended: 2026-07-17 same-day — F-leg fold: V6 + Gate-1 revised (null overturned), V1 confirmed`
`status: PROVISIONAL — all verdicts pending-gavel (G-B) · derivation base for card (P6)`
`processed corpus: C1 · C2(+RAW) · E1 · E2 · E3 · bed sample (gavels.md G-01…G-11) ·`
`therapy #last-turn sample · L1 (leg-online.result.2026-07-17.md, incl. follow-up round 1) ·`
`L2 (leg-offline-math.result.2026-07-17.md)`
`outstanding: L3 only (cross-vendor, majkee relay — folds at P7)`

## Corrections registry

| # | Correction | Status |
|---|-----------|--------|
| X1 | Seat claimed `#last-turn` absent from live therapy files → FALSE; glob-scoped Grep (`*/therapy.md`) silently failed to traverse subdirs. Direct grep finds the tag across all seats. Retracted before artifact-entry. | closed |
| X2 | Seat claimed E3's G-09 wire missing from `houston/therapy.md` → FALSE; same tool artifact. Wire verified at line 163. | closed |
| X3 | Verified replacement finding: `epoch/therapy.md` carries TWO live `#last-turn` anchors (lines 57=arc 1, 170=arc 4; older never demoted). Cross-seat demotion conventions diverge (houston: `was #last-turn` · atlas: HTML-comment relocation · epoch: accumulation). | verified |
| X4 | Pulse line "oraculum seat dir absent/empty" is stale — `raw.therapy/oraculum/therapy.md` exists with read-protocol header. Pulse update queued for close (shared-state, ask-first). | queued |
| X5 | E1 blast counterfactual stays LOW confidence (unrun) — carried at stated weight, not inflated. | held |
| X6 | **F-leg overturned L1's broad Q4 null**: mode/strategy selection IS occupied under "query routing / adaptive RAG" terminology (RAGRouter-Bench arXiv:2602.00296 + 2604.03455 · Self-RAG 2310.11511 · TARG 2511.09803 · Adaptive Query Routing 2604.14222). V6 and Gate-1 amended same-day, before derivation. Unoccupied residue narrowed — see V6-rev. | closed |

## Convergences (independent agreement — strongest signal first)

**V1 · Anchor test is real, its metric is unoccupied (F-2 CONFIRMED), and its guard is external.**
C1 §6b (continuity ⊥ fidelity; consistent confabulator) × L1-Q3 ("Too Consistent to Detect":
all four detection methods fail on self-consistent errors; DRIFTLENS: reasoning drifts under
stable fluent surface; MIT 2026: cross-model disagreement beats self-consistency) × L2-T4
(D3 predict-your-own-earliest-stratum measures *honesty*, disjoint null-space from D1/D2;
self-reference hole closed only by held-out anchor + external grader) × L2-T5 (C-4: blind
cross-brand leg is load-bearing, not decoration) × AGENTS.md triangulation clause × live
harness (G-09: the anchor test fired on the operator, caught by majkee in real time).
**F-2 verification: null confirmed** — adjacent work (BeliefShift, E-mem, MEMPROBE) does not
retrodict the agent's own earliest stratum. Confidence M (unindexed preprints not excludable);
the card carries this hedge verbatim. Strongest claim of the run.

**V2 · One invariant, four appearances: classify state before acting; immutable raw stratum + pure downstream read.**
L2's cross-task synthesis (T3 classify-edges / T4 CRDT confluence / T5 C-1 / T6 read-classify-
before-write) × E1 (sufficiency-gated escalation GREEN — same invariant, behaviorally
validated) × E2 (its violation, self-diagnosed as "act before sufficiency-check") × C2
substrate layer ("therapy.md + gavels.md always substrate, never compressed" — asserted as
taste in C2, *derived* as the confluence condition by L2 independently). Doctrine-grade.

**V3 · Key/ID uniqueness is one failure class, read-side and write-side.**
E2 (write-side: duplicate G-06, TOCTOU per L2-T6 theorem) × X3 (read-side: duplicate
`#last-turn` anchor live in epoch seat) × L1-Q1 failure modes (silent staleness, keyword
clutter) × L1-Q5 (lock-free plain-file sequential IDs: documented null — broker or optimistic
repair are the known solutions). The grep-ladder well design *requires* a key-discipline
contract; the live harness already violates it benignly. Card must carry the contract.

**V4 · Mode 3's stated stop rule is a bug with a free fix; the fix territory is unoccupied.**
L2-T3 (theorem: exit-on-first-own-mark = cycle detection, false-closes whenever seed
girth-cycle ⊊ reachable set; exact fix free: marks classify edges, frontier-exhaustion
decides; O(1) open-edge counter) × L1-Q6 (novelty saturation / coverage stopping active
2026; "revisit detection" as named technique: null). The chalk marks survive; the stop
predicate changes. Subjective recognition gate ("hold full context in one view") stays as
the *experienced* signal, backed by the objective counter as ground truth.

**V5 · Grep-engine below the line is viable at lab scale, and the line is now exact.**
L2-T7 (boundary = dense *learned* embedding + ranking in that space; BM25/sparse-lexical =
grey zone *below* the line; relational join across wells = still grep-side; hidden learned
scorer = embedding in disguise) × L1-Q1 (practitioner consensus: BM25/grep >90% under ~1K
docs because writer and searcher share vocabulary; scale wall ~10K; memweave hybrid numbers)
× C2 anti-pattern (no RAG-in-RAG). R-3 answer lands; see D1 ruling for the residual tension.

**V6-rev · Mode-selection: field occupied, framing unoccupied.** (Amended per X6.)
Broad selection/routing IS an active formalized field (RAGRouter-Bench: per-query classifier,
macro-F1 0.928; Self-RAG reflection-token gates; TARG entropy thresholds; tier-based routing).
What remains unoccupied, per F-1 targeted probe (confidence H): **the tri-modal framing** —
deterministic key lookup / stochastic probing-with-informative-failure / exhaustive traversal
as named modes with an explicit selector — and L2-T2's (H,c,σ) axis-aligned decision tree as
its formalization. The card ADOPTS routing literature as adjacent plumbing (cite), CLAIMS only
the tri-modal frame + selector. L1-Q7 unchanged: no controlled format eval exists; R-1's
README-vs-settings.json test remains novel. "Testing proves it, not design" still derived
(thresholds empirical), now also consistent with how the routing field itself works
(learned/tuned classifiers, not designed constants).

**V7 · Q-E1 has a formal answer.**
L2-T1: Mode 2's native output is (state + slope trajectory τ) — a different type from a
ladder row; a row is its image under a lossy projection that discards τ. Two documents iff
rejections should compound; one document only by deliberate forgetting of slope. C2's own
"achievements populate Mode 1's right column" is the projection π, now formally named.

**V8 · R-2 resolves as trajectory retention at the human layer.** (Seat synthesis, this run.)
The SPECIAL PATH note is exactly τ-retention for a human writer: majkee's RAW already states
its format — "what you tried, what it returned, and the fork that opens from it." Raw,
unprocessed, no filler when motivation is absent (C2). One concept covers Q-E1 and R-2:
keep the slope. Pending-gavel as the card's SPECIAL PATH format.

## Divergences + rulings

**D1 · Hybrid-retrieval numbers vs the no-RAG doctrine.**
L1's memweave data (89% hybrid > 68% BM25) argues embeddings buy recall; L2-T7 puts dense
embeddings across the line; C2 forbids. RULING: no contradiction — different envelopes.
At lab scale (≪1K rows, shared writer/searcher vocabulary) the semantic gap "barely exists"
(L1). Stay below the line; **instrument the miss-rate**. The reopening trigger is measured,
not doctrinal: sustained semantic-gap misses or approach to the ~10K wall. This also names
the parked "'42' trigger condition": corpus size × retrieval miss-rate, both measurable.

**D2 · "Agentic taste" vs the hidden-embedding warning.**
L2-T7: a learned scorer implementing taste is a φ in disguise — crosses the line with no
vector DB in sight. RULING: taste lives in the agent (in-context judgment at read time),
never as a trained ranker over the store. Doctrine line for the card. Note post-X6: the
routing field's learned classifiers (RAGRouter-Bench's TF-IDF+SVM) sit exactly on this
line — adopting their *framing* is safe; adopting their *learned selector* would cross D2.

**D3 · Tombstones: novel or reinvented?** (Gate 1 honesty.)
L1-Q2: mechanism prior art is real — Graphiti bi-temporal soft tombstones, ESAA event-log +
read-model projection, 2P-Set CRDT semantics (L2-T4). RULING: the *mechanism* is adopted
with citations, not claimed. What remains novel: identity-as-read-function coupling
(two personas, same log, different tombstone sets), mourning as first-class dual of therapy,
and the D3-honesty coupling. Claim the doctrine, cite the plumbing.

**D4 · E2's rule is necessary but not sufficient.**
E2 self-prescribes read-before-append; L2-T6 proves it fails under concurrency (TOCTOU;
trilemma: sequential-ID ∧ concurrent ∧ lock-free — pick two); L1-Q5 confirms no known
lock-free plain-file discipline. RULING: adopt the *named regime* "read-before-append +
detect-not-prevent under human-paced writes" (this is what actually caught E2), with an
explicit escalation trigger: if write concurrency becomes real → flock around R;C;A or
ID-derived-from-append. Regime assumption made visible, not silently trusted.

## Reality-gate provisional verdicts (pending G-B)

| Gate | Verdict | Basis |
|------|---------|-------|
| 1 Reinventing wheel | PARTIAL-ADOPT | Occupied → adopt + cite: file-native memory, tombstones, event-sourcing, drift measurement, **query/strategy routing (X6)**. Unoccupied → claim: tri-modal framing + (H,c,σ) selector (F-1 residue, conf H) · anchor-reconstruction D3 (F-2 confirmed, conf M) · operator-as-node honesty constraints · chalk-mark→frontier refinement · R-1 format eval. |
| 2 Theatre | PASS-WITH-FIX | Every metaphor has a formal core (L2 T1–T7); the one unmoored piece was Mode 3's stop rule — fixed exactly (V4). Metaphor layer stays as framing per manifest. |
| 3 Technical wall | PASS-WITH-TRIGGERS | No wall at lab scale. Named triggers: ~10K scale wall (V5/D1) · write-concurrency regime (D4) · O_APPEND atomicity breaks on synced/NFS substrates (L2-T6 hole) · Mode-2 cost class changes if the "bottom" oracle is majkee-latency (L2-T1/T2 hole). |

## Operator-in-tensor (PIN) — provisional model

Q-E2 answer: majkee writes rows directly, **role-typed** — every operator event tagged
`contributor` vs `adjudicator` (L2-C-3); mixing lets a contribution masquerade as a ruling.
Observation model for the card: C-1 raw stratum immutable, measurement = pure read-only
projection · C-2 anchor test on the operator with held-out earliest stratum · C-4 external
cross-brand grader (the L3 leg + triangulation roster ARE this guard). Live evidence: bed
annotations `[majkee]`/`[eagle]` on G-06…G-10 already function as operator-observation rows;
G-09 is the anchor test firing on the operator in real time. Failure modes to name in the
card: confirmation attractor (mirror sharpens bias into false identity) · measurement-display
entanglement (showing the metric changes the next write).

## Naming (Q-E3) — evidence in, taste out

L1-Q8: all three candidates unoccupied. SML carries oral-collision risk with SLM (dominant
adjacent term). "Meditation room" and "SUPER-README" clean. Team tip (tip only, majkee's
gavel): the formalization favors *meditation room* — the modes are literally techniques
practiced in one place (dive, grep, gravity), and C1's meditation core is the instrument's
actual foundation stone. Decision is taste → majkee.

## Consolidated gavel queue — G-B slice

| # | Item | Class |
|---|------|-------|
| Q1 | Gate verdicts as tabled above (PARTIAL-ADOPT incl. X6 amendment / PASS-WITH-FIX / PASS-WITH-TRIGGERS) | technical (delegable, Janus counter-sign) |
| Q2 | Mode-3 stop-rule correction into card: marks classify, frontier decides; open-edge counter behind the recognition gate | technical (delegable) |
| Q3 | Q-E1 + R-2 ruling: two structures (ladder + trajectory log), π on settle; SPECIAL PATH note = human-layer τ ("tried / returned / fork opened") — recommend retain-τ | taste-adjacent → majkee |
| Q4 | R-3 ruling: '42' ceiling = exact/regex/relational-join + optional sparse-lexical ranking; never dense-learned φ; trigger condition = measured miss-rate/scale | technical + taste edge |
| Q5 | E2 invariant upgrade: named regime "read-before-append + detect-not-prevent, human-paced" + escalation trigger (D4) | technical (delegable) |
| Q6 | Operator-in-tensor model as above (role-typed events; C-1…C-4; D3-on-operator with held-out anchor + cross-brand grader) | ownership/doctrine → majkee |
| Q7 | Naming: majkee's gavel; evidence says all clean, SML oral-risk, seat tip = meditation room | taste → majkee |
| Q8 | Key-discipline contract for wells (from V3/X3): one live `#last-turn` per file, demotion convention unified; routing of the epoch duplicate-anchor repair → owning seat, not this run | technical + housekeeping |
| Q9 | Pulse staleness (X4) — update at close | housekeeping |
| Q10 | Carried from manifest: Agol cold-start budget call (Fable sunset) · both still parked | carried |

## Seam note

The shared meta-question with Track 3 ("what substrate operations help an agent think")
received independent convergent input here (V2's invariant, V4's stop-rule shape). Per
manifest: convergence is signal, not waste — final synthesis reads this seam first.
Track 2 feeder (per PIN): surviving L4 output + V5/D1/D2 boundary rulings.

`— seat, 2026-07-17. Next: G-B gavel → P5 (L4 philosophy leg, seat) → P6 card → G-C.`
