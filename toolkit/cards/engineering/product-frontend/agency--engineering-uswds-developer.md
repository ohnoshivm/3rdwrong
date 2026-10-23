---
title: USWDS Developer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:engineering-uswds-developer
department: engineering
sub_department: product-frontend
job: ui-implementation
role: specialist
trigger: "Use for tasks involving Expert U."
kind: upstream-agent
availability: claude-managed
distribution: vendor
source: .claude/agents/engineering-uswds-developer.md
invoke: "Claude Code agent: USWDS Developer Agent"
pairs_with: [agency:engineering-cms-developer, skill:building-accessible-interfaces]
---
# USWDS Developer

USWDS Developer is the studio's specialist for `ui-implementation`; use it when the registry trigger below applies.

## What it does

- Builds with USWDS tokens, Sass settings, components and responsive grid
- Integrates USWDS with Drupal or WordPress
- Treats federal accessibility and IDEA requirements as implementation constraints

## When to use

- Use for tasks involving Expert U.
- Only for approved federal/public-sector interfaces requiring USWDS
- Use during theme and component implementation

## When not to use

- For studio sites use the project design system
- For independent conformance use an accessibility checker
- Do not use to approve its own work; assign a separate checker.

## Inputs it needs

- USWDS version/build method and CMS
- Approved theme tokens and federal elements
- Accessibility and responsive requirements

## How to run it

1. Confirm the task matches the job and, for a specialist, the registry trigger.
2. Invoke `Claude Code agent: USWDS Developer Agent` and provide the approved brief, artefacts, constraints and source context.
3. Ask for the documented deliverable; inspect assumptions and verification before handoff.

```text
Use `agency:engineering-uswds-developer` for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform/version: {links and versions}. Constraints: {accessibility, performance, delivery}. Work within the documented scope and registry trigger. Label evidence Documented, Interpretation, Hypothesis or Unknown; return the requested artefact, assumptions, limitations, verification actually performed and a concrete next action.
```

## What good output looks like

- Token-based implementation using maintained components
- Keyboard, screen-reader and contrast checks

## Quality checks

- [ ] Work matches the approved brief and the maker is not its checker.
- [ ] Claims are supported by source or supplied evidence; label uncertainty explicitly.
- [ ] Responsive behaviour, accessibility and performance are checked where they apply.
- [ ] Verification lists only commands, tests or browser checks actually run.

## Pairs with

- `agency:engineering-cms-developer` — coordinate the artefacts and handoff at the relevant stage.
- `skill:building-accessible-interfaces` — coordinate the artefacts and handoff at the relevant stage.

## Limits and cautions

- Do not fork components or edit vendored USWDS
- registry trigger “Expert U.” is incomplete versus source scope
- Keep client data and credentials out of the public repository (D-0021); check licence and distribution prerequisites, including installation or sign-in when required.
