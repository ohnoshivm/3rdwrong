---
title: 05 Production build
type: method
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# 05 Production build

## Purpose

Build every page, template, content flow and integration in the signed scope
on the architecture proven at the prototype, within budget.

## Roles and sign-off

- **Engineering** (product-frontend, platform-performance,
  engineering-qa-security): architecture, implementation, CMS, integrations,
  tests, code review.
- **Design** (experience-design, design-qa): specifications, responsive
  behaviour, design review in the browser.
- **Production:** content intake, schedule, change control.
- **Sign-off:** Engineering and Design leads confirm feature completeness;
  founder logs gate DX-05.

## Inputs

- DX-04 accepted prototype, budgets and fallbacks.
- Templates, tokens, component states and content per the delivery plan.

## Steps

1. Record the architecture decision (framework, rendering mode, CMS, hosting)
   in `decisions.md`; prefer the smallest stack that meets the brief.
2. Implement tokens, then components with all states, then templates, then
   pages.
3. Integrate the CMS with structured content models and editor previews.
4. Build integrations named in scope only; review inputs, secrets and
   dependencies as you go.
5. Write tests for logic and critical flows; keep the production build green.
6. Review code for every change; no self-merging of consequential changes.
7. Run a design review in the browser on each completed template at three
   widths; log defects.
8. Check budgets on every significant merge; stop and escalate when a budget
   is exceeded.

## Outputs

- Feature-complete build on staging; CMS with content models; tests; design
  review log; budget checks.

## Quality gate

- [ ] Every scoped page and integration exists; nothing out of scope was added
      without a change request.
- [ ] Production build and tests pass; first-party console is clean.
- [ ] Budgets hold on the reference devices, or exceptions are approved.
- [ ] No secrets in code; dependencies reviewed.
- [ ] Design review defects are fixed or logged with severity.

## Evidence required

Build and test output, budget measurements per milestone, code-review record,
design-review screenshots (vault).

## Failure modes

- Adding dependencies speculatively.
- Hard-coding content that the client must edit later.
- Discovering budget overruns only at stage 08.
- Accepting "works on my machine" as a design review.

## Related

[04 Prototype](04-prototype.md) ·
[06 Motion, 3D & interaction](06-motion-3d-and-interaction.md) ·
[Web standards](../quality/web-standards.md#cms-and-content-handover)
