@AGENTS.md

# Claude Code notes

- Read `INDEX.md` first for retrieval, then follow the task router in `AGENTS.md`.
- When a task involves gathering inspiration or visual/interactive references, use `taste/`: start at `taste/README.md`, then `taste/swipe-file.md`, `taste/discovery-sources.md`, `taste/award-site-teardowns.md` and `taste/studio-websites.md`; cite the specific source page used.
- Skills are discovered through `.claude/skills` symlinks to `skills/`.
- Run `uv run python scripts/validate.py` before proposing a pull request.
- Use plan mode for strategy changes so a human can review the decision path.
- A human must approve any status change to `approved`.
