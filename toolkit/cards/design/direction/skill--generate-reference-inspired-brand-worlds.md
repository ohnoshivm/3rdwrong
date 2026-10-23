---
title: Generate Reference-Inspired Brand Worlds
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:generate-reference-inspired-brand-worlds
department: design
sub_department: direction
job: concept-direction
role: specialist
trigger: "When exploring original visual territories from references or comparing several distinct directions."
kind: skill
availability: claude
distribution: manual
source: /Users/hustle/.claude/skills-library/master-of-20261021/visual-design/generate-reference-inspired-brand-worlds/SKILL.md
invoke: "/generate-reference-inspired-brand-worlds skill"
pairs_with: [skill:3w-creative-direction, skill:ceos-art-direction, skill:imagegen]
---

# Generate Reference-Inspired Brand Worlds

An originality-aware specialist for generating distinct brand worlds from supplied visual references. For 3RDWRONG, use this specialist when the registry trigger applies: “When exploring original visual territories from references or comparing several distinct directions.”

## What it does

- Inspects supplied images and separates reusable visual grammar from protected signature elements.
- Uses a similarity dial to communicate intent, not as a measured similarity score.
- Builds a distinct-brand matrix and writes one image-generation prompt per brand.
- Preserves originality by changing meaning, subjects, arrangement, signature objects and letterforms.

## When to use

- When exploring original visual territories from references or comparing several distinct directions.
- When supplied artwork needs a related but materially original brand-world alternative.

## When not to use

- Copying an existing brand identity or reproducing a protected signature composition.
- Concept strategy without a supplied visual reference; use `skill:3w-creative-direction`.

## Inputs it needs

- Supplied reference images and current concept/content anchor, if revising.
- Brand name, meaning and intended similarity range.

## How to run it

1. Invoke `/generate-reference-inspired-brand-worlds` in Claude Code.
2. Inspect references and list reusable grammar and protected signature elements.
3. Generate one prompt per distinct brand and route through the available image-generation tool.

```text
Use /generate-reference-inspired-brand-worlds skill. Task: {specific decision or output}. Context: {approved strategy, source links, version and constraints}. Return the documented format, label evidence and unknowns, and stop where required inputs or approval are missing.
```

## What good output looks like

- Brand worlds form a coherent family without becoming colour swaps.
- Protected marks, wording, poses, layouts and letterforms are excluded.

## Quality checks

- [ ] The output answers the registry job and, for a specialist, the exact trigger.
- [ ] Every factual claim comes from supplied evidence or the tool’s documented method.
- [ ] An independent reviewer checks the output; the maker does not approve their own work.
- [ ] Accessibility, reduced motion and responsive behaviour are checked where relevant.

## Pairs with

- `skill:3w-creative-direction` — upstream context or hand-off.
- `skill:ceos-art-direction` — downstream review or delivery.
- `skill:imagegen` — downstream review or delivery.

## Limits and cautions

- Claude skill; image generation tool is a prerequisite for generating outputs.
- Similarity percentages express intent and are not measurable scores.
- Keep reference images out of reusable assets unless owned and explicitly authorised.
- Manual distribution: installation, account access or sign-in may be required before invocation; verify availability in the target host.
