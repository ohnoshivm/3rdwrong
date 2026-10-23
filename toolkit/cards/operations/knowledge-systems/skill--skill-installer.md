---
title: Skill Installer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:skill-installer
department: operations
sub_department: knowledge-systems
job: skill-authoring
role: specialist
trigger: "Use when the approved work needs this capability: Install Codex skills into $CODEX_HOME/skills from a curated list or a GitHub repo path. Use when a user asks to list installable skills, install a curated skill, or install a skill from another repo (including private repos)"
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/standalone-skill-installer-9d2c16be/skills/skill-installer/SKILL.md
invoke: "`skill:skill-installer` skill in Claude Code or Codex"
pairs_with: [skill-creator:skill-creator]
---
# Skill Installer

A specialist for skill authoring at 3RDWRONG, called when Install Codex skills into $CODEX_HOME/skills from a curated list or a GitHub repo path. Use when a user asks to list installable skills, install a curated skill, or install a skill from another repo (including private repos).

## What it does

- Install Codex skills into $CODEX_HOME/skills from a curated list or a GitHub repo path. Use when a user asks to list installable skills, install a curated skill, or install a skill from another repo (including…
- Install from the curated list when the user provides a skill name.
- Install from another repo when the user provides a GitHub repo/path (including private repos).
- `scripts/list-skills.py` (prints skills list with installed annotations)

## When to use

- Use when the approved work needs this capability: Install Codex skills into $CODEX_HOME/skills from a curated list or a GitHub repo path. Use when a user asks to list installable skills, install a curated skill, or install a skill from another repo (including private repos)
- In a 3RDWRONG project, use during the relevant skill authoring task and pass its output to the project owner for review.

## When not to use

- Do not use when the request falls outside skill authoring or fails the registered specialist trigger.
- Do not use its output as client approval, verified research or professional advice.
- For the paired skill-creator:skill-creator work, use that tool and hand off this artefact.

## Inputs it needs

- The target skill, agent, plugin or command and its repository/context, plus the requested create/review outcome.
- Relevant documents, source links and constraints; keep client records and personal data in the approved private store.

## How to run it

1. Check the task against the registered job and trigger.
2. Read the source instructions and provide the minimum necessary inputs.
3. Invoke the tool using the name above and request the required artefact.
4. Have a separate reviewer check evidence, accuracy, privacy and fit before hand-off.

```text
Use skill:skill-installer. Task: {task}. Project phase: {phase}. Context and source material: {links/files and constraints}. Deliverable: {format and audience}. Follow the tool's documented instructions; distinguish evidence from interpretation, state unknowns and do not claim approval.
```

## What good output looks like

- The deliverable addresses the requested task and follows the source-documented workflow.
- Facts, assumptions and unknowns are distinguishable; no capability is implied beyond the source.

## Quality checks

- [ ] The task fits the registry job and any specialist trigger.
- [ ] A reviewer other than the maker checked the output and source evidence.
- [ ] Assumptions and unknowns are visible; unsupported claims are removed.
- [ ] No client-confidential data or personal information entered the public repository.

## Pairs with

- `skill-creator:skill-creator` — coordinate the hand-off for the same job; pass the artefact and constraints.

## Limits and cautions

- Capabilities are limited to those documented in the source; ask for unknown details rather than assuming them.
- Human review remains responsible for factual accuracy, suitability and approval.
- Distribution: vendor; availability: both. Confirm setup or sign-in requirements before relying on the tool.
