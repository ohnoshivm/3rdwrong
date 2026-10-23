---
title: Composition system
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:3w-composition-system
department: design
sub_department: identity-craft
job: composition-layout
role: lead
trigger: ""
kind: repo-skill
availability: repo
distribution: repo
source: skills/3w-composition-system/SKILL.md
invoke: "3w-composition-system skill"
pairs_with: [skill:3w-mark-exploration, skill:3w-typography-system, skill:3w-colour-system, skill:3w-identity-system-critic, skill:3w-brand-consistency-qa, design-skills:design-elevation]
---
# Composition system

The studio's lead tool for brand-wide composition: invariants, variables, grids and hierarchy rules that hold across digital, print, social, environmental and motion formats.

## What it does

- Separates a few measurable invariants from variables and named exceptions.
- Derives grids and modules from a stated base unit so they scale between formats.
- Sets reading order, levels allowed and what gives way first when space runs out.
- Defines type-image rules, format behaviours and required information visible without motion.
- Tests on the agreed application set, runs an unfamiliar-colleague test and packages templates.

## When to use

- Phase 05 Identity, once draft mark, type and colour exist.
- Phase 06 System, to specify and test rules across applications.
- When a new format joins the system after launch.

## When not to use

- To style a single hero mock-up or design a product interface's flows.
- As a preset layout recipe — presets such as `skill:split-layout-technical` are specialists for that exact device.
- For refining one approved artefact — use `design-skills:design-elevation`.

## Inputs it needs

- Chosen route; draft logo, type and colour.
- Applications with real dimensions, fixed content blocks and representative content.
- Image direction and motion scope if any.

## How to run it

1. Collect the inputs above in one folder or message; state whether the route is chosen or the run is formative.
2. Run the skill; a human designer makes every form decision it records.
3. Hand the output to someone other than the maker for review.
4. File the output in the project folder; nothing it produces is an approval.

```text
Use the 3w-composition-system skill for {{project}}. Route: {{link}}. Mark, type and colour drafts: {{links}}. Applications with dimensions and fixed content: {{list}}. Return the skill's exact output structure; label stand-in dimensions; do not approve anything.
```

## What good output looks like

- Few invariants with measures and the smallest format they survive.
- Format behaviours for every in-scope family; others marked out of scope.
- Application tests at real dimensions with long and short content, and an unfamiliar-colleague result.

## Quality checks

- [ ] Invariants are measurable and few.
- [ ] At least three unlike applications tested, or the limit stated.
- [ ] Required information is visible without motion; reduced-motion version exists.
- [ ] The unfamiliar-colleague test ran or is listed as not run.
- [ ] Reviewer is not the maker.

## Pairs with

- Upstream: `skill:3w-mark-exploration`, `skill:3w-typography-system`, `skill:3w-colour-system`.
- Downstream: `skill:3w-identity-system-critic`, then `skill:3w-brand-consistency-qa` once rules are approved.
- Specialist: `design-skills:design-elevation` for one bounded artefact.

## Limits and cautions

- Experimental; one fictional run so far, with stand-in dimensions and no drawn layouts.
- An AI rebuild from the rule sheet is only a proxy for the human unfamiliar-colleague test.
- Do not hide failing layouts with mock-up lighting or texture.
