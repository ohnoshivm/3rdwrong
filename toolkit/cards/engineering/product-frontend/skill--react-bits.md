---
title: React Bits
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:react-bits
department: engineering
sub_department: product-frontend
job: ui-implementation
role: specialist
trigger: "Use for tasks involving Find and install animated or interactive React Bits components for React, Next."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-ohnoshivm-creative-engineering-os-mit/skills/react-bits
invoke: "react-bits skill"
pairs_with: [skill:vercel-composition-patterns, agent:frontend-architect]
---
# React Bits

React Bits is the studio's specialist for `ui-implementation`; use it when the registry trigger below applies.

## What it does

- Finds and installs animated/interactive React Bits components
- Requires selecting a specific official component/variant
- Checks added source, dependencies, keyboard, focus, responsive and motion

## When to use

- Use for tasks involving Find and install animated or interactive React Bits components for React, Next.
- Only when a specific React component serves approved concept
- Phase 05

## When not to use

- For non-React use another tool
- Do not add motion because library exists
- Do not use to approve its own work; assign a separate checker.

## Inputs it needs

- Interaction need and approved intent
- React/Next and style variant
- Package runner/accessibility needs

## How to run it

1. Confirm the task matches the job and, for a specialist, the registry trigger.
2. Invoke `react-bits skill` and provide the approved brief, artefacts, constraints and source context.
3. Ask for the documented deliverable; inspect assumptions and verification before handoff.

```text
Use `skill:react-bits` for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform/version: {links and versions}. Constraints: {accessibility, performance, delivery}. Work within the documented scope and registry trigger. Label evidence Documented, Interpretation, Hypothesis or Unknown; return the requested artefact, assumptions, limitations, verification actually performed and a concrete next action.
```

## What good output looks like

- Official component adapted to project
- Source and dependency reviewed with behaviours checked

## Quality checks

- [ ] Work matches the approved brief and the maker is not its checker.
- [ ] Claims are supported by source or supplied evidence; label uncertainty explicitly.
- [ ] Responsive behaviour, accessibility and performance are checked where they apply.
- [ ] Verification lists only commands, tests or browser checks actually run.

## Pairs with

- `skill:vercel-composition-patterns` — coordinate the artefacts and handoff at the relevant stage.
- `agent:frontend-architect` — coordinate the artefacts and handoff at the relevant stage.

## Limits and cautions

- Not for non-React or gratuitous motion
- do not install jsrepo globally
- Keep client data and credentials out of the public repository (D-0021); check licence and distribution prerequisites, including installation or sign-in when required.
