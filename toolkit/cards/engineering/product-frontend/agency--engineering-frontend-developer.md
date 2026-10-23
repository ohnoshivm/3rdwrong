---
title: Frontend Developer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:engineering-frontend-developer
department: engineering
sub_department: product-frontend
job: ui-implementation
role: lead
trigger: ""
kind: upstream-agent
availability: claude-managed
distribution: vendor
source: .claude/agents/engineering-frontend-developer.md
invoke: "Claude Code agent: Frontend Developer Agent"
pairs_with: [agent:frontend-architect, agent:implementer, skill:building-accessible-interfaces]
---
# Frontend Developer

Frontend Developer is the studio's lead for `ui-implementation`.

## What it does

- Builds responsive web apps with React, Vue, Angular or Svelte
- Implements component libraries, design systems, API integration and state
- Covers performance, accessibility, testing and cross-browser behaviour

## When to use

- Lead implementation of approved web UI
- Phase 05 Development after Design supplies direction and tokens

## When not to use

- For CMS-specific work use `agency:engineering-cms-developer`
- For a bounded routine task use `agent:implementer`
- Do not use to approve its own work; assign a separate checker.

## Inputs it needs

- Approved design, content and interaction states
- Framework, repository patterns and API contracts
- Accessibility and performance constraints

## How to run it

1. Confirm the task matches the job and, for a specialist, the registry trigger.
2. Invoke `Claude Code agent: Frontend Developer Agent` and provide the approved brief, artefacts, constraints and source context.
3. Ask for the documented deliverable; inspect assumptions and verification before handoff.

```text
Use `agency:engineering-frontend-developer` for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform/version: {links and versions}. Constraints: {accessibility, performance, delivery}. Work within the documented scope and registry trigger. Label evidence Documented, Interpretation, Hypothesis or Unknown; return the requested artefact, assumptions, limitations, verification actually performed and a concrete next action.
```

## What good output looks like

- Working responsive implementation with suitable component boundaries
- Actual test/build and known-gap report

## Quality checks

- [ ] Work matches the approved brief and the maker is not its checker.
- [ ] Claims are supported by source or supplied evidence; label uncertainty explicitly.
- [ ] Responsive behaviour, accessibility and performance are checked where they apply.
- [ ] Verification lists only commands, tests or browser checks actually run.

## Pairs with

- `agent:frontend-architect` — coordinate the artefacts and handoff at the relevant stage.
- `agent:implementer` — coordinate the artefacts and handoff at the relevant stage.
- `skill:building-accessible-interfaces` — coordinate the artefacts and handoff at the relevant stage.

## Limits and cautions

- Do not claim visual fidelity from code alone
- independent rendered inspection is required
- Keep client data and credentials out of the public repository (D-0021); check licence and distribution prerequisites, including installation or sign-in when required.
