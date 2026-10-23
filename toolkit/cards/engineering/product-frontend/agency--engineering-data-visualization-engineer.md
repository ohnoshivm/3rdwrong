---
title: Data Visualization Engineer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:engineering-data-visualization-engineer
department: engineering
sub_department: product-frontend
job: ui-implementation
role: specialist
trigger: "When the approved scope specifically requires composition layout expertise."
kind: upstream-agent
availability: claude-managed
distribution: vendor
source: .claude/agents/engineering-data-visualization-engineer.md
invoke: "Claude Code agent: Data Visualization Engineer Agent"
pairs_with: [agency:engineering-frontend-developer, skill:building-accessible-interfaces]
---
# Data Visualization Engineer

Data Visualization Engineer is the studio's specialist for `ui-implementation`; use it when the registry trigger below applies.

## What it does

- Chooses chart encoding from the question and data shape
- Checks axes, aggregation, uncertainty and colour for perceptual honesty
- Plans accessible interaction and rendering for real data volume

## When to use

- When the approved scope specifically requires composition layout expertise.
- Use at concept and implementation when an approved deliverable needs truthful data charts
- Registry trigger says composition layout expertise, while source is specifically data visualisation

## When not to use

- For ordinary page composition use design/architecture
- For data provenance, ask the data owner
- Do not use to approve its own work; assign a separate checker.

## Inputs it needs

- Question and decision the chart supports
- Representative data, units, volume and uncertainty
- Approved visual direction and accessibility constraints

## How to run it

1. Confirm the task matches the job and, for a specialist, the registry trigger.
2. Invoke `Claude Code agent: Data Visualization Engineer Agent` and provide the approved brief, artefacts, constraints and source context.
3. Ask for the documented deliverable; inspect assumptions and verification before handoff.

```text
Use `agency:engineering-data-visualization-engineer` for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform/version: {links and versions}. Constraints: {accessibility, performance, delivery}. Work within the documented scope and registry trigger. Label evidence Documented, Interpretation, Hypothesis or Unknown; return the requested artefact, assumptions, limitations, verification actually performed and a concrete next action.
```

## What good output looks like

- Chart choice tied to question and data
- Honest axes, accessible alternative and measured rendering plan

## Quality checks

- [ ] Work matches the approved brief and the maker is not its checker.
- [ ] Claims are supported by source or supplied evidence; label uncertainty explicitly.
- [ ] Responsive behaviour, accessibility and performance are checked where they apply.
- [ ] Verification lists only commands, tests or browser checks actually run.

## Pairs with

- `agency:engineering-frontend-developer` — coordinate the artefacts and handoff at the relevant stage.
- `skill:building-accessible-interfaces` — coordinate the artefacts and handoff at the relevant stage.

## Limits and cautions

- Reject truncated bar baselines, unjustified dual axes, chartjunk and decorative 3D
- Trigger appears inconsistent with source scope
- Keep client data and credentials out of the public repository (D-0021); check licence and distribution prerequisites, including installation or sign-in when required.
