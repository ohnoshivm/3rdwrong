---
title: Building Web Artifacts
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:building-web-artifacts
department: engineering
sub_department: product-frontend
job: ui-implementation
role: specialist
trigger: "Use when building elaborate, multi-component HTML artifacts using modern frontend technologies (React, Tailwind CSS, shadcn/ui)."
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.config/opencode/skills/building-web-artifacts/SKILL.md
invoke: "building-web-artifacts skill"
pairs_with: [agent:frontend-architect, skill:tailwindcss]
---
# Building Web Artifacts

Building Web Artifacts is the studio's specialist for `ui-implementation`; use it when the registry trigger below applies.

## What it does

- Guides elaborate multi-component HTML artifacts
- Uses React, Tailwind and shadcn where context fits
- Supports a runnable browser artifact

## When to use

- Use when building elaborate, multi-component HTML artifacts using modern frontend technologies (React, Tailwind CSS, shadcn/ui).
- For substantial multi-component HTML deliverables
- Phase 05 Development

## When not to use

- For simple static page keep existing stack
- For Sites workflow use `sites:sites`
- Do not use to approve its own work; assign a separate checker.

## Inputs it needs

- Artifact purpose/content/interactions
- Existing stack and dependencies
- Approved design/assets and responsive needs

## How to run it

1. Confirm the task matches the job and, for a specialist, the registry trigger.
2. Invoke `building-web-artifacts skill` and provide the approved brief, artefacts, constraints and source context.
3. Ask for the documented deliverable; inspect assumptions and verification before handoff.

```text
Use `skill:building-web-artifacts` for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform/version: {links and versions}. Constraints: {accessibility, performance, delivery}. Work within the documented scope and registry trigger. Label evidence Documented, Interpretation, Hypothesis or Unknown; return the requested artefact, assumptions, limitations, verification actually performed and a concrete next action.
```

## What good output looks like

- Runnable multi-component artifact with working interactions
- Responsive and accessible rendering verified

## Quality checks

- [ ] Work matches the approved brief and the maker is not its checker.
- [ ] Claims are supported by source or supplied evidence; label uncertainty explicitly.
- [ ] Responsive behaviour, accessibility and performance are checked where they apply.
- [ ] Verification lists only commands, tests or browser checks actually run.

## Pairs with

- `agent:frontend-architect` — coordinate the artefacts and handoff at the relevant stage.
- `skill:tailwindcss` — coordinate the artefacts and handoff at the relevant stage.

## Limits and cautions

- Do not add frameworks speculatively
- visual completion needs rendered inspection
- Keep client data and credentials out of the public repository (D-0021); check licence and distribution prerequisites, including installation or sign-in when required.
