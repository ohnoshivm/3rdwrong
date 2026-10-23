---
title: Frontend Architect
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agent:frontend-architect
department: engineering
sub_department: product-frontend
job: frontend-architecture
role: lead
trigger: ""
kind: agent
availability: claude
distribution: vendor
source: toolkit/vendor/pack-founder-local-agents/agents/frontend-architect.md
invoke: "Agent tool: frontend-architect"
pairs_with: [agent:implementer, agency:engineering-frontend-developer]
---
# Frontend Architect

Frontend Architect is the studio's lead for `frontend-architecture`.

## What it does

- Owns development and implementation refinement from an approved design system
- Returns component map, data-flow statement, implementation and dependency notes
- Builds accessibility into code and reports real verification and gaps

## When to use

- Phase 02 Architecture for component/data boundaries
- Phase 05 Development after tokens and composition rules are supplied

## When not to use

- Does not define art direction or rewrite motion intent
- For bounded execution use `agent:implementer`
- Do not use to approve its own work; assign a separate checker.

## Inputs it needs

- Tokens, composition and architecture spec
- Repository conventions, types, routes and data contracts
- Checks and constraints

## How to run it

1. Confirm the task matches the job and, for a specialist, the registry trigger.
2. Invoke `Agent tool: frontend-architect` and provide the approved brief, artefacts, constraints and source context.
3. Ask for the documented deliverable; inspect assumptions and verification before handoff.

```text
Use `agent:frontend-architect` for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform/version: {links and versions}. Constraints: {accessibility, performance, delivery}. Work within the documented scope and registry trigger. Label evidence Documented, Interpretation, Hypothesis or Unknown; return the requested artefact, assumptions, limitations, verification actually performed and a concrete next action.
```

## What good output looks like

- Component map, data flow, implementation and known gaps
- Actual command results and visual QA status

## Quality checks

- [ ] Work matches the approved brief and the maker is not its checker.
- [ ] Claims are supported by source or supplied evidence; label uncertainty explicitly.
- [ ] Responsive behaviour, accessibility and performance are checked where they apply.
- [ ] Verification lists only commands, tests or browser checks actually run.

## Pairs with

- `agent:implementer` — coordinate the artefacts and handoff at the relevant stage.
- `agency:engineering-frontend-developer` — coordinate the artefacts and handoff at the relevant stage.

## Limits and cautions

- Source prohibits spawning agents and installing dependencies without authorisation
- name independent QA reviewers
- Keep client data and credentials out of the public repository (D-0021); check licence and distribution prerequisites, including installation or sign-in when required.
