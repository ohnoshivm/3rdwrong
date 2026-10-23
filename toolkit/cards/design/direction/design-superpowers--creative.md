---
title: Design Superpowers Creative
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: design-superpowers:creative
department: design
sub_department: direction
job: art-direction
role: specialist
trigger: "An approved strategy needs rough digital visual-direction alternatives before implementation."
kind: plugin-skill
availability: claude
distribution: vendor
source: toolkit/vendor/plugin-account-synced-design-superpowers-marketplace/skills/creative
invoke: "/creative"
pairs_with: [skill:3w-creative-direction, skill:ceos-art-direction]
---

# Design Superpowers Creative

A design exploration skill for generating digital visual-direction alternatives from an approved strategy. For 3RDWRONG, use this specialist when the registry trigger applies: “An approved strategy needs rough digital visual-direction alternatives before implementation.”

## What it does

- Detects design-system maturity from L0 greenfield through L3 enterprise constraints and announces the level.
- Routes direction work to moodboard, palette, typography, layout, refresh or brand-design sub-agents.
- Produces three theme variants across distinct style families, then asks the user to choose or iterate.
- Offers a next step such as palette or typography work; imagery paths are offered when the direction requires images.

## When to use

- An approved strategy needs rough digital visual-direction alternatives before implementation.
- Phase 04 Concept, when alternatives are exploratory and not final visual approval.

## When not to use

- The identity concept gate; use `skill:3w-creative-direction`.
- Final implementation or QA; use the relevant maker and independent checker.

## Inputs it needs

- Project or product, desired feeling, creativity and density preferences, and any admired references.
- Existing design system or `DESIGN.md`, approved direction and brand constraints.
- Brand colours or type when palette/typography work is requested.

## How to run it

1. Invoke `/creative` in Claude Code and provide the project and direction question.
2. Let it detect maturity and return a theme table with safe, balanced and bold variants.
3. Choose or iterate, then request a routed palette, typography or layout pass as needed.
4. Record founder selection before implementation.

```text
Use `/creative` in Claude Code. Task: {specific decision or output}. Context: {approved strategy, source links, version and constraints}. Return the documented format, label evidence and unknowns, and stop where required inputs or approval are missing.
```

## What good output looks like

- Three distinct theme variants each have key traits and a “best for” use.
- The selected direction respects the existing design-system maturity and approved strategy.
- No output is treated as approved without founder review.

## Quality checks

- [ ] The output answers the registry job and, for a specialist, the exact trigger.
- [ ] Every factual claim comes from supplied evidence or the tool’s documented method.
- [ ] An independent reviewer checks the output; the maker does not approve their own work.
- [ ] Accessibility, reduced motion and responsive behaviour are checked where relevant.

## Pairs with

- `skill:3w-creative-direction` — upstream context or hand-off.
- `skill:ceos-art-direction` — downstream review or delivery.

## Limits and cautions

- Claude plugin skill distributed from a synced vendor package.
- At L0/L1, the source says Figma inspection is unavailable unless the adapter is installed; do not imply live inspection.
- The source may ask the user to choose a direction; do not treat a variant as approved.
- Do not use black backgrounds, heavy grotesk and neon for 3RDWRONG own identity; obey D-0006.
