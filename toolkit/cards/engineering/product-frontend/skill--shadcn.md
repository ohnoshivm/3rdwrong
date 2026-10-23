---
title: shadcn/ui
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:shadcn
department: engineering
sub_department: product-frontend
job: ui-implementation
role: specialist
trigger: "Use for tasks involving Manages shadcn components and projects."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-shadcn-ui-ui-mit/skills/shadcn
invoke: "Claude Code: load the shadcn skill as context (not directly user-invocable)"
pairs_with: [skill:tailwindcss, agent:frontend-architect]
---
# shadcn/ui

shadcn/ui is the studio's specialist for `ui-implementation`; use it when the registry trigger below applies.

## What it does

- Manages shadcn components/projects using package runner
- Searches registries/docs before implementation
- Uses semantic tokens and accessible composition rules

## When to use

- Use for tasks involving Manages shadcn components and projects.
- When project uses or explicitly selects shadcn/ui
- Phase 05

## When not to use

- For another component system follow it
- For Tailwind only use `skill:tailwindcss`
- Do not use to approve its own work; assign a separate checker.

## Inputs it needs

- Package manager and current config
- Requested component/issue
- Tokens and base choice

## How to run it

1. Confirm the task matches the job and, for a specialist, the registry trigger.
2. Load the `shadcn` skill as model context and provide the approved brief, artefacts, constraints and source context; its source marks it not directly user-invocable.
3. Ask for the documented deliverable; inspect assumptions and verification before handoff.

```text
Use `skill:shadcn` for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform/version: {links and versions}. Constraints: {accessibility, performance, delivery}. Work within the documented scope and registry trigger. Label evidence Documented, Interpretation, Hypothesis or Unknown; return the requested artefact, assumptions, limitations, verification actually performed and a concrete next action.
```

## What good output looks like

- Components fit config and composition rules
- CLI/package runner and API verified

## Quality checks

- [ ] Work matches the approved brief and the maker is not its checker.
- [ ] Claims are supported by source or supplied evidence; label uncertainty explicitly.
- [ ] Responsive behaviour, accessibility and performance are checked where they apply.
- [ ] Verification lists only commands, tests or browser checks actually run.

## Pairs with

- `skill:tailwindcss` — coordinate the artefacts and handoff at the relevant stage.
- `agent:frontend-architect` — coordinate the artefacts and handoff at the relevant stage.

## Limits and cautions

- Do not add library speculatively
- source requires accessible titles and semantic tokens
- Keep client data and credentials out of the public repository (D-0021); check licence and distribution prerequisites, including installation or sign-in when required.
