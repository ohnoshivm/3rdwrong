---
title: Skill Creator
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill-creator:skill-creator
department: operations
sub_department: knowledge-systems
job: skill-authoring
role: lead
trigger: ""
kind: plugin-skill
availability: both
distribution: vendor
source: toolkit/vendor/plugin-claude-plugins-official-skill-creator-marketplace/skills/skill-creator/SKILL.md
invoke: "`skill-creator:skill-creator` skill (Codex plugin; Claude availability: both)"
pairs_with: [agent:plugin-dev:agent-creator, agent:plugin-dev:plugin-validator]
---
# Skill Creator

The lead for skill authoring at 3RDWRONG, supporting knowledge systems work.

## What it does

- Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark…
- Decide what you want the skill to do and roughly how it should do it
- Write a draft of the skill
- Create a few test prompts and run claude-with-access-to-the-skill on them

## When to use

- Use for skill authoring in Phase 02 Research or the relevant production / hand-off phase when the request matches the documented scope.

## When not to use

- Do not use when the request falls outside skill authoring or fails the registered specialist trigger.
- Do not use its output as client approval, verified research or professional advice.
- For the paired agent:plugin-dev:agent-creator work, use that tool and hand off this artefact.

## Inputs it needs

- The target skill, agent, plugin or command and its repository/context, plus the requested create/review outcome.
- Relevant documents, source links and constraints; keep client records and personal data in the approved private store.

## How to run it

1. Check the task against the registered job and trigger.
2. Read the source instructions and provide the minimum necessary inputs.
3. Invoke the tool using the name above and request the required artefact.
4. Have a separate reviewer check evidence, accuracy, privacy and fit before hand-off.

```text
Use skill-creator:skill-creator. Task: {task}. Project phase: {phase}. Context and source material: {links/files and constraints}. Deliverable: {format and audience}. Follow the tool's documented instructions; distinguish evidence from interpretation, state unknowns and do not claim approval.
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

- `agent:plugin-dev:agent-creator` — coordinate the hand-off for the same job; pass the artefact and constraints.
- `agent:plugin-dev:plugin-validator` — coordinate the hand-off for the same job; pass the artefact and constraints.

## Limits and cautions

- Capabilities are limited to those documented in the source; ask for unknown details rather than assuming them.
- Human review remains responsible for factual accuracy, suitability and approval.
- Distribution: vendor; availability: both. Confirm setup or sign-in requirements before relying on the tool.
