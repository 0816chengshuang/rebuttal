#!/usr/bin/env python3
"""Dependency-free structural validator for the Rebuttal Assistant Agent Skill."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / ".agents" / "skills" / "rebuttal-assistant"
SKILL_FILE = SKILL_DIR / "SKILL.md"


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def check(condition: bool, message: str) -> None:
    if not condition:
        fail(message)
    print(f"PASS: {message}")


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        fail("SKILL.md must begin with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        fail("YAML frontmatter closing delimiter not found")
    raw = text[4:end]
    fields: dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = re.match(r"^([A-Za-z][A-Za-z0-9_-]*):\s*(.*?)\s*$", line)
        if not match:
            fail(f"Unsupported or malformed frontmatter line: {line}")
        key, value = match.groups()
        fields[key] = value.strip().strip('"').strip("'")
    return fields, text[end + 5 :]


def check_markdown_links(md_file: Path, text: str) -> None:
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        target = target.strip()
        if not target or target.startswith(("https://", "http://", "mailto:", "#")):
            continue
        target_path = target.split("#", 1)[0]
        if not target_path:
            continue
        resolved = (md_file.parent / target_path).resolve()
        check(resolved.exists(), f"local link exists: {md_file.relative_to(ROOT)} -> {target}")


def main() -> None:
    check(SKILL_FILE.is_file(), "SKILL.md exists at the standard skill path")
    text = SKILL_FILE.read_text(encoding="utf-8")
    fields, body = parse_frontmatter(text)

    check("name" in fields, "frontmatter contains name")
    check("description" in fields, "frontmatter contains description")

    name = fields.get("name", "")
    check(bool(re.fullmatch(r"[a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?", name)), "skill name uses valid lowercase kebab-case")
    check("--" not in name, "skill name has no consecutive hyphens")
    check(len(name) <= 64, "skill name is at most 64 characters")
    check(name == SKILL_DIR.name, "skill name matches its directory name")

    description = fields.get("description", "")
    check(bool(description), "description is non-empty")
    check(len(description) <= 1024, "description is at most 1024 characters")
    check("<" not in description and ">" not in description, "description contains no angle brackets")

    allowed = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
    check(set(fields).issubset(allowed), "frontmatter uses only standard Agent Skills fields")
    check(len(text.splitlines()) <= 500, "SKILL.md is at most 500 lines")

    # Check Markdown links in the main skill and all references.
    check_markdown_links(SKILL_FILE, text)
    references = sorted((SKILL_DIR / "references").glob("*.md"))
    check(bool(references), "reference directory contains Markdown resources")
    for ref in references:
        ref_text = ref.read_text(encoding="utf-8")
        check(bool(ref_text.strip()), f"reference is non-empty: {ref.relative_to(ROOT)}")
        check_markdown_links(ref, ref_text)

    openai_yaml = SKILL_DIR / "agents" / "openai.yaml"
    check(openai_yaml.is_file(), "agents/openai.yaml exists")
    openai_text = openai_yaml.read_text(encoding="utf-8")
    for key in ("display_name", "short_description", "default_prompt"):
        check(bool(re.search(rf"^\s*{key}:\s*\".+\"\s*$", openai_text, re.M)), f"OpenAI UI metadata contains quoted {key}")
    short_desc = re.search(r'^\s*short_description:\s*"(.*?)"\s*$', openai_text, re.M)
    if short_desc:
        check(25 <= len(short_desc.group(1)) <= 64, "OpenAI short description is 25–64 characters")
    default_prompt = re.search(r'^\s*default_prompt:\s*"(.*?)"\s*$', openai_text, re.M)
    if default_prompt:
        check("$rebuttal-assistant" in default_prompt.group(1), "default prompt explicitly invokes the skill")

    check((ROOT / "LICENSE").is_file(), "repository has a LICENSE file")
    check((ROOT / "README.md").is_file(), "repository has a README")
    print(f"\nSkill validation passed. {len(references)} reference files checked.")


if __name__ == "__main__":
    main()
