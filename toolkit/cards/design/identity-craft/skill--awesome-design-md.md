---
title: Awesome DESIGN.md
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-24
tool_id: skill:awesome-design-md
department: design
sub_department: identity-craft
job: design-system-guidelines
role: specialist
trigger: "Use when you need a DESIGN.md reference to study a brand or product visual system; it is inspiration only, never a source to copy into client work."
kind: repo-skill
availability: both
distribution: repo
source: skills/awesome-design-md/SKILL.md
invoke: "awesome-design-md skill; reads the fetched library at ~/.3rdwrong/fetch/pack-voltagent-awesome-design-md-mit/design-md"
pairs_with: [skill:3w-taste-graph, skill:3w-category-code-audit, skill:impeccable]
---
# Awesome DESIGN.md

A reference wrapper around a pinned library of 84 DESIGN.md analyses of brand and product websites. Use it to study how a visual system is organised: type scale, spacing, colour roles, radii and motion timing.

## What it does

- Points agents at one `<brand>/DESIGN.md` at a time, from the fetched library.
- Sets the rule that the library is for study: principles only, never layouts, assets, copy or brand identity.
- Requires evidence labels (Documented or Interpretation) for anything taken from a file.

## When to use

- Phase 04 Concept or Phase 05 Prototype, when a design-system pattern needs a concrete external reference.
- Studying how a category leader structures tokens before writing the studio's own DESIGN.md.
- Comparing token approaches across several reference systems.

## When not to use

- Copying a brand's system into client or studio work.
- Brand identity decisions: use the approved strategy and identity-craft specialists.
- When the library is not fetched: report it as unavailable; do not reconstruct a brand system from memory.

## Inputs it needs

- The brand or product name to study, and the question the study must answer.
- The fetched library at its pinned commit (installed by the toolkit fetch step).

## How to run it

1. Confirm the library is present; if not, say so and stop.
2. Open only the one brand folder that answers the question.
3. Write the findings as principles with Documented and Interpretation labels, and state what you did not take.

```text
Use the awesome-design-md skill. Question: {the token or system question}. Reference brand: {name}. Read only that brand's DESIGN.md. Return principles (not copied values or assets), each labelled Documented or Interpretation, and say how they would apply to the approved direction.
```

## What good output looks like

- Principles, not copied values, with the source file named.
- Clear separation between what the file says and what you infer.
- A statement of what is not transferable to the studio's work.

## Quality checks

- [ ] No layout, asset, copy or brand identity copied.
- [ ] Only the named brand file was read.
- [ ] The taste graph pack was loaded for any creative output.

## Pairs with

- `skill:3w-taste-graph`: references and anti-patterns before creative output.
- `skill:3w-category-code-audit`: category conventions before a direction.
- `skill:impeccable`: craft once a direction is chosen.

## Limits and cautions

- MIT licence on the upstream library; the library is fetched, not vendored, and keeps its own LICENSE file.
- The brand entries are third-party analyses. Treat them as references, not as the truth about those brands.
- Inspiration only (AGENTS.md; D-0006).
