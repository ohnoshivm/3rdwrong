---
title: Rea MCP server
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: mcp:rea
department: engineering
sub_department: platform-performance
job: backend-and-api
role: specialist
trigger: "Use for tasks involving Additional configured stdio MCP launches rea-agents@6."
kind: mcp
availability: mcp
distribution: fetch
source: ~/.claude.json
invoke: "rea MCP server"
pairs_with: [agency:engineering-backend-architect]
---
# Rea MCP server

The registry lists this configured MCP server for `backend-and-api` work, but its local configuration does not document what operations it exposes.

## What it does

- Not documented in the MCP configuration source.
- The registry trigger identifies the intended task context; it does not describe available tools or results.

## When to use

- Use for tasks involving Additional configured stdio MCP launches rea-agents@6.
- Only after checking the server's live tool list and confirming the requested operation is supported.

## When not to use

- When the operation is absent from the server's advertised tools; use the relevant documented tool or job lead.
- To approve its own work; use an independent checker.

## Inputs it needs

- A supported operation confirmed from the live MCP tool list.
- Task scope, relevant context, constraints and acceptance criteria.

## How to run it

1. Confirm the MCP server is connected and inspect its advertised tools.
2. Select only a documented operation that matches the brief.
3. Review returned data for completeness and verify consequential results independently.

```text
Use the rea MCP server only if its advertised tools support this operation: {operation}. Context: {approved scope}. Return the result, sources and limitations; mark unsupported or unknown capabilities as Unknown.
```

## What good output looks like

- The selected operation is present in the live tool list and matches the approved task.
- Returned information is traceable and limitations are stated.
- No unsupported capability or outcome is claimed.

## Quality checks

- [ ] Confirmed the operation is exposed by the connected server.
- [ ] Checked returned data independently for consequential decisions.
- [ ] No client data or credentials were copied into the public repository.

## Pairs with

- Upstream: `agency:engineering-backend-architect` for backend/API scope and interface decisions.
- Downstream: an independent reviewer; hand off the operation, result and evidence.

## Limits and cautions

- Supported operations and outputs are **Not documented** in the local configuration source.
- The configured connection does not prove runtime availability or successful execution.
- Keep credentials and client data private; separate maker and checker.
