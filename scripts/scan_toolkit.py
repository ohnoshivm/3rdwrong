#!/usr/bin/env python3
"""Compare this Mac's local toolkit with the proposed department registry.

Local inventory only: no network, subprocesses, configuration writes or secrets
in output. PyYAML is the sole dependency (already in the repository environment).
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import tomllib

import yaml


REPO = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".trash"}
MCP_ALIASES = {"hyperframes": "hyperframes", "claude docs": "claude-docs",
               "chatcut-desktop": "chatcut_desktop"}
JOBS = {
    "direction": {"research", "inspiration-taste", "category-audit", "concept-direction",
                  "art-direction", "verbal-identity", "ux-research-methods"},
    "identity-craft": {"typography", "colour", "mark-logo", "composition-layout",
                       "image-generation-direction", "design-system-guidelines", "handover-specs", "presentation"},
    "living-digital": {"motion-principles", "motion-implementation", "generative-creative-coding",
                       "realtime-3d", "ui-build", "interaction-architecture", "video-motion-graphics"},
    "critique-qa": {"concept-critique", "ux-audit", "accessibility", "originality-audit",
                    "visual-qa-browser", "performance", "consistency-qa"},
    "outside": {"strategy", "marketing", "engineering", "quality-security", "operations", "workflow", "business", "media", "other"},
}


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9_.-]+", "-", value.lower()).strip("-")


def public_path(path: Path, home: Path, repo: Path) -> str:
    """Keep machine usernames and absolute checkout locations out of the registry."""
    try:
        return path.relative_to(repo).as_posix()
    except ValueError:
        try:
            return "~/" + path.relative_to(home).as_posix()
        except ValueError:
            return str(path)


def read_json(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    return value if isinstance(value, dict) else {}


def walk_files(root: Path, errors: list[str]):
    """Follow skill-directory symlinks, without escaping into cycles or hiding failures."""
    if not root.exists():
        return
    visited: set[tuple[int, int]] = set()

    def onerror(error: OSError):
        errors.append(f"Cannot scan {error.filename}: {error.strerror}")

    for folder, dirs, files in os.walk(root, followlinks=True, onerror=onerror):
        path = Path(folder)
        try:
            stat = path.stat()
        except OSError as error:
            onerror(error)
            dirs[:] = []
            continue
        identity = (stat.st_dev, stat.st_ino)
        if identity in visited:
            dirs[:] = []
            continue
        visited.add(identity)
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
        for name in sorted(files):
            yield path / name


def skill_header(path: Path) -> tuple[str, str, str]:
    """Read the requested first forty lines, plus complete frontmatter if longer."""
    content = path.read_text(encoding="utf-8")
    lines = content.splitlines()
    excerpt = "\n".join(lines[:40])
    metadata: dict = {}
    if lines and lines[0].strip() == "---":
        end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
        if end is not None:
            try:
                parsed = yaml.safe_load("\n".join(lines[1:end]))
                if isinstance(parsed, dict):
                    metadata = parsed
            except yaml.YAMLError:
                # Some installed upstream skills contain unquoted ':' descriptions.
                # Preserve their header rather than silently dropping the candidate.
                pass
    name = str(metadata.get("name") or path.parent.name)
    description = str(metadata.get("description") or "")
    if not description:
        match = re.search(r"^description:\s*(.+)$", excerpt, re.MULTILINE)
        description = match.group(1).strip("\"'") if match else excerpt
    return name, " ".join(description.split()), excerpt


def plugin_for(path: Path, root: Path) -> str:
    """Use the closest real plugin manifest; layout inference is the fallback."""
    for parent in path.parents:
        if parent == root.parent:
            break
        for candidate in (parent / ".claude-plugin/plugin.json",
                          parent / ".codex-plugin/plugin.json", parent / "plugin.json"):
            if candidate.is_file():
                try:
                    name = read_json(candidate).get("name")
                    if name:
                        return slug(str(name))
                except (OSError, ValueError):
                    continue
    parts = path.relative_to(root).parts
    if parts[0] in {"cache", "marketplaces", "synced"}:
        parts = parts[1:]
    if "plugins" in parts[:-1]:
        return slug(parts[parts.index("plugins") + 1])
    if "external_plugins" in parts[:-1]:
        return slug(parts[parts.index("external_plugins") + 1])
    if len(parts) > 1 and parts[1] == "app":
        return slug(parts[0])
    if len(parts) >= 2:
        # cache/<marketplace>/<plugin>/<version>, marketplaces/<market>/<plugin>
        return slug(parts[1])
    return slug(parts[0])


def discover(home: Path, repo: Path) -> tuple[dict[str, dict], list[str]]:
    found: dict[str, dict] = {}
    errors: list[str] = []

    def add(tool_id: str, kind: str, name: str, source: str, availability: str,
            path: Path, description: str = "", excerpt: str = "", plugin: str = ""):
        occurrence = {"source": source, "availability": availability,
                      "path": public_path(path, home, repo)}
        if excerpt:
            occurrence["header_sha256"] = hashlib.sha256(excerpt.encode()).hexdigest()
        record = found.setdefault(tool_id, {"id": tool_id, "kind": kind, "name": name,
                                  "plugin": plugin, "description": description,
                                  "excerpt": excerpt, "occurrences": []})
        if occurrence not in record["occurrences"]:
            record["occurrences"].append(occurrence)

    roots = [(home / ".claude/skills", "claude-skill", "claude", False),
             (home / ".claude/skills-library", "parked-claude-skill", "claude", False),
             (home / ".agents/skills", "codex-skill", "codex", False),
             (home / ".codex/skills", "codex-skill", "codex", False),
             (home / ".config/opencode/skills", "shared-skill-library", "both", False),
             (home / "creative-engineering-os/library/skills", "ceos-reference-library", "both", False),
             (home / ".claude/plugins", "plugin-skill", "claude", True),
             (home / ".claude/cowork_plugins", "plugin-skill", "claude", True),
             (home / ".codex/plugins/cache", "plugin-skill", "codex", True),
             (repo / "skills", "repo-skill", "repo", False)]
    plugin_roots: list[tuple[Path, str]] = []
    for root, source, availability, is_plugin in roots:
        if is_plugin:
            plugin_roots.append((root, availability))
        for path in walk_files(root, errors):
            if is_plugin and path.suffix == ".md" and "agents" in path.relative_to(root).parts[:-1] and path.name.lower() != "readme.md":
                try:
                    name, description, excerpt = skill_header(path)
                    plugin = plugin_for(path, root)
                    add(f"agent:{plugin}:{slug(path.stem)}", "agent", name,
                        "plugin-agent", availability, path, description, excerpt, plugin)
                except (OSError, UnicodeError) as error:
                    errors.append(f"Cannot read {public_path(path, home, repo)}: {type(error).__name__}")
            if path.name != "SKILL.md":
                continue
            try:
                name, description, excerpt = skill_header(path)
                plugin = plugin_for(path, root) if is_plugin else ""
                # Directory names are stable across provider-specific display names.
                stem = slug(path.parent.name)
                tool_id = f"{plugin}:{stem}" if plugin else f"skill:{stem}"
                kind = "plugin-skill" if is_plugin else ("repo-skill" if availability == "repo" else "skill")
                add(tool_id, kind, name, source, availability, path, description, excerpt, plugin)
            except (OSError, UnicodeError) as error:
                errors.append(f"Cannot read {public_path(path, home, repo)}: {type(error).__name__}")

    for root, kind, availability in [(home / ".claude/agents", "agent", "claude"),
                                     (repo / ".claude/agents", "upstream-agent", "repo")]:
        for path in walk_files(root, errors):
            if path.suffix != ".md":
                continue
            try:
                name, description, excerpt = skill_header(path)
                namespace = "agent" if kind == "agent" else "agency"
                add(f"{namespace}:{slug(path.stem)}", kind, name, kind, availability,
                    path, description, excerpt)
            except (OSError, UnicodeError) as error:
                errors.append(f"Cannot read {public_path(path, home, repo)}: {type(error).__name__}")

    def add_mcp(name: str, path: Path, availability: str, plugin: str = ""):
        canonical = MCP_ALIASES.get(name.lower(), slug(name))
        add(f"mcp:{canonical}", "mcp", name, "mcp-config", "mcp", path,
            f"Configured MCP server: {name}. Transport details and credentials are not inventoried.",
            plugin=plugin)

    def mcp_json(path: Path, availability: str, plugin: str = ""):
        try:
            data = read_json(path)
            for key in ("mcpServers", "mcp_servers"):
                servers = data.get(key, {})
                if isinstance(servers, dict):
                    for name in servers:
                        add_mcp(name, path, availability, plugin)
                elif isinstance(servers, str):
                    # Plugin manifests may point to an adjacent .mcp.json.
                    target = path.parent.parent / servers.removeprefix("./")
                    if target.is_file() and target != path:
                        mcp_json(target, availability, plugin)
            # Claude stores project-scoped MCP declarations in its global config.
            for project in data.get("projects", {}).values():
                if isinstance(project, dict):
                    for name in project.get("mcpServers", {}):
                        add_mcp(name, path, availability, plugin)
            # A plugin's .mcp.json can be the server mapping itself.
            if path.name == ".mcp.json" and not {"mcpServers", "mcp_servers"} & data.keys():
                for name, config in data.items():
                    if isinstance(config, dict) and any(k in config for k in ("command", "url", "type")):
                        add_mcp(name, path, availability, plugin)
        except (OSError, ValueError, TypeError) as error:
            errors.append(f"Cannot inspect MCP declarations in {public_path(path, home, repo)}: {type(error).__name__}")

    for path in (home / ".claude.json", home / ".claude/settings.json", repo / ".mcp.json"):
        if path.is_file():
            mcp_json(path, "claude")
    for root, availability in plugin_roots:
        for path in walk_files(root, errors):
            if path.name == ".mcp.json" or (path.name == "plugin.json" and path.parent.name in {".claude-plugin", ".codex-plugin"}):
                mcp_json(path, availability, plugin_for(path, root))
    config = home / ".codex/config.toml"
    if config.is_file():
        try:
            data = tomllib.loads(config.read_text(encoding="utf-8"))
            for name in data.get("mcp_servers", {}):
                add_mcp(name, config, "codex")
        except (OSError, ValueError) as error:
            errors.append(f"Cannot inspect Codex MCP declarations: {type(error).__name__}")

    for record in found.values():
        record["occurrences"].sort(key=lambda item: (item["availability"], item["path"]))
        providers = {item["availability"] for item in record["occurrences"]}
        record["availability"] = "both" if "both" in providers or {"claude", "codex"} <= providers else sorted(providers)[0]
        record["path"] = record["occurrences"][0]["path"]
    return dict(sorted(found.items())), errors


def validate_registry(data: dict) -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()
    if data.get("schema_version") != 1 or data.get("status") != "proposed" or data.get("owner") != "founder":
        errors.append("Registry requires schema_version: 1, status: proposed and owner: founder")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(data.get("last_reviewed", ""))):
        errors.append("Registry requires last_reviewed in YYYY-MM-DD format")
    leads: Counter = Counter()
    for entry in data.get("tools", []):
        if not isinstance(entry, dict):
            errors.append("Each tool must be a mapping")
            continue
        label = str(entry.get("id", "<missing id>"))
        for key in ("id", "kind", "source", "availability", "summary", "sub_department", "role", "job"):
            if not isinstance(entry.get(key), str) or not entry[key].strip():
                errors.append(f"{label}: missing {key}")
        if label in seen:
            errors.append(f"Duplicate registry id: {label}")
        seen.add(label)
        if entry.get("kind") not in {"skill", "plugin-skill", "agent", "upstream-agent", "mcp", "repo-skill"}:
            errors.append(f"{label}: invalid kind")
        if entry.get("sub_department") not in {"direction", "identity-craft", "living-digital", "critique-qa", "outside"}:
            errors.append(f"{label}: invalid sub_department")
        if entry.get("job") not in JOBS.get(entry.get("sub_department"), set()):
            errors.append(f"{label}: job does not belong to sub_department")
        if entry.get("availability") not in {"claude", "codex", "both", "mcp", "repo", "claude-managed"}:
            errors.append(f"{label}: invalid availability")
        if entry.get("install_state") not in {"active", "parked", "reference-library", "plugin-cache", "account-managed", "declared"}:
            errors.append(f"{label}: invalid install_state")
        division = entry.get("division")
        if division is not None:
            if division not in {"strategy", "design", "media", "marketing", "engineering", "quality-security", "business", "operations"}:
                errors.append(f"{label}: invalid division")
            if (division == "design") == (entry.get("sub_department") == "outside"):
                errors.append(f"{label}: division and Design ownership disagree")
        role = entry.get("role")
        if role not in {"lead", "specialist", "bench", "outside"}:
            errors.append(f"{label}: invalid role")
        if role == "specialist" and not entry.get("trigger"):
            errors.append(f"{label}: specialist requires trigger")
        if role in {"bench", "outside"} and not entry.get("reason"):
            errors.append(f"{label}: {role} requires reason")
        if (role == "outside") != (entry.get("sub_department") == "outside"):
            errors.append(f"{label}: outside role and placement must agree")
        if not (entry.get("path") or entry.get("url")):
            errors.append(f"{label}: missing path or url")
        if role == "lead":
            leads[entry.get("job")] += 1
    for job, count in leads.items():
        if count > 2:
            errors.append(f"{job}: {count} leads exceeds the maximum of two")
    aliases = data.get("discovery_aliases", {})
    if not isinstance(aliases, dict):
        errors.append("discovery_aliases must be a mapping")
    else:
        for alias, target in aliases.items():
            if not isinstance(alias, str) or not isinstance(target, str) or target not in seen:
                errors.append(f"Invalid discovery alias: {alias}")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", action="store_true", help="Print departmental and role counts")
    parser.add_argument("--home", type=Path, default=Path.home(), help="Alternate home for isolated fixture checks")
    parser.add_argument("--repo", type=Path, default=REPO, help="Alternate repository for isolated fixture checks")
    parser.add_argument("--registry", type=Path, help="Override the registry path")
    args = parser.parse_args(argv)
    registry_path = args.registry or args.repo / "studio/departments/design-toolkit.yaml"
    try:
        data = yaml.safe_load(registry_path.read_text(encoding="utf-8"))
        if not isinstance(data, dict) or not isinstance(data.get("tools"), list):
            raise ValueError("Expected a mapping containing a tools list")
    except (OSError, ValueError, yaml.YAMLError) as error:
        print(f"Registry error: {error}", file=sys.stderr)
        return 2
    errors = validate_registry(data)
    if errors:
        for error in errors:
            print(f"ERROR {error}", file=sys.stderr)
        return 2
    found, scan_errors = discover(args.home.resolve(), args.repo.resolve())
    errors.extend(scan_errors)
    entries = {entry["id"]: entry for entry in data["tools"]}
    # Aliases explicitly merge the same skill exposed by different packaging.
    aliases = data.get("discovery_aliases", {})
    resolved = {aliases.get(tool_id, tool_id) for tool_id in found}
    missing = sorted(resolved - entries.keys())
    absent = sorted(tool_id for tool_id, entry in entries.items()
                    if tool_id not in resolved and entry.get("verification") != "founder-reported-remote"
                    and entry.get("availability") != "claude-managed")
    remote = [entry for entry in entries.values() if entry.get("verification") == "founder-reported-remote" and entry["kind"] == "mcp"]
    managed = [entry for entry in entries.values() if entry.get("availability") == "claude-managed"]
    for tool_id in missing:
        print(f"UNCLASSIFIED {tool_id}")
    for tool_id in absent:
        print(f"NO LONGER INSTALLED {tool_id}")
    for error in errors:
        print(f"ERROR {error}", file=sys.stderr)
    occurrences = sum(len(record["occurrences"]) for record in found.values())
    print(f"Found: {occurrences} local occurrences; {len(resolved)} deduplicated local tools")
    print(f"Unclassified: {len(missing)}; no longer installed: {len(absent)}; inventory/registry errors: {len(errors)}")
    print(f"Remote founder-reported MCPs (connection not verified): {len(remote)}")
    print(f"Account-managed Claude tools (removal not locally verifiable): {len(managed)}")
    if args.report:
        counts = Counter((entry["sub_department"], entry["role"]) for entry in entries.values())
        print("Department | Lead | Specialist | Bench | Outside | Total")
        for department in ("direction", "identity-craft", "living-digital", "critique-qa", "outside"):
            values = [counts[department, role] for role in ("lead", "specialist", "bench", "outside")]
            print(f"{department} | " + " | ".join(map(str, values + [sum(values)])))
        print(f"Registry total: {len(entries)}; listed but not found: {len(data.get('listed_but_not_found', []))}")
    # Stale entries fail as well: a clean result must mean the registry is current.
    return 2 if errors else (1 if missing or absent else 0)


if __name__ == "__main__":
    raise SystemExit(main())
