---
title: Vercel React Composition Patterns
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:vercel-composition-patterns
department: engineering
sub_department: product-frontend
job: ui-implementation
role: specialist
trigger: "When the approved scope specifically requires use when the task specifically needs react composition patterns that scale."
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.config/opencode/skills/vercel-composition-patterns/SKILL.md
invoke: "vercel-composition-patterns skill"
pairs_with: [agent:frontend-architect, vercel:react-best-practices]
---
# Vercel React Composition Patterns

Vercel React Composition Patterns is the studio's specialist for `ui-implementation`; use it when the registry trigger below applies.

## What it does

- Guides scalable React component composition
- Uses compound components and state boundaries over boolean prop growth
- Includes React 19 patterns

## When to use

- When the approved scope specifically requires use when the task specifically needs react composition patterns that scale.
- When reusable React APIs or boolean-heavy components need architecture
- Phase 02/05

## When not to use

- For non-React use native project guidance
- For Next routing use `vercel:nextjs`
- Do not use to approve its own work; assign a separate checker.

## Inputs it needs

- React version and component consumers
- Current API, variants and state ownership

## How to run it

1. Confirm the task matches the job and, for a specialist, the registry trigger.
2. Invoke `vercel-composition-patterns skill` and provide the approved brief, artefacts, constraints and source context.
3. Ask for the documented deliverable; inspect assumptions and verification before handoff.

```text
Use `skill:vercel-composition-patterns` for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform/version: {links and versions}. Constraints: {accessibility, performance, delivery}. Work within the documented scope and registry trigger. Label evidence Documented, Interpretation, Hypothesis or Unknown; return the requested artefact, assumptions, limitations, verification actually performed and a concrete next action.
```

## What good output looks like

- Composable API with clear state boundaries
- Version assumptions and migration effects stated

## Quality checks

- [ ] Work matches the approved brief and the maker is not its checker.
- [ ] Claims are supported by source or supplied evidence; label uncertainty explicitly.
- [ ] Responsive behaviour, accessibility and performance are checked where they apply.
- [ ] Verification lists only commands, tests or browser checks actually run.

## Pairs with

- `agent:frontend-architect` — coordinate the artefacts and handoff at the relevant stage.
- `vercel:react-best-practices` — coordinate the artefacts and handoff at the relevant stage.

## Limits and cautions

- Guidance, not a runtime checker
- do not refactor without consumer context
- Keep client data and credentials out of the public repository (D-0021); check licence and distribution prerequisites, including installation or sign-in when required.
