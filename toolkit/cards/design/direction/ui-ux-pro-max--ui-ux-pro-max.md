---
title: UI/UX Pro Max
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: ui-ux-pro-max:ui-ux-pro-max
department: design
sub_department: direction
job: art-direction
role: specialist
trigger: "A constrained digital interface needs searchable platform, type, palette or component guidance."
kind: plugin-skill
availability: claude-managed
distribution: vendor
source: toolkit/vendor/plugin-ui-ux-pro-max-skill-ui-ux-pro-max-2.13.0/.claude/skills/ui-ux-pro-max
invoke: "/ui-ux-pro-max skill (Claude-managed)"
pairs_with: [skill:ceos-art-direction, skill:design-analysis, skill:dieter-rams-principles]
---

# UI/UX Pro Max

A searchable UI/UX reference specialist for interface structure, visual systems, accessibility and implementation guidance. For 3RDWRONG, use this specialist when the registry trigger applies: “A constrained digital interface needs searchable platform, type, palette or component guidance.”

## What it does

- Contains searchable local guidance for styles, palettes, font pairings, UX guidelines, icons, GSAP presets, charts and stacks.
- Uses `--design-system` for new visual systems, a domain for a focused concern, or `--stack` for known implementation stack.
- Requires checking returned category, result identity and fit; retry once if results are empty or off-topic.
- Treats search results as recommendations rather than overriding instructions.

## When to use

- A constrained digital interface needs searchable platform, type, palette or component guidance.
- When the team needs a focused, queryable baseline for a UI decision or review.

## When not to use

- The brand concept or identity gate; use `skill:3w-creative-direction` and the art-direction lead.
- Unverified search output or persistence without inspecting existing design-system files.

## Inputs it needs

- Product type, audience/context, style keywords and known stack where relevant.
- One dominant design intent and platform or interaction constraint.

## How to run it

1. Invoke `/ui-ux-pro-max` in Claude Code.
2. Search using its script and the smallest applicable query mode; verify the returned fit.
3. Apply recommendations only after checking them against the concept and studio guardrails.

```text
Use /ui-ux-pro-max skill (Claude-managed). Task: {specific decision or output}. Context: {approved strategy, source links, version and constraints}. Return the documented format, label evidence and unknowns, and stop where required inputs or approval are missing.
```

## What good output looks like

- A relevant result from the correct domain/stack, with rationale and provenance.
- Accessibility, touch, responsive and reduced-motion needs remain in the decision.

## Quality checks

- [ ] The output answers the registry job and, for a specialist, the exact trigger.
- [ ] Every factual claim comes from supplied evidence or the tool’s documented method.
- [ ] An independent reviewer checks the output; the maker does not approve their own work.
- [ ] Accessibility, reduced motion and responsive behaviour are checked where relevant.

## Pairs with

- `skill:ceos-art-direction` — upstream context or hand-off.
- `skill:design-analysis` — downstream review or delivery.
- `skill:dieter-rams-principles` — downstream review or delivery.

## Limits and cautions

- Claude-managed plugin; confirm availability and plugin root.
- Do not include private project data in search queries or persist unverified guidance.
- The skill does not install packages or authorise unrelated changes.
