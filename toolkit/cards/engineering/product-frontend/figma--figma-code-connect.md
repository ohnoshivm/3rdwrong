---
title: Figma Code Connect
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: figma:figma-code-connect
department: engineering
sub_department: product-frontend
job: ui-implementation
role: specialist
trigger: "Use for engineering/product-frontend/ui-implementation when the brief specifically requires: Creates and maintains Figma Code Connect template files that map Figma components to code snippets ."
kind: plugin-skill
availability: both
distribution: fetch
source: https://github.com/figma/mcp-server-guide
invoke: "figma-code-connect skill"
pairs_with: [figma:figma-design-to-code, agent:frontend-architect]
---
# Figma Code Connect

Figma Code Connect is the studio's specialist for `ui-implementation`; use it when the registry trigger below applies.

## What it does

- Creates `.figma.ts` templates mapping published Figma components to code
- Uses Figma MCP suggestions and component properties
- Writes parserless templates and never `.figma.tsx`

## When to use

- Use for engineering/product-frontend/ui-implementation when the brief specifically requires: Creates and maintains Figma Code Connect template files that map Figma components to code snippets .
- When the task explicitly needs Code Connect mappings
- after published components are selected

## When not to use

- For full-screen implementation use `figma:figma-design-to-code`
- Stop if Figma MCP unavailable or components unpublished
- Do not use to approve its own work; assign a separate checker.

## Inputs it needs

- Figma URL with node-id and published library components
- Connected Figma MCP
- Code paths and TypeScript config

## How to run it

1. Confirm the task matches the job and, for a specialist, the registry trigger.
2. Invoke `figma-code-connect skill` and provide the approved brief, artefacts, constraints and source context.
3. Ask for the documented deliverable; inspect assumptions and verification before handoff.

```text
Use `figma:figma-code-connect` for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform/version: {links and versions}. Constraints: {accessibility, performance, delivery}. Work within the documented scope and registry trigger. Label evidence Documented, Interpretation, Hypothesis or Unknown; return the requested artefact, assumptions, limitations, verification actually performed and a concrete next action.
```

## What good output looks like

- Valid mappings for selected published components
- Resolved node IDs and code snippets match project

## Quality checks

- [ ] Work matches the approved brief and the maker is not its checker.
- [ ] Claims are supported by source or supplied evidence; label uncertainty explicitly.
- [ ] Responsive behaviour, accessibility and performance are checked where they apply.
- [ ] Verification lists only commands, tests or browser checks actually run.

## Pairs with

- `figma:figma-design-to-code` — coordinate the artefacts and handoff at the relevant stage.
- `agent:frontend-architect` — coordinate the artefacts and handoff at the relevant stage.

## Limits and cautions

- The fetch manifest records the upstream licence as `none-found`; check usage rights before redistribution.
- Requires Figma MCP and organisation/enterprise plan
- fetched plugin may need installation
- Keep client data and credentials out of the public repository (D-0021); check licence and distribution prerequisites, including installation or sign-in when required.
