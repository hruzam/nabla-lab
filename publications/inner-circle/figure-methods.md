# Figure methods and numerical checks

**2026-10-27 · analytic illustrations and constructed examples only**

All eleven figures were produced with ReportLab's vector drawing/chart tools. SVG is used in the Markdown reading copies and embedded inline in the HTML. A matching PDF and CSV are supplied beside each SVG. No figure uses an agent transcript, a fitted parameter or a measured performance result. The formulas below and the CSVs are the reproducibility record; no external service is required to view the HTML.

| Study / file stem | Construction | Domain and interpretation |
|---|---|---|
| `stance-geometry/figures/flow` | `δ(t)=2 atan[tan(δ₀/2) exp(−2t)]`; exact antipode held at 180° | t=0…3, step 0.02; δ₀=120°,170°,180°; degrees displayed |
| `stance-geometry/figures/fisher` | `2 acos[√(0.5q)+√(0.5(1−q))]` | q=0…1, step 0.005; binary distance from (0.5,0.5); boundary limits included |
| `spectral-retrieval/figures/filters` | `exp(−tλ)` and `(1−α)/(1−α+αλ)` | λ=0…2, step 0.01; α=0.85, t=α/(1−α); matched mean walk length |
| `coalition-evidence/figures/coalitions` | `½1[{1,2}⊆A]+½1[{3,4}⊆A]` versus `|A|/4` | All 16 subsets of four voters; sorted by size and lexicographic membership |
| `cascade-diagnostics/figures/transient` | `0.6^t+0.7t·0.6^(t−1)` for t≥1, initial total 1 | Generations 0…15; comparator 0.6^t; expected counts, not random realizations |
| `tensor-analytics/figures/factors` | `exp[−(t−0.30)²/0.02]`, `exp[−(t−0.75)²/0.02]` | t=0…1, step 0.01; prescribed generating profiles, not recovered factors |
| `flow-control-stopping/figures/sampling` | `exp(−kh)`, `|1−kh|`, and boundary 1 | kh=0…4, step 0.01; exact sampling versus Euler pole magnitude |
| `coherence-composition/figures/cycle` | `s²/3` | s=−2…2, step 0.01; minimum squared discrepancy of the stated three-cycle |
| `mental-map/figures/coverage` | Visited fractions `[1/3,2/3,2/3,2/3]` vs `[1/3,2/3,2/3,1]` | Processing steps 0…3; graph s→a→s with branch s→b; halted curve held fixed |
| `scratch-instruments/figures/budget` | `1−exp(−b)−a·b` for a=0.2,1,1.2 | b=0…4, step 0.01; dimensionless illustration; boundary/interior optima |
| `interactive-interposition/figures/completion` | `1[t≥2]+1[t≥3]` and `2·1[t≥3]` | t=0…4, step 0.01; available observations vs acceptance signal scaled to 2; synthetic timeline |

## What can be checked independently

- The stance solution starts at its declared angle and decreases for initial separations strictly between zero and π; the exact antipode remains fixed under the chosen law.
- The binary Fisher curve is symmetric under q↔1−q, zero at q=0.5 and π/2 at either boundary. The separate worked example p=(0.9,0.1), q=(0.1,0.9) gives 1.8545904360032246.
- Both spectral filters equal one at λ=0. At the matched mean, PageRank's response is `1/(1+tλ)` and is at least the heat response for λ≥0.
- The complete-pair capacity is normalized and monotone on all subsets. Each exact Shapley value is 0.25; equal-size coalition values still differ.
- Matrix iteration of the stated K reproduces the transient formula, starting with totals 1, 1.3, 1.2 and 0.972.
- The prescribed tensor profiles attain one at their respective centers. No fit or rank-recovery result is inferred from plotting them.
- The Euler pole has magnitude one at kh=0 and kh=2, and exceeds one beyond two. The exact pole lies strictly below one for positive kh.
- The cycle example's residual is (−1/3,−1/3,−1/3), with squared norm 1/3; the plotted parabola is nonnegative and zero at zero circulation.
- The graph revisit leaves coverage at 2/3; the exhausted traversal reaches 1 on the specified graph.
- The budget model's interior maximum for a=0.2 lies at log(5); for a≥1 its maximum is at zero.
- At time 2 only one completion observation exists; acceptance is zero until both are available at time 3. The drawn segments interpolate the sampled step signals; no continuous rise is intended.

Numerical checks validate the displayed constructions and data transcription. They do not validate semantic stance measurements, causal influence, archive factorization, retrieval benefit or a safe stopping policy.
