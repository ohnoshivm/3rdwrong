---
title: CEOS Art Direction
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:ceos-art-direction
department: design
sub_department: direction
job: art-direction
role: lead
trigger: ""
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-ohnoshivm-creative-engineering-os-mit/skills/ceos-art-direction
invoke: "/ceos-art-direction skill"
pairs_with: [skill:3w-creative-direction, agent:frontend-architect, agent:visual-qa-engineer]
---

# CEOS Art Direction

The visual-system lead for turning an approved concept into tokens, responsive composition and screenshot-based critique. For 3RDWRONG, this is the lead tool for art direction.

## What it does

- Sets typography, grid, colour roles, imagery/material direction and responsive art direction.
- Translates the concept into tokens and section compositions before building all sections.
- Calls for a real browser prototype and a screenshot-based critique with evidence, rule and exact fix.
- Lists failure criteria including too many type sizes, generic grids, gradients, grey text and magic numbers.

## When to use

- Phase 04/05, when an approved concept needs to become a visual system or a rendered page looks off.
- When setting type, fonts, palettes, grids, imagery or materials for a digital experience.

## When not to use

- Generating the identity concept itself; use `skill:3w-creative-direction` first.
- Implementation, motion or performance ownership; hand off to engineering/motion leads.

## Inputs it needs

- Approved `CONCEPT.md`, brand assets, content inventory and imagery inventory.
- A real page or representative first screen to prototype and inspect.

## How to run it

1. Invoke `/ceos-art-direction` in Claude Code or Codex.
2. Supply the approved concept and inventories; request tokens and desktop/phone composition rules.
3. Inspect real screenshots and fix issues using evidence → violated rule → exact change.

```text
Use /ceos-art-direction skill. Task: {specific decision or output}. Context: {approved strategy, source links, version and constraints}. Return the documented format, label evidence and unknowns, and stop where required inputs or approval are missing.
```

## What good output looks like

- Concept-linked tokens and compositions, including a separate phone composition.
- Screenshot findings are measurable and each has a concrete fix.

## Quality checks

- [ ] The output answers the registry job and, for a specialist, the exact trigger.
- [ ] Every factual claim comes from supplied evidence or the tool’s documented method.
- [ ] An independent reviewer checks the output; the maker does not approve their own work.
- [ ] Accessibility, reduced motion and responsive behaviour are checked where relevant.

## Pairs with

- `skill:3w-creative-direction` — upstream context or hand-off.
- `agent:frontend-architect` — downstream review or delivery.
- `agent:visual-qa-engineer` — downstream review or delivery.

## Limits and cautions

- Requires a real rendered prototype for critique; do not claim unrun visual checks.
- Verify font licences; do not present found/stock/generated images as client work.
- Reduced motion/accessibility and 3RDWRONG identity guardrails apply.
