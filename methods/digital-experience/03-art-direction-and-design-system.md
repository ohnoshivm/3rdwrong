---
title: 03 Art direction & design system
type: method
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# 03 Art direction & design system

## Purpose

Turn the approved concept into a visual and motion language with tokens first,
then the smallest component inventory the templates need.

## Roles and sign-off

- **Design** (direction, identity-craft, experience-design): art direction,
  typography, colour, layout rules, motion language, components and states.
- **Engineering** (product-frontend): token format and naming that maps to
  code; component feasibility.
- **Sign-off:** founder; `C1` approves art direction on two or three key
  templates (gate DX-03). Tokens are then frozen for the prototype; later
  changes go through change control.

## Inputs

- DX-02 concept, sitemap and signature moments.
- Identity system specification and assets with rights.

## Steps

1. Write the art direction: concept sentence, typographic hierarchy, colour
   roles, layout rules, imagery and material direction, motion language,
   interaction behaviours and responsive principles.
2. Define tokens before components: spacing scale, type scale, colour roles
   with contrast pairs, radii, shadows or materials, motion durations and
   easings, breakpoints.
3. Design two or three key templates at desktop, tablet and mobile widths
   with real content, not filler.
4. List components and their states (default, hover, focus, active, disabled,
   loading, error, empty) only as far as the templates need.
5. Check contrast for every text and interface colour pair against
   [web standards](../quality/web-standards.md#accessibility).
6. Critique against the concept and identity; record defects and fixes.

## Outputs

- Art direction document; design tokens (as data, e.g. JSON); key template
  designs; component inventory with states; motion language with durations and
  easings.

## Quality gate

- [ ] Tokens exist and are named before components are built.
- [ ] Real content is used; no headline wraps beyond three lines at any width.
- [ ] Every text pair meets WCAG 2.2 AA contrast; focus states are designed.
- [ ] Motion language has named durations and easings and a reduced-motion
      rule.
- [ ] Original composition; no layout, asset or copy is copied from a
      reference.

## Evidence required

Token file version, key templates at three widths, contrast results, critique
record and `C1`'s approval logged with version.

## Failure modes

- Designing desktop only and discovering mobile at build time.
- Components before tokens, so values drift.
- Decorative gradients, nested cards and default typography standing in for
  decisions.
- Approving art direction from mood boards instead of real templates.

## Related

[02 Experience strategy & concept](02-experience-strategy-and-concept.md) ·
[04 Prototype](04-prototype.md) ·
[Identity system testing](../quality/identity-system-testing.md)
