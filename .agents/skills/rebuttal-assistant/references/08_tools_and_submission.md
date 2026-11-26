# 08 — Tools and Submission

## 1. OpenReview Preview

用户提供的项目：
https://github.com/CYandYue/Openreview-Preview

根据用户提供的项目介绍，工具为单 HTML 本地预览页面，包含：
- Markdown 实时预览。
- LaTeX 公式预览。
- 表格预览。
- 字符计数。
- Markdown 导入与导出。

用途：在本地撰写和检查格式，降低直接在 OpenReview 对话框中调整格式的风险。

注意：
- 这是第三方开源项目，不是 OpenReview 官方工具。
- 当前记录基于用户提供的项目介绍；未在本 Skill 中独立审计代码或验证兼容性。
- 本地预览不保证与 OpenReview 官方渲染完全一致。
- 最终应在实际投稿系统中检查。
- 使用者应自行评估代码、依赖和安全性。

## 2. Conference rules checklist

每次投稿都应核对当届官方说明：
- Rebuttal 是否开放以及截止时间。
- 字符/字数限制。
- 字符计数规则。
- 是否匿名。
- 是否允许外部链接或附件。
- 是否允许表格、公式和 Markdown。
- 是否允许新增实验结果。
- 是否允许承诺 Camera Ready 修改。
- 是否允许与审稿人进行额外沟通。
- 是否有禁止披露的信息。

不要将某届 ACL、ICLR 或其他会议的规则泛化为长期规则。

## 3. Submission safety

- 在外部编辑器中保存副本。
- 提交前检查 Reviewer ID、段落顺序、公式和表格。
- 避免将 Cancel、Save、Submit 等操作混淆。
- 最终粘贴后再次核对字符数和渲染。
- 不要在未确认内容时点击 Submit。


## 4. Mandatory format research before drafting

不要默认所有会议都采用同一种 Rebuttal 模板。按以下来源顺序调研：

1. **当前届官方来源**：Author Guidelines、Rebuttal Instructions、FAQ、CFP、官方公告及投稿系统中的 Author Response / Rebuttal 页面。
2. **主办方或出版机构来源**：会议组织方、学会、出版社或期刊编辑部发布的规则。
3. **往届官方材料**：只能作为历史参考，必须标注届次，不能直接推定本届仍适用。
4. **公开作者范例**：只作为写法参考，不是官方要求。
5. **第三方经验材料**：博客、教程、个人模板仅供参考，不能覆盖官方规则。

建议检索：
- `[venue] [year] rebuttal instructions`
- `[venue] [year] author response guidelines`
- `[venue] rebuttal template`
- `[publisher/journal] response to reviewers template`
- `[venue] OpenReview author response character limit`
- `[venue] rebuttal FAQ`

核对具体年份/届次、Track、投稿类型和评审阶段；是否有官方可下载模板或只是系统文本框；回复字段布局；字符/字数限制；Markdown、LaTeX、表格、图片、链接和附件限制；匿名要求；是否允许新增实验、补充材料和 Camera Ready 承诺。

若未找到官方模板，明确写出“未检索到该届公开的官方统一模板”，并说明检索过的官方来源。以当届官方规则和实际系统字段为准构建提交结构。往届或公开作者样例只能标注为“非官方参考”。如果关键要求只能在登录后的投稿系统中看到，提醒用户提供页面截图或字段说明后再定稿。

## 5. Submission Format Brief

正式起草前，先向用户汇报：

| 项目 | 调研结果 |
|---|---|
| Venue / year / track | [具体信息] |
| Official template | [有/未找到/仅系统字段] |
| Official response structure | [具体结构] |
| Submission fields | [单框/Reviewer 分栏/Common + individual/其他] |
| Character or word limit | [限制及计数方式] |
| Formatting restrictions | [Markdown/LaTeX/table/link/attachment] |
| Anonymity and confidentiality | [要求] |
| Additional experiments / revision promises | [允许范围] |
| Sources | [官方来源链接、发布日期、适用届次] |
| Unverified items | [需要作者登录系统确认的内容] |

## 6. Final output must be portal-ready

最终稿应按系统的真实字段交付：分栏提交则每位 Reviewer 单独成稿；单框提交则输出完整合并稿；Common Response 与 Reviewer-specific 字段分别输出；AC / Editor confidential note 单独输出；期刊 point-by-point response 按编辑部要求组织。不得因为通用模板更美观就忽略实际系统字段和格式。
