---
title: "Creative Production MCP"
type: "tool-card"
status: "proposed"
owner: "founder"
last_reviewed: "2026-10-23"
tool_id: "mcp:creative_production_mcp"
department: "media"
sub_department: "film-motion-graphics"
job: "media-tool-access"
role: "specialist"
trigger: "Use when the connected production server is required."
kind: "mcp"
availability: "mcp"
distribution: "manual"
source: "toolkit/sources/managed-tool-descriptions.md"
invoke: "MCP server creative_production_mcp"
pairs_with: []
---

# Creative Production MCP

Records a configured media connector whose capabilities require verification before use. It is a specialist for media-tool-access.

## What it does

- Records the configured creative_production_mcp server.
- Available operations and supported outputs: Not documented.
- Runtime and authentication requirements: Not documented.

## When to use

- Only when an explicit request names this connector and its operations can be inspected first.

## When not to use

- For production based on configuration alone; no capability documentation was found on disk.

## Inputs it needs

- An explicit approved task and access to inspect the server’s actual documentation and tool list.

## How to run it

1. Verify the server’s connectivity and obtain its documented tool list before using it.
2. Match the requested task to a documented operation; stop if the capability remains unknown.
3. Use only approved inputs and independently review any returned result.

```text
Verify creative_production_mcp before use for {{task}}. Report its documented operations and prerequisites. If they cannot be verified, return Not documented rather than inventing a workflow.
```

## What good output looks like

- A documented capability and connection assessment; unresolved operations remain Unknown.

## Quality checks

- [ ] A reviewer other than the maker checks capability claims and output evidence.
- [ ] Access, connectivity and prerequisites are verified before use.
- [ ] Client assets, credentials and personal data stay outside the public repository.

## Pairs with

- The job lead receives the result and unresolved prerequisites before the next production step.

## Limits and cautions

- Status: verify before use. Configuration does not establish an operational service.
- Do not infer capabilities from separately installed Creative Production skills.
- Documented from the founder’s account description dated 2026-10-23; this card remains proposed.
