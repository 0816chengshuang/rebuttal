# 04 — Response Templates

## Contents

- [1. 通用结构](#1-通用结构)
- [2. 解释疑问 / 言外之意](#2-解释疑问--言外之意图片提供的原始模板)
- [3. 处理误解](#3-处理误解图片提供的原始模板)
- [4. 回应结果重要性/质疑](#4-回应结果重要性质疑图片提供的原始模板)
- [5. 创新性差异拆解模板](#5-创新性差异拆解模板)
- [6. Validity 四步证据链模板](#6-validity-四步证据链模板)
- [7. Evidence / Baseline 公平性模板](#7-evidence--baseline-公平性模板)

所有模板仅供适配，不应机械复制。方括号内容必须替换为真实信息。使用前确认会议规则是否允许承诺修改稿件。

## 1. 通用结构

```text
[Optional] Common Response

Response to Reviewer [ID]

Q1: [Concise summary of the concern]

A1: [Direct answer.]
    [Evidence from the manuscript or additional experiments.]
    [Clarification or qualification.]
    [Specific revision action and location, if permitted.]
    [Concluding statement.]
```

## 2. 解释疑问 / 言外之意（图片提供的原始模板）

```text
Thank you for this insightful comment regarding
[xxx, e.g., model size vs. module effect].
To directly address this concern, we conducted
an additional experiment on XXX. The results,
preliminarily showing X% gain attributed to the
module, confirm the effectiveness of our proposed
component beyond just parameter count. We will
include this detailed analysis in the revised
manuscript in Section XXX. We hope this clarifies
the source of the improvement.
```

使用条件：
- 确实完成了对应实验。
- X% 的归因有合理实验设计支持。
- “preliminarily” 和 “confirm” 等措辞与证据强度匹配。
- 只有规则允许时才保留 “We will include...”。

## 3. 处理误解（图片提供的原始模板）

```text
Thank you for your comment regarding XX topic.
We addressed this in Section XXX, where we detail
[brief mention, e.g., our temporal encoding layer].
We acknowledge the presentation may have lacked
clarity, and we will revise Section XXX by
[specific action, e.g., adding emphasis /
rephrasing] to make this point more prominent
in the final version. We hope this clarification
helps.
```

使用条件：
- 论文确实已经包含相关内容。
- Section XXX 必须准确。
- 如果原稿并未包含该设计，不得使用此模板伪装成误解。
- 修改承诺须符合会议规则。

## 4. 回应结果重要性/质疑（图片提供的原始模板）

```text
Regarding the significance of our results:
The X% improvement achieved on xxx represents
a meaningful advance within the context of XX
Task. This is particularly relevant because
[briefly state context justifying significance,
e.g., this benchmark is highly competitive /
state-of-the-art has seen diminishing returns /
it addresses a known bottleneck]. In addition
to this performance gain, our method provides
benefits in [efficiency/robustness/...]. We will
ensure this context highlighting the significance
is clearly integrated into the XXX section of
the revised manuscript.
```

使用条件：
- X% 和任务名称准确。
- “meaningful advance”等评价必须有背景或证据支撑。
- 效率、鲁棒性等额外优势必须有数据支持。
- 不得无依据宣称 benchmark 饱和或 SOTA 提升空间有限。
- 修改承诺须符合会议规则。

## 5. 创新性差异拆解模板

逻辑骨架：
- 先承认论文可能没有充分突出差异（如果属实）。
- 明确最接近的已有工作。
- 分别解释任务设定、方法机制、能力/结果的差异。
- 说明差异为什么重要。
- 引用对比表、公式、方法章节或实验。

可使用的句型片段：
- “Our work differs from [prior work] in three aspects.”
- “Unlike [prior work], we address [specific setting].”
- “The key distinction lies in [mechanism/assumption/objective].”
- “This design enables [capability], as supported by [evidence].”

## 6. Validity 四步证据链模板

```text
The motivation for module M is [specific problem].
Mechanistically, M [explain how it works].
The ablation/sensitivity analysis in [Table/Figure]
shows [verified result], supporting [bounded conclusion].
We will clarify [specific explanation] in [location],
if the conference rules permit manuscript changes.
```

## 7. Evidence / Baseline 公平性模板

```text
Following the reviewer's suggestion, we conducted
a comparison with [Baseline] under [verified conditions].
Specifically, [backbone], [data split], [training budget],
and [metrics] were [the same / controlled as described].
The results show [exact result]. This supports
[appropriately bounded conclusion].
```

只有实际控制了相应条件，才能声称公平比较。若条件不完全相同，应明确差异而不是隐藏。

## 8. 表达问题模板

```text
Thank you for pointing this out. We agree that
the description of [specific topic] could be clearer.
We will [specific action] in [exact location] so that
[the intended concept / notation / workflow] is explicit.
```

不要只写“We will improve the writing”。如果会议不允许承诺修改，应在当前回复中直接给出澄清。

## 9. Common Response

适用情况：多个审稿人提出同一共性问题，且统一说明不会掩盖个别问题。

```text
Common Response: [Shared concern]

We thank the reviewers for raising this common concern.
[Direct shared answer.]
[Shared evidence and exact manuscript locations.]
[Specific action, if permitted.]
```

随后仍应在 Reviewer-specific response 中补充各自独有的问题，必要时简短指向 Common Response。

## 10. 语言和承诺替换提醒

- 不要把已完成的实验写成 “We will conduct...”；直接报告结果。
- 不要在无法保证时写 “We will add...”；可改为当前回复中直接澄清。
- 不要为了礼貌写 “We agree that our method lacks novelty”，除非作者确实接受这一结论。
- 可以承认表达问题：“We agree that the presentation could be clearer”，但不能因此承认方法无效。
