---
title: Minimal Change Engineer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:engineering-minimal-change-engineer
department: engineering
sub_department: product-frontend
job: code-modernization
role: lead
trigger: ""
kind: upstream-agent
availability: claude-managed
distribution: vendor
source: .claude/agents/engineering-minimal-change-engineer.md
invoke: "Claude Code agent: Minimal Change Engineer Agent"
pairs_with: [agent:implementer, agent:frontend-architect]
---
# Minimal Change Engineer

Minimal Change Engineer is the studio's lead for `code-modernization`.

## What it does

- Limits implementation to the smallest diff that solves the request
- Avoids unrelated refactors and speculative abstractions
- Surfaces out-of-scope improvements as separate follow-ups

## When to use

- For a tightly scoped bug fix or small feature
- Phase 05 Development or targeted repair

## When not to use

- For a broad redesign use `agent:frontend-architect`
- Clarify ambiguous scope before expanding
- Do not use to approve its own work; assign a separate checker.

## Inputs it needs

- Exact task and acceptance criteria
- Reproduction and relevant project conventions
- Targeted test or verification command

## How to run it

1. Confirm the task matches the job and, for a specialist, the registry trigger.
2. Invoke `Claude Code agent: Minimal Change Engineer Agent` and provide the approved brief, artefacts, constraints and source context.
3. Ask for the documented deliverable; inspect assumptions and verification before handoff.

```text
Use `agency:engineering-minimal-change-engineer` for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform/version: {links and versions}. Constraints: {accessibility, performance, delivery}. Work within the documented scope and registry trigger. Label evidence Documented, Interpretation, Hypothesis or Unknown; return the requested artefact, assumptions, limitations, verification actually performed and a concrete next action.
```

## What good output looks like

- Minimal patch with each line justified
- Out-of-scope follow-ups and actual verification

## Quality checks

- [ ] Work matches the approved brief and the maker is not its checker.
- [ ] Claims are supported by source or supplied evidence; label uncertainty explicitly.
- [ ] Responsive behaviour, accessibility and performance are checked where they apply.
- [ ] Verification lists only commands, tests or browser checks actually run.

## Pairs with

- `agent:implementer` — coordinate the artefacts and handoff at the relevant stage.
- `agent:frontend-architect` — coordinate the artefacts and handoff at the relevant stage.

## Limits and cautions

- Do not change unrequested files or claim correctness without targeted checks
- Keep client data and credentials out of the public repository (D-0021); check licence and distribution prerequisites, including installation or sign-in when required.
