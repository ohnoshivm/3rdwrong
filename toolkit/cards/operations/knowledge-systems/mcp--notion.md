---
title: Notion
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: mcp:notion
department: operations
sub_department: knowledge-systems
job: tool-integration
role: specialist
trigger: "Use when the approved work needs this capability: Configured MCP server: notion. Transport details and credentials are not inventoried"
kind: mcp
availability: mcp
distribution: manual
source: /Users/hustle/.claude/plugins/synced/88e7af4e-a2cf-4b40-8488-91a856697e04_aa2d1473-adba-46ff-9558-93fbf2ea6240/2da0c8d9-1e96-4394-b0f4-3249613186f8/.mcp.json
invoke: "MCP server `notion`"
pairs_with: [agency:testing-tool-evaluator]
---
# Notion

A specialist for tool integration at 3RDWRONG, called when Configured MCP server: notion. Transport details and credentials are not inventoried.

## What it does

- Specific capabilities: Not documented in the readable source.

## When to use

- Use when the approved work needs this capability: Configured MCP server: notion. Transport details and credentials are not inventoried
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
Use mcp:notion. Task: {task}. Project phase: {phase}. Context and source material: {links/files and constraints}. Deliverable: {format and audience}. Follow the tool's documented instructions; distinguish evidence from interpretation, state unknowns and do not claim approval.
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
- Distribution: Not documented; availability: mcp. Confirm setup or sign-in requirements before relying on the tool.
