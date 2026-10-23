---
title: Figma Design to Code
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: figma:figma-design-to-code
department: engineering
sub_department: product-frontend
job: ui-implementation
role: specialist
trigger: "Use for engineering/product-frontend/ui-implementation when the brief specifically requires: **MANDATORY prerequisite** — you MUST invoke this skill BEFORE calling the `get_design_context` Figma MCP tool ."
kind: plugin-skill
availability: both
distribution: fetch
source: https://github.com/figma/mcp-server-guide
invoke: "figma-design-to-code skill"
pairs_with: [figma:figma-code-connect, agent:frontend-architect]
---
# Figma Design to Code

Figma Design to Code is the studio's specialist for `ui-implementation`; use it when the registry trigger below applies.

## What it does

- Mandatory prerequisite before `get_design_context` for Figma-to-code
- Requires initial screenshot and high-fidelity design context
- Reuses Code Connect mappings/assets and verifies requested scope

## When to use

- Use for engineering/product-frontend/ui-implementation when the brief specifically requires: **MANDATORY prerequisite** — you MUST invoke this skill BEFORE calling the `get_design_context` Figma MCP tool .
- Before any Figma design-context call for implementation
- continue through requested screen verification

## When not to use

- For library mappings use `figma:figma-code-connect`
- Not for non-Figma implementation
- Do not use to approve its own work; assign a separate checker.

## Inputs it needs

- Figma design link and requested screen
- Figma MCP and screenshot/context
- Project stack and existing components/assets

## How to run it

1. Confirm the task matches the job and, for a specialist, the registry trigger.
2. Invoke `figma-design-to-code skill` and provide the approved brief, artefacts, constraints and source context.
3. Ask for the documented deliverable; inspect assumptions and verification before handoff.

```text
Use `figma:figma-design-to-code` for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform/version: {links and versions}. Constraints: {accessibility, performance, delivery}. Work within the documented scope and registry trigger. Label evidence Documented, Interpretation, Hypothesis or Unknown; return the requested artefact, assumptions, limitations, verification actually performed and a concrete next action.
```

## What good output looks like

- Implementation aligned to high-fidelity context
- Visible assets local and in correct rendered slots

## Quality checks

- [ ] Work matches the approved brief and the maker is not its checker.
- [ ] Claims are supported by source or supplied evidence; label uncertainty explicitly.
- [ ] Responsive behaviour, accessibility and performance are checked where they apply.
- [ ] Verification lists only commands, tests or browser checks actually run.

## Pairs with

- `figma:figma-code-connect` — coordinate the artefacts and handoff at the relevant stage.
- `agent:frontend-architect` — coordinate the artefacts and handoff at the relevant stage.

## Limits and cautions

- The fetch manifest records the upstream licence as `none-found`; check usage rights before redistribution.
- Do not use screenshot as a code asset or leave temporary Figma URLs
- visual match needs rendered evidence
- Keep client data and credentials out of the public repository (D-0021); check licence and distribution prerequisites, including installation or sign-in when required.
