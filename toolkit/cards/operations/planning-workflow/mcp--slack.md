---
title: Slack
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: mcp:slack
department: operations
sub_department: planning-workflow
job: automation-operations
role: specialist
trigger: "Use when the approved work needs this capability: Configured MCP server: slack. Transport details and credentials are not inventoried"
kind: mcp
availability: mcp
distribution: manual
source: /Users/hustle/.claude/plugins/synced/88e7af4e-a2cf-4b40-8488-91a856697e04_aa2d1473-adba-46ff-9558-93fbf2ea6240/2da0c8d9-1e96-4394-b0f4-3249613186f8/.mcp.json
invoke: "MCP server: slack"
pairs_with: []
---
# Slack

The Slack tool supports 3RDWRONG specialist when Use when the approved work needs this capability: Configured MCP server: slack. Transport details and credentials are not inventoried.

## What it does

- "url": "<https://mcp.datadoghq.com/api/unstable/mcp-server/mcp>"

## When to use

- Use when the approved work needs this capability: Configured MCP server: slack. Transport details and credentials are not inventoried

## When not to use

- When the brief needs a different job than `automation-operations`; choose the registered tool for that job.
- Do not treat its output as independent verification when it produced the work.

## Inputs it needs

- The requested outcome, relevant project context, constraints and source material.
- Any criteria, data or decisions specified in the source instructions; otherwise: Not documented.

## How to run it

1. Confirm the source instructions and required access are available.
2. Invoke using the exact tool name above.
3. Give it the brief, context and acceptance criteria; review its evidence and handoff.

```text
Use MCP server: slack. Job: automation-operations. Brief: {project brief}. Context and source materials: {links/files}. Constraints: {constraints}. Return the documented output, cite evidence, and label anything not supported as Not documented.
```

## What good output looks like

- Addresses the stated outcome and follows the source instructions.
- Separates documented evidence from assumptions and names unresolved inputs.
- Includes a useful next action or handoff where the source calls for one.

## Quality checks

- [ ] A reviewer confirms claims against source evidence.
- [ ] Assumptions and missing inputs are explicit.
- [ ] The result is reviewed by someone other than its maker when it is used to check work.

## Pairs with

- No registry pairings are documented. Handoff: share the brief, output and open questions with the next tool selected for the project.

## Limits and cautions

- Capabilities are limited to those stated in the tool file; details not stated there are Not documented.
- Distribution/access: follow the installed package and access rules.
- Keep client data out of the public repository (D-0021).
- Apply evidence labels: Documented, Interpretation, Hypothesis or Unknown; preserve human review for consequential decisions.
