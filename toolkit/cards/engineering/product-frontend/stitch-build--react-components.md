---
title: Stitch Build React Components
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: stitch-build:react-components
department: engineering
sub_department: product-frontend
job: ui-implementation
role: specialist
trigger: "Use for engineering/product-frontend/ui-implementation when the brief specifically requires: Converts Stitch designs into modular Vite and React components, or syncs/updates existing React components to align with the latest Stitch designs, using system-level networking and AST-based validation ."
kind: plugin-skill
availability: both
distribution: vendor
source: toolkit/vendor/plugin-google-labs-code-stitch-skills-stitch-build-0337446dadde/skills/react-components
invoke: "react-components skill"
pairs_with: [stitch-utilities:stitch-loop, agent:frontend-architect]
---
# Stitch Build React Components

Stitch Build React Components is the studio's specialist for `ui-implementation`; use it when the registry trigger below applies.

## What it does

- Converts Stitch screens into modular Vite/React components or syncs components
- Requires fetching every screen through Stitch MCP and visually auditing screenshots
- Uses metadata and AST validation

## When to use

- Use for engineering/product-frontend/ui-implementation when the brief specifically requires: Converts Stitch designs into modular Vite and React components, or syncs/updates existing React components to align with the latest Stitch designs, using system-level networking and AST-based validation .
- Only when Stitch is selected and project/screen data exists
- Phase 05

## When not to use

- For Figma use `figma:figma-design-to-code`
- Not without Stitch access
- Do not use to approve its own work; assign a separate checker.

## Inputs it needs

- Stitch project and screens
- DESIGN.md/SITE.md and metadata
- Local app and components

## How to run it

1. Confirm the task matches the job and, for a specialist, the registry trigger.
2. Invoke `react-components skill` and provide the approved brief, artefacts, constraints and source context.
3. Ask for the documented deliverable; inspect assumptions and verification before handoff.

```text
Use `stitch-build:react-components` for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform/version: {links and versions}. Constraints: {accessibility, performance, delivery}. Work within the documented scope and registry trigger. Label evidence Documented, Interpretation, Hypothesis or Unknown; return the requested artefact, assumptions, limitations, verification actually performed and a concrete next action.
```

## What good output looks like

- Modular implementation matching audited Stitch screens
- All screens retrieved/audited and AST validation done

## Quality checks

- [ ] Work matches the approved brief and the maker is not its checker.
- [ ] Claims are supported by source or supplied evidence; label uncertainty explicitly.
- [ ] Responsive behaviour, accessibility and performance are checked where they apply.
- [ ] Verification lists only commands, tests or browser checks actually run.

## Pairs with

- `stitch-utilities:stitch-loop` — coordinate the artefacts and handoff at the relevant stage.
- `agent:frontend-architect` — coordinate the artefacts and handoff at the relevant stage.

## Limits and cautions

- Every retrieval/download/audit step is mandatory
- ask before refreshing existing files
- Keep client data and credentials out of the public repository (D-0021); check licence and distribution prerequisites, including installation or sign-in when required.
