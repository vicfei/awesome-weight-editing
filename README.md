<div align="center">

# Awesome Weight Editing

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](LICENSE)
[![Radar](https://github.com/vicfei/awesome-weight-editing/actions/workflows/radar.yml/badge.svg)](https://github.com/vicfei/awesome-weight-editing/actions/workflows/radar.yml)
[![Last commit](https://img.shields.io/github/last-commit/vicfei/awesome-weight-editing)](https://github.com/vicfei/awesome-weight-editing/commits)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**The map of modifying model weights directly — knowledge editing, steering &
abliteration, task arithmetic & merging, unlearning, and the brand-new
weight-space programming wave.**

English · [简体中文](README.zh-CN.md)

🤖 **Daily arXiv radar:** [docs/radar.md](docs/radar.md) — auto-refreshed every day.

</div>

---

## The thesis

Training is not the only way to change what a model does. A second family of
techniques treats **weights as the directly editable substrate**: locate the
rows/columns/directions that encode a behavior, and write to them — with no
gradient step. This list maps that family across its five subfields, from the
2021-era knowledge-editing classics to the weight-space programming wave that
started in November 2026.

Two companions make the triangle:

- **Theory** — the "modification operator" framing lives in
  [awesome-agentic-ml](https://github.com/vicfei/awesome-agentic-ml) §Weight editing
  (capability acquisition / transfer / behavioral surgery).
- **Practice** — [modifyllm](https://github.com/vicfei/modifyllm) implements this
  operator as a transaction: edit → screened against random controls → committed
  with a receipt → rollback-able.

## The five families

| Family | Changes what | Signal | Representative |
|---|---|---|---|
| **Knowledge editing** | Individual facts | (subject, relation, object) edits | ROME, MEMIT, EasyEdit |
| **Steering & abliteration** | Behavior directions | Contrastive pairs of activations | Refusal direction, CAA, RepE |
| **Task arithmetic & merging** | Whole capabilities | Task vectors, ± composition | Task arithmetic, mergekit |
| **Unlearning** | Deletion of knowledge/skills | Forget-set only | TOFU, WMDP |
| **Weight-space programming** | Anything an LLM can read | An LLM reads the weights and writes | Sparks of WSP |

## Weight-space programming (the November 2026 wave)

| Work | What it is |
|---|---|
| [Sparks of Weight Space Programming](https://rikiyat.github.io/blog/weight-space-programming/) · [full experiment logs](https://github.com/RikiyaT/lm_understand-logs) — MIT CSAIL | The origin: an LLM natively reads weights (which game this policy plays) and writes them; a 0.016% rank-1 edit lifts Qwen3.5-0.8B MATH-500 from 7.9% to 48.1%. Blog-only; complete logs published. |
| [Auditing clinical decision networks](https://arxiv.org/abs/2611.05341) | First follow-up paper: WSP as an audit lens for clinical networks. |
| [Image-restoration diffusion models](https://arxiv.org/abs/2611.04268) | WSP with a recursive improvement loop — the WSP × RSI crossover. |
| [weight-space-galaxy10](https://github.com/DaybreakWannaCode/weight-space-galaxy10) | All 475k CNN weights written from closed-form statistics, no gradients: 73.7% vs 82.4% trained. |
| [weight-space-programming-skill](https://github.com/di37/weight-space-programming-skill) | The technique packaged as a Claude Code skill, with random-control screening. |
| [model-weight-editing-lab](https://github.com/Teylersf/model-weight-editing-lab) | Ongoing direct edits of a 27B model; honest about failures. |
| [modifyllm](https://github.com/vicfei/modifyllm) | The transactional toolkit for this whole list: edits with receipts, controls, and rollback. |

## Knowledge editing (the classics)

| Year | Work | Contribution |
|---|---|---|
| 2021 | [MEND](https://arxiv.org/abs/2104.08164) | Learned editors that fix factual errors via low-rank weight updates. |
| 2022 | [ROME](https://arxiv.org/abs/2202.05262) | Locate-then-edit: causal tracing finds where a fact lives; a rank-one update writes it. |
| 2022 | [Knowledge Neurons](https://arxiv.org/abs/2104.08696) | Neurons that express a fact, found by attribution. |
| 2023 | [MEMIT](https://arxiv.org/abs/2210.07229) | ROME scaled to thousands of simultaneous edits. |
| 2023 | [EasyEdit](https://arxiv.org/abs/2308.07269) · [code](https://github.com/zjunlp/EasyEdit) | The standard toolkit: plug-and-play editing methods over one interface. |
| 2023 | [Knowledge Editing Survey](https://arxiv.org/abs/2310.16218) | The field's map of methods and evaluation. |

## Steering and abliteration

| Year | Work | Contribution |
|---|---|---|
| 2023 | [Representation Engineering](https://arxiv.org/abs/2310.01405) | Top-down: read and steer "truth", "honesty", "fairness" directions. |
| 2023 | [CAA](https://arxiv.org/abs/2312.06681) | Contrastive activation addition steers persona and behavior at inference. |
| 2024 | [Refusal is a single direction](https://arxiv.org/abs/2406.11717) · [abliterator](https://github.com/FailSpy/abliterator) | One direction mediates refusal — and ablating it from weights unlocks it. The canonical *weight-side* steering result. |
| 2026 | [How Far Can You Steer?](https://arxiv.org/abs/2611.06001) | Behavior-capability frontiers of contrastive steering — where steering stops being free. |

## Task arithmetic and merging

| Work | What it is |
|---|---|
| [Editing Models with Task Arithmetic](https://arxiv.org/abs/2212.04089) | Task vectors: add to install a skill, subtract to remove, negate to forget. |
| [mergekit](https://github.com/arcee-ai/mergekit) | The production toolkit for composing model weights (TIES, DARE, SLERP…). |
| [Awesome-Model-Merging](https://github.com/EnnengYang/Awesome-Model-Merging-Methods-Theories-Applications) | The deep map of this subfield (survey companion) — merging lives there. |

## Unlearning

| Work | What it is |
|---|---|
| [Who's Harry Potter?](https://arxiv.org/abs/2310.02238) | Approximate unlearning of a whole book series from an LLM. |
| [TOFU](https://arxiv.org/abs/2401.06121) | Fictitious-author benchmark: forget cleanly, retain the rest. |
| [WMDP](https://arxiv.org/abs/2403.03218) | Measuring and reducing hazardous knowledge. |
| [awesome-llm-unlearning](https://github.com/chrisliu298/awesome-llm-unlearning) | The deep map of this subfield — unlearning lives there. |

## Benchmarks

| Benchmark | Measures | Link |
|---|---|---|
| **MQuAKE** | Multi-hop ripple effects of an edit | [paper](https://arxiv.org/abs/2305.14795) |
| **TOFU** | Forget-set vs retain-set tradeoff | [paper](https://arxiv.org/abs/2401.06121) |
| **WMDP** | Hazardous-knowledge removal | [paper](https://arxiv.org/abs/2403.03218) |

## Pitfalls and safety

- [Unveiling the Pitfalls of Knowledge Editing](https://arxiv.org/abs/2310.02129) — edited models answer the target fact and fail the reasoning around it: the ripple-effect warning for every family above.
- **Ablation is symmetric.** The same rank-one removal that deletes a thinking loop deletes refusal (see the refusal-direction row). Any editing tooling must ship with verification — this is [modifyllm](https://github.com/vicfei/modifyllm)'s core stance (random controls, frozen single evaluation, rollback receipts).
- Unlearning is approximate: WMDP/TOFU measure reduction, not absence.

## 🤖 Radar

`docs/radar.md` is regenerated **daily** by [`scripts/radar.py`](scripts/radar.py) (GitHub Actions, [workflow](.github/workflows/radar.yml)) from arXiv new-submission listings, keyword-filtered for editing-family titles. Tune the keywords via PR.

## Related lists

- [SajjadPSavoji/awesome-weight-space-programming](https://github.com/SajjadPSavoji/awesome-weight-space-programming) and [brighterr/awesome-weight-space-programming](https://github.com/brighterr/awesome-weight-space-programming) — same-week WSP lists (Nov 2026); this list aims to cover the whole editing family, not only the wave.
- [EnnengYang/Awesome-Model-Merging](https://github.com/EnnengYang/Awesome-Model-Merging-Methods-Theories-Applications) · [chrisliu298/awesome-llm-unlearning](https://github.com/chrisliu298/awesome-llm-unlearning) — subfield deep maps cited above.
- Sibling matrix: [awesome-self-improving-coding-agents](https://github.com/vicfei/awesome-self-improving-coding-agents) (code) · [awesome-agentic-ml](https://github.com/vicfei/awesome-agentic-ml) (model & data production, operator theory) · [awesome-chatbi](https://github.com/vicfei/awesome-chatbi) (data serving) · [awesome-ai-native](https://github.com/vicfei/awesome-ai-native) (organization) · [modifyllm](https://github.com/vicfei/modifyllm) (the toolkit).

## Contributing

PRs welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). The bar: primary sources, one line on **what is being changed in the weights**, family classification, and verification status (tested/scanned-only/benchmark) where known.

## License

[CC0 1.0](LICENSE) — public domain.
