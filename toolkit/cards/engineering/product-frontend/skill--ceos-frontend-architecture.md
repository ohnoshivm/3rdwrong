---
title: Creative Engineering Frontend Architecture
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:ceos-frontend-architecture
department: engineering
sub_department: product-frontend
job: frontend-architecture
role: specialist
trigger: "Use for tasks involving Chooses and structures the frontend for creative websites."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-ohnoshivm-creative-engineering-os-mit/skills/ceos-frontend-architecture
invoke: "ceos-frontend-architecture skill"
pairs_with: [agent:frontend-architect, agency:engineering-frontend-developer]
---
# Creative Engineering Frontend Architecture

Creative Engineering Frontend Architecture is the studio's specialist for `frontend-architecture`; use it when the registry trigger below applies.

## What it does

- Chooses frontend architecture for creative websites
- Frames stack and boundaries around the experience
- Provides an implementation foundation before detailed build

## When to use

- Use for tasks involving Chooses and structures the frontend for creative websites.
- Phase 02 Architecture before framework/rendering/component choices

## When not to use

- For settled React/Next implementation use `agent:frontend-architect`
- For CMS theme use CMS developer
- Do not use to approve its own work; assign a separate checker.

## Inputs it needs

- Experience brief and approved direction
- Interactions/content model
- Repo, team and hosting constraints

## How to run it

1. Confirm the task matches the job and, for a specialist, the registry trigger.
2. Invoke `ceos-frontend-architecture skill` and provide the approved brief, artefacts, constraints and source context.
3. Ask for the documented deliverable; inspect assumptions and verification before handoff.

```text
Use `skill:ceos-frontend-architecture` for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform/version: {links and versions}. Constraints: {accessibility, performance, delivery}. Work within the documented scope and registry trigger. Label evidence Documented, Interpretation, Hypothesis or Unknown; return the requested artefact, assumptions, limitations, verification actually performed and a concrete next action.
```

## What good output looks like

- Concise architecture with boundaries and trade-offs
- Fits concept, conventions and performance/accessibility

## Quality checks

- [ ] Work matches the approved brief and the maker is not its checker.
- [ ] Claims are supported by source or supplied evidence; label uncertainty explicitly.
- [ ] Responsive behaviour, accessibility and performance are checked where they apply.
- [ ] Verification lists only commands, tests or browser checks actually run.

## Pairs with

- `agent:frontend-architect` — coordinate the artefacts and handoff at the relevant stage.
- `agency:engineering-frontend-developer` — coordinate the artefacts and handoff at the relevant stage.

## Limits and cautions

- Does not replace art direction or visual QA
- avoid speculative dependencies
- Keep client data and credentials out of the public repository (D-0021); check licence and distribution prerequisites, including installation or sign-in when required.
