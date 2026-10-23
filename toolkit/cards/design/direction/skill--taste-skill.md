---
title: Design Taste Frontend
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:taste-skill
department: design
sub_department: direction
job: inspiration-taste
role: lead
trigger: ""
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-leonxlnx-taste-skill-mit/skills/taste-skill
invoke: "/design-taste-frontend skill"
pairs_with: [skill:3w-creative-direction, skill:ceos-art-direction, skill:design-analysis]
---

# Design Taste Frontend

The inspiration-taste lead for subject-specific digital direction, image planning and measured browser review. For 3RDWRONG, this is the lead tool for inspiration taste.

## What it does

- Uses a draw script to offer researched page directions, then produces a direction sheet with type, palette, hero and section compositions.
- Derives the idea from the subject’s own facts and requires a live thing tied to that idea.
- Specifies image sourcing, responsive composition, semantic states and purposeful motion.
- Uses lint and a real-browser inspector across 1440, 768 and 390 widths, followed by screenshot critique and fixes.

## When to use

- Use for the studio’s recurring digital taste work and when a public-facing page needs a subject-specific direction.
- For weekly taste practice or calibration when the brief concerns a page or app screen.

## When not to use

- Brand identity routes without the signed strategy gate; use `skill:3w-creative-direction`.
- When required inspection/runtime prerequisites are unavailable and the task requires verified QA.

## Inputs it needs

- Subject, audience, action, stack, brand, real assets and constraints.
- A reference pack and project-specific material; the skill requires authentic subject detail.

## How to run it

1. Invoke `/design-taste-frontend` in Claude Code or Codex.
2. Follow the ordered draw, idea, copy, build, image, live-thing and inspect workflow in the skill.
3. Inspect all listed screenshots after the final change and report checks actually run.

```text
Use /design-taste-frontend skill. Task: {specific decision or output}. Context: {approved strategy, source links, version and constraints}. Return the documented format, label evidence and unknowns, and stop where required inputs or approval are missing.
```

## What good output looks like

- A subject-specific idea, complete content and a responsive direction sheet.
- Final report includes inspection evidence, remaining limitations and media credits where applicable.

## Quality checks

- [ ] The output answers the registry job and, for a specialist, the exact trigger.
- [ ] Every factual claim comes from supplied evidence or the tool’s documented method.
- [ ] An independent reviewer checks the output; the maker does not approve their own work.
- [ ] Accessibility, reduced motion and responsive behaviour are checked where relevant.

## Pairs with

- `skill:3w-creative-direction` — upstream context or hand-off.
- `skill:ceos-art-direction` — downstream review or delivery.
- `skill:design-analysis` — downstream review or delivery.

## Limits and cautions

- Requires Node 22+ and browser software for the full inspector; scripts install nothing.
- No network means open asset collections cannot be searched; state that limitation.
- Its house aesthetic conflicts with some other style skills; follow the approved project concept, accessibility and 3RDWRONG identity guardrails.
