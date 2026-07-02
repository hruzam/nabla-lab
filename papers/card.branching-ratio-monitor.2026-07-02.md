# Instrument card — Branching-Ratio Monitor (context-pollution alarm)

`shaped: 2026-07-02 · revised same day per @Janus gate (REVISE-LIGHT accepted: the two ρ's split explicitly)`
`derived from: WHOLE Atlas №1 (I.7, I.1 bridge, health scalar) + processed №2 (no №2 dependency) per flag lock 3`
`destination: subai.devenv (bus side) · status: BUILD-NOW (ρ_br monitor) · OPERATIONALIZE (ρ_op companion read)`

## Concept — two ρ's, not one (the earlier card conflated them)

Associative activation on the bus is a branching process; whether a cascade dies or explodes is governed by criticality. Two **distinct estimators** of it:

- **ρ_op — operator estimate:** spectral radius of the excitation kernel W (the bus graph's structural propagation operator). Computed directly from the graph; theory-side link to I.1 and to Hopfield≡attention (Ramsauer et al., arXiv:2008.02217 — **upgraded `[t]`→`[v]` this run**).
- **ρ_br — behavioral estimate:** the branching parameter estimated from **observed cascade size distributions** (Wilting–Priesemann multistep regression — robust under subsampling, which is the bus case: not every influence is an explicit reply).

**These coincide only under mean-field/homogeneous-mixing assumptions the bus will not satisfy** (hubs, sessions, heterogeneous agents). That is not a defect — **their divergence is itself a diagnostic**: ρ_br ≫ ρ_op means cascades run hotter than structure predicts (content-driven amplification); ρ_op ≫ ρ_br means structural risk not yet expressed. The monitor ships ρ_br; ρ_op arrives as a scalar read from the spectral brick when exposed (it fits subai's locked brick shape exactly: out-of-process, scalar return).

Regimes (for ρ_br, the shipped alarm): `<1` subcritical (sluggish recall) · `≈1` critical, edge-of-chaos optimum · `>1` supercritical = **context pollution, measured**.

## Mapping

- Bus health alarm on ρ_br over cascade records; cascade graph = the **L0 structural layer** of the spectral core's edge stack (explicit reply/session/citation edges) — defined there, consumed here.
- Feeds the Atlas №1 health scalar (`branching_ratio ρ` argument) — report ρ_br, annotate with ρ_op divergence when available.
- Actuation hook: sustained `ρ_br>1` → orchestrator tightens summarizer/rate-limit (the R element of I.6) — alarm and actuator in one frame.

## Prior art

- Criticality/branching-at-unity: Beggs & Plenz 2003; Bertschinger & Natschläger 2004 — branching parameter near 1 optimizes information transmission while preventing runaway. `BORROWED` `[v]`
- Estimation under subsampling: Wilting & Priesemann (MR. Estimator) — the exact tool for partially observed cascades. `[v]`
- ρ as an *LLM context-pollution alarm*: `OPEN` application — no agent product monitors it (Atlas №1 Part IV).

## Production

`MR. Estimator` (Python) off the shelf for ρ_br; input = per-cascade size counts from bus JSONL over L0 edges. Minimal build: cascade extractor + estimator + banded alarm + journal line. **Calibration discipline (the card's null):** the cascade definition (edge types, time window) is a modeling choice — validate bands against known-bad sessions (recorded runaway tangents) before trusting thresholds; log the ρ_br/ρ_op pair once both exist and treat persistent divergence as a first-class finding.

> **NOTES (majkee):**
>
