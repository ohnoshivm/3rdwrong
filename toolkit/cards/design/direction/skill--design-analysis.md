---
title: Design Analysis
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:design-analysis
department: design
sub_department: direction
job: inspiration-taste
role: specialist
trigger: "When the approved scope specifically requires extracting visual properties from a screenshot or live page."
kind: skill
availability: codex
distribution: manual
source: /Users/hustle/.agents/skills/design-analysis/SKILL.md
invoke: "/design-analysis skill"
pairs_with: [skill:dieter-rams-principles, ui-ux-pro-max:ui-ux-pro-max, agent:visual-qa-engineer]
---

# Design Analysis

A forensics specialist that measures and describes the properties of a supplied screenshot or live page. For 3RDWRONG, use this specialist when the registry trigger applies: “When the approved scope specifically requires extracting visual properties from a screenshot or live page.”

## What it does

- Analyses typography, colour, layout, composition, imagery, spacing, shape and motion.
- For a URL, captures desktop and mobile views and harvests computed styles.
- Uses pixel sampling and DOM measurements rather than guessing values.
- Keeps extraction separate from critique and hands off to an appropriate review tool.

## When to use

- When the approved scope specifically requires extracting visual properties from a screenshot or live page.
- Before critique when the design’s actual properties have not been measured.

## When not to use

- For an unmeasured impression or final design verdict; use `skill:dieter-rams-principles` or another critique tool after analysis.
- When exact measurements are requested from a pasted image without a file path or URL.

## Inputs it needs

- Image file, URL, local dev server or Figma link.
- A bounded scope: page, component or flow.

## How to run it

1. Invoke `/design-analysis` in Codex.
2. For URL inputs, run the skill’s capture workflow and measurement scripts.
3. Report measured properties separately from interpretation; cite the inspected scope.

```text
Use /design-analysis skill. Task: {specific decision or output}. Context: {approved strategy, source links, version and constraints}. Return the documented format, label evidence and unknowns, and stop where required inputs or approval are missing.
```

## What good output looks like

- Measured font, colours and spacing with scope and source specified.
- No guessed hex, font size or spacing value where measurement was possible.

## Quality checks

- [ ] The output answers the registry job and, for a specialist, the exact trigger.
- [ ] Every factual claim comes from supplied evidence or the tool’s documented method.
- [ ] An independent reviewer checks the output; the maker does not approve their own work.
- [ ] Accessibility, reduced motion and responsive behaviour are checked where relevant.

## Pairs with

- `skill:dieter-rams-principles` — upstream context or hand-off.
- `ui-ux-pro-max:ui-ux-pro-max` — downstream review or delivery.
- `agent:visual-qa-engineer` — downstream review or delivery.

## Limits and cautions

- Codex skill; URL analysis depends on browser tooling and Playwright.
- The source includes fallback setup instructions; do not claim measurements if its scripts did not run.
- Visual analysis does not establish preference or audience response.
