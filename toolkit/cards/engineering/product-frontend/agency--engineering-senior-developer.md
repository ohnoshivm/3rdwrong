---
title: Senior Developer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:engineering-senior-developer
department: engineering
sub_department: product-frontend
job: ui-implementation
role: specialist
trigger: "Use for engineering/product-frontend/ui-implementation when the brief specifically requires: Premium implementation specialist - Masters Laravel/Livewire/FluxUI, advanced CSS, Three.js integration ."
kind: upstream-agent
availability: claude-managed
distribution: vendor
source: .claude/agents/engineering-senior-developer.md
invoke: "Claude Code agent: Senior Developer Agent"
pairs_with: [agent:frontend-architect, agent:3d-webgl-engineer]
---
# Senior Developer

Senior Developer is the studio's specialist for `ui-implementation`; use it when the registry trigger below applies.

## What it does

- Implements advanced CSS and Three.js with Laravel/Livewire/FluxUI contexts
- Builds interface effects and details in those technologies
- Uses responsive, interaction and performance QA

## When to use

- Use for engineering/product-frontend/ui-implementation when the brief specifically requires: Premium implementation specialist - Masters Laravel/Livewire/FluxUI, advanced CSS, Three.js integration .
- When the approved scope requires Laravel/Livewire/FluxUI, advanced CSS or Three.js integration
- Phase 05 Development

## When not to use

- For React/Next architecture use `agent:frontend-architect`
- For Three.js scene architecture use `agent:3d-webgl-engineer`
- Do not use to approve its own work; assign a separate checker.

## Inputs it needs

- Approved design and stack
- Framework versions and existing components
- Performance, accessibility and motion constraints

## How to run it

1. Confirm the task matches the job and, for a specialist, the registry trigger.
2. Invoke `Claude Code agent: Senior Developer Agent` and provide the approved brief, artefacts, constraints and source context.
3. Ask for the documented deliverable; inspect assumptions and verification before handoff.

```text
Use `agency:engineering-senior-developer` for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform/version: {links and versions}. Constraints: {accessibility, performance, delivery}. Work within the documented scope and registry trigger. Label evidence Documented, Interpretation, Hypothesis or Unknown; return the requested artefact, assumptions, limitations, verification actually performed and a concrete next action.
```

## What good output looks like

- Focused implementation aligned to existing stack
- Responsive and interaction checks with gaps recorded

## Quality checks

- [ ] Work matches the approved brief and the maker is not its checker.
- [ ] Claims are supported by source or supplied evidence; label uncertainty explicitly.
- [ ] Responsive behaviour, accessibility and performance are checked where they apply.
- [ ] Verification lists only commands, tests or browser checks actually run.

## Pairs with

- `agent:frontend-architect` — coordinate the artefacts and handoff at the relevant stage.
- `agent:3d-webgl-engineer` — coordinate the artefacts and handoff at the relevant stage.

## Limits and cautions

- Avoid rejected black/heavy-grotesk/neon identity direction
- motion serves concept and honours reduced motion
- Keep client data and credentials out of the public repository (D-0021); check licence and distribution prerequisites, including installation or sign-in when required.
