---
title: Emil design engineering
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-24
tool_id: skill:emil-design-eng
department: design
sub_department: experience-design
job: ui-design
role: specialist
trigger: "Use when the user wants UI polish, component design, animation decisions or the invisible details that make software feel great."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-emilkowalski-skills-mit/skills/emil-design-eng
invoke: "emil-design-eng skill"
pairs_with: [skill:impeccable, frontend-design:frontend-design, skill:motion, skill:gsap-core]
---
# Emil design engineering

A specialist for interface polish, component detail and animation decisions, based on one designer's craft philosophy: unseen details compound, and beauty is leverage. Use it when UI works but does not yet feel right.

## What it does

- Applies a craft philosophy to component design: defaults, timing, and the small details users rarely notice.
- Reviews UI code and must answer in a Before/After markdown table (its own required format).
- Guides animation decisions, including reverse-engineering interactions it admires.

## When to use

- Phase 05 Prototype or Phase 06 Development, when a component works but feels generic or unfinished.
- Polish pass before a visual sign-off, on the studio's own digital touchpoints.
- Deciding whether an animation earns its place.

## When not to use

- Brand identity, mark or palette work: use the identity-craft specialists.
- Accessibility audit or certification: use `building-accessible-interfaces`.
- Backend or non-UI code.

## Inputs it needs

- The component or screen, its current state, and the interaction that is wrong.
- The approved motion language and duration/easing tokens, if they exist.

## How to run it

1. Start from the specific component or interaction, not the whole site.
2. Ask for a review in the required Before/After table, then decide each change against the approved brief.
3. Verify in a real browser; check reduced-motion behaviour.

```text
Use the emil-design-eng skill. Component: {name and file}. Current behaviour: {what feels wrong}. Approved motion tokens: {link or none}. Return a Before/After table of proposed polish changes, then list which you would not make and why. Do not change brand colour or type decisions.
```

## What good output looks like

- A Before/After table with a reason for each change, tied to a visible or felt effect.
- Changes limited to the named component; a short list of rejected ideas.
- Browser evidence that the change works, including reduced motion.

## Quality checks

- [ ] Each change is justified by the interaction, not by taste alone.
- [ ] Reduced motion is honoured; no animation runs without purpose.
- [ ] The independent reviewer confirms the result in a real browser.

## Pairs with

- `skill:impeccable`: the lead for overall UI design; use this for the detail pass.
- `frontend-design:frontend-design`: distinctive direction before polish.
- `skill:motion` and `skill:gsap-core`: implementation of motion once the decision is made.

## Limits and cautions

- MIT licence; the vendored copy keeps its upstream notice.
- The source is a philosophy and review format, not a measured standard. Treat its claims as Interpretation until checked on the studio's own work.
- Do not let polish override the approved art direction.
