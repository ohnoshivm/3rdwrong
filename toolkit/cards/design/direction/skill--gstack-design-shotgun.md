---
title: Design Shotgun
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:gstack-design-shotgun
department: design
sub_department: direction
job: concept-direction
role: specialist
trigger: "When exploring original visual territories from references or comparing several distinct directions."
kind: skill
availability: both
distribution: fetch
source: /Users/hustle/.config/opencode/skills/gstack-design-shotgun/SKILL.md
invoke: "/design-shotgun skill"
pairs_with: [skill:3w-creative-direction, skill:ceos-art-direction, ui-ux-pro-max:ui-ux-pro-max]
---

# Design Shotgun

A design-exploration specialist for creating multiple UI variants, a comparison board and structured iteration. For 3RDWRONG, use this specialist when the registry trigger applies: “When exploring original visual territories from references or comparing several distinct directions.”

## What it does

- Generates multiple AI design variants and opens a comparison board.
- Collects structured feedback and iterates on selected designs.
- Can be used for standalone exploration and proactively when a UI idea has not been visualised.
- Requires its gstack preamble and installation status before workflow use.

## When to use

- When exploring original visual territories from references or comparing several distinct directions.
- When a digital direction needs alternatives before detailed implementation.

## When not to use

- Final design approval or implementation QA; use `agent:visual-qa-engineer` and the project’s design lead.
- When gstack is unavailable or its required setup preamble fails.

## Inputs it needs

- The interface brief, intended action, constraints and design direction context.
- A host with the skill’s required gstack runtime.

## How to run it

1. Confirm gstack setup with its status workflow and run `/design-shotgun`.
2. Provide the UI brief and request multiple distinct alternatives plus a comparison board.
3. Collect structured feedback, iterate, then route the selected proposal to the accountable design lead.

```text
Use /design-shotgun skill. Task: {specific decision or output}. Context: {approved strategy, source links, version and constraints}. Return the documented format, label evidence and unknowns, and stop where required inputs or approval are missing.
```

## What good output looks like

- Several meaningfully different options are compared against explicit criteria.
- The selected direction remains proposed until a human signs it off.

## Quality checks

- [ ] The output answers the registry job and, for a specialist, the exact trigger.
- [ ] Every factual claim comes from supplied evidence or the tool’s documented method.
- [ ] An independent reviewer checks the output; the maker does not approve their own work.
- [ ] Accessibility, reduced motion and responsive behaviour are checked where relevant.

## Pairs with

- `skill:3w-creative-direction` — upstream context or hand-off.
- `skill:ceos-art-direction` — downstream review or delivery.
- `ui-ux-pro-max:ui-ux-pro-max` — downstream review or delivery.

## Limits and cautions

- Fetch distribution; requires gstack runtime and setup.
- The skill contains interactive question/workflow rules; follow them when invoked.
- Do not average concepts or present variants as approved; avoid own-identity rejected tropes.
