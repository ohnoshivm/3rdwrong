---
title: Build Awwwards Quality Sites
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:build-awwwards-quality-sites
department: engineering
sub_department: product-frontend
job: ui-implementation
role: specialist
trigger: "When the approved scope specifically requires building a distinctive, motion-rich studio website or portfolio touchpoint."
kind: skill
availability: both
distribution: fetch
source: https://github.com/MengTo/Skills
invoke: "build-awwwards-quality-sites skill"
pairs_with: [agent:frontend-architect, skill:gstack-design-html]
---
# Build Awwwards Quality Sites

Build Awwwards Quality Sites is the studio's specialist for `ui-implementation`; use it when the registry trigger below applies.

## What it does

- Guides distinctive motion-rich studio websites and portfolio touchpoints
- Supports composition and motion implementation under an approved concept
- Targets high-quality frontend craft

## When to use

- When the approved scope specifically requires building a distinctive, motion-rich studio website or portfolio touchpoint.
- Only when approved scope is a distinctive motion-rich studio touchpoint
- Phase 05 after direction and motion purpose

## When not to use

- For art direction use design lead
- For ordinary UI use `agency:engineering-frontend-developer`
- Do not use to approve its own work; assign a separate checker.

## Inputs it needs

- Approved concept, assets and responsive states
- Project stack and performance budget
- Reduced-motion/accessibility needs

## How to run it

1. Confirm the task matches the job and, for a specialist, the registry trigger.
2. Invoke `build-awwwards-quality-sites skill` and provide the approved brief, artefacts, constraints and source context.
3. Ask for the documented deliverable; inspect assumptions and verification before handoff.

```text
Use `skill:build-awwwards-quality-sites` for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform/version: {links and versions}. Constraints: {accessibility, performance, delivery}. Work within the documented scope and registry trigger. Label evidence Documented, Interpretation, Hypothesis or Unknown; return the requested artefact, assumptions, limitations, verification actually performed and a concrete next action.
```

## What good output looks like

- Distinct implementation aligned to brief
- Rendered responsive inspection and motion/accessibility checks

## Quality checks

- [ ] Work matches the approved brief and the maker is not its checker.
- [ ] Claims are supported by source or supplied evidence; label uncertainty explicitly.
- [ ] Responsive behaviour, accessibility and performance are checked where they apply.
- [ ] Verification lists only commands, tests or browser checks actually run.

## Pairs with

- `agent:frontend-architect` — coordinate the artefacts and handoff at the relevant stage.
- `skill:gstack-design-html` — coordinate the artefacts and handoff at the relevant stage.

## Limits and cautions

- References inspire but are not copied
- avoid rejected identity motifs
- fetch may require install
- Keep client data and credentials out of the public repository (D-0021); check licence and distribution prerequisites, including installation or sign-in when required.
