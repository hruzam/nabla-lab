# triangulation roster — template proposal (Oraculum's Y on majkee's X, 2026-07-08)

`DELIVERY TARGET: temple level (reposoma) — this is federation-scoped, not lab-scoped; majkee`
`places + Atlas canonizes the final location/name. Below: the template itself + design rationale.`

---

## The template (proposed file: `reposoma/triangle.md` or similar)

```markdown
---
what: who is available TODAY for blind triangulation, by capability
updated: <date>                    # staleness is the #1 failure mode — see rationale R1
side-orchestrator: majkee          # provides blind legs from standard UIs when CLI legs are down
blind-protocol: nabla-lab flag lock 6   # one researcher sees all forks; legs blind until cross-measure
optimal-scheme:                    # the CURRENT best trio/quad — evidence-based, see notes below
  depth-research: epoch            # brand: anthropic
  heterogeneity-leg: gemini-cli    # brand: google — cross-brand REQUIRED for full blindness
  math-verify: color               # brand: anthropic
  fallback-heterogeneity: majkee-ui-gemini   # side-orchestrator path
seats:
  - seat: epoch
    brand: anthropic
    surface: CLI global
    for: [prior-art, policy-verification, date-calibrated research]
    status: available
    verified: <date>
  - seat: gemini-cli
    brand: google
    surface: CLI (bluebottle.zsh / reconstructed agents)
    for: [heterogeneity-leg, second-opinion research]
    status: <available|degraded|down>
    verified: <date>
  - seat: cursor-agent
    brand: cursor
    surface: CLI (`! agent`)
    for: [code-review leg, implementation second-opinion]
    status: expected
    verified: <date>
  - seat: majkee-ui
    brand: any (human-mediated)
    surface: standard web UIs
    for: [blind triangulation when CLI legs down, taste checks]
    status: available-when-present
    verified: <date>
---

# experience notes (append-only, dated — the evidence behind optimal-scheme)

- <date> · <run> · <leg>: <what happened — quality, degradation, brief friction>
```

---

## Design rationale — the Y itself

**R1 — staleness field is mandatory.** "Available TODAY" decays by definition. Every seat carries
`verified: <date>`; consumers treat entries older than ~7 days as `[t]`-grade leads, not facts —
same freshness discipline the lab already uses for prior art. An availability file that silently
rots is worse than none: it manufactures false confidence in a blind protocol.

**R2 — capability axis, brand as attribute.** Seats are listed by *role* (depth / heterogeneity /
math / code-review), with brand as a field. The optimal scheme then survives brand churn
(portability law) — when Gemini degrades, the heterogeneity SLOT persists and refills.

**R3 — cross-brand is what makes blind actually blind.** Same-brand triangulation shares training
priors; three Anthropic legs can converge on the same wrong answer with high mutual confidence
(majkees addendum point 1 — correct, and evidenced: this is *why* lock 6 wanted the Gemini leg).
The heterogeneity slot should never be filled by the same brand as the depth slot.

**R4 — evidence-based scheme, not aspirational.** The Atlas №2 run recorded a *degraded* Gemini
leg. The notes section exists so `optimal-scheme` is derived from logged leg quality, not hope.
Scheme changes when notes justify it — and the change is visible in git history.

**R5 — the side-orchestrator is a first-class seat.** majkee running blind legs from standard UIs
is not a fallback hack — it is the only leg that survives ALL CLI outages and all vendor policy
shifts. It costs his attention (the scarcest resource), so the scheme uses it last, but it is
listed, versioned, and briefed with the same neutral-brief discipline as any agent leg.
