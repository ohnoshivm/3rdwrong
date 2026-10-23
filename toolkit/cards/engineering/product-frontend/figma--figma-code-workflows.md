---
title: Figma Code Workflows
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: figma:figma-code-workflows
department: engineering
sub_department: product-frontend
job: ui-implementation
role: specialist
trigger: "Use for engineering/product-frontend/ui-implementation when the brief specifically requires: Import or upload local HTML or project files into Figma, choose editable Design frames, runnable Code Layers or standalone Code (also known as Make), and repair imported previews ."
kind: plugin-skill
availability: both
distribution: fetch
source: https://github.com/figma/mcp-server-guide
invoke: "figma-code-workflows skill"
pairs_with: [figma:figma-design-to-code, figma:figma-code-connect]
---
# Figma Code Workflows

Figma Code Workflows is the studio's specialist for `ui-implementation`; use it when the registry trigger below applies.

## What it does

- Imports local HTML/projects as editable Design layers, runnable Code Layers or standalone Code
- Chooses destination from explicit output choice
- Reports import and preview only when confirmed

## When to use

- Use for engineering/product-frontend/ui-implementation when the brief specifically requires: Import or upload local HTML or project files into Figma, choose editable Design frames, runnable Code Layers or standalone Code (also known as Make), and repair imported previews .
- Only when an import into Figma is explicitly requested

## When not to use

- For Figma-to-code use `figma:figma-design-to-code`
- Do not use for ordinary code projects
- Do not use to approve its own work; assign a separate checker.

## Inputs it needs

- Local HTML/project and explicit output choice
- Destination Figma file/key
- Project setup and validation context

## How to run it

1. Confirm the task matches the job and, for a specialist, the registry trigger.
2. Invoke `figma-code-workflows skill` and provide the approved brief, artefacts, constraints and source context.
3. Ask for the documented deliverable; inspect assumptions and verification before handoff.

```text
Use `figma:figma-code-workflows` for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform/version: {links and versions}. Constraints: {accessibility, performance, delivery}. Work within the documented scope and registry trigger. Label evidence Documented, Interpretation, Hypothesis or Unknown; return the requested artefact, assumptions, limitations, verification actually performed and a concrete next action.
```

## What good output looks like

- Requested layers/code appear in destination
- Confirmed import status and blockers

## Quality checks

- [ ] Work matches the approved brief and the maker is not its checker.
- [ ] Claims are supported by source or supplied evidence; label uncertainty explicitly.
- [ ] Responsive behaviour, accessibility and performance are checked where they apply.
- [ ] Verification lists only commands, tests or browser checks actually run.

## Pairs with

- `figma:figma-design-to-code` — coordinate the artefacts and handoff at the relevant stage.
- `figma:figma-code-connect` — coordinate the artefacts and handoff at the relevant stage.

## Limits and cautions

- The fetch manifest records the upstream licence as `none-found`; check usage rights before redistribution.
- If output is unclear, source says ask Design layers or Code layer
- Figma tools required
- Keep client data and credentials out of the public repository (D-0021); check licence and distribution prerequisites, including installation or sign-in when required.
