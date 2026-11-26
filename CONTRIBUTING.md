# Contributing

Contributions that improve correctness, portability, clarity, or submission readiness are welcome.

## Guidelines

- Keep `SKILL.md` focused on the core workflow and reference routing; put detailed playbooks in `references/`.
- Preserve the four issue categories: Contribution, Validity, Evidence, and Presentation.
- Keep official venue rules separate from historical instructions, public author examples, and third-party advice.
- Never add fabricated results, citations, reviewer comments, or venue requirements.
- Use imperative, actionable instructions and avoid duplicating the same rule across multiple files.
- Link every new reference directly from `SKILL.md` and keep reference links one level deep.
- Keep the skill name and directory name synchronized.

## Validation

Run:

```bash
python scripts/validate_skill.py
```

Pull requests should pass the GitHub Actions validation workflow. When changing trigger descriptions or workflow behavior, also review `tests/acceptance_cases.md` and confirm that the expected behaviors remain covered.
