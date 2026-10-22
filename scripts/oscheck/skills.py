from __future__ import annotations

import re
from pathlib import Path

from .common import Issue, is_iso_date, parse_frontmatter, relative_path
from .decisions import _h2_headings

NAME = re.compile(r"^[a-z0-9-]{1,64}$")


def check_skills(root: Path, config: dict) -> list[Issue]:
    issues: list[Issue] = []
    skill_paths = sorted((root / "skills").glob("*/SKILL.md")) if (root / "skills").exists() else []
    skill_names = {path.parent.name for path in skill_paths}
    aliases = root / ".claude" / "skills"
    alias_names = {path.name for path in aliases.iterdir()} if aliases.is_dir() else set()

    for path in skill_paths:
        rel = relative_path(root, path)
        name = path.parent.name
        parsed = parse_frontmatter(path.read_text(encoding="utf-8"))
        if parsed.data is None:
            issues.append(Issue(rel, parsed.error_line, "skills", parsed.error))
            continue
        data = parsed.data
        if data.get("name") != name:
            issues.append(Issue(rel, 2, "skills", "frontmatter name must match the skill folder"))
        if not NAME.fullmatch(str(data.get("name", ""))):
            issues.append(Issue(rel, 2, "skills", "name must match ^[a-z0-9-]{1,64}$"))
        description = data.get("description")
        if not isinstance(description, str) or not 1 <= len(description) <= 1024:
            issues.append(Issue(rel, 2, "skills", "description must contain 1 to 1024 characters"))
        metadata = data.get("metadata")
        if not isinstance(metadata, dict):
            issues.append(Issue(rel, 2, "skills", "metadata must be a mapping"))
            metadata = {}
        if "version" in metadata and (not isinstance(metadata["version"], str) or not metadata["version"].strip()):
            issues.append(Issue(rel, 2, "skills", "metadata.version must be a non-empty string when present"))
        if metadata.get("type") != "skill":
            issues.append(Issue(rel, 2, "skills", "metadata.type must be 'skill'"))
        if not isinstance(metadata.get("status"), str) or metadata["status"] not in set(config["statuses"]):
            issues.append(Issue(rel, 2, "skills", f"invalid skill status '{metadata.get('status', '')}'"))
        if not is_iso_date(metadata.get("last_reviewed")):
            issues.append(Issue(rel, 2, "skills", "metadata.last_reviewed must be an ISO date"))
        headings = [heading for _, heading in _h2_headings(parsed.body)]
        cursor = 0
        for required in config["required_skill_sections"]:
            try:
                cursor = headings.index(required, cursor) + 1
            except ValueError:
                issues.append(Issue(rel, 1, "skills", f"required H2 section missing or out of order: '{required}'"))
                break
        alias = aliases / name
        if not alias.is_symlink():
            issues.append(Issue(relative_path(root, alias), 1, "skills", "each skill must have a .claude/skills symlink"))
        else:
            expected = (root / "skills" / name).resolve()
            if alias.resolve() != expected:
                issues.append(Issue(relative_path(root, alias), 1, "skills", "symlink must resolve to the matching skills/<name> directory"))
    for extra in sorted(alias_names - skill_names):
        issues.append(Issue(relative_path(root, aliases / extra), 1, "skills", "symlink has no matching skills/<name>/SKILL.md"))
    return issues
