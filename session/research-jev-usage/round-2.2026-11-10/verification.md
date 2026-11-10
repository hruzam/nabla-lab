# Round 2 verification and limits

**2026-11-10 · research evidence.** Main wrote the assigned research documents and a small scientific calculation reproducer. No application implementation or code review, installation, paid inference, model training, remote-host operation or Git publication occurred.

## Executed observations and calculations

- Read-only office probe: [timestamped JSON](office-observation.json), captured 07:54:52 UTC. About 15.38 GiB total / 1.345 GiB available RAM, no swap; Python 3.14.7 and listed packages absent from that interpreter. No benchmark or home probe. Earlier same-sitting snapshot had about 1.337 GiB available.
- `python session/research-jev-usage/round-2.2026-11-10/scientific-checks.py`: completed with PASS. [Receipt](scientific-receipt.json) includes the reproducer SHA256 and timestamp.
- Exact full-matrix tiny-network arithmetic: 256 binary vectors, zero mismatches; 161 parameters / 644 float32 payload bytes. No learning or cache workload run.
- Exact rational tent-map calculations: 5,160 expression-parity cases; 2,046 predicted branch endpoint/midpoint/slope checks through depth 10; 518 dyadic input cases through denominator exponent 8, all reaching zero within exponent+1 steps; 129 contraction-bound checks.
- Decimal union/rounding arithmetic and the one-sided 59-positive binomial illustration reproduced. Conditional event-matching and independence assumptions remain in the protocol.
- Existing private provider request/response SHA256 values independently recomputed and matched the brief. No transcript bodies or credentials copied into this directory.
- Closing artifact checks: 56 local Markdown links resolved; all three JSON receipts/manifests parsed; calculation-source hash matched; Jev-01 handoff body and declared hash matched the canonical protocol. `git diff --check` passed for tracked edits. The exact ia-sync presence record used for the handoff was detached successfully.

## Review and corrections

The position-aware `/root/jev_challenge` review identified four specification gaps: the paired fixture count versus unknown diagnostics; mixed-status group gold/three-valued unknown propagation; group forecasts incorrectly described as atom-weighted scores; necessary coherence screens versus global joint feasibility. Main corrected all four. The helper reread the changed passages and returned **PROCEED, no remaining material blocker**, explicitly bounded to research design, with fixture texts and independent labels still future work. Main inspected the changed passages before integration.

Two implementation-boundary clarifications were also incorporated: the exact tiny network uses a hidden ReLU and **linear output**, and authoritative invalidation/version signals must be permitted, costed runtime inputs rather than free oracle information. Mathematical review found no blocker in the stated arithmetic/constructions. Same-provider review does not satisfy a cross-vendor or named Janus gate.

## Source verification

[Source manifest](source-manifest.json) records twelve local source byte identities. A hash establishes identity, not reading depth; the README records which reader covered each source. Current TypeSafe customization and pinned Laya training capability were checked against primary documentation. Calibration papers, neural depth and spatial-ordering references were checked at their linked primary sources. No upstream performance claim was reproduced or used as a local benchmark.

The primary literature supports established mechanisms and distinctions. The proposed fixtures, outcome ladder, observation-sufficiency framing and experiment order are this round's synthesis. No originality, publication promotion or theorem novelty is claimed.

## Remaining work, deliberately unexecuted

| Work | Present state / next natural owner |
|---|---|
| Exact calibration fixture texts and independent annotation | Protocol ready; Jev builder/evaluation owner implements after assignment |
| Paid Jev evaluation, calibration fitting and utility trial | Not authorized/executed by this round; existing single-use grant consumed |
| Observer and cache full sequential replay | Implementation contract prepared; downstream implementer owns execution |
| Local model installation/inference/training | Candidate path only; host budget, environment and labels must be measured first |
| Home's actual capacity/environment | Stale guide only; measure locally there under a separate execution assignment |
| New cross-vendor evidence and formal promotion | Not exercised; existing lab gates retain authority |
| Wider private-vault stratification | Optional branch offered by majkee; not needed for this four-document intake |
| Successor CACHE collector | Option A selected; no collector/card fork; established reading chain updated |

At the time this research snapshot was written, the lab already had uncommitted November 5 changes in `implementer-brief.md` and `.html`; this round preserved them. The research outputs and those brief edits were then still local and uncommitted. In a subsequent scoped Git release on 2026-11-10, the lab materials and dated Jev-01 `raw/` handoff were committed and pushed to their existing branches. That transport records publication state only: it does not change the research status, clear the lab promotion gates, or alter Jev-01 tasks or STATUS. The central successor card records the resulting lab and ia-sync commit IDs.

## Subsequent November 10 local-model and successor follow-up

Majkee clarified that accessible local weights are the motivation for Laya and requested supported alternatives plus a cold-start card. Added [local-model-candidates.md](local-model-candidates.md), using a bounded Terra primary-source comparison and main checks of decisive model/runtime documentation. No new computation benchmark or installation accompanied that shortlist.

Created the requested central card through the cold-start-card skill; the earlier multi-reader closure card remains unchanged. The bonded context capture was run, HEAD/branch/upstream and the vault mapping were independently checked, and ignored mail omitted by the capture was explicitly recorded. YAML parsed with the shared keys in order; all ten source pointers plus root and rollout existed; nineteen local links in the updated entrance and candidate note resolved. At the time of that bonded capture, the card and new research files were local/uncommitted; no successor runtime smoke test is claimed. The subsequent scoped release publishes the research files and card through their owning repositories. This explicit follow-up supersedes the earlier decision not to create a card; option A still means no CACHE/transcript-collector fork.
