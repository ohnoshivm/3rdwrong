---
title: Gstack Design HTML
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:gstack-design-html
department: engineering
sub_department: product-frontend
job: ui-implementation
role: specialist
trigger: "When building or restyling the studio’s own web presence or a key digital touchpoint."
kind: skill
availability: both
distribution: fetch
source: https://github.com/garrytan/gstack
invoke: "gstack-design-html skill"
pairs_with: [skill:build-awwwards-quality-sites, agent:frontend-architect]
---
# Gstack Design HTML

Gstack Design HTML is the studio's specialist for `ui-implementation`; use it when the registry trigger below applies.

## What it does

- Guides building/restyling the studio web presence or key touchpoint
- Combines visual specificity with implementation iteration
- Supports a distinctive HTML result

## When to use

- When building or restyling the studio’s own web presence or a key digital touchpoint.
- When building/restyling studio web presence or key digital touchpoint
- Phase 05 after direction and content hierarchy

## When not to use

- For art-direction approval use design lead
- For architecture use `agent:frontend-architect`
- Do not use to approve its own work; assign a separate checker.

## Inputs it needs

- Approved concept, copy, assets and responsive behaviours
- Codebase and preview
- Accessibility/performance constraints

## How to run it

1. Confirm the task matches the job and, for a specialist, the registry trigger.
2. Invoke `gstack-design-html skill` and provide the approved brief, artefacts, constraints and source context.
3. Ask for the documented deliverable; inspect assumptions and verification before handoff.

```text
Use `skill:gstack-design-html` for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform/version: {links and versions}. Constraints: {accessibility, performance, delivery}. Work within the documented scope and registry trigger. Label evidence Documented, Interpretation, Hypothesis or Unknown; return the requested artefact, assumptions, limitations, verification actually performed and a concrete next action.
```

## What good output looks like

- Distinct implementation aligned to route
- Rendered desktop/mobile defects corrected

## Quality checks

- [ ] Work matches the approved brief and the maker is not its checker.
- [ ] Claims are supported by source or supplied evidence; label uncertainty explicitly.
- [ ] Responsive behaviour, accessibility and performance are checked where they apply.
- [ ] Verification lists only commands, tests or browser checks actually run.

## Pairs with

- `skill:build-awwwards-quality-sites` — coordinate the artefacts and handoff at the relevant stage.
- `agent:frontend-architect` — coordinate the artefacts and handoff at the relevant stage.

## Limits and cautions

- Avoid rejected identity direction and agency imitation
- fetch may need install
- Keep client data and credentials out of the public repository (D-0021); check licence and distribution prerequisites, including installation or sign-in when required.
