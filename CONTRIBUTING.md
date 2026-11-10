# Contributing

Thanks for keeping this list sharp. 谢谢帮助维护本列表。中文说明在下半部分。

## The bar for an entry

1. **Primary sources only.** arXiv abs page, official repo, or official lab blog. No aggregators, no tweets, no secondhand summaries.
2. **One line on what is being changed in the weights** — rows, columns, directions, task vectors — not just "editing".
3. **Family classification**: knowledge editing / steering & abliteration / task arithmetic & merging / unlearning / weight-space programming. Deep merging and unlearning bibliographies belong in their own dedicated lists (linked as related).
4. **Verification status where known**: tested-with-controls / scan-only / benchmarked / blog-only. Claims from blog-only works must be labeled as such.
5. **Scope**: direct modification of model weights (or activations used to edit behavior). Fine-tuning recipes and prompt optimization belong elsewhere; see the sibling matrix in the README.

## Checklist for PRs

- [ ] Added to the right family in **both** `README.md` and `README.zh-CN.md` (keep the two in sync).
- [ ] Link resolves (no 404) — yes, please actually click it.
- [ ] Family + one-line "what changes in the weights" + verification status included.
- [ ] One-line description, English in `README.md`, 中文在 `README.zh-CN.md`。

## 贡献指南（中文）

**收录门槛：**

1. **只链一手来源**——arXiv 页面、官方仓库或官方实验室博客；不收聚合站、推特转述或二手总结。
2. **一句话说明改了权重里的什么**——行、列、方向、任务向量——而不是笼统的"编辑"。
3. **家族归类**：知识编辑 / 转向与消融 / 任务算术与合并 / 遗忘 / 权重空间编程。合并与遗忘的深度书目请投各自的专门列表（已作相邻列表引用）。
4. **已知验证状态**：带对照测试 / 仅扫描 / 有基准 / 仅有博客。仅博客工作的主张必须如实标注。
5. **范围**：模型权重（或用于编辑行为的激活）的直接修改。微调配方与提示词优化不在本列表——见 README 的姊妹矩阵。

**PR 检查项：** 中英两个 README 同步更新；链接实际点开过；家族 + "改了权重里的什么"一句话 + 验证状态齐全；一句话描述中英各一份。
