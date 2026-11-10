# Local models with accessible weights and existing tooling

**2026-11-10 follow-up · research shortlist, no installation or benchmark.** Majkee clarified that Laya's appeal is precisely its accessible local model and adaptation path, and asked for supported alternatives without requiring Ollama. This is a bounded shortlist for the existing experiment, not an exhaustive catalogue or a newest-model ranking.

## Recommendation

Keep **Laya** as the typed-decision candidate. Add **multilingual MiniLM with a frozen encoder and a trained small head** as the simple linguistic comparison. Use **SetFit** only as a distinct later arm that also adapts the encoder. Add **Qwen3-0.6B** if flexible instructions/generation are required, or **SmolLM2-135M** for a smaller English experiment. ModernBERT is an optional English encoder comparison, not the first Czech target.

This preserves the original intent: inspect and modify local parameters using supported tools, then measure what those changes actually do. Running locally, having weights available, permitting modification under a licence, and reproducing the original training data/process are different properties. The shortlist establishes accessible model/tooling routes, not full training-data provenance or independently measured accuracy.

## Candidate map

| Candidate | Why it belongs | First experimental arm / limitation |
|---|---|---|
| **Laya** | Native typed questions; local parameters and documented head training. The model card labels the weights Apache-2.0. | Use its matching loader and multilingual checkpoint for Czech/English. Compare frozen inference, calibration and frozen-encoder head fitting separately; measure each rather than assuming vendor-like probability behavior. [Model card](https://huggingface.co/convaiinnovations/laya), [pinned training guide](https://github.com/NandhaKishorM/laya/blob/4444f2f56acdd31a633d594e9f3227f853241d9e/docs/finetune.md). |
| **Multilingual MiniLM + classifier; optional SetFit** | A conventional sentence encoder gives 384-dimensional features. Its card describes 50 languages, Apache-2.0 and a default 128-token input limit. SetFit supplies encoder adaptation plus a classifier; it is a framework rather than another checkpoint. | Start with frozen embeddings and logistic regression. Cache by input/preprocessing/encoder revision. Train a classifier on labelled Czech/English examples; language coverage is not task accuracy. Later compare SetFit encoder adaptation under the same split. [Encoder card](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2), [SetFit mechanism](https://huggingface.co/docs/setfit/conceptual_guides/setfit). |
| **ModernBERT-base** | Accessible English encoder, Apache-2.0; useful for task-specific classification after adding/fitting a head. | Optional English-only comparison. It is not a ready-made typed decision service, and its English card does not establish Czech suitability. [Model card](https://huggingface.co/answerdotai/ModernBERT-base). |
| **SmolLM2-135M / 360M Instruct** | Small Apache-2.0 generative checkpoints, primarily English. | Begin with 135M for a constrained A/B/NONE comparison or an adapter experiment. Generation adds parsing, abstention and malformed-output cases; 360M is a separate memory/quality tradeoff. [135M card](https://huggingface.co/HuggingFaceTB/SmolLM2-135M-Instruct), [360M card](https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct). |
| **Qwen3-0.6B** | Apache-2.0 generative model; the family documentation includes Czech and English. | Candidate for multilingual instruction-based decisions, with non-thinking mode fixed for the initial comparison. Family language support does not establish this checkpoint's task accuracy. [Model card](https://huggingface.co/Qwen/Qwen3-0.6B), [language coverage](https://qwenlm.github.io/blog/qwen3/). |

A fixed classifier normally learns a fixed label space; it does not acquire Laya's arbitrary-question interface simply because both return labels. For A/B/NONE choice with changing options, define how state, options and question enter the representation, retain their identities/order, and test unseen options. Encoding only the state and silently omitting the requested decision would be an invalid comparison. Similarity is a baseline, not an entailment guarantee; negation, numbers and contradictory evidence need explicit fixtures.

## No Ollama dependency is required

**For research and weight access:** use the supported Python stack directly—PyTorch/Transformers, Sentence Transformers, SetFit, or Laya's own loader as appropriate. Keep local checkpoint snapshots and pinned package versions. Training a head, adapting an encoder and fitting LoRA have different costs and artifacts; a LoRA result needs its matching base checkpoint and adapter configuration. [PEFT documentation](https://huggingface.co/docs/peft/quicktour).

**For standalone local inference:** llama.cpp provides a C/C++ runtime and supports quantized model execution. Its supported architectures and exact converter/runtime determine compatibility; a `.gguf` suffix does not make every custom model head executable. In particular, do not assume the Laya decision head maps onto a causal-language-model runtime. Train/adapt in a compatible training stack, then validate the intended deployment conversion and any adapter path. [llama.cpp](https://github.com/ggml-org/llama.cpp), [model support](https://github.com/ggml-org/llama.cpp/blob/master/docs/models.md), [Qwen3 local guide](https://github.com/QwenLM/Qwen3/blob/main/docs/source/run_locally/llama.cpp.md).

**For an exported frozen model:** ONNX Runtime is another deployment route. Treat export and quantization as transformations whose outputs and performance must be compared against the original checkpoint; this is not a training interface equivalent to PyTorch. [ONNX Runtime documentation](https://onnxruntime.ai/docs/).

These routes allow local execution after required files are acquired. Network-free operation must be tested with a complete local snapshot and dependencies; “downloadable model” alone does not establish offline reproducibility. No hosted account is inherently required to evaluate an already acquired compatible local checkpoint.

## Capacity and a fair first experiment

The [office observation](office-observation.json) is a point-in-time measurement, not a standing reservation: about 1.34 GiB available, no swap. Arithmetic alone gives approximately 1.34 GiB for 360 million FP32 parameters and 1.20 GiB for the source manual's roughly 322-million-parameter Laya multilingual checkpoint, before runtime/activations/loading peaks. Quantization changes those terms but does not establish a safe total job footprint. Home remains unmeasured beyond stale documentation. Even smaller models need live headroom and peak-RSS measurements.

For a bounded next study, choose one task and build independent train/dev/calibration/test examples before loading a model. Compare deterministic rules, frozen MiniLM+head and frozen Laya using equivalent evidence. Keep a separate task-native-window comparison if equal windows truncate required evidence; do not call it the same input experiment. Score Czech and English separately, with ambiguity, negation, option swaps, unseen labels and insufficient evidence. Measure load/warm latency, memory, label error, abstention and calibration where probability semantics are defined. A generated label is not automatically a calibrated probability.

Only after that result should a successor select one adaptation arm—head training, SetFit, or a generative adapter—and a fixed measured resource budget. For direct scalar-weight or recursive-function experiments, the tiny numerical network from the substrate is still more inspectable than a pretrained language model. This distinction leaves both research questions open without forcing them into one tool.

## Evidence and continuity

`/root/jev_sources` performed a bounded primary-source comparison; main verified decisive SetFit/encoder, model-card and runtime anchors. All recommendations are synthesis from documented mechanisms and the existing host receipt. No checkpoint download, installation, inference, training or performance benchmark occurred. The next-session transfer is [CS.nabla-lab-jev-local-models.2026-11-10.md](/home/hruzam/reposoma/_cold-start/card/CS.nabla-lab-jev-local-models.2026-11-10.md).
