# L2 brief — offline-formal (@Color) · forced compression as mechanism

`run: Track 3 synthesis-run · fired 2026-07-18 · blind leg — sealed: work ONLY`
`from this brief; write ONLY your artifact file. No web. Do not read other files.`

## The mechanism to formalize

Human handwriting is slower than thought; the writer cannot transcribe verbatim
and must **select and compress**. Hypothesized agent analogue: a **hard token
budget B on a pre-artifact scratch phase** ("say it in 20 tokens first") forces
lossy selection before full generation, playing the role of hand-speed.

**Question: is this a sound mechanism? Under what conditions does it help,
under what conditions does it harm?**

## Asks

1. **Formal framing** — model the capped scratch phase. Candidate lenses (use
   what holds, discard what doesn't): information bottleneck (compress
   representation while preserving task-relevant information), rate-distortion
   (distortion at rate B), selection-under-budget / attention allocation.
2. **The inverted-U conjecture** — quality of the downstream artifact as a
   function of B: degenerate at B→0 (starvation), no selection pressure at B→∞.
   Does an interior optimum follow from your framing, and under what assumptions?
   What determines its location (task complexity, redundancy of the idea,
   model's prior)?
3. **Failure modes** — enumerate: compression of surface instead of substance
   (metric gaming), loss of rare-but-load-bearing detail, budget mis-tuned per
   task class, cap applied to the wrong phase. Which are structural, which
   are tuning?
4. **Testable predictions** — what should an A/B experiment observe if the
   mechanism is real vs if it is theatre? 2–4 concrete, discriminating
   predictions (these will shape a later experiment design — make them
   measurable by blind scoring of output artifacts).
5. **Special case** — the "one-line governing insight required before any
   artifact" ritual as B≈20–30 tokens: does your framing justify it?

## Output

Write your dated artifact to:
`/home/hruzam/nabla-lab/session/research-handwriting/leg2-offline.color.2026-07-18.md`

Sections: `## Assumptions` · `## Model` · `## Results` (conditions, any bounds)
· `## Predictions for A/B` · `## Failure modes` · `## Verdict`
(sound / conditionally-sound / unsound — one line each why).
Honest non-landing allowed and respected: if the mechanism does not formalize
cleanly, say exactly where it breaks — that IS a result.
