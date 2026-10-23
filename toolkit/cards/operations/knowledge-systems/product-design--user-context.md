---
title: User Context
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: product-design:user-context
department: operations
sub_department: knowledge-systems
job: knowledge-management
role: specialist
trigger: "Use when the approved work needs this capability: Load or manage Product Design's saved user context. Use when the user asks to set up Product Design, get started, onboard, save product or design sources, see what Product Design remembers, update saved context, or remember Product Design preferences. Examples include product URLs, Figma files, screenshots, reference images, codebase paths, Storybook, tokens, design systems, brand assets, and general product/design notes"
kind: plugin-skill
availability: codex
distribution: manual
source: /Users/hustle/.codex/plugins/cache/openai-curated-remote/product-design/0.1.56/skills/user-context/SKILL.md
invoke: "`product-design:user-context` skill (Codex plugin; Claude availability: codex)"
pairs_with: [agency:zk-steward]
---
# User Context

A specialist for knowledge management at 3RDWRONG, called when Load or manage Product Design's saved user context. Use when the user asks to set up Product Design, get started, onboard, save product or design sources, see what Product Design remembers, update saved context, or remember Product Design preferences. Examples include product URLs, Figma files, screenshots, reference images, codebase paths, Storybook, tokens, design systems, brand assets, and general product/design notes.

## What it does

- Load or manage Product Design's saved user context. Use when the user asks to set up Product Design, get started, onboard, save product or design sources, see what Product Design remembers, update saved context, or…
- get started with Product Design
- onboard with Product Design
- save product or design sources

## When to use

- Use when the approved work needs this capability: Load or manage Product Design's saved user context. Use when the user asks to set up Product Design, get started, onboard, save product or design sources, see what Product Design remembers, update saved context, or remember Product Design preferences. Examples include product URLs, Figma files, screenshots, reference images, codebase paths, Storybook, tokens, design systems, brand assets, and general product/design notes
- In a 3RDWRONG project, use during the relevant knowledge management task and pass its output to the project owner for review.

## When not to use

- Do not use when the request falls outside knowledge management or fails the registered specialist trigger.
- Do not use its output as client approval, verified research or professional advice.
- For the paired agency:zk-steward work, use that tool and hand off this artefact.

## Inputs it needs

- A specific brief, intended output and project phase.
- Relevant documents, source links and constraints; keep client records and personal data in the approved private store.

## How to run it

1. Check the task against the registered job and trigger.
2. Read the source instructions and provide the minimum necessary inputs.
3. Invoke the tool using the name above and request the required artefact.
4. Have a separate reviewer check evidence, accuracy, privacy and fit before hand-off.

```text
Use product-design:user-context. Task: {task}. Project phase: {phase}. Context and source material: {links/files and constraints}. Deliverable: {format and audience}. Follow the tool's documented instructions; distinguish evidence from interpretation, state unknowns and do not claim approval.
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

- `agency:zk-steward` — coordinate the hand-off for the same job; pass the artefact and constraints.

## Limits and cautions

- Capabilities are limited to those documented in the source; ask for unknown details rather than assuming them.
- Human review remains responsible for factual accuracy, suitability and approval.
- Distribution: Not documented; availability: codex. Confirm setup or sign-in requirements before relying on the tool.
