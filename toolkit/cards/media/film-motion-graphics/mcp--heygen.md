---
title: "HeyGen HyperFrames connector"
type: "tool-card"
status: "proposed"
owner: "founder"
last_reviewed: "2026-10-23"
tool_id: "mcp:heygen"
department: "media"
sub_department: "film-motion-graphics"
job: "media-tool-access"
role: "specialist"
trigger: "Use when the approved work needs this capability: Configured MCP server: heygen. Transport details and credentials are not inventoried"
kind: "mcp"
availability: "claude-managed"
distribution: "manual"
source: "toolkit/sources/managed-tool-descriptions.md"
invoke: "HyperFrames by HeyGen connector in Claude"
pairs_with: []
---

# HeyGen HyperFrames connector

Provides the account-managed HeyGen connector for hosted HTML video projects and cloud rendering. It is a specialist for media-tool-access.

## What it does

- Composes or edits a hosted HTML video project through a background job.
- Lists projects and retrieves metadata, player views, project status and render status.
- Renders video as MP4, WebM or MOV at a selected frame rate.

## When to use

- When the approved film needs a hosted HeyGen/HyperFrames project, cloud render or shareable project.

## When not to use

- For local editable compositions in CLI/IDE agents; use the local HyperFrames skills instead.

## Inputs it needs

- The approved brief, brand assets, output format and founder’s HeyGen OAuth access.

## How to run it

1. Open the signed-in HyperFrames by HeyGen connector in Claude and inspect the documented tools.
2. Use compose for the hosted project, then inspect background job status.
3. Request render_video only in the supported connector context and verify render status.

```text
Use the hosted HyperFrames by HeyGen connector for {{approved film}}. Assets: {{approved assets}}. Format: {{format}}. Track composition and render status; report missing prerequisites without assuming success.
```

## What good output looks like

- A hosted project and verified render status matching the approved brief and requested format.

## Quality checks

- [ ] A reviewer other than the maker checks capability claims and output evidence.
- [ ] Access, connectivity and prerequisites are verified before use.
- [ ] Client assets, credentials and personal data stay outside the public repository.

## Pairs with

- The job lead receives the result and unresolved prerequisites before the next production step.

## Limits and cautions

- compose and render_video are disabled from CLI/IDE agents including Claude Code and Codex.
- Local work uses /hyperframes, /hyperframes-cli and /hyperframes-media skills.
- Requires founder’s HeyGen OAuth account; purposeful motion and accessibility remain studio requirements.
- Documented from the founder’s account description dated 2026-10-23; this card remains proposed.
