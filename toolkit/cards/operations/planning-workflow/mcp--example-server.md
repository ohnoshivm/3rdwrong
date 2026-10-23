---
title: Example Server
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: mcp:example-server
department: operations
sub_department: planning-workflow
job: automation-operations
role: specialist
trigger: "Use when the approved work needs this capability: Configured MCP server: example-server. Transport details and credentials are not inventoried"
kind: mcp
availability: mcp
distribution: manual
source: /Users/hustle/.claude/plugins/marketplaces/claude-plugins-official/plugins/example-plugin/.mcp.json
invoke: "MCP server: example-server"
pairs_with: []
---
# Example Server

The Example Server tool supports 3RDWRONG specialist when Use when the approved work needs this capability: Configured MCP server: example-server. Transport details and credentials are not inventoried.

## What it does

- Supports automation operations work as described in its source instructions

## When to use

- Use when the approved work needs this capability: Configured MCP server: example-server. Transport details and credentials are not inventoried

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
Use MCP server: example-server. Job: automation-operations. Brief: {project brief}. Context and source materials: {links/files}. Constraints: {constraints}. Return the documented output, cite evidence, and label anything not supported as Not documented.
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
