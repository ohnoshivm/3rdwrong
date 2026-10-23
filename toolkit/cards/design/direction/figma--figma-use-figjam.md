---
title: Figma Use FigJam
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: figma:figma-use-figjam
department: design
sub_department: direction
job: concept-direction
role: specialist
trigger: "A Figma file/workspace exists or is explicitly requested, and the task requires use figjam. Load this prerequisite only for its corresponding Figma operation."
kind: plugin-skill
availability: both
distribution: fetch
source: /Users/hustle/.claude/plugins/cache/claude-plugins-official/figma/2.2.120/skills-figquery/figma-use-figjam/SKILL.md
invoke: "`figma-use-figjam` in `skillNames` on the Figma `use_figma` operation"
pairs_with: [figma:figma-use, figma:figma-generate-diagram, skill:3w-creative-direction]
---

# Figma Use FigJam

A FigJam-specific companion skill for the Figma MCP workflow. For 3RDWRONG, use this specialist when the registry trigger applies: “A Figma file/workspace exists or is explicitly requested, and the task requires use figjam. Load this prerequisite only for its corresponding Figma operation.”

## What it does

- Adds FigJam-specific context for the `use_figma` tool; the foundational `figma-use` skill provides general plugin/API context.
- Requires `figma-use-figjam` in the comma-separated `skillNames` parameter for FigJam operations.
- Uses `get_figjam` to inspect a FigJam file; `get_metadata` is for Design files and does not work on FigJam.
- Covers board content, sections, stickies, connectors, text, shapes, tables, labels, images and batch modifications through linked references.

## When to use

- A Figma file/workspace exists or is explicitly requested, and the task requires use FigJam. Load this prerequisite only for its corresponding Figma operation.
- When generating or editing a FigJam board, before invoking the related Figma MCP operation.

## When not to use

- Figma Design-file work; use `figma:figma-use`.
- A board without a Figma file key or required MCP access.

## Inputs it needs

- A FigJam URL/file key and the intended board operation.
- Existing node IDs from `get_figjam` when modifying existing nodes.

## How to run it

1. Load the Figma MCP schemas needed for the operation.
2. For existing boards, inspect with `get_figjam` first.
3. Call `use_figma` and include `figma-use-figjam` in `skillNames`; use returned IDs for follow-up changes.

```text
Use `figma-use-figjam` in `skillNames` on the Figma `use_figma` operation. Task: {specific decision or output}. Context: {approved strategy, source links, version and constraints}. Return the documented format, label evidence and unknowns, and stop where required inputs or approval are missing.
```

## What good output looks like

- The correct FigJam-only API is selected and existing node IDs come from inspection.
- Text and image mutations follow the linked references’ recipes.

## Quality checks

- [ ] The output answers the registry job and, for a specialist, the exact trigger.
- [ ] Every factual claim comes from supplied evidence or the tool’s documented method.
- [ ] An independent reviewer checks the output; the maker does not approve their own work.
- [ ] Accessibility, reduced motion and responsive behaviour are checked where relevant.

## Pairs with

- `figma:figma-use` — upstream context or hand-off.
- `figma:figma-generate-diagram` — downstream review or delivery.
- `skill:3w-creative-direction` — downstream review or delivery.

## Limits and cautions

- Figma plugin and account access are prerequisites; availability does not prove authentication.
- Use `get_figjam`, not `get_metadata`, for FigJam inspection.
- Fetched plugin skill; install/sign-in may be required.
