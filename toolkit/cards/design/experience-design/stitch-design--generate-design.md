---
title: Stitch generate design
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-24
tool_id: stitch-design:generate-design
department: design
sub_department: experience-design
job: ui-design
role: specialist
trigger: "Use when generating new screens from text prompts or images, editing existing screens, or generating design variants with Stitch MCP."
kind: plugin-skill
availability: both
distribution: vendor
source: toolkit/vendor/plugin-google-labs-code-stitch-skills-stitch-design-0337446dadde/skills/generate-design
invoke: "generate-design skill; requires the Stitch MCP server (mcp__stitch__*)"
pairs_with: [skill:impeccable, stitch-design:manage-design-system, stitch-design:code-to-design, stitch-design:extract-design-md]
---
# Stitch generate design

A specialist for generating and editing screens in Google Stitch from a text prompt or an image, and for producing design variants. It requires the Stitch MCP server and a Stitch account.

## What it does

- Enhances the prompt before any generation, using project context and the design system's tokens.
- Finds or creates the Stitch project and reads the design system before generating.
- Generates new screens from text or images, edits existing screens, and produces variants.
- Uses the design-system tokens (colour, font, roundness) so screens stay consistent.

## When to use

- Phase 05 Prototype, for quick screen exploration against an approved direction.
- Producing several screen variants for a comparison review.
- Editing an existing Stitch screen with a prompt rather than rebuilding it.

## When not to use

- Without the Stitch MCP server connected: the skill cannot run. Report it as unavailable.
- Client material that has not been cleared for upload to Stitch (D-0021).
- Final production build: use engineering and the implementation stack.

## Inputs it needs

- Approved direction, content and the screen's purpose.
- The Stitch project and design system to use, or permission to create one.
- Reference images only where the rights allow.

## How to run it

1. Confirm the Stitch MCP server is connected; if not, stop and say so.
2. List projects and design systems; reuse the existing ones.
3. Generate, review the screen against the brief, and iterate with prompts.

```text
Use the generate-design skill with the Stitch MCP. Project: {name or new}. Design system: {existing or none}. Screen purpose: {goal}. Approved direction: {link}. Generate two variants, label each claim Documented or Interpretation, and report which variant fits the brief and what was not checked.
```

## What good output looks like

- Screens in the chosen Stitch project that match the design system tokens.
- Variants with a stated reason for each difference.
- Open questions and unverified checks named.

## Quality checks

- [ ] Output checked against the approved direction by someone other than the maker.
- [ ] Screens rendered at the shipped widths before any sign-off.
- [ ] No client name, data or asset in a prompt without approval.

## Pairs with

- `skill:impeccable`: craft and critique of generated screens.
- `stitch-design:manage-design-system`: tokens before generation.
- `stitch-design:code-to-design` and `stitch-design:extract-design-md`: the reverse routes.

## Limits and cautions

- It depends on an external service and an account. Check data-handling terms before client use.
- Apache-2.0 licence; the vendored copy keeps its upstream notice.
- Generated screens are drafts. A generic result is a failure, not a starting point to ship.
