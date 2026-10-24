---
title: Frontend Slides
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-24
tool_id: skill:frontend-slides
department: design
sub_department: identity-craft
job: presentation
role: specialist
trigger: "Use when the user wants to build a presentation, convert a PPT/PPTX to web, or create slides for a talk or pitch."
kind: skill
availability: both
distribution: fetch
source: ~/.3rdwrong/fetch/pack-zarazhangrui-frontend-slides-mit (pinned 9906a34d640d2111f724544cbc50f7f130569ae1)
invoke: "frontend-slides skill"
pairs_with: [superdesign:superdesign, skill:3w-creative-direction, skill:impeccable]
---
# Frontend Slides

A specialist for building a presentation as a single, zero-dependency HTML file that runs in the browser, with a fixed 16:9 stage and animation. It can also convert a PowerPoint file to web slides.

## What it does

- Produces single HTML decks with inline CSS and JS, and no build step.
- Helps a non-designer choose a style by showing visual previews rather than abstract options.
- Uses a fixed 1920×1080 stage scaled to the viewport, so slides stay 16:9 on every screen.
- Converts an existing PPT/PPTX into a web deck.

## When to use

- A pitch, talk or workshop deck where a web-native, animated deck adds value.
- Converting a legacy deck into an accessible, shareable web version.
- A short presentation that needs to run offline from one file.

## When not to use

- Board or client decks that must be edited in PowerPoint or Keynote by others.
- Print or PDF-only deliverables: use the document route.
- Identity or strategy content that has no approved direction yet.

## Inputs it needs

- Approved outline, message and audience.
- Brand direction and tokens, or an explicit decision to use a preset.
- The source PPTX if converting.

## How to run it

1. Confirm the outline is approved and the audience is stated.
2. Pick a style by previewing options, then build the single HTML file.
3. Check it at desktop, tablet and phone sizes, with keyboard navigation and reduced motion.

```text
Use the frontend-slides skill. Audience: {audience}. Approved outline: {link}. Direction: {approved tokens or preset}. Build one HTML file with a 16:9 stage, keyboard navigation and reduced-motion support. Report the widths checked and any slide that overflows.
```

## What good output looks like

- A single HTML deck that stays 16:9 on every screen and works offline.
- Visible slide hierarchy; motion used for emphasis only.
- A list of checked widths and any unverified slides.

## Quality checks

- [ ] Every slide checked at phone and desktop widths in a real browser.
- [ ] Keyboard navigation and reduced motion work.
- [ ] Fonts and images carry licences and are cleared for use.

## Pairs with

- `superdesign:superdesign`: composition exploration before the deck is built.
- `skill:3w-creative-direction`: the strategy route before any direction is chosen.
- `skill:impeccable`: craft pass on the finished slides.

## Limits and cautions

- MIT licence; the upstream checkout keeps its LICENSE file.
- The skill includes a style library with generic-AI warnings; do not let a preset replace the approved direction.
- Client material stays out of the public repository (D-0021).
