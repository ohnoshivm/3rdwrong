---
title: Start
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency-mcp:start
department: operations
sub_department: knowledge-systems
job: tool-integration
role: specialist
trigger: "Use only when the named content, channel, lifecycle, or campaign task is explicitly in the approved marketing scope."
kind: plugin-skill
availability: claude
distribution: vendor
source: toolkit/vendor/plugin-account-synced-agency-mcp-marketplace/skills/start/SKILL.md
invoke: "`agency-mcp:start` skill (Codex plugin; Claude availability: claude)"
pairs_with: [agency:testing-tool-evaluator]
---
# Start

A specialist for tool integration at 3RDWRONG, called when Use only when the named content, channel, lifecycle, or campaign task is explicitly in the approved marketing scope.

## What it does

- First-run guide for Agency MCP. Use when the user asks how to set Agency MCP up, what it can do, what to do first, or opens a fresh session with it — "how do I set this up", "what can you do", "where do I start".…
- One sentence on what this is: their clients' Google, Meta, WordPress and CRM accounts,
- What is ready for them right now, naming their actual clients.
- The `next_step`, only if `status` is not `ready`. If it is a dashboard step, give the link.

## When to use

- Use only when the named content, channel, lifecycle, or campaign task is explicitly in the approved marketing scope.
- In a 3RDWRONG project, use during the relevant tool integration task and pass its output to the project owner for review.

## When not to use

- Do not use when the request falls outside tool integration or fails the registered specialist trigger.
- Do not use its output as client approval, verified research or professional advice.
- For the paired agency:testing-tool-evaluator work, use that tool and hand off this artefact.

## Inputs it needs

- The named connected service and the requested read or change; confirm the correct account and file.
- Relevant documents, source links and constraints; keep client records and personal data in the approved private store.

## How to run it

1. Check the task against the registered job and trigger.
2. Read the source instructions and provide the minimum necessary inputs.
3. Invoke the tool using the name above and request the required artefact.
4. Have a separate reviewer check evidence, accuracy, privacy and fit before hand-off.

```text
Use agency-mcp:start. Task: {task}. Project phase: {phase}. Context and source material: {links/files and constraints}. Deliverable: {format and audience}. Follow the tool's documented instructions; distinguish evidence from interpretation, state unknowns and do not claim approval.
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

- `agency:testing-tool-evaluator` — coordinate the hand-off for the same job; pass the artefact and constraints.

## Limits and cautions

- Capabilities are limited to those documented in the source; ask for unknown details rather than assuming them.
- Human review remains responsible for factual accuracy, suitability and approval.
- Distribution: vendor; availability: claude. Confirm setup or sign-in requirements before relying on the tool.
