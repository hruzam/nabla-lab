# design · edge-first session state — larva / muticula / ulx

_v0 · released 2026-09-29 · Phase B sketch — a proposal to argue with, not a decision. Lens: `thread.edge-space.2026-09-29.md`. Math: `thread.nabla-coin.2026-09-29.md`. Checked against `principles.md` (derived-is-disposable, one writer per file, tombstones, Last Standing Man) and the muticula restart rule (lightest form, grow only if needed)._

**Provenance** — same legend as the lens file: `[buffer]` Majkee × Nabla voice session, two-party · **(M)** Majkee's words · `[NABLA]` single-agent · `[NABLA · corrects]` · `[world ✓]` checked this session · `[world ~]` recall · `[OPEN]` · `[MEASURE]` a claim the logs must settle.

---

## 0 · On one screen

1. `[buffer]` **(M)** A boolean is fine for deterministic systems. Agent sessions are not: running / not running is the clean case, and the edge carries the weight. `[MEASURE]` — a hypothesis until counted (§4).
2. `[NABLA]` **Write evidence, not verdicts.** Running, wedged, orphaned are regions a reader carves at read time. A boolean written at write time is a projection taken too early; the edge dimension is gone for good. Not a new invariant — *derived-is-disposable*, applied to session state.
3. `[NABLA]` **A session on its edge is the worst witness of its own state.** The twins cannot answer about themselves; a crashed process cannot be told from a slow one from inside the protocol; Last Standing Man already says a degrading agent passes a pointer, not a verdict. Classification is external and read-only.
4. `[NABLA · corrects]` In voice I pitched `deform` and `stability` as operations of a new type. Sharper: `deform` lives in the **reader** (its thresholds); `stability` is a **table** on modes (does waiting resolve it?). No new algebra needed yet.
5. `[NABLA]` Lightest form first — one record format, one classifier script. A library only if the counts, and more than one consumer, ask for it.

---

## 1 · The edge modes
`[buffer]` — examples from the voice session, not measured frequencies.

| mode | what it looks like |
|---|---|
| Suspect | alive by some signals, silent by others; could go either way |
| Wedged | alive, holding something, making no progress |
| Exited | gone — possibly leaving a half-finished write on disk |
| Orphaned | a lock or claim whose holder no longer exists |
| Contended | two sessions each believe they hold the same thing (muticula's case) |
| Waiting-forever | blocked on a reply that will not come (reads as Suspect, then Wedged) |

`[NABLA]` In lens terms (lens §4): *Suspect* is the escaping edge — more than one future. *Wedged* and *Contended* are sliding — the session lives on the boundary under rules of its own. A clean state change is crossing.

---

## 2 · Prior art — distributed systems already live on the edge

- **Crashed vs slow is undecidable from inside.** In an asynchronous system you cannot tell a crashed process from a slow one; the FLP impossibility result (1985) rests on this `[world ~]`. The edge is structural, not a bug.
- **Failure detectors answer "suspect", not "dead".** Chandra & Toueg (1996): unreliable failure detectors output revisable suspicion, characterised by completeness and accuracy `[world ~]`.
- **φ accrual: suspicion as a number, thresholds as the reader's choice.** Hayashibara, Défago, Yared & Katayama (2004) replace the boolean with a continuous suspicion level, φ = −log₁₀(1 − F(time since last heartbeat)), where F is fitted to the history of heartbeat intervals; the consumer sets the threshold `[world ✓]`. Low thresholds catch crashes fast but raise more false suspicions; high thresholds err less and detect later `[world ✓]`. Implemented in Akka / Pekko and Hazelcast `[world ✓]`. Applications act differently at different levels — stop sending new work at mild suspicion, reassign it at stronger suspicion `[world ✓]`. **This is the edge-first state type, already in production.**
- **Leases and fencing.** Time-bounded locks (Gray & Cheriton 1989) turn "holder vanished" into an ordinary expiry; a monotonically increasing fencing token lets the resource refuse a holder that wakes up late (Kleppmann 2016) `[world ~]`. Directly muticula's territory.
- **Supervision.** Erlang/OTP's "let it crash" (Armstrong 2003) makes a crash an expected, supervised mode `[world ~]`.
- **Hysteresis.** Separate enter/leave thresholds stop a state from flapping across a boundary (circuit breakers, `study-two.technical.2026-07-13.md` §6) — the practical cure for sliding-mode chatter.
- **An inversion.** "Make illegal states unrepresentable" (Minsky) `[world ~]` — here, the states we treated as illegal are legal and common. Make them representable.

---

## 3 · The design — evidence in, verdicts out
`[NABLA]`

**Evidence log** — append-only text, one writer (the observer), no verdict fields:

```
2026-09-29T10:14:03Z  s=7f3a  layer=pty   sig=out_bytes    v=0     win=30s
2026-09-29T10:14:03Z  s=7f3a  layer=proc  sig=state        v=S
2026-09-29T10:14:03Z  s=7f3a  layer=hook  sig=tool_start   v=Bash  id=a91c
2026-09-29T10:14:05Z  s=7f3a  layer=git   sig=index_lock   v=held  age=41s
```

- The layers are the ones ulx already watches (kernel/proc, PTY, multiplexer, hooks), plus git for muticula. ulx stays read-only toward sessions; its own log is the one file it writes.
- A released lock is recorded as a tombstone line, never by deletion.

**Classifier** — a reader: derived, disposable, rebuildable (Python, larva's core language):

```python
from enum import Enum

class Mode(Enum):
    RUNNING = "running"; SUSPECT = "suspect"; WEDGED = "wedged"
    EXITED = "exited"; ORPHANED = "orphaned"; CONTENDED = "contended"

def classify(events, th) -> Mode:
    """Pure: same log slice + same thresholds -> same mode. Writes nothing back."""
    ...
```

- If modes are persisted, they go to a separate derived file — never into the evidence log.
- **`deform`, in practice:** the thresholds are the lens's aspect ratio. Raising `th.suspect` moves mass from Suspect to Running — fewer false alarms, slower detection. Nothing on disk changes; only the carving moves. That is the whole argument against writing verdicts: a log can be re-carved, a boolean cannot.
- Different readers carve the same log differently: a status line can be jumpy, a merge guard conservative. larva already has per-consumer cursors for *position*; this adds per-consumer thresholds for *meaning*.
- **Hysteresis:** two thresholds per boundary (enter Suspect at φ₁, leave at φ₀ < φ₁).

**Stability table** — the second operation, as a lookup. Hypotheses; the logs decide:

| mode | does waiting resolve it? | default action |
|---|---|---|
| Running | — | none |
| Suspect | usually (transient) | wait up to a bound, reclassify |
| Wedged | no | signal, then kill; release its holdings |
| Exited | — | reap; scan for half-writes |
| Orphaned | only if a lease expires | lease expiry; tombstone the lock |
| Contended | no | arbitration (muticula); fencing token |

The table answers the operator's only real question at the edge: **wait, or act?** In lens terms that is basin stability — does the state come back on its own?

---

## 4 · Build order — grow only on evidence
`[NABLA]`

0. ulx writes evidence lines for real sessions — already its job.
1. One script, `classify`: a pure function over the log and a thresholds file; prints modes. No daemon.
2. **Count.** Time-in-mode per session over a week of real work — an empirical basin stability. This is the test of **(M)**'s inversion. If Running dominates by far, the boolean was fine: stop here and keep the script.
3. Only if edge modes carry real weight: add the stability table and default actions; muticula consumes Orphaned and Contended.
4. Only if two or more consumers need the same carving: extract a small library. Precedent for an algebra built around its edge values: wheels (lens §3) — a reminder that the laws change, not just the values.

---

## 5 · Open
`[OPEN]`

- Is the C# session head — first in, holds observations through the task, last out — the natural carver for its own session, or does classification belong in a separate reader? (Tension with §0.3: the head is inside the session.)
- Which layer gives the earliest honest signal of Wedged: process state, PTY silence, or a hook that started and never ended?
- Contended: does muticula *prevent* it while this note *represents* it — or does muticula become one consumer of the log?
- May a session's self-report ever count as evidence? Last Standing Man says: as a pointer, never as a verdict.
- Learning the boundary from data — classifier uncertainty as an edge detector (arXiv:2608.14743) — probably overkill for a few scripts; kept as a pointer.

---

## References

Checked in this session `[world ✓]`:
- N. Hayashibara, X. Défago, R. Yared, T. Katayama, *The φ accrual failure detector*, JAIST research report IS-RR-2004-010 (2004); implementations: Akka / Pekko `PhiAccrualFailureDetector`, Hazelcast.
- *Generative learning of separatrices*, arXiv:2608.14743 (pointer only).
- Project file: `study-two.technical.2026-07-13.md` §6 (hysteresis, circuit breakers).

From recall, not re-fetched `[world ~]`: Fischer, Lynch & Paterson, JACM 1985 (FLP); Chandra & Toueg, JACM 1996; Gray & Cheriton, SOSP 1989 (leases); M. Kleppmann, *How to do distributed locking* (2016); J. Armstrong, PhD thesis (2003); Y. Minsky, "make illegal states unrepresentable".
