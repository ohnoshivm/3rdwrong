---
title: Zk Steward
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:zk-steward
department: operations
sub_department: knowledge-systems
job: knowledge-management
role: lead
trigger: ""
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/zk-steward.md
invoke: "Agent tool: `zk-steward` (Claude Code)"
pairs_with: [product-design:user-context, skill:import-memory]
---
# Zk Steward

The lead for knowledge management at 3RDWRONG, supporting knowledge systems work.

## What it does

- Knowledge-base steward in the spirit of Niklas Luhmann's Zettelkasten. Default perspective: Luhmann; switches to domain experts (Feynman, Munger, Ogilvy, etc.) by task. Enforces atomic notes, connectivity, and…
- Role**: Niklas Luhmann for the AI age—turning complex tasks into **organic parts of a knowledge network**, not one-off answers.
- Experience**: Domain thinking locks onto expert-level output (Karpathy-style conditioning); indexing is entry points, not classification; one note can sit under multiple indices.
- Atomic knowledge management and organic network growth.

## When to use

- Use for knowledge management in Phase 02 Research or the relevant production / hand-off phase when the request matches the documented scope.

## When not to use

- Do not use when the request falls outside knowledge management or fails the registered specialist trigger.
- Do not use its output as client approval, verified research or professional advice.
- For the paired product-design:user-context work, use that tool and hand off this artefact.

## Inputs it needs

- A bounded task brief, relevant context, constraints and expected deliverable.
- Only provide files and information needed for the task.

## How to run it

1. Check the task against the registered job and trigger.
2. Read the source instructions and provide the minimum necessary inputs.
3. Invoke the tool using the name above and request the required artefact.
4. Have a separate reviewer check evidence, accuracy, privacy and fit before hand-off.

```text
Use agency:zk-steward. Task: {task}. Project phase: {phase}. Context and source material: {links/files and constraints}. Deliverable: {format and audience}. Follow the tool's documented instructions; distinguish evidence from interpretation, state unknowns and do not claim approval.
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

- `product-design:user-context` — coordinate the hand-off for the same job; pass the artefact and constraints.
- `skill:import-memory` — coordinate the hand-off for the same job; pass the artefact and constraints.

## Limits and cautions

- Capabilities are limited to those documented in the source; ask for unknown details rather than assuming them.
- Human review remains responsible for factual accuracy, suitability and approval.
- Distribution: vendor; availability: repo. Confirm setup or sign-in requirements before relying on the tool.
