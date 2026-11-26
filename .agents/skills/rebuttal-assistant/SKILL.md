---
name: rebuttal-assistant
description: Analyze peer-review reports and prepare evidence-based, submission-ready rebuttals and journal response letters. Use when a researcher shares reviewer comments, scores, weaknesses, questions, rebuttal drafts, or asks for response strategy, official rebuttal-format research, point-by-point replies, revision responses, or character-limit editing.
license: MIT
---

# Rebuttal Assistant

## Purpose

Help researchers understand reviewer concerns, decide what evidence is needed, and prepare accurate, persuasive responses that fit the target conference or journal's actual submission process. The workflow is especially suited to computer-science and machine-learning venues, but can be adapted to other peer-reviewed fields.

The goal is not to argue with reviewers. It is to reduce uncertainty about the paper's contribution, methodological validity, experimental evidence, and presentation so that reviewers and editors can make an informed decision.

## When to use

Use this skill when the user asks to:
- analyze reviewer reports, scores, weaknesses, questions, or meta-reviews;
- classify concerns and prioritize responses;
- plan additional experiments or evidence;
- draft, translate, revise, or compress a conference rebuttal;
- prepare a journal point-by-point response letter;
- research official rebuttal instructions, templates, portal fields, or character limits;
- audit a response before submission.

Do not use it for generic paper writing unless the task is specifically about responding to peer review.

## Non-negotiable principles

1. **Respectful, not submissive.** Be professional and calm. Acknowledge valid concerns without adopting unsupported negative conclusions.
2. **Direct answer first.** Answer the specific question before explaining background or pointing to manuscript locations.
3. **Evidence over assertion.** Support claims with verified manuscript content, experiments, calculations, or sources.
4. **No fabricated work.** Never invent results, baselines, statistical significance, citations, section numbers, figure/table references, or completed revisions.
5. **Bounded claims.** Distinguish what the evidence establishes from what it does not establish. Do not infer causality from correlation or generalize beyond the evaluated setting.
6. **Credible commitments.** Promise revisions or experiments only when they are feasible and permitted by the target venue's rules.
7. **Preserve the argument.** Develop the complete reasoning before compressing it to a word or character limit.
8. **Submission-aware.** The final deliverable must match the actual portal fields or journal response-letter requirements, not an assumed generic template.

For detailed tone and argument principles, read [Core Principles](references/01_core_principles.md).

## Intake: establish the working context

Use information already provided; do not ask the user to repeat it. Identify, where available:

- target conference/journal, year or edition, track/article type, and review stage;
- reviewer IDs, scores, full comments, questions, and meta-review;
- the exact submitted manuscript version;
- existing experiments, code, analyses, and facts the authors can verify;
- deadline and practical ability to run additional experiments;
- portal fields, character/word limits, and formatting restrictions, if known.

If information is missing, proceed with the analysis that is still possible and label unknowns. Ask only the most important clarification when it blocks the next step. If the venue or edition is unknown, review analysis may proceed, but do not claim the final response is submission-compliant until the target format is verified.

## End-to-end workflow

### Step 0 — Research the official submission format (mandatory before final drafting)

Research the exact venue, edition, track, submission type, and review stage. Use available web-search or browser tools, prioritizing current official sources:

1. Current official author instructions, rebuttal instructions, FAQ, CFP, announcements, and submission-portal guidance.
2. Official organizer, society, publisher, or journal-editorial instructions.
3. Prior-year official instructions, clearly labeled with their year and treated as historical evidence only.
4. Public author examples and third-party templates, clearly labeled as non-official writing references.

Verify whether there is a downloadable official template or only portal fields; response structure; reviewer-specific and common-response fields; confidential AC/editor fields; word/character limits and counting rules; Markdown/LaTeX/table/image/link/attachment restrictions; anonymity; and rules on new experiments or revision promises. For journals, also check point-by-point response letters, tracked-changes and clean manuscripts, editor cover letters, and change-location requirements.

Produce a concise **Submission Format Brief** with source links, dates, applicability, and unresolved items. If no current official template is found, say so explicitly; do not manufacture one. If critical rules are visible only after login, ask the user for portal screenshots or field descriptions. If search tools are unavailable, disclose that the research is incomplete and request official links or portal evidence.

Read [Submission Format Research](references/10_submission_format_research.md) for the source hierarchy, research checklist, and brief format.

### Step 1 — Parse reviewer comments faithfully

Extract each reviewer ID, score, strength, weakness, question, and concrete request. Preserve the reviewer's meaning and intensity. Keep original wording available for traceability; do not silently turn a tentative concern into a definitive accusation.

### Step 2 — Diagnose each issue on two dimensions

**Content category** (multiple labels may apply):
- **Contribution** — novelty, originality, significance, and distinction from prior work.
- **Validity** — methodological rationale, assumptions, derivations, correctness, and scope.
- **Evidence** — baselines, datasets, fairness, metrics, ablations, robustness, and statistical support.
- **Presentation** — motivation, notation, related work, figures, organization, and clarity.

**Issue nature** (multiple labels may apply):
- **Hidden concern** — a plausible underlying concern behind the wording; label it as an inference, not a fact.
- **Misunderstanding** — relevant material may already exist but was unclear or overlooked.
- **Substantive concern** — a real evidence, method, or reasoning gap.
- **Limitation** — a genuine boundary that needs to be acknowledged and scoped.
- **Minor presentation issue** — a specific editorial or explanatory repair.

Use [Reviewer Issue Taxonomy](references/02_review_taxonomy.md) when detailed diagnosis is needed.

### Step 3 — Prioritize

Rank issues by likely impact on the decision, severity, reviewer score, overlap across reviewers, evidence gap, and answerability within the rebuttal window. Give particular attention to low-scoring reviewers' central objections, but do not ignore a high-scoring reviewer's critical correctness concern.

Do not apply a fixed priority order mechanically. Evidence and Validity often matter greatly, but Contribution may be decisive when novelty is the core rejection reason.

### Step 4 — Choose a response strategy

For each issue, decide whether the best response is to:
- clarify an existing point and cite its exact location;
- explain the motivation and mechanism;
- compare against the closest prior work;
- add a relevant experiment, ablation, or analysis;
- explain fairness and limitations of comparisons;
- acknowledge a real limitation and bound its impact;
- propose a specific manuscript change, if permitted.

Read [Response Strategy Playbook](references/03_response_playbook.md) for issue-specific methods.

### Step 5 — Build an evidence inventory

For every substantive claim, record its provenance and status:
- **Verified in supplied material** — directly supported by the manuscript, data, code, or result provided.
- **Author-confirmed** — explicitly confirmed by the user but not independently inspectable.
- **Proposed** — an experiment or analysis that has not yet been run.
- **Unknown / pending** — requires confirmation; do not use as a factual claim.

Track direct answer, manuscript location, result, missing evidence, proposed action, and conclusion boundary. Never describe a proposed experiment as completed. Read [Evidence and Experiments](references/05_evidence_and_experiments.md) when evidence planning is substantial.

### Step 6 — Draft the Chinese logic version

Unless the user requests otherwise, first organize the complete reasoning in Chinese:
1. What exactly is the reviewer asking?
2. What is the authors' direct answer or position?
3. What verified evidence supports it?
4. What clarification, concession, or qualification is needed?
5. What does the evidence establish, and what is its boundary?
6. What specific change is proposed or completed, and where?

### Step 7 — Draft or revise the English response

Preserve the Chinese argument, evidence, and qualifications. Use concise, natural academic English. Answer each question directly, place key evidence near the claim, and avoid repetitive thanks, vague claims, and unsupported certainty. Read [Writing and Length Control](references/06_writing_and_length.md) and [Response Templates](references/04_templates.md) when useful.

### Step 8 — Adapt to the actual submission interface

Generate field-ready text based on the Submission Format Brief:
- separate reviewer fields: output each field independently;
- one combined field: output one complete response in the required order;
- common plus reviewer-specific fields: keep them separate and avoid losing individual concerns;
- confidential AC/editor field: draft separately and label it confidential;
- journal response letter: follow the journal's point-by-point structure and identify manuscript changes and locations as required.

Never invent a portal field. If the actual interface is unknown, label the structure as provisional and state what must be checked. Include character/word counts for each field when useful, and state the counting method if the official counter is unavailable.

### Step 9 — Final audit

Run the [Quality Checklist](references/09_quality_checklist.md). Re-check the official rules, reviewer order, field mapping, length, anonymity, links/attachments, and every factual claim. The final response should be ready to paste or upload, subject only to explicitly listed author confirmations.

## Output modes

Choose only what the user needs; do not force every stage into every answer:

- **Review analysis** — reviewer-by-reviewer translation, classification, and core concerns.
- **Strategy plan** — priorities, evidence gaps, and response actions.
- **Chinese logic draft** — complete argument before English drafting.
- **English rebuttal** — field-ready reviewer responses.
- **Journal response letter** — point-by-point response with manuscript-change references.
- **Revision / compression** — improve an existing draft while preserving its meaning and evidence.
- **Submission audit** — policy, length, formatting, evidence, and tone checks.

## Reference map

Load only the references needed for the current stage:

- [01 Core Principles](references/01_core_principles.md) — stance, tone, evidence, limitations, and commitments.
- [02 Reviewer Issue Taxonomy](references/02_review_taxonomy.md) — four categories and issue-nature labels.
- [03 Response Strategy Playbook](references/03_response_playbook.md) — Contribution, Validity, Evidence, Presentation, and cross-cutting cases.
- [04 Response Templates](references/04_templates.md) — adaptable English response patterns.
- [05 Evidence and Experiments](references/05_evidence_and_experiments.md) — baseline fairness, ablations, statistics, and evidence provenance.
- [06 Writing and Length Control](references/06_writing_and_length.md) — Chinese-to-English drafting, compression, tone, and counting.
- [07 Workflow and Output Formats](references/07_workflow_and_output.md) — planning tables and deliverable modes.
- [08 Tools and Submission](references/08_tools_and_submission.md) — optional preview tools and submission safety.
- [09 Quality Checklist](references/09_quality_checklist.md) — final review gate.
- [10 Submission Format Research](references/10_submission_format_research.md) — official source hierarchy, venue rules, and portal-ready format research.

## Prohibitions

- Do not fabricate experiments, results, citations, statistical significance, or manuscript locations.
- Do not treat an inferred hidden concern as a reviewer's stated intent.
- Do not disguise a genuine limitation as a misunderstanding.
- Do not equate unclear presentation with an invalid method.
- Do not claim a baseline comparison is fair when material conditions differ without explaining them.
- Do not promise experiments, revisions, or camera-ready changes that are infeasible or disallowed.
- Do not describe proposed work as completed work.
- Do not present historical or third-party templates as current official requirements.
- Do not mix confidential editor/AC notes into public reviewer responses.
- Do not compress away a direct answer, decisive evidence, or a necessary qualification merely to meet a character limit.
