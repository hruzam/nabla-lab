# Card amendment A1 — § Composer (write-side architecture)

`amends: card.mental-map.DRAFT.2026-07-19.md · per header amendment slot`
`provenance: gavel session 2026-07-24/25 (Oraculum seat, majkee in-chat) — flag locks 22–24`
`merge: fold into card body at shaped/ crossing or next desktop pass; until then this file travels with the card`

## § Composer — the write-side half of the instrument

**Concept.** The room's readability is manufactured on the write side. Composer =
mount-string substrate + attach-drill-release workers + cron cadence:

- **Mount-string substrate** — entries carry designed, grep-stable markers (tags, IDs,
  τ-lines, section anchors). Format conventions ARE the engineering surface; the
  mount-string standard is decided by **R-1** (format-taste experiment — hereby promoted
  from post-run curiosity to **composer-critical path**).
- **Attach-drill-release** — composition is not one mind milling everything: a drill
  worker greps a mount string, attaches, deep-reads only that neighborhood, releases a
  distilled stratum, detaches. **Releases append new strata, never mutate the source**
  (identity = file lineage; compression between lives, not overwriting of lives).
  Repair path = re-drill; bad composition is recoverable, never fatal.
- **Grid version** — mount points are independent → embarrassingly parallel drill
  sweeps. Grid release is the named T2 concurrency case: engage flock or
  ID-from-append around release before any parallel run.

**Hybrid split (gaveled).** Two composition classes:
- **Class M — mechanical** (mapping strata, cross-well joins, index/freshness sweeps,
  dedup): may run on cheap cross-brand drills (Gemini candidate; Codex CLI rider —
  tasked-from-Claude posture). Condition: **extractive-first briefs + mount-string
  format cage** — protects writer/searcher vocabulary coherence, which is the entire
  basis of grep viability (>90% under ~1K rests on shared vocabulary).
- **Class I — identity-bearing** (therapy residue, gavel distillation, session-close
  compression): composes **in-family, in-seat, always**. The write licenses release —
  this composition is the agent's own meditation; foreign compression choices do not
  enter the lineage the read function is identity over.

**Cadence (gaveled).** Two-stage cron — the stone's daemon+model composite made literal:
1. **Detector cron** — deterministic script, buildable anytime, no posture conflict:
   sweeps the wall, inventories mount points, measures composition backlog +
   vocabulary drift + retrieval miss-rate (D1 day-one instrumentation). Emits a work
   manifest — notification, not payload. **This is the sensor that produces
   "recognized special need" evidence for both the engine (T1) and the composer seat.**
2. **Drill-firing cron** — unattended mind-spawning = always-on posture → held under
   flag **lock 12 DEFER**. Until revisit: cron prepares the queue, an attended session
   releases the drills.

**Mapping.** Composer-as-discipline is live now (therapy loops, gavel collection,
session-close distillation). Composer-as-seat is **parked until recognized special
need** — same recognition rule as the engine (lock 22 pattern), its **own signal**:
composition backlog / vocabulary drift between wells (NOT miss-rate — that is the
engine's signal). Every unit of composition quality is engine-need removed; the two
components are inversely coupled.

**Prior art.** Stone §4 (daemon+model composite, low-duty-cycle router, unspawned
expensive minds) — the cadence architecture pre-existed in the corpus · online-leg edge
result ("meditation cron job", practitioner pattern, conf L) · memweave
vocabulary-coherence rationale (D1) · YOURS on the mount-string/attach-drill-release
assembly · `[t]` this amendment, gavel-derived, not leg-derived — L3 fold may touch it.

**Production.** Detector cron: plain script (ripgrep + wc + diff-based drift check),
crontab entry — no agent runtime. Drills: cheap-tier API calls, format-caged prompts,
extractive-first. Grid: flock(1) around append, or ID-derived-from-append.

**Trigger table addition (extends card T1–T4):**

| # | Trigger | Fires when | Response |
|---|---------|-----------|----------|
| T5 | Composer-seat need | detector cron shows sustained composition backlog / inter-well vocabulary drift | recognition event (majkee or seat + counter-sign per lock 9) → assemble drills, Class split enforced |
| T6 | Drill-cron posture | lock 12 DEFER revisited with smoke data + policy watch | unattended drill-firing may enable; until then attended release only |

> **NOTES (majkee):**
