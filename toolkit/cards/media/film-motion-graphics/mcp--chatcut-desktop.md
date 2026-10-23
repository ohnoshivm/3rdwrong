---
title: "ChatCut desktop connector"
type: "tool-card"
status: "proposed"
owner: "founder"
last_reviewed: "2026-10-23"
tool_id: "mcp:chatcut_desktop"
department: "media"
sub_department: "film-motion-graphics"
job: "media-tool-access"
role: "specialist"
trigger: "Use when the connected production server is required."
kind: "mcp"
availability: "mcp"
distribution: "manual"
source: "toolkit/sources/managed-tool-descriptions.md"
invoke: "MCP server chatcut_desktop"
pairs_with: []
---

# ChatCut desktop connector

Connects to the ChatCut desktop editor for media production; the configured binary is currently missing. It is a specialist for media-tool-access.

## What it does

- Provides the configured connection to the ChatCut desktop editor.
- Runtime capabilities beyond the separately installed ChatCut skills: Not documented.
- Recorded status: connection failing because the configured MCP binary is not installed.

## When to use

- When the approved task needs the desktop editor and the ChatCut app has been installed and connected.

## When not to use

- While the configured binary is missing or before connectivity and available operations are verified.

## Inputs it needs

- An installed ChatCut desktop app, a working connector and the approved media brief.

## How to run it

1. Install the ChatCut desktop app through its official distribution before attempting this connector.
2. Verify the actual server connection and available tools; do not infer capabilities from the configuration.
3. Load the relevant separately installed ChatCut skill for the requested media task.

```text
Check the ChatCut desktop connector for {{approved media task}}. Report connection status and documented operations first. If the MCP binary is missing, stop and report the prerequisite.
```

## What good output looks like

- An explicit connectivity result and a documented workflow, or a precise missing-installation report.

## Quality checks

- [ ] A reviewer other than the maker checks capability claims and output evidence.
- [ ] Access, connectivity and prerequisites are verified before use.
- [ ] Client assets, credentials and personal data stay outside the public repository.

## Pairs with

- The job lead receives the result and unresolved prerequisites before the next production step.

## Limits and cautions

- ChatCut skills are separately installed for Codex; the GPL-3.0 plugin is FETCH.
- This connector card does not prove the editor or any generation service is available.
- Documented from the founder’s account description dated 2026-10-23; this card remains proposed.
