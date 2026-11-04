# Verification and closure receipt

**2026-11-03 · internal research edition.**

## Scientific review

- `/root/jev_math`, requested Sol/high: fully read both Coin drafts and four related studies; supplied proofs, counterexamples, prior-art qualification and finite checks. Decisive calculations and sources were checked by the main. [Correction register](corrections.md).
- `/root/jev_sources`, requested Terra/high: neutral primary-source pass, then deeper selected-passage checks on both Jev evaluation papers. A later position-aware source gate passed with version/Box and wording-dependence clarifications, both incorporated.
- `/root/jev_challenge`, requested default/gpt-6.1-sol/high: independent position-aware full read of all four new manuscripts; verdict **PROCEED**. Principal risk was confounding decomposition and rejection. Its three changes (factorial comparisons, unidentified-probability controls and constraint-aware pivotality) were applied. Bounded reread confirmed PROCEED with no unresolved material correction. This is an internal challenge, not the named Janus gate or a cross-vendor leg.
- The challenger independently reports zero discrepancies across 2,466 partial assignments of AND2, OR3, majority7 and nonweighted5. The main's separately reproduced, durably recorded checks below have the narrower explicit counts; do not merge these into an inflated independent sample.

## Reproducible construction

Command, from the repository root:

```sh
python3 session/research-jev-usage/build-artifacts.py
python3 session/research-jev-usage/check-artifacts.py
git diff --check
```

The [scientific construction script](build-artifacts.py) uses Python standard-library enumeration and ReportLab figures, plus Python Markdown for reading copies. It is offline research/document tooling, not a Jev implementation. The existing eleven-study generator and its historical receipt are unchanged. It renders only four new reading copies and the reading index. [Machine receipt](construction-checks.json) contains original-input hashes and figure hashes.

Observed checks:

- All 243 partial assignments of `(x1 AND x2) OR (x3 AND x4)` with dummy x5; 1,024 completion occurrences; **zero endpoint or existential-pivot discrepancies**.
- Result counts: 75 TAIL, 51 FACE, 117 GROUP_EDGE. Pivot-count histogram: 0→126, 1→60, 2→42, 3→12, 4→3.
- All 280 majority-seven configurations with exactly four unresolved elements have both possible results and four potential pivots.
- The one-sided independent-binomial zero-of-50 upper bound is 0.058155079116972264; not used as a clustered-study guarantee.
- Source hashes are unchanged during generation. Git's tracked changes are confined to the publication entrance; new research files live only in the approved homes. The pre-existing untracked `drafts/jev/` remains an input.

These are finite construction checks and a separately stated proof. They are not measured Jev accuracy, calibration or experiment results.

## Figures and reading copies

Two figures have SVG/PDF/CSV artifacts: rotation is an analytic observation model; completions is a finite synthetic enumeration. PDF previews were generated with:

```sh
pdftoppm -scale-to 1100 -singlefile -png publications/inner-circle/jev-usage/figures/rotation.pdf /tmp/jev-rotation-preview
pdftoppm -scale-to 1100 -singlefile -png publications/inner-circle/jev-usage/figures/completions.pdf /tmp/jev-completions-preview
```

Both previews were visually inspected: labels, points and counts are readable and consistent with the manuscript. HTML embeds the figures and existing publication styling; no external scripts or fonts are required. Link and final-diff checks are recorded in [artifact-checks.json](artifact-checks.json). HTML structure/link checks do not claim a full browser interaction test.

## Scope disposition

**Complete:** declared-corpus usage map (U01–U23), current primary-source refresh, mathematical audit, explicit rotating-ball candidate, E0–E6 experiment designs, implementer brief, internal reading copies, figure construction and internal challenge.

**Open by design:** live Jev usefulness/calibration/cost, empirical orientation benefit, richer-state identifiability beyond the demonstrated single-observation impossibility, majkee's intended rotating-ball construction, dataset and paid-run choices. The two external substrate studies, historical gavels, named Janus and genuine cross-vendor work were not assigned or exercised. This publication does not convert those into completed work or block on their completion.

No implementation was released, no source draft was promoted, no session pulse or flag was written, and no mail, commit, push or external publication was performed.
