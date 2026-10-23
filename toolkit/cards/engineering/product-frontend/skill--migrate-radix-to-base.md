---
title: Migrate Radix to Base UI
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:migrate-radix-to-base
department: engineering
sub_department: product-frontend
job: frontend-architecture
role: specialist
trigger: "Use for tasks involving Migrates React projects and components from Radix UI to Base UI."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-shadcn-ui-ui-mit/skills/migrate-radix-to-base
invoke: "migrate-radix-to-base skill"
pairs_with: [skill:shadcn, agent:frontend-architect]
---
# Migrate Radix to Base UI

Migrate Radix to Base UI is the studio's specialist for `frontend-architecture`; use it when the registry trigger below applies.

## What it does

- Guides migration of React components from Radix UI to Base UI
- Maps existing component use to target APIs
- Preserves project-specific component context

## When to use

- Use for tasks involving Migrates React projects and components from Radix UI to Base UI.
- Only for explicitly approved Radix-to-Base migration

## When not to use

- For shadcn management use `skill:shadcn`
- Not for unrelated redesign
- Do not use to approve its own work; assign a separate checker.

## Inputs it needs

- React project and Radix inventory
- Target Base UI version
- Tests and compatibility constraints

## How to run it

1. Confirm the task matches the job and, for a specialist, the registry trigger.
2. Invoke `migrate-radix-to-base skill` and provide the approved brief, artefacts, constraints and source context.
3. Ask for the documented deliverable; inspect assumptions and verification before handoff.

```text
Use `skill:migrate-radix-to-base` for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform/version: {links and versions}. Constraints: {accessibility, performance, delivery}. Work within the documented scope and registry trigger. Label evidence Documented, Interpretation, Hypothesis or Unknown; return the requested artefact, assumptions, limitations, verification actually performed and a concrete next action.
```

## What good output looks like

- Migrated components retain intended interaction/accessibility
- Migration map and test results

## Quality checks

- [ ] Work matches the approved brief and the maker is not its checker.
- [ ] Claims are supported by source or supplied evidence; label uncertainty explicitly.
- [ ] Responsive behaviour, accessibility and performance are checked where they apply.
- [ ] Verification lists only commands, tests or browser checks actually run.

## Pairs with

- `skill:shadcn` — coordinate the artefacts and handoff at the relevant stage.
- `agent:frontend-architect` — coordinate the artefacts and handoff at the relevant stage.

## Limits and cautions

- Keyboard behaviour can change
- review independently and verify actual versions
- Keep client data and credentials out of the public repository (D-0021); check licence and distribution prerequisites, including installation or sign-in when required.
