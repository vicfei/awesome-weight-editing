<div align="center">

# Awesome 权重编辑

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](LICENSE)
[![Radar](https://github.com/vicfei/awesome-weight-editing/actions/workflows/radar.yml/badge.svg)](https://github.com/vicfei/awesome-weight-editing/actions/workflows/radar.yml)
[![Last commit](https://img.shields.io/github/last-commit/vicfei/awesome-weight-editing)](https://github.com/vicfei/awesome-weight-editing/commits)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**直接修改模型权重的全景地图 —— 知识编辑、转向与消融、任务算术与合并、
遗忘，以及 2026 年 11 月刚爆发的权重空间编程浪潮。**

[English](README.md) · 简体中文

🤖 **每日 arXiv 雷达：** [docs/radar.md](docs/radar.md) —— 每天自动刷新。

</div>

---

## 核心论点

训练不是改变模型行为的唯一方式。第二个技术家族把**权重当作可直接编辑的基质**：定位编码某行为的行/列/方向，然后直接写入——没有任何梯度步。本列表绘制这个家族的五个子领域，从 2021 年的知识编辑经典到 2026 年 11 月开始的权重空间编程浪潮。

两个伙伴构成三角：

- **理论**——"修改算子"框架在 [awesome-agentic-ml](https://github.com/vicfei/awesome-agentic-ml) §权重编辑（能力获取/转移/行为手术）。
- **实践**——[modifyllm](https://github.com/vicfei/modifyllm) 把这个算子实现为事务：编辑 → 随机对照筛查 → 带回执提交 → 可回滚。

## 五个家族

| 家族 | 改什么 | 信号来源 | 代表 |
|---|---|---|---|
| **知识编辑** | 单条事实 | (主语, 关系, 宾语) 编辑对 | ROME、MEMIT、EasyEdit |
| **转向与消融** | 行为方向 | 激活对比对 | 拒绝方向、CAA、RepE |
| **任务算术与合并** | 整项能力 | 任务向量、加减组合 | Task Arithmetic、mergekit |
| **遗忘** | 删除知识/技能 | 仅遗忘集 | TOFU、WMDP |
| **权重空间编程** | LLM 能读懂的一切 | LLM 读权重再写 | Sparks of WSP |

## 权重空间编程（2026 年 11 月浪潮）

| 工作 | 是什么 |
|---|---|
| [Sparks of Weight Space Programming](https://rikiyat.github.io/blog/weight-space-programming/) · [完整实验日志](https://github.com/RikiyaT/lm_understand-logs) —— MIT CSAIL | 源头：LLM 原生读取权重（这个策略网络玩哪个游戏）并直接书写；对 Qwen3.5-0.8B 的 0.016% rank-1 编辑使 MATH-500 从 7.9% 升至 48.1%。仅有博客；完整日志已公开。 |
| [审计临床决策网络](https://arxiv.org/abs/2611.05341) | 首篇后续论文：WSP 作为临床网络的审计透镜。 |
| [图像修复扩散模型](https://arxiv.org/abs/2611.04268) | 带递归改进环的 WSP——与 RSI 的首次交叉。 |
| [weight-space-galaxy10](https://github.com/DaybreakWannaCode/weight-space-galaxy10) | 47.5 万 CNN 权重全部由闭式统计写就、无梯度：73.7% vs 梯度训练 82.4%。 |
| [weight-space-programming-skill](https://github.com/di37/weight-space-programming-skill) | 技术的 Claude Code skill 封装，自带随机对照筛查。 |
| [model-weight-editing-lab](https://github.com/Teylersf/model-weight-editing-lab) | 27B 模型的持续直接编辑实验；对失败诚实。 |
| [modifyllm](https://github.com/vicfei/modifyllm) | 本列表的事务化工具包：带回执、对照与回滚的编辑。 |

## 知识编辑（经典）

| 年份 | 工作 | 贡献 |
|---|---|---|
| 2021 | [MEND](https://arxiv.org/abs/2104.08164) | 学习型编辑器：以低秩权重更新修复事实错误。 |
| 2022 | [ROME](https://arxiv.org/abs/2202.05262) | 定位再编辑：因果追踪找到事实所在，rank-one 更新写入。 |
| 2022 | [Knowledge Neurons](https://arxiv.org/abs/2104.08696) | 用归因找到表达某事实的神经元。 |
| 2023 | [MEMIT](https://arxiv.org/abs/2210.07229) | ROME 规模化：数千条编辑同时进行。 |
| 2023 | [EasyEdit](https://arxiv.org/abs/2308.07269) · [代码](https://github.com/zjunlp/EasyEdit) | 标准工具箱：即插即用的编辑方法跑在同一接口上。 |
| 2023 | [知识编辑综述](https://arxiv.org/abs/2310.16218) | 该领域的方法与评测地图。 |

## 转向与消融

| 年份 | 工作 | 贡献 |
|---|---|---|
| 2023 | [Representation Engineering](https://arxiv.org/abs/2310.01405) | 自上而下：读取并操纵"诚实""公平"等表征方向。 |
| 2023 | [CAA](https://arxiv.org/abs/2312.06681) | 对比激活加法在推理时转向人设与行为。 |
| 2024 | [拒绝是单一方向](https://arxiv.org/abs/2406.11717) · [abliterator](https://github.com/FailSpy/abliterator) | 一个方向中介拒绝行为——从权重中消融它即可解除。权重侧转向的标志性结果。 |
| 2026 | [How Far Can You Steer?](https://arxiv.org/abs/2611.06001) | 对比转向的行为-能力边界——转向在哪里不再免费。 |

## 任务算术与合并

| 工作 | 是什么 |
|---|---|
| [Editing Models with Task Arithmetic](https://arxiv.org/abs/2212.04089) | 任务向量：加法安装技能、减法移除、取反遗忘。 |
| [mergekit](https://github.com/arcee-ai/mergekit) | 模型权重组合的生产级工具箱（TIES、DARE、SLERP…）。 |
| [Awesome-Model-Merging](https://github.com/EnnengYang/Awesome-Model-Merging-Methods-Theories-Applications) | 该子领域的深度地图（综述配套）——合并住在那里。 |

## 遗忘

| 工作 | 是什么 |
|---|---|
| [Who's Harry Potter?](https://arxiv.org/abs/2310.02238) | 从 LLM 中近似遗忘整套书。 |
| [TOFU](https://arxiv.org/abs/2401.06121) | 虚构作者基准：干净遗忘、保留其余。 |
| [WMDP](https://arxiv.org/abs/2403.03218) | 度量并削减危险知识。 |
| [awesome-llm-unlearning](https://github.com/chrisliu298/awesome-llm-unlearning) | 该子领域的深度地图——遗忘住在那里。 |

## 基准

| 基准 | 度量什么 | 链接 |
|---|---|---|
| **MQuAKE** | 编辑的多跳涟漪效应 | [论文](https://arxiv.org/abs/2305.14795) |
| **TOFU** | 遗忘集 vs 保留集的权衡 | [论文](https://arxiv.org/abs/2401.06121) |
| **WMDP** | 危险知识的移除 | [论文](https://arxiv.org/abs/2403.03218) |

## 陷阱与安全

- [Unveiling the Pitfalls of Knowledge Editing](https://arxiv.org/abs/2310.02129)——被编辑的模型答对了目标事实、却答错围绕它的一切：对上表每个家族都成立的涟漪效应警告。
- **消融是对称的。** 能删除思考循环的 rank-one 移除，同样能删除拒绝（见拒绝方向一行）。任何编辑工具都必须自带验证——这是 [modifyllm](https://github.com/vicfei/modifyllm) 的核心立场（随机对照、冻结单次评估、回滚回执）。
- 遗忘是近似的：WMDP/TOFU 度量的是削减，不是不存在。

## 🤖 雷达

`docs/radar.md` 由 [`scripts/radar.py`](scripts/radar.py)（GitHub Actions，[workflow](.github/workflows/radar.yml)）基于 arXiv 新提交列表**每天**重建，按编辑家族标题关键词过滤。欢迎提 PR 调整关键词。

## 相邻列表

- [SajjadPSavoji/awesome-weight-space-programming](https://github.com/SajjadPSavoji/awesome-weight-space-programming) 与 [brighterr/awesome-weight-space-programming](https://github.com/brighterr/awesome-weight-space-programming)——同周出现的 WSP 列表（2026-11）；本列表覆盖整个编辑家族，不止浪潮。
- [EnnengYang/Awesome-Model-Merging](https://github.com/EnnengYang/Awesome-Model-Merging-Methods-Theories-Applications) · [chrisliu298/awesome-llm-unlearning](https://github.com/chrisliu298/awesome-llm-unlearning)——上文引用的子领域深度地图。
- 姊妹矩阵：[awesome-self-improving-coding-agents](https://github.com/vicfei/awesome-self-improving-coding-agents)（代码）· [awesome-agentic-ml](https://github.com/vicfei/awesome-agentic-ml)（模型与数据生产、算子理论）· [awesome-chatbi](https://github.com/vicfei/awesome-chatbi)（数据服务）· [awesome-ai-native](https://github.com/vicfei/awesome-ai-native)（组织）· [modifyllm](https://github.com/vicfei/modifyllm)（工具）。

## 贡献

欢迎 PR —— 见 [CONTRIBUTING.md](CONTRIBUTING.md)。门槛：一手来源、一句话说明**改了权重里的什么**、家族归类、已知验证状态（已测试/仅扫描/有基准）。

## 许可

[CC0 1.0](LICENSE) —— 公共领域。
