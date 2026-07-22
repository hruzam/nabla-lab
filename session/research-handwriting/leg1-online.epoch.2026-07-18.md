# L1 research artifact — online-depth (@Epoch)
# Handwriting analogue · Track 3 blind leg
Date: 2026-07-18
Recalibrated: training cutoff Aug 2025 → verified against live sources 2026-07-18
Scope: Part A (four neuroscience claims) + Part B (five LLM/agent prior-art areas)

---

## Claim verdicts

### Claim 1: Mueller & Oppenheimer 2014 — "The Pen Is Mightier Than the Keyboard"

STATUS: PARTIALLY CONFIRMED / SUBSTANTIALLY WEAKENED by replication record

The original 2014 paper (Psychological Science, Sagepub) remains published and cited.
The core mechanism claim — that longhand forces compression/selection, which produces
deeper conceptual encoding than verbatim laptop notes — has face validity and partial
support, but the large effect sizes from 2014 have not held up.

REPLICATION HISTORY (live-verified):

- Morehead, Dunlosky & Rawson (2019), Educational Psychology Review: Direct replication
  and extension. Meta-analysis across direct replications found small, non-significant
  effects favoring longhand. Trends toward longhand advantage existed but were not
  consistent across experiments.
  SOURCE: https://link.springer.com/article/10.1007/s10648-019-09468-2
  CONFIDENCE: H

- Urry et al. (2021), Psychological Science: "Don't Ditch the Laptop Just Yet" — direct
  replication of Mueller & Oppenheimer Study 1 plus mini-meta-analyses. Laptop
  participants did not perform worse. Meta-analysis (8 similar studies) confirmed small,
  non-significant difference. The paper explicitly does not support the encoding-via-
  compression hypothesis.
  SOURCE: https://journals.sagepub.com/doi/abs/10.1177/0956797620965541
  CONFIDENCE: H

- A broader meta-analysis cited in the wild (14 studies, 3,075 participants) finds a
  ~25% more students below the mean with electronic notes, suggesting some real signal,
  but effect size and ecological validity are disputed.
  CONFIDENCE: M (aggregator sourcing, not primary)

- No post-2022 large RCT or pre-registered replication was found in this search.
  What exists from 2022–2025 is primarily secondary commentary and review articles, not
  new primary replication data. The arxiv paper 2604.17023 ("The Instrumental Dissolution
  of Typing," 2026) references the replication crisis around this study.

VERDICT: The conceptual compression mechanism is plausible but the original effect size
is overstated. The claim that longhand reliably outperforms laptop for conceptual learning
is not robustly replicated. Treat the mechanism (forced selection = deeper encoding) as a
reasonable hypothesis, not an established finding. Flag with [PARTIAL].

---

### Claim 2: Longcamp et al. — handwriting engages motor-perceptual loops beyond language areas

STATUS: CONFIRMED (core findings) / WELL REPLICATED

Longcamp and colleagues have a substantial body of work across the 2000s–2020s showing:

- Handwriting activates left premotor cortex (BA6, resembling Exner's area) during both
  production AND during subsequent visual perception of self-produced letters.
- The left fusiform gyrus and superior parietal lobule show greater engagement for
  handwritten-learned characters vs. keyboard-learned characters.
- fMRI shows: symbols learned by handwriting recruit the same neural pathways as
  canonical letters; typewriter-learned symbols do not.
- Premotor activations during letter perception depend on the hand used to write —
  confirming motor-perceptual binding, not merely visual familiarity.

A 2024 MDPI Life review ("The Neuroscience Behind Writing: Handwriting vs. Typing") cites
Longcamp's work as foundational and still current.
SOURCE: https://www.mdpi.com/2075-1729/15/3/345 (2025)
SOURCE: https://pmc.ncbi.nlm.nih.gov/articles/PMC4274624/ (Longcamp lineage)
SOURCE: https://www.researchgate.net/publication/5650672 (fMRI evidence, behavioral)
CONFIDENCE: H

A 2025 commentary by Pinet and Longcamp in Frontiers in Psychology (response to van der
Meer 2024) confirms Longcamp remains an active researcher and that the motor-perceptual
loop framework is still considered established, even while questioning newer connectivity
claims.
SOURCE: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11750765/
CONFIDENCE: H

VERDICT: CONFIRMED. The motor-perceptual loop claim is one of the better-supported
findings in the handwriting neuroscience literature.

---

### Claim 3: van der Meer & van der Weel — EEG connectivity handwriting vs. typewriting

STATUS: CONFIRMED AS PUBLISHED / METHODOLOGICALLY CONTESTED

The 2024 paper (van der Weel & van der Meer, Frontiers in Psychology 2023/published 2024)
is real and significant:
- 36 university students
- 256-channel EEG
- Handwriting produced 32 statistically significant cluster differences across 16 neural
  connections
- Widespread theta-alpha coherence across left parietal, midline parietal, right parietal,
  and central cortical hubs during handwriting
- This coherence was absent during typing
SOURCE: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1219945/full
SOURCE: https://pmc.ncbi.nlm.nih.gov/articles/PMC10853352/
CONFIDENCE: H

CONTESTED BY: Pinet & Longcamp (2025 commentary, Frontiers in Psychology, PMC11750765)

Key methodological critiques:
1. Typing condition used single right-index-finger input — not ecologically valid bimanual typing
2. Visual feedback differed between conditions (pen vs. screen)
3. No learning task was included — the study measured connectivity during the act, not
   during or after learning; the educational implications in the title are inferential
4. Typing skill was not controlled or measured
5. Statistical comparison was condition-difference only, not within-condition connectivity

VERDICT: The connectivity difference is reported and peer-reviewed. The jump from
"handwriting produces more distributed EEG connectivity during the task" to "this
promotes learning" is not demonstrated — it is an inference. The 2025 commentary by
Pinet and Longcamp (two respected researchers in the field) is a formal methodological
challenge. Treat the connectivity finding as real-but-contested and the educational
implication as unvalidated inference.

---

### Claim 4: "Fine motorics of writing driven from centres near speech production; handwriting activates different parts than typing"

STATUS: PARTIALLY CONFIRMED — some parts well-supported, some folk-neuroscience

WHAT IS DOCUMENTED:

A. Exner's area is real and localized.
   Exner's area is in the posterior middle frontal gyrus, Brodmann area 6 (premotor
   cortex). It was postulated at "the foot of the second frontal convolution, immediately
   above Broca's speech area." Anatomical proximity to Broca's area (BA44/45, inferior
   frontal gyrus) is confirmed — they are in adjacent gyri of the left frontal lobe.
   SOURCE: https://www.nature.com/articles/s42003-021-01971-z (Exner's area, 2021, PMC)
   SOURCE: https://pubmed.ncbi.nlm.nih.gov/19847902/ (Exner's area revisited)
   CONFIDENCE: H

B. "Near speech production" — PARTIALLY TRUE but requires precision.
   - Broca's area (speech production) = BA44/45, inferior frontal gyrus
   - Exner's area (handwriting motor programs) = BA6, posterior middle frontal gyrus
   - These are adjacent but distinct structures. They are not the same area and do not
     fully overlap. The folk claim that handwriting is "driven from centres near speech"
     is approximately correct anatomically, but "near" should not be read as "shared" or
     "co-activating during both tasks simultaneously."
   - There IS evidence for partial overlap: premotor cortex (BA6) is involved in both
     speech production (supplementary motor area for vocalization) and handwriting.
     Dominant PMC activation during naming and speech has been documented.
   - The 2021 Nature Communications Biology paper on Exner's area in blind participants
     shows Exner's area can take over word-form learning functions, coupling with
     hippocampus — suggesting a multi-functional zone, not a narrow handwriting engine.
   CONFIDENCE: M (inferential from adjacent-area literature)

C. "Handwriting activates different parts than typing" — CONFIRMED
   The consensus from Longcamp, van der Meer, and multiple fMRI studies: handwriting
   recruits premotor/parietal/fusiform pathways that typewriting does not equivalently
   activate. This is the best-supported claim in the group.
   CONFIDENCE: H

VERDICT BREAKDOWN:
- Exner's area exists and is adjacent to Broca's: CONFIRMED
- Fine motorics "near speech production": APPROXIMATELY TRUE, not folk-neuroscience,
  but requires anatomical precision — adjacent, not shared
- Handwriting activates different parts than typing: CONFIRMED
- The claim that handwriting ACTIVATES SPEECH PRODUCTION AREAS during writing: NOT
  CONFIRMED as a general statement; the adjacency is anatomical, not functional co-activation

---

## Prior art

### B1: Sketch-first / diagram-first prompting; canvas-based agent workflows; tldraw ecosystem

EXISTS: PARTIAL (ecosystem active, theory underspecified)

tldraw has an official LLM documentation layer and an agent template (GitHub:
tldraw/agent-template) as of 2025. Agents can interpret and interact with canvas drawings,
create/update/delete shapes, and respond to freehand input.

"Make It Real" (tldraw, 2023–2024): viral demo where wireframe → functioning UI via
multimodal LLM. Described as "accidentally making a very good visual multimodal prompting
environment." This is canvas-as-input, not canvas-as-reasoning-scratchpad.

SketchAgent (CVPR 2025, arXiv:2508.01237 for diagram variant): language-driven sequential
sketch generation. Given a text prompt, produces stroke sequences. LLM→canvas direction,
not canvas→reasoning direction.
SOURCE: https://openaccess.thecvf.com/content/CVPR2025/papers/Vinker_SketchAgent_Language-Driven_Sequential_Sketch_Generation_CVPR_2025_paper.pdf
CONFIDENCE: H

"Agents on the Canvas with tldraw" (Max Drake, GitNation, 2025): conference talk
demonstrating agent-canvas integration. Shows two-way agent-canvas interaction.
SOURCE: https://gitnation.com/contents/agents-on-the-canvas-with-tldraw-3450
CONFIDENCE: M

GAP: No published system found where a model explicitly SKETCHES A DIAGRAM FIRST before
generating prose, as a deliberate forced-compression step analogous to handwriting's
motor-selection constraint. The canvas→reasoning direction is nascent; the
reasoning→canvas direction (visualization of results) is more developed.

BUILD-READINESS: Medium. Primitives exist (tldraw API, multimodal LLMs). A
sketch-first-then-answer pipeline could be prototyped. Not theorized as a training
intervention.

---

### B2: Visualization-of-Thought / Whiteboard-of-Thought

EXISTS: FULLY (as research paradigm, 2024–2025)

Three distinct lines:

A. Visualization-of-Thought (VoT) — "Mind's Eye of LLMs" (arXiv:2404.03622, NeurIPS 2024)
   Prompts LLM to visualize reasoning traces at each step for spatial reasoning tasks.
   The model emits a textual/ASCII representation of spatial state as intermediate output.
   SOURCE: https://arxiv.org/abs/2404.03622
   SOURCE: https://proceedings.neurips.cc/paper_files/paper/2024/file/a45296e83b19f656392e0130d9e53cb1-Paper-Conference.pdf
   CONFIDENCE: H

B. Whiteboard-of-Thought (WoT) — (arXiv:2406.14562, 2024)
   Equips multimodal LLMs to synthesize drawing code → execute code → generate image →
   parse image → produce final answer. Actual image generation in the reasoning loop.
   SOURCE: https://arxiv.org/html/2406.14562v1
   CONFIDENCE: H

C. "Visualizing Thought: Conceptual Diagrams Enable Robust Planning in LMMs"
   (arXiv:2503.11790, March 2025)
   LMMs reason through chains of self-generated conceptual diagrams, significantly
   enhancing combinatorial planning.
   SOURCE: https://arxiv.org/html/2503.11790v1
   CONFIDENCE: H

STATUS: Active research area, multiple papers, NeurIPS 2024 presence. The specific
analogue to handwriting's modality-shift mechanism (generating visual intermediate
representation forces different cognitive constraints than text) is being studied, though
not framed that way in the literature.

BUILD-READINESS: Medium-high for inference-time techniques. Training-time interventions
on visual intermediates remain thin.

---

### B3: Token-capped / compressed intermediate drafting

EXISTS: FULLY (multiple lines, very active 2024–2026)

Key entries:

A. Chain-of-Density (CoD, Adams et al. 2023): iterative summarization with forced
   density increase each round. Training origin but the compression-improves-quality
   intuition is foundational.

B. Skeleton-of-Thought (Ning et al. 2023–2024): answer skeleton first, then parallel
   elaboration. Latency reduction, not quality improvement per se.

C. Sketch-of-Thought (arXiv:2503.05179, March 2025): three cognitive paradigms
   (Conceptual Chaining, Chunked Symbolism, Expert Lexicons) with a routing model that
   selects the paradigm per query. Up to 84% token reduction across 18 reasoning datasets
   with minimal accuracy loss.
   SOURCE: https://arxiv.org/abs/2503.05179
   CONFIDENCE: H

D. Token-Budget-Aware Reasoning (arXiv:2412.18547, 2024–2025): treats chain length as
   a resource, estimates sensible budget per query, cuts tokens ~2/3 on math tasks with
   small accuracy drops.
   SOURCE: https://arxiv.org/html/2412.18547v5
   CONFIDENCE: H

E. Chain of Draft (CoD, ~2024): model writes minimal drafts at each step instead of full
   sentences, using ~7.6% of standard CoT tokens with comparable accuracy.
   CONFIDENCE: M (cited in secondary sources; primary arxiv not confirmed in this run)

F. "The Coupling Tax" (arXiv:2605.07686, 2026): finds that shared token budgets between
   visible CoT and final answer UNDERMINE reasoning quality under fixed output limits.
   This is directly relevant — it suggests that budget constraints can degrade rather
   than improve quality depending on how the budget is structured.
   SOURCE: https://arxiv.org/pdf/2605.07686
   CONFIDENCE: H

KEY FINDING: The evidence on whether hard budget on intermediate reasoning IMPROVES
downstream quality (vs. merely cheapens it) is MIXED. Sketch-of-Thought and CoD show
quality preservation under compression. The Coupling Tax (2026) shows that improperly
structured budgets degrade quality. The analogy to handwriting's forced-selection
mechanism is real but the mechanism needs careful operationalization.

BUILD-READINESS: High. Multiple published techniques available to build on.

---

### B4: Ephemeral scratchpads — non-persisted intermediate thinking

EXISTS: PARTIALLY (foundational work solid; ephemerality as a variable studied tangentially)

A. Nye et al. 2021 ("Show Your Work: Scratchpads for Intermediate Computation"):
   foundational paper showing training transformers on intermediate steps improves task
   performance. The scratchpad is treated as a workspace, not persisted as output.
   CONFIDENCE: H (training-data era; confirmed as foundational by multiple 2024–2025 citations)

B. Self-Notes (Lanchantin et al. 2023, arXiv:2305.00833): model can interleave
   "self-notes" mid-input to reason, then discard them from the output stream.
   SOURCE: https://arxiv.org/pdf/2305.00833
   CONFIDENCE: H

C. "Writing in the Margins" (arXiv:2408.14906, 2024): inference-time pattern for long
   context retrieval using margin annotations as ephemeral intermediate working memory.
   SOURCE: https://arxiv.org/pdf/2408.14906
   CONFIDENCE: H

D. "Intermediate Artifacts as First-Class Citizens" (Rosen & Rosen, arXiv:2605.12087,
   May 2026): argues the OPPOSITE of ephemerality — that intermediate work products
   SHOULD be durable, typed, versioned, and inspectable. Distinguishes durable artifacts
   from chain-of-thought / scratchpads. Frames ephemerality as a current design deficiency.
   SOURCE: https://arxiv.org/abs/2605.12087
   CONFIDENCE: H

GAP: Ephemerality ITSELF as an independent variable — whether discarding intermediates
is better than persisting them for downstream quality — is studied obliquely. Most
scratchpad literature treats ephemerality as incidental (scratchpads happen to be
ephemeral because they are not final output), not as a designed property. The Rosen 2026
paper is the clearest counter-position: arguing for durability. No paper found that
directly compares ephemeral vs. persisted intermediate reasoning on output quality.

BUILD-READINESS: Medium. Scratchpad primitives are available in Claude and other models
(extended thinking). The ephemerality variable is uncontrolled.

---

### B5: Spatial / 2D intermediate formats — tables, trees, position-as-meaning

EXISTS: PARTIAL (active, but "position-as-meaning" as deliberate cognitive intervention is underspecified)

A. "Spatial Reasoning via Modality Switching" (arXiv:2606.31285, June 2026):
   grid-based grounding converts spatial stories into structured 2D layouts; adaptive
   switching between natural language and structured representation based on complexity
   and trustworthiness signals.
   SOURCE: https://arxiv.org/html/2606.31285v1
   CONFIDENCE: H

B. "Landscape of Thoughts" (arXiv:2503.22165, March 2025): visualizes reasoning process
   of LLMs as a landscape/topology — more a monitoring tool than a reasoning primitive.
   SOURCE: https://arxiv.org/html/2503.22165v1
   CONFIDENCE: H

C. Coordinate/JSON spatial formats: research shows (x,y) JSON coordinates outperform
   natural language for geometric calculations. Format choice matters for spatial accuracy.
   CONFIDENCE: M

D. "Thinking with Spatial Code" (arXiv:2603.05591, 2026): spatial code as intermediate
   representation for physical-world video reasoning.
   SOURCE: https://arxiv.org/pdf/2603.05591
   CONFIDENCE: H

GAP: Tables and trees as intermediate reasoning formats (non-spatial tasks) exist in
practice but are undertheorized as deliberate modality-shift interventions. The idea
that position-as-meaning (2D layout) forces different cognitive operations on the model
— analogous to how spatial arrangement forces human note structure in handwriting — is
not a recognized research primitive. The spatial reasoning literature addresses geometry
tasks specifically, not general reasoning.

BUILD-READINESS: Low-medium. The spatial reasoning primitives exist but the general
"use 2D intermediate format to improve non-spatial reasoning" hypothesis has not been
operationalized.

---

## Surprises

1. "The Coupling Tax" (2026): The finding that shared token budgets between visible CoT
   and final answer DEGRADE reasoning quality under fixed output limits is a genuine
   surprise. The folk assumption is that compression always helps (handwriting analogy:
   forced selection = better encoding). The Coupling Tax result suggests the
   budget-structure matters as much as the budget-size. An LLM analogue to handwriting's
   compression mechanism could backfire if the budget is applied to the wrong layer.

2. Rosen & Rosen 2026 "durable intermediate artifacts": A May 2026 paper arguing
   explicitly AGAINST ephemeral scratchpads — for durable, versioned, inspectable
   intermediate artifacts. This is a direct counter-position to the ephemeral-scratchpad
   paradigm and maps interestingly onto the handwriting question: handwriting notes ARE
   persistent (unlike inner speech during typing). The durability angle may be as
   important as the motor-selection angle.

3. Pinet & Longcamp 2025 commentary is co-authored by Longcamp — the same researcher
   whose earlier work (Claim 2) is the best-supported evidence FOR handwriting's neural
   advantages. Longcamp is not anti-handwriting; she is being precise about what the van
   der Meer 2024 study actually proves. This internal methodological discipline within
   the pro-handwriting research community is notable and credibility-enhancing.

4. The tldraw ecosystem has moved significantly toward agent-canvas integration (2024–2025)
   but the direction is primarily LLM→canvas (model draws), not canvas→LLM (sketch first,
   then reason). The forced-compression-via-sketch-first direction is not yet built.

---

## Confidence map

| Area | Confidence | Notes |
|------|-----------|-------|
| Mueller/Oppenheimer core mechanism | M | Plausible, not robustly replicated |
| Mueller/Oppenheimer replication status pre-2022 | H | Urry 2021 is definitive |
| Mueller/Oppenheimer post-2022 literature | L | No new large RCT found in this run |
| Longcamp motor-perceptual loop | H | Multiple studies, well-replicated |
| van der Meer 2024 connectivity finding | H | Peer-reviewed, published |
| van der Meer educational implication | L | Contested by Pinet/Longcamp 2025 |
| Exner/Broca anatomical adjacency | H | Multiple neurology sources |
| Exner/speech co-activation during writing | L-M | Inferred from adjacency; not directly shown as simultaneous activation |
| VoT/WoT prior art | H | NeurIPS 2024, multiple papers |
| Sketch-of-Thought (B3) | H | arXiv:2503.05179, EMNLP 2025 |
| Token-budget-improves-quality claim | M | Mixed: SoT yes, Coupling Tax no |
| Scratchpad ephemerality as variable | L | Studied obliquely; no direct comparison found |
| Spatial/2D intermediate formats (general) | M | Active for spatial tasks; thin for general reasoning |
| Canvas-first prompting (sketch-first direction) | L | No published system found |

---

Sections to refresh: [Mueller post-2022 replication landscape; ephemerality-as-variable
direct comparison studies; canvas→reasoning (sketch-first-then-answer) systems if any
have shipped since this search; Exner/speech co-activation fMRI direct evidence]
