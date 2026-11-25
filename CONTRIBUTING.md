# Contributing

Thanks for keeping this list sharp. 谢谢帮助维护本列表。中文说明在下半部分。

## The bar for an entry

1. **Primary sources only.** arXiv abs page, official repo, or official lab blog. No aggregators, no tweets, no secondhand summaries.
2. **One line on what is being changed in the weights** — rows, columns, directions, task vectors — not just "editing".
3. **Family classification**: knowledge editing / steering & abliteration / task arithmetic & merging / unlearning / weight-space programming. Deep merging and unlearning bibliographies belong in their own dedicated lists (linked as related).
4. **Evidence tier, stated explicitly**: peer-reviewed / preprint / blog-only / community-experiment — every claim inherits its tier, and blog-only headline numbers must be labeled as such.
5. **Decoding-regime caveat for behavioral edits**: if a headline number was measured with sampling (temperature, presence penalty), say so — edits whose gains evaporate under greedy decoding have happened (see the SGNE-CC audit in the README). Report greedy numbers when available.
6. **Reproduction contract, where claimable**: access mode (weights-only / forward passes / activations), search budget (attempts, model, tokens), construction (closed-form / fitted / learned), and evaluation (held-out splits, seeds). "No gradients" does not imply "no fitting"; a low parameter count does not imply low total storage.
7. **Scope**: direct modification of model weights (or activations used to edit behavior). Fine-tuning recipes and prompt optimization belong elsewhere; see the sibling matrix in the README.

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
4. **明确标注证据层级**：同行评审 / 预印本 / 仅有博客 / 社区实验——每个主张继承其层级，仅有博客的头条数字必须如实标注。
5. **行为类编辑的解码域限定**：头条数字若在采样设置（温度、presence penalty）下测得，必须注明——贪心解码下收益蒸发的情况已经发生过（见 README 中 SGNE-CC 审计）。有贪心数字时优先报告。
6. **可主张时的复现契约**：访问方式（仅权重 / 前向 / 激活）、搜索预算（尝试次数、所用模型、token 量）、构造方式（闭式 / 拟合 / 学习）、评测（held-out 划分与种子）。"无梯度"不等于"无拟合"；低参数量不等于低总存储。
7. **范围**：模型权重（或用于编辑行为的激活）的直接修改。微调配方与提示词优化不在本列表——见 README 的姊妹矩阵。

**PR 检查项：** 中英两个 README 同步更新；链接实际点开过；家族 + "改了权重里的什么"一句话 + 验证状态齐全；一句话描述中英各一份。
