---
title: build-mcp-server
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: mcp-server-dev:build-mcp-server
department: engineering
sub_department: platform-performance
job: backend-and-api
role: specialist
trigger: "Use for engineering/platform-performance/backend-and-api when the brief specifically requires: This skill should be used when the user asks to \"build an MCP server\", \"create an MCP\", \"make an MCP integration\", \"wrap an API for Claude\", \"expose tools to Claude\", \"make an MCP app\", or discusses building something with the Model Context Protocol ."
kind: plugin-skill
availability: claude
distribution: vendor
source: toolkit/vendor/plugin-claude-plugins-official-mcp-server-dev-marketplace/skills/build-mcp-server
invoke: "build-mcp-server skill"
pairs_with: [agency:engineering-backend-architect]
---
# build-mcp-server

This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integration", "wrap an API for Claude", "expose tools to Claude", "make an MCP app", or discusses building something with the Model Context Protocol. It is the entry point for MCP server development — it interrogates the user about their use case, determines the right deployment model (remote HTTP, MCPB, local stdio), picks a tool-design pattern, and hands off to specialized skills.

## What it does

- This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integration", "wrap an API for Claude", "expose tools to Claude", "make an MCP app", or discusses building something with the Model Context Protocol. It is the entry point for MCP server development — it interrogates the user about their use case, determines the right deployment model (remote HTTP, MCPB, local stdio), picks a tool-design pattern, and hands off to specialized skills.
- OAuth 2.0 → you'll need a remote server with CIMD (preferred) or DCR support; see `references/auth.md`
- Zero install friction — users add a URL, done
- One deployment serves all users; you control upgrades

## When to use

- Use for engineering/platform-performance/backend-and-api when the brief specifically requires: This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integration", "wrap an API for Claude", "expose tools to Claude", "make an MCP app", or discusses building something with the Model Context Protocol .
- Before changing production behaviour, with scope, baseline and decision owner stated.

## When not to use

- When the task is outside `backend-and-api` or its stated trigger; route to the appropriate job lead.
- To approve its own work; use an independent checker.

## Inputs it needs

- The approved scope, relevant repository or system context, and decision requested.
- Baseline evidence, constraints, and acceptance criteria relevant to the task.
- Access and environment details only when required; keep client data outside the public repository.

## How to run it

1. Confirm the brief matches `backend-and-api` and the trigger above.
2. Provide the inputs and ask for findings tied to the supplied evidence.
3. Review the output independently; implement only approved changes and record before/after evidence.

```text
Use build-mcp-server skill. Task: {specific task}. Context: {repository/system and approved scope}. Evidence available: {baseline, traces, logs, or constraints}. Return documented capabilities and limits, identify unknowns, and give a proposed next action with evidence. Do not claim unmeasured results.
```

## What good output looks like

- Recommendations map to the stated task and cite supplied evidence.
- Unknowns, assumptions and risks are explicit.
- Any performance or reliability claim has a comparable baseline and follow-up measure.

## Quality checks

- [ ] The work matches the registry job and trigger.
- [ ] Claims trace to supplied evidence; unknowns are labelled.
- [ ] An independent reviewer checks the result.

## Pairs with

- Upstream: `agency:engineering-backend-architect`.
- Downstream: an independent reviewer and the relevant delivery or QA owner; hand off findings, evidence and unresolved risks.

## Limits and cautions

- The source describes a role or workflow; it does not prove live system access, successful execution or performance outcomes.
- Keep maker and checker separate; label evidence **Documented**, **Interpretation**, **Hypothesis** or **Unknown**.
- Protect client data; do not place confidential or identifying material in this public repository.
