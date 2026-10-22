---
title: Getting started
type: guide
status: proposed
owner: founder
last_reviewed: 2026-10-22
---

# Getting started

Use this page to open the OS locally, make a first contribution, or start a fresh Claude Code session.

## For a human designer

1. Clone the public repository locally:

   ```bash
   git clone https://github.com/ohnoshivm/3rdwrong.git
   cd 3rdwrong
   ```

2. Install the locked dependency and validate the repository:

   ```bash
   uv sync --locked
   uv run python scripts/validate.py
   ```

3. Read the generated [`INDEX.md`](../INDEX.md) first, then open [`README.md`](../README.md) and choose the closest workflow in [`docs/workflows.md`](workflows.md). For a small writing fix, use GitHub's web editor and submit a pull request. For code or tool changes, regenerate the index and run the unit tests too.

## For a fresh Claude Code session

1. Start Claude Code from the repository root with `claude`.
2. Have it read `INDEX.md` first, then use `AGENTS.md` as the task router. Ask for a specific task and name the relevant input files.
3. Ask it to prepare a proposed change, not silently approve a policy or invent evidence.

Example first prompts:

- “Read the route for adding an agency study. Help me plan a source-based study of the supplied public work and mark claims Documented, Interpretation, Hypothesis, or Unknown.”
- “Read the identity-project route and prepare a proposed brief from these notes. Flag anything that needs private storage.”
- “Use the 3w-identity-system-critic skill on the supplied work. Return evidence-linked observations and questions for human review.”

## Keep the first task small

Read the route entry and the named files only. Check their status before reusing a claim. Run `uv run python scripts/validate.py` before submitting a change; run `uv run python -m unittest discover -s tests -q` if you changed validator or maintenance-tool code.

## Use as an Obsidian vault

Open the cloned repository folder as a vault. Notes remain plain Markdown with relative file links; wikilinks are not required, so they work in GitHub and other editors too. Obsidian's local settings directory is ignored by Git.
