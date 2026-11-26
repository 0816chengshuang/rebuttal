# 02 — Reviewer Issue Taxonomy

## Contents

- [A. 四类核心问题](#a-四类核心问题)
- [B. 第二维度：问题性质](#b-第二维度问题性质)
- [C. 交叉诊断](#c-交叉诊断)
- [D. 不要混淆](#d-不要混淆)

## A. 四类核心问题

### 1. Contribution — 新意与贡献

核心问题：这篇论文新不新、贡献是否清晰、是否值得接收？

常见质疑：
- Novelty 不足。
- 贡献偏增量。
- 与已有工作相似。
- Significance 不足。

审稿人想确认：
- 工作是否超出已有方法的简单组合或参数扩张？
- 与最接近工作的本质差异是什么？
- 这些差异为什么重要？
- 新方法带来了什么新能力、新结论或更好的表现？

### 2. Validity — 合理性与可信度

核心问题：方法设计是否合理，假设、推导和结论是否站得住？

常见质疑：
- 设计看起来 ad-hoc。
- 方法机制不清楚。
- 假设不合理。
- 理论、推导或证明存在疑问。

审稿人想确认：
- 为什么需要该设计？
- 模块如何起作用？
- 关键假设是否合理？
- 实验或理论是否支持作者的解释？
- 方法适用边界是什么？

### 3. Evidence — 实验与证据

核心问题：实验是否充分、公平、可靠？

常见质疑：
- 缺少关键 Baseline。
- 数据集规模不足。
- 比较不公平。
- 指标不完整。
- 缺少统计显著性、消融或关键分析。

审稿人想确认：
- 实验是否足以支持论文结论？
- 比较条件是否公平？
- 结果是否稳定、可信？
- 是否存在关键对照缺失？

### 4. Presentation — 表达与清晰度

核心问题：论文是否清楚、成熟、易于理解？

常见质疑：
- Motivation 不清楚。
- Notation 混乱。
- Related Work 不完整。
- Figure 不清晰。
- Limitations 未充分说明。

审稿人想确认：
- 问题、方法和贡献是否讲清楚？
- 符号和图表是否容易理解？
- 相关工作是否覆盖关键研究？
- 局限是否透明？

## B. 第二维度：问题性质

四类内容分类之外，还要判断审稿人提出问题的性质：

1. **Hidden Concern（言外之意）**：表面质疑背后可能有更深层担忧。例如“提升是否来自更大模型”可能意味着审稿人担心贡献只是参数量增加。
2. **Misunderstanding（误解）**：论文已有内容未被理解，或原稿表达不够清楚。
3. **Substantive Concern（实质性质疑）**：论文确实需要补充实验、论证或分析。
4. **Limitation（局限）**：客观存在、需要承认并界定影响范围的问题。
5. **Minor Presentation Issue（轻微表达问题）**：可通过具体编辑动作修复的问题。

一条意见可以同时属于多个类别。例如：
- “The gain may come from a larger model” = Contribution + Evidence，且可能包含 Hidden Concern。
- “The method does not consider temporal information”，但论文已有 Temporal Encoding = Validity + Presentation，可能是 Misunderstanding。
- “Missing a strong baseline” = Evidence，通常是 Substantive Concern。

不要把对审稿人动机的推断当作事实，应使用“可能的真实关注点”表述。

## C. 交叉诊断

对每条意见至少记录：

| 字段 | 内容 |
|---|---|
| Reviewer / 原文 | 审稿人编号及原始意见 |
| Issue category | Contribution / Validity / Evidence / Presentation，可多选 |
| Issue nature | Hidden Concern / Misunderstanding / Substantive Concern / Limitation / Minor Issue |
| Core concern | 审稿人真正需要确认的事项 |
| Severity | 高 / 中 / 低 |
| Existing evidence | 原稿中已有的证据 |
| Evidence gap | 目前缺少什么 |
| Recommended response | 澄清、实验、分析、承认局限或修改表达 |
| Required author input | 需要作者补充或确认的事实 |

## D. 不要混淆

- “审稿人误解”不等于“审稿人一定错”；先核对原稿。
- “表达不清”不等于“方法无效”。
- “性能提升”不自动证明方法机制合理。
- “有新模块”不自动证明创新性。
- “无法补实验”不自动意味着现有证据充分。
