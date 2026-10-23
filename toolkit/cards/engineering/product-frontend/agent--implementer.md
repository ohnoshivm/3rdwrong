---
title: Implementer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agent:implementer
department: engineering
sub_department: product-frontend
job: ui-implementation
role: specialist
trigger: "Use for tasks involving Default Sonnet executor for clear implementation, tests, docs and routine debugging work."
kind: agent
availability: claude
distribution: vendor
source: toolkit/vendor/pack-founder-local-agents/agents/implementer.md
invoke: "Agent tool: implementer"
pairs_with: [agent:frontend-architect, agency:engineering-minimal-change-engineer]
---
# Implementer

Implementer is the studio's specialist for `ui-implementation`; use it when the registry trigger below applies.

## What it does

- Executes clear feature, test, documentation, debugging and refactor briefs
- Follows project conventions and makes the smallest correct change
- Reports actual commands and flags ambiguity

## When to use

- Use for tasks involving Default Sonnet executor for clear implementation, tests, docs and routine debugging work.
- For clear, bounded implementation work in Phase 05 Development

## When not to use

- For architecture spanning components/data use `agent:frontend-architect`
- Do not self-approve
- Do not use to approve its own work; assign a separate checker.

## Inputs it needs

- Task and acceptance criteria
- Relevant project files and conventions
- Targeted verification commands

## How to run it

1. Confirm the task matches the job and, for a specialist, the registry trigger.
2. Invoke `Agent tool: implementer` and provide the approved brief, artefacts, constraints and source context.
3. Ask for the documented deliverable; inspect assumptions and verification before handoff.

```text
Use `agent:implementer` for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform/version: {links and versions}. Constraints: {accessibility, performance, delivery}. Work within the documented scope and registry trigger. Label evidence Documented, Interpretation, Hypothesis or Unknown; return the requested artefact, assumptions, limitations, verification actually performed and a concrete next action.
```

## What good output looks like

- Small implementation with actual verification
- Completion report: done, changed paths, verified and open

## Quality checks

- [ ] Work matches the approved brief and the maker is not its checker.
- [ ] Claims are supported by source or supplied evidence; label uncertainty explicitly.
- [ ] Responsive behaviour, accessibility and performance are checked where they apply.
- [ ] Verification lists only commands, tests or browser checks actually run.

## Pairs with

- `agent:frontend-architect` — coordinate the artefacts and handoff at the relevant stage.
- `agency:engineering-minimal-change-engineer` — coordinate the artefacts and handoff at the relevant stage.

## Limits and cautions

- If ambiguous or larger than brief, report back
- maker is not checker
- Keep client data and credentials out of the public repository (D-0021); check licence and distribution prerequisites, including installation or sign-in when required.
