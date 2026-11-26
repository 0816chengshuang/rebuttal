# 03 — Response Strategy Playbook

## Contents

- [1. Contribution](#1-contribution创新性与贡献不足)
- [2. Validity](#2-validity方法合理性与可信度)
- [3. Evidence](#3-evidence实验充分性公平性与可信度)
- [4. Presentation](#4-presentation表达与清晰度)
- [5. Hidden Concern](#5-hidden-concern回应言外之意)
- [6. Misunderstanding](#6-misunderstanding处理误解)
- [7. Substantive Concern](#7-substantive-concern实质性质疑)
- [8. Limitation](#8-limitation承认局限)

## 1. Contribution：创新性与贡献不足

### 诊断
找到审稿人认为最接近的已有工作，确认其质疑针对任务设定、关键假设、方法机制、能力还是结果。

### 推荐策略：差异拆解

从三个维度说明差异：
1. **任务 / 问题不同**：解决更实际、更困难或更一般化的问题。
2. **方法机制不同**：关键假设、目标函数、建模方式或推理流程不同。
3. **能力 / 结果不同**：带来新的能力、新结论或更好的表现。

### 推荐证据
- 最接近 prior work 的直接比较。
- 任务设定、关键假设、方法机制、能力/结果对比表。
- 消融或实验结果。
- 相关工作引用和明确定位。

### 避免
- 只说“We are novel”。
- 回避最接近的工作。
- 只谈性能，不解释方法机制差异。
- 只强调模块名称不同，却没有说明实质区别。

一句话组织思路：
“我们并非只是将 X 用于 Y，而是在 Z 设定下提出 M，从而带来 N 能力。”
这是逻辑模板，必须用论文真实内容填充。

## 2. Validity：方法合理性与可信度

### 推荐策略：四步证据链

1. **Motivation**：为什么需要该设计？它解决什么问题？
2. **Mechanism**：模块/方法如何工作？为什么可能解决该问题？
3. **Evidence**：消融、敏感性分析、理论分析或失败案例如何支持解释？
4. **Revision**：论文中将如何补充机制、推导、假设或适用边界？

### 推荐方法
- Ablation Study。
- Sensitivity Analysis。
- 澄清假设与推导步骤。
- 补充 Failure Case 或适用边界。

### 避免
- 情绪化辩护。
- 只说“效果好”，不解释为什么。
- 掩盖真实的小错误。
- 从单个消融结果过度推断理论机制完全成立。

一句话组织思路：
“模块 M 的设计动机是……；其作用机制是……；实验显示移除 M 后……，这支持了该模块在……方面的作用。”

## 3. Evidence：实验充分性、公平性与可信度

### 常见问题
- 缺少关键 Baseline。
- 数据集规模或覆盖不足。
- 实验比较不公平。
- 指标不完整。
- 缺少统计显著性、消融或关键分析。

### 推荐策略
1. 能补关键实验时，优先补充最相关、最强的 Baseline。
2. 明确比较条件与公平性。
3. 补充关键消融、统计分析或错误分析。
4. 若不能补实验，具体说明原因，并提供真实的替代证据和结论边界。

### 公平性检查
- Same backbone。
- Same data split。
- Same training budget。
- Same metrics。
- Same or reasonably equivalent tuning fairness。

### 避免
- 仅以资源限制作为拒绝补实验的理由。
- 说某个 baseline 不重要，却不提供依据。
- 堆砌无关实验。
- 未控制实验条件却宣称比较完全公平。
- 以不完整指标支持过强结论。

## 4. Presentation：表达与清晰度

| 审稿问题 | 具体修改动作 |
|---|---|
| Motivation unclear | 重写 Introduction 中的问题动机和研究缺口 |
| Notation confusing | 增加 Notation Table，统一符号 |
| Related work incomplete | 补充关键相关工作及差异比较 |
| Figure unclear | 重绘流程图、补充图注或标注 |
| Limitations missing | 增加局限性讨论并界定适用范围 |

### 回复要求
- 不要只说“We will improve the writing”。
- 说明具体修改动作。
- 指出准确位置：Section / Figure / Table / Equation / Appendix。
- 多个审稿人反复指出同一表达问题时，可合并修复，但仍应逐一回应其关注点。

## 5. Hidden Concern：回应言外之意

示例：
“It is unclear whether the improvement comes from the proposed module or the larger model size.”

可能的真实顾虑：
- 提升是否只是参数量增加的结果？
- 模块是否具有独立贡献？
- 创新是否只是模型规模扩张？

优先策略：
- 如果可行，设计参数量或计算预算可比的 baseline。
- 报告控制模型规模后的结果。
- 解释实验如何隔离模块效果。
- 若无法补实验，说明限制并用已有证据限定结论。

核心原则：不要只解释事实，要用事实解除疑虑。

## 6. Misunderstanding：处理误解

示例：
“The method does not consider temporal information.”
但原稿 Section 3.2 已经介绍 Temporal Encoding Layer。

推荐步骤：
1. 礼貌感谢。
2. 指出原稿具体位置。
3. 用简短文字直接解释该设计。
4. 承认原稿表述可能不够突出。
5. 说明具体的澄清或修改动作（如规则允许）。

不要讽刺审稿人没有认真阅读。也不要把真实缺失包装成误解。

## 7. Substantive Concern：实质性质疑

- 明确回答质疑。
- 判断是否需要补实验或分析。
- 使用最直接、最有区分力的证据。
- 如果无法补充，说明原因、替代证据和结论边界。
- 不要以泛泛解释代替关键证据。

## 8. Limitation：承认局限

- 承认具体事实，不扩大其影响。
- 说明局限影响哪些设置、不影响哪些核心结论。
- 用现有证据支持影响边界。
- 不作无法兑现的未来承诺。
