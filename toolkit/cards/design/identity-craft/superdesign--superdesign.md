---
title: Superdesign
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-24
tool_id: superdesign:superdesign
department: design
sub_department: identity-craft
job: composition-layout
role: specialist
trigger: "Use when the user wants to design or redesign a page, feature, flow, slide deck or brand-new product on the Superdesign canvas, or to compare and explore visual variants."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/plugin-account-synced-superdesign-marketplace/skills/superdesign
invoke: "superdesign skill; it drives the Superdesign CLI (npx @superdesign/cli)"
pairs_with: [skill:impeccable, frontend-design:frontend-design, skill:3w-creative-direction]
---
# Superdesign

A specialist for composition and layout exploration on the Superdesign canvas: it generates design drafts, compares directions across models and iterates on a chosen draft.

## What it does

- Designs or redesigns pages, features, flows, slide decks and graphics on an infinite canvas.
- Lists and compares leading design models, and explores independent directions side by side.
- Analyses a codebase for reusable UI context (`superdesign init`) and reproduces or extracts a reference URL's design language.
- Keeps version history when a draft is refined, and branches only for real alternatives.

## When to use

- Phase 04 Concept or Phase 05 Prototype, when several composition routes need to be compared quickly.
- Presentation or graphic layouts where an editable outline is needed before the visual pass.
- Continuing a saved Superdesign draft.

## When not to use

- Final brand identity, mark or colour decisions: use the identity-craft specialists and the approved strategy first.
- Client material that has not been cleared for upload to an external model.
- Production code: hand the approved draft to engineering.

## Inputs it needs

- Approved strategy and brief version, and the decision the layout must support.
- Content and real references; a live reference URL only when the rights allow it.
- A decision on which model(s) to use, and whether client data may leave the studio.

## How to run it

1. Run the environment preflight the skill requires before any CLI step. If shell execution is unavailable, report that and stop.
2. Choose the entry path (codebase or blank canvas) and state the brief.
3. Generate two or three directions, compare them against the brief, and pick one to iterate.

```text
Use the superdesign skill. Brief: {approved brief, version}. Deliverable: {page or deck}. Content: {links}. Generate three composition directions with different layout logic, label them Documented (from the brief) or Interpretation, and do not upload client material without approval. Return the chosen direction's canvas link and open questions.
```

## What good output looks like

- Three distinct compositions with stated rationale and a clear winner against the brief.
- Labelled claims; no invented metrics or client facts.
- An explicit list of what was not verified in a real browser.

## Quality checks

- [ ] The directions differ in layout logic, not only in colour or type.
- [ ] Nothing client-owned left the studio without approval (D-0021).
- [ ] An independent reviewer checks the chosen direction against the brief.

## Pairs with

- `skill:impeccable` or `frontend-design:frontend-design`: detail and craft once a composition is chosen.
- `skill:3w-creative-direction`: the strategy route before any direction is chosen.

## Limits and cautions

- It runs through an external CLI and cloud models. Account, data-handling and cost terms are set by Superdesign; check them before use on client work.
- MIT licence; the vendored copy keeps its upstream notice.
- Generated output is a draft, not evidence of quality. Inspect renders at the shipped sizes.
