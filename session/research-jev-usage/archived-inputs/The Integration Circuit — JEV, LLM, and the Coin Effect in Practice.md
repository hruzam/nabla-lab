# The Integration Circuit — JEV, LLM, and the Coin Effect in Practice

Oct 8, 2026 · @Michal Hrůza

Companion to The Coin Effect — Mathematical Foundations. That document states the hypothesis; this one is how to run it and find out whether it holds.

## What transfers from the analog computer

When a system of differential equations had no closed form, engineers built a circuit whose voltages obeyed the same equations, let it settle, and measured the answer. The capacitor integrates current; wire it into feedback and the steady state *is* the solution.

The transferable principle is not the hardware. It is this: **when you cannot derive, build a system governed by the same structure and measure its behaviour instead.** The rigour lives in the correspondence, not in the components.

Two consequences follow, and both apply directly here.

**Measurement substitutes for derivation.** JEV is queried, not solved. It returns a calibrated distribution over a predefined option set — a reading, not a proof. This is the right instrument for a problem whose structure is known but whose values are not.

**The topology is the solver.** No single component in a differential analyser solved anything; the answer lived in how they were wired. Likewise here, neither JEV nor the LLM holds the coin effect. The EDGE state exists in the harness, in the relationship between a measurement and a threshold — nowhere in either model's weights.

This is also the reason the hypothesis can be tested before it is proved. The two-completion result and the orientation claim are both statements about circuit behaviour, and circuit behaviour is observable by running it.

## Component map

&#91;embedded content: the circuit · 5 components, 1 feedback loop\]

Each component does the one thing its construction suits it for, and no more.

| Component | Role | Cost | Why this component |
| --- | --- | --- | --- |
| Frame | Declares the odd group and its minimal winning coalitions | Once, static | Enumeration and contradiction belong here, before any measurement |
| JEV | Measures each element against a typed two-option question | Cheap, fast | Calibrated probabilities are exactly what a threshold needs |
| Edge detector | Reads the distribution; assigns FACE, TAIL, or EDGE plus orientation | Free | A comparator, not a model. The coin effect lives here |
| Group rule | Two completions of the simple game over the element states | Two evaluations | Decides whether any EDGE actually matters |
| LLM | Re-poses the question for pivotal EDGE elements only | Expensive, slow | The only component that can generate a new option set |

The asymmetry in the cost column is the design constraint. JEV can be called freely; the LLM cannot. The group rule sits between them precisely to decide which expensive calls are worth making.

## The settling loop

Six stages. The circuit runs until it settles or the budget runs out, exactly as an analog solver does.

1. **Frame.** Decompose the decision into an odd-sized group of elements. Enumerate the minimal winning coalitions — this is where contradiction does its work, eliminating configurations that cannot pass. Static per decision type, not per query.
2. **Measure.** One JEV call per element, each a typed two-option question. Never ask JEV about the configuration as a whole at this stage, and never offer EDGE as an option.
3. **Detect.** For each returned distribution, apply the concentration test. Concentrated on one option gives FACE or TAIL; not concentrated gives EDGE, with an orientation assigned by the harness.
4. **Compose.** Evaluate the group rule twice — all EDGE forced to FACE, then all forced to TAIL. Agreement ends the run with that verdict. Disagreement means at least one EDGE element is pivotal.
5. **Resolve, selectively.** Identify which EDGE elements are pivotal. For those only, call the LLM: re-pose the question on the axis the orientation selects, producing a new typed option set. Hand that set back to JEV and return to stage 3.
6. **Settle or report.** Repeat until the two completions agree, or until the call budget is exhausted. If it will not settle, the answer is `GROUP_EDGE` — reported as a result, not an error.

### The budget rule

Stage 5 is the whole economic argument for the design.

Without the pivotality filter you would resolve every EDGE element — the expensive path, run on elements that cannot change the answer. With it, you resolve only elements whose resolution can move the verdict. In a group of seven with four elements on their edge, it is common for none of them to be pivotal, and the run costs nothing beyond stage 4.

This is the Banzhaf index doing operational work rather than descriptive work.

### Two things the loop must not do

**Do not let the LLM assign element states.** It re-poses questions and generates option sets. The measurement stays with JEV, which is the calibrated instrument. An LLM asked to also judge confidence will produce a number that looks like a probability and is not one.

**Do not resolve an EDGE by taking the argmax.** If the distribution did not concentrate, the larger of two near-equal values is noise. Taking it converts a detected EDGE into a false FACE or TAIL, which is the exact failure the circuit exists to prevent.

## Edge detection

The detector is the smallest component and carries the most conceptual weight. It is where a two-valued instrument is made to report a three-valued world.

### Why JEV must not emit EDGE

Adding EDGE to JEV's option set looks convenient and is wrong on three counts.

It makes EDGE compete with FACE and TAIL for probability mass, which re-embeds it as a third ordered alternative — the exact structure Part B of the foundations document rules out. It also means the model must be trained to recognise EDGE, when the whole point is that EDGE is defined by the *absence* of concentration, which is a property of the distribution rather than of the input. And it destroys the diagnostic: a flat distribution over three options tells you nothing about whether the binary question failed.

Keep JEV binary. Read EDGE off the shape of its answer.

### Candidate criteria

Three tests, in increasing order of what they demand from calibration. Which one is right is an empirical question, not a theoretical one.

| Criterion | Trigger | Depends on |
| --- | --- | --- |
| Margin | The gap between the top two probabilities falls below a threshold | Nothing but the ordering. Most robust |
| Entropy | Distribution entropy exceeds a threshold | The shape of the whole distribution. Equivalent to margin for two options |
| Calibrated confidence | The reported confidence falls below a threshold | JEV's calibration being trustworthy at that operating point |

For a two-option question, margin and entropy are monotone transforms of each other; pick margin, as it is the easier one to explain and to tune. Calibrated confidence is worth adding only once you have measured whether JEV's confidence tracks accuracy in your domain.

### Setting the threshold

Do not guess it. Run the circuit with the detector disabled, record the distributions, and plot accuracy against margin. The threshold goes where accuracy stops being usable — which is a decision about your tolerance for a wrong confident answer, not a property of the model.

A practical starting point is to set it so that EDGE fires on a small minority of elements. If most elements land on their edge, either the questions are posed wrongly or the decomposition is too fine. An edge that is common is a sign of a bad frame, not a rich phenomenon.

### Orientation

The orientation `EDGE_POS` / `EDGE_NEG` is assigned by the harness from whatever signal distinguishes the two resolution strategies in your domain. It is explicitly *not* read from JEV's distribution — a near-tie carries no direction.

This is the weakest-specified part of the circuit, and deliberately so. Until the orientation is shown to change outcomes, it should be treated as an untested hypothesis carried along, not as a working mechanism.

## Calibration does not compose

JEV is calibrated per call. The circuit is not calibrated by inheritance, and assuming otherwise is the most likely way this system produces a confident wrong answer.

### Why it fails

**Errors correlate.** Five JEV calls on five elements of the same decision share the input context, the prompt template, and whatever systematic bias the model has in this domain. Independent-error arithmetic overstates composite reliability, often badly.

**The group rule is not smooth.** It is a threshold function. A small shift in one element's measurement flips the verdict discontinuously when that element is pivotal. Composite reliability is therefore dominated by the calibration of the few pivotal elements, not by the average across all of them.

**Thresholds are not probabilities.** Once the detector converts a distribution into FACE, TAIL, or EDGE, the probability is discarded. Whatever calibration guarantee JEV offered does not survive that conversion.

### What to measure instead

Test the composite end to end, against held-out cases with known verdicts.

| Measure | Question it answers |
| --- | --- |
| Composite accuracy | How often is the group verdict right when it is determinate |
| EDGE rate | What fraction of runs end in `GROUP_EDGE` |
| EDGE precision | When the circuit reports `GROUP_EDGE`, was the case genuinely hard |
| False-confident rate | How often does a determinate verdict turn out wrong |
| Pivotal-EDGE rate | What fraction of EDGE elements actually needed resolving |

The fourth row is the one that matters. A circuit that reports `GROUP_EDGE` too often is merely expensive. A circuit that returns confident wrong verdicts has laundered uncertainty into false precision, which is worse than having no circuit.

The fifth row tells you whether the pivotality filter is earning its complexity. If nearly every EDGE element turns out pivotal, the filter is not saving calls and the group may be too small or too tightly coupled.

### The honest comparison

Run a baseline alongside: one JEV call on the whole decision, no decomposition, no group rule, no edge detection. If the circuit does not beat that baseline on false-confident rate, the structure is not paying for itself, however elegant the theory behind it.

## The smallest first experiment

One decision type, one group of five, roughly fifty labelled cases. Small enough to build in an afternoon, large enough to decide all three falsification conditions.

### Setup

Pick a decision you already make by hand often enough to have ground truth for. Decompose it into exactly five elements. Write the minimal winning coalitions by hand — if you cannot, the decomposition is wrong and nothing downstream will work.

Then run three configurations over the same cases.

| Configuration | What it isolates |
| --- | --- |
| Baseline: one JEV call on the whole decision | Whether decomposition helps at all |
| Group rule, no edge detection: JEV argmax per element, composed by W | Whether the group layer alone beats the baseline |
| Full circuit: edge detection, two-completion test, selective resolution | Whether the coin effect adds anything over the group layer |

The second configuration is the one people skip, and it is the one that matters most. If it already matches the full circuit, the entire EDGE apparatus is unnecessary and the borrowed mathematics was the whole answer.

### Reading the result

**If the group layer beats the baseline but the full circuit does not beat the group layer** — the coin effect is not earning its place in this domain. Keep the simple game, drop EDGE. No loss; the foundations document already says the skeleton is the sound part.

**If the full circuit lowers the false-confident rate** — EDGE is doing real work. Then test orientation: run the resolution step with the orientation honoured, and again with it randomised. No difference means orientation is decoration.

**If cases where the two completions disagree are also the cases a human finds genuinely ambiguous** — that is the strongest available evidence that `GROUP_EDGE` names something real rather than a measurement artefact.

### What this experiment cannot settle

Whether EDGE is orthogonal rather than ordered. Fifty cases in one domain will not distinguish a genuine third state from a well-behaved abstention, and the two make nearly identical predictions at this scale.

That question needs a case where the orientation changes the group verdict directly — the third falsification condition in the foundations document. Design for it deliberately once the circuit runs; it will not appear on its own.

### Instrumentation

Log every run as a record carrying the case id, each element's distribution, each element's assigned state and orientation, the pivotal set, both completions, the verdict, and the resolution calls made. Everything in the analysis above is recoverable from that record, and nothing is recoverable without it.
