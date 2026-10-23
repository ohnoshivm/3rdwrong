---
title: Building Accessible Interfaces
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:building-accessible-interfaces
department: engineering
sub_department: product-frontend
job: accessibility-implementation
role: lead
trigger: ""
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.config/opencode/skills/building-accessible-interfaces/SKILL.md
invoke: "building-accessible-interfaces skill"
pairs_with: [agency:engineering-frontend-developer, skill:web-accessibility]
---
# Building Accessible Interfaces

Building Accessible Interfaces is the studio's lead for `accessibility-implementation`.

## What it does

- Guides semantic accessible interactive implementation
- Covers keyboard interaction, focus and accessible state patterns
- Treats accessibility as a build-time concern

## When to use

- During implementation/repair of interactive web interfaces
- shape controls and focus behaviour early

## When not to use

- For formal independent audit use `skill:web-accessibility`
- For data charts pair with data visualisation engineer
- Do not use to approve its own work; assign a separate checker.

## Inputs it needs

- Interaction/content requirements
- Target browsers and assistive technology
- Existing component system and audit findings

## How to run it

1. Confirm the task matches the job and, for a specialist, the registry trigger.
2. Invoke `building-accessible-interfaces skill` and provide the approved brief, artefacts, constraints and source context.
3. Ask for the documented deliverable; inspect assumptions and verification before handoff.

```text
Use `skill:building-accessible-interfaces` for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform/version: {links and versions}. Constraints: {accessibility, performance, delivery}. Work within the documented scope and registry trigger. Label evidence Documented, Interpretation, Hypothesis or Unknown; return the requested artefact, assumptions, limitations, verification actually performed and a concrete next action.
```

## What good output looks like

- Semantic, labelled, keyboard-operable controls
- Focus, error, contrast and motion behaviour checked

## Quality checks

- [ ] Work matches the approved brief and the maker is not its checker.
- [ ] Claims are supported by source or supplied evidence; label uncertainty explicitly.
- [ ] Responsive behaviour, accessibility and performance are checked where they apply.
- [ ] Verification lists only commands, tests or browser checks actually run.

## Pairs with

- `agency:engineering-frontend-developer` — coordinate the artefacts and handoff at the relevant stage.
- `skill:web-accessibility` — coordinate the artefacts and handoff at the relevant stage.

## Limits and cautions

- Implementation guidance does not certify WCAG
- use independent review and actual assistive technology tests
- Keep client data and credentials out of the public repository (D-0021); check licence and distribution prerequisites, including installation or sign-in when required.
