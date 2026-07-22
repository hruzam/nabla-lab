# L2 — offline-formal (@Color) · forced compression via hard token budget B

`run: Track 3 synthesis · leg L2 (sealed offline) · 2026-07-18 · first-principles, no web/repo`

VERDICT (headline): **conditionally-sound.** The mechanism formalizes cleanly, but the
inverted-U — the whole reason to bother — does **not** follow from compression theory alone.
It requires one extra, empirically-checkable assumption about how the downstream generator
uses the scratch. Name that assumption or the mechanism collapses to "just prompt better."

---

## Assumptions

Objects and types, stated so the derivation is falsifiable.

- **Idea** `X` — the latent content the writer holds (voice note, insight). Random variable.
- **Task target** `Y` — the task-relevant part of `X`; the artifact is scored against `Y`,
  not against `X`. `I(X;Y) ≤ H(X)`; the gap `H(X) − I(X;Y)` is *idea redundancy* (detail
  present in `X` that does not move the score).
- **Scratch** `Z` — the capped pre-artifact utterance, `H(Z) ≤ B` tokens (bits, up to a
  constant `log₂|vocab|`). `Z = f(X)` under a hard length constraint.
- **Artifact** `A` — full generation, produced by a stochastic decoder `A ~ P(A | X, Z)`.
- **Quality** `Q = 𝔼[ s(A, Y) ]`, `s` a blind score in `[0,1]`.
- **A1 (task-relevance is compressible).** `Y` occupies far fewer bits than `X`:
  `I(X;Y) ≪ H(X)`. If false (every detail load-bearing), no compression can help — see failure F2.
- **A2 (the decoder conditions on Z, not just X).** `Z` is not a throwaway; it re-weights
  `P(A|·)`. Formally `I(A; Z | X) > 0`. If the decoder ignores `Z`, `B` is inert (theatre).
- **A3 (the LOAD-BEARING one — anchoring).** Beyond some scratch length, additional scratch
  tokens are spent on *surface / near-verbatim* content that the decoder **over-anchors** to,
  displacing exploration and re-importing the transcription the cap was meant to prevent.
  I write this as a cost `Anchor(B)`, non-decreasing, eventually with positive marginal cost.
  **This assumption alone produces the inverted-U. Compression theory does not.**

---

## Model

**Why the obvious lenses do not, by themselves, give an inverted-U.**

- *Rate–distortion.* `D(R)` (min distortion at rate `R=B`) is convex and **non-increasing**.
  So distortion-of-the-scratch is monotone in `B`: more budget never hurts the scratch. RD is
  correct machinery but predicts a *plateau*, not a peak. It cannot be the whole story.
- *Information bottleneck.* Minimize `I(Z;X) − β I(Z;Y)` — the right decomposition (it
  separates "bits about the idea" from "bits about what matters"), and it explains *why a small
  Z can be near-optimal*: once `I(Z;Y) → I(X;Y)`, extra capacity only adds `I(Z; X | Y)`,
  i.e. irrelevant detail. But `I(Z;Y)` is **monotone non-decreasing** in the capacity `B`.
  IB explains the plateau and the diminishing returns; it still does **not**, by itself, bend
  the curve back down.

**Where the non-monotonicity actually lives.** Not in the scratch — in the *coupling* between
scratch and decoder. Decompose quality into two opposing pathways:

    Q(B)  ≈  Fidelity(B)  −  Anchor(B)

- `Fidelity(B) = g( I(Z;Y) )`, `g` increasing, and `I(Z;Y)` **concave-saturating** in `B`
  (IB: saturates at `I(X;Y)`, reached at a finite `B* ≈ I(X;Y)` bits by A1). This is the
  "enough plan to not starve" term.
- `Anchor(B)` — A3 — non-decreasing, marginal cost eventually positive: the "the scratch
  became a draft and the decoder copied it" term.

`Fidelity` is bounded and saturating; `Anchor` keeps rising. Their difference has an interior
maximum **iff** the marginal anchoring cost overtakes the marginal fidelity gain at some finite
`B` — i.e. `Fidelity'(B) < Anchor'(B)` past the fidelity knee. That crossing is an *empirical*
property of the decoder, not a theorem.

---

## Results (conditions, bounds)

**R1 — the two endpoints are provable; the peak is conditional.**
- `B → 0` (starvation): `H(Z) → 0 ⇒ I(Z;Y) → 0 ⇒ Fidelity → g(0)`. The decoder runs on `X`
  alone with no plan; `Q → Q_baseline`, and if the ritual *replaces* free generation with a
  starved plan, `Q < Q_baseline` (degenerate). **Proven** from A2.
- `B → ∞` (no selection pressure): the constraint is slack, `Z` can equal a verbatim draft.
  `Fidelity` has saturated at `g(I(X;Y))`; `Anchor` is at its max. `Q(∞) = g(I(X;Y)) − Anchor(∞)`.
  **Proven** that fidelity gives nothing beyond `B*`; whether `Q(∞) < Q(B*)` depends on A3.
- **Interior optimum exists ⇔ A3 holds with `Anchor'` overtaking `Fidelity'`.** Under A1+A2+A3
  the peak is at
      `B_opt  ≈  argmax_B [ g(I(Z;Y)(B)) − Anchor(B) ]`,
  and to first order it sits **just past the fidelity knee** `B* ≈ I(X;Y)` — enough bits to
  name the governing idea, not enough to draft it. **Conditional**, not proven.

**R2 — location of `B_opt` (comparative statics, all first-order):**
- ↑ **task complexity** (larger `I(X;Y)`) → knee `B*` moves right → `B_opt` **larger**.
- ↑ **idea redundancy** (`H(X)−I(X;Y)` large; rambling voice note) → fixed `B` captures a
  *smaller fraction* of `Y`; but also more surface for the decoder to anchor on → `B_opt`
  **smaller relative to `H(X)`** (compress hard) even as absolute `B_opt` is modest.
- **strong model prior on the task** → `Fidelity` saturates at smaller `B` (the model already
  knows the shape) **and** `Anchor` bites sooner (it will happily copy a near-draft) → `B_opt`
  **smaller**. Capable models want *shorter* scratch, not longer.

**R3 — no closed form, and that is honest.** `g`, `I(Z;Y)(B)`, `Anchor(B)` are model-specific.
The framing yields *shape* (endpoints, existence-conditions, comparative statics), not a number.
`B_opt` must be measured per model×task-class. Any single universal `B` is a coincidence.

**R4 — special case, "one governing line before any artifact," B≈20–30 tokens.** Justified
**iff** for the target task class `I(X;Y)` is expressible in ~20–30 tokens (one sentence of
genuine information ≈ 20–40 bits-of-plan). That is exactly the regime of a *single load-bearing
insight*: one claim, one mechanism. So the ritual is well-founded **for single-insight artifacts
with high idea-redundancy and a capable model** — the regime where R2 pushes `B_opt` small on
all three axes simultaneously. It is *not* justified as a universal constant: for a multi-part
spec (`I(X;Y)` spans several independent claims), 20–30 tokens is below the knee → starvation
(F1). The ritual is a well-chosen point estimate for one task class, wrongly generalized is F3.

---

## Predictions for A/B (blind-scored, discriminating)

Design: same idea `X`, same decoder, vary only the scratch regime. Blind-score artifacts `A`.
Arms: **(N)** no scratch; **(C_B)** capped scratch at budget `B` swept low→high; **(U)** uncapped
scratch (draft-then-write). Prediction *P0 is the go/no-go*; the rest discriminate mechanism vs theatre.

- **P1 (the peak — strongest, decisive).** `Q(C_B)` vs `B` is **single-peaked (inverted-U)**:
  rises from `B→0`, maxes at an interior `B_opt`, then *declines* toward `Q(U)`. If the mechanism
  is real, blind scores show `Q(C_{B_opt}) > Q(U)` **and** `> Q(N)` with the max strictly interior.
  *Theatre signature:* monotone-increasing or flat — no interior peak; any gain is just "more
  planning tokens," and an uncapped draft would do as well or better. This single curve is the
  whole experiment.
- **P2 (capable-model shift — strongest structural test).** Run P1 on a weak and a strong
  decoder. Mechanism predicts `B_opt` moves **left** for the stronger model (R2). *Theatre
  signature:* `B_opt` invariant to model strength, or moves right (would mean "bigger models
  just want more context," not selection pressure). Direction of the shift is the discriminator.
- **P3 (substance vs surface — separates F1 from F5/metric-gaming).** Score `A` on two blind
  rubrics: *substantive* (correct governing idea, right load-bearing detail) and *surface*
  (fluency, length, polish). Mechanism: at `B_opt` the **substantive** score peaks. Theatre /
  metric-gaming: only the **surface** score improves with `B`, substantive flat → the cap is
  compressing prose, not thought (F1).
- **P4 (redundancy interaction).** Bucket ideas by measured redundancy (transcript length ÷
  information content). Mechanism predicts the *height* of the peak (gain over `N`) is **larger**
  for high-redundancy ideas and the optimal *ratio* `B_opt/H(X)` is **smaller** (R2). Flat
  interaction ⇒ the cap is not doing selection, it is a fixed prompt tweak.

---

## Failure modes

Structural (S) = no `B` fixes it, the mechanism is misapplied. Tuning (T) = right mechanism,
wrong knob.

- **F1 — surface compression, not substance (metric gaming).** *(S if scoring is surface-only;
  T otherwise.)* The model satisfies the token cap by dropping *detail* rather than *redundancy*
  — it keeps fluent framing and discards the load-bearing clause. Structural whenever the score
  rewards surface; A3 guarantees this is the *easy* way to hit the cap. Mitigation is not a
  budget, it is P3-style substantive scoring. **This is the mechanism's primary risk.**
- **F2 — loss of rare-but-load-bearing detail (violates A1).** *(Structural.)* If a single
  low-frequency token *is* the point (a name, a constant, a sign), any lossy `Z` risks dropping
  exactly the high-surprisal item that compression discards first. Where A1 fails, forced
  compression is *contraindicated*: pass such detail verbatim, do not cap it.
- **F3 — budget mis-tuned per task class.** *(Tuning.)* One global `B` across single-insight and
  multi-claim artifacts: starves the latter (below knee → F1/F2), over-permits the former (past
  peak → anchoring). Fix: per-class `B` (R2). This is exactly R4's over-generalization risk.
- **F4 — cap on the wrong phase.** *(Structural.)* Capping the *artifact* (output) rather than
  the *scratch* (plan) truncates delivery, not thought — pure loss, no selection benefit. The
  mechanism only works when the cap sits on a phase that *conditions* a later uncapped phase
  (A2). Capping the sole generative phase is just a length limit.
- **F5 — decoder ignores the scratch (violates A2).** *(Structural.)* If `I(A;Z|X)=0`, `B` is
  inert; observed "gains" are noise or a Hawthorne/prompt-format artifact. This is the theatre
  null; P1's flat curve detects it.
- **F6 — anchoring past the knee (the A3 cost itself).** *(Tuning.)* At `B > B_opt` the scratch
  becomes a draft the decoder copies verbatim — the very transcription the mechanism opposed.
  Bounded by keeping `B` at/below the peak; this is the descending arm of P1.

---

## Verdict

- **sound** — *no.* As stated ("a hard cap forces compression, therefore quality up") it is not
  sound: RD and IB both prove the scratch's own distortion is **monotone** in `B`; compression
  theory yields a plateau, never a peak. The headline claim overreaches.
- **conditionally-sound** — *yes, this is the landing.* The mechanism is well-formed and the
  inverted-U is real **iff** assumption **A3 (downstream anchoring)** holds — i.e. the benefit is
  not "compression" per se but *forcing early commitment to a low-dimensional plan while denying
  the decoder a verbatim draft to over-copy.* Under A1+A2+A3 the endpoints are provable
  (starvation at 0, saturation+anchoring at ∞) and an interior `B_opt` exists, sitting just past
  the fidelity knee `B* ≈ I(X;Y)`. The B≈20–30 ritual is a correct point estimate **for
  single-insight, high-redundancy tasks on a capable model**, and only there.
- **unsound** — *only if A2 or A3 fails.* If the decoder ignores the scratch (A2), `B` is inert.
  If nothing is gained by denying a verbatim draft (A3 false, `Anchor'≡0`), the curve is monotone
  and "uncapped scratch" dominates — the cap is theatre. **P1's single inverted-U curve is the
  entire go/no-go: an interior peak confirms; a monotone/flat curve refutes.**

**Load-bearing assumption, in one line:** the win is *anti-anchoring* (deny the decoder a
verbatim draft), not *compression* — and that is an empirical property of the generator, testable
by P1, not a theorem.

**Cheap-seat note (advisory):** the derivation is complete offline; the *only* external need is
measuring `Fidelity'/Anchor'` crossing per model×task — a bench A/B (P1–P4), not a proof. That is
implementation, not mathematics: hand it to a coder seat (@Trajectory) to script the sweep and a
blind-scoring rubric, not to me and not to a literature pass.
