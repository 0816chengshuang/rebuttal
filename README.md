# Rebuttal Assistant

A reusable, evidence-driven Agent Skill for analyzing peer reviews and preparing submission-ready conference rebuttals and journal response letters.

The skill follows the [open Agent Skills specification](https://agentskills.io/specification) and is organized for progressive disclosure: agents load the short description first, the main workflow when invoked, and detailed playbooks only when needed.

## What it does

- Classifies reviewer concerns as **Contribution**, **Validity**, **Evidence**, and **Presentation**.
- Separates issue nature: hidden concern, misunderstanding, substantive concern, limitation, or minor presentation issue.
- Prioritizes concerns by decision impact, reviewer scores, evidence gaps, and answerability.
- Builds an evidence inventory and proposes targeted experiments or clarifications without inventing results.
- Drafts Chinese logic versions and concise academic-English responses.
- Researches the target venue's current official rebuttal rules, templates, portal fields, and character limits.
- Adapts the final output to reviewer-specific fields, common-response fields, confidential editor/AC fields, or journal point-by-point response letters.

## Repository structure

```text
.
├── .agents/skills/rebuttal-assistant/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── references/
├── scripts/validate_skill.py
├── .github/workflows/validate.yml
├── CONTRIBUTING.md
├── CHANGELOG.md
├── LICENSE
└── README.md
```

## Compatibility

- Portable core: Agent Skills `SKILL.md` with standard `name` and `description` metadata, Markdown instructions, and relative `references/` resources.
- Codex repository discovery: `.agents/skills/rebuttal-assistant/`.
- ChatGPT desktop UI metadata: `agents/openai.yaml`.
- Other compatible agents: install through the [skills CLI](https://github.com/vercel-labs/skills) or the agent's documented skill directory.

## Install

### Codex (global install)

Requires Node.js and the `skills` CLI (invoked through `npx`):

```bash
npx skills add https://github.com/0816chengshuang/rebuttal/tree/main/.agents/skills/rebuttal-assistant -g -a codex
```

### Claude Code (global install)

```bash
npx skills add https://github.com/0816chengshuang/rebuttal/tree/main/.agents/skills/rebuttal-assistant -g -a claude-code
```

### Other supported agents

The `skills` CLI supports multiple Agent Skills-compatible tools. Select the relevant agent with `-a`; see the [CLI documentation](https://github.com/vercel-labs/skills) for the current supported-agent list.

### Update after a new release

```bash
npx skills update rebuttal-assistant
```

Check installation:

```bash
npx skills list
```

In Codex, invoke explicitly with `$rebuttal-assistant` or let the agent select it from a matching request. ChatGPT desktop also supports standalone skills; add the skill through the app's current Skills workflow, then invoke it from the Skills selector with `@`. The `npx skills` CLI installation command above targets supported coding agents and should not be assumed to install a skill into ChatGPT web chat.

## How to use

Example prompts:

- `Use $rebuttal-assistant to classify these reviews and identify the three highest-priority concerns.`
- `Use $rebuttal-assistant to research the official rebuttal rules for [venue, year] before drafting.`
- `Use $rebuttal-assistant to turn this Chinese response plan into a concise English rebuttal under the official character limit.`
- `Use $rebuttal-assistant to audit this response against the journal's point-by-point requirements.`

For the most accurate result, provide the submitted manuscript version, complete reviewer reports, verified experiment results, and the target venue/edition. The skill can begin with partial material but will label unknowns rather than guessing.

## Validate locally

No third-party Python dependencies are required:

```bash
python scripts/validate_skill.py
```

A GitHub Actions workflow runs the same validation on pushes and pull requests. Manual behavior checks are documented in [`tests/acceptance_cases.md`](tests/acceptance_cases.md).

## Scope and limitations

This repository provides reusable instructions and reference material; it does not guarantee acceptance or replace author verification. Venue policies change, so every submission must be checked against the current official instructions and the live submission portal. If no public official template is found, the skill must say so and distinguish historical or third-party examples from official requirements.

## References

- [Agent Skills specification](https://agentskills.io/specification)
- [OpenAI: Build skills for ChatGPT and Codex](https://learn.chatgpt.com/docs/build-skills)
- [Vercel skills CLI](https://github.com/vercel-labs/skills)
