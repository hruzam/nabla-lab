# Publication generation and checks

These durable tools preserve the formulas, construction checks and reading-copy
style from Oraculum's 2026-10-27 scripts, previously held only in `/tmp`. Paths now
resolve from this publication directory; `--root` selects a scratch publication copy.
They support these eleven editions, not arbitrary future figures or research claims.

From the lab root, check the current files without changing the historical receipt:

```sh
python3 publications/inner-circle/tools/verify.py --output /tmp/nabla-study-check.json
```

Without `--output`, verification prints its new receipt and writes nothing. It checks
the existing equations/examples, source hashes, local Markdown links and asset
structure. It performs no literature, empirical, visual/browser or model-runtime
verification. The original publication `verification.json` remains a dated record.
This checker uses only the Python standard library.

Render only an intentionally changed study:

```sh
python3 publications/inner-circle/tools/render.py --study jev-judgment
```

Repeat `--study` for several named studies. `--all` explicitly rebuilds all study and
index reading copies; neither is selected by default. Rendering requires Python
Markdown and ReportLab (locally exercised: 3.10.3 and 5.0.1). Existing SVG/CSV/HTML
bytes are kept when identical. A PDF is retained when its SVG and CSV are unchanged;
after a drawing/style change, inspect the regenerated PDF. This preserves metadata
without claiming that CSV alone proves layout or every dependency is unchanged.
For a deliberately forced PDF refresh, work in a scratch copy with that PDF absent.

For preview builds, pass `--root` pointing to the copied publication directory.
The verifier also needs the original paths named in the coverage ledger and the
project Oraculum addendum under the corresponding scratch lab root. Review output
before searching it or adopting it; dependent steps run sequentially. Preserve the
study's edition/provenance labels unless the editorial assignment changes them.

Record the command, input/source revision, actual outcome and output location in the
assigned task evidence. New studies require explicit generator/check coverage; a
green check for these constructions is not a scientific completeness certificate.
