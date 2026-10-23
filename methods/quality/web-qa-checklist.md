---
title: Web QA checklist
type: checklist
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Web QA checklist

Run at [stage 07](../digital-experience/07-qa.md) on the production build, not
a development server. Thresholds live in [web standards](web-standards.md).
Record each result in the project's `qa/README.md` with the build, reviewer
role and evidence filename; screenshots stay in the vault. Mark an item **not
testable** with a reason rather than leaving it blank.

## Visual and responsive

- [ ] Every template inspected at 390, 834 and 1440 CSS px, plus 320 and 1920.
- [ ] No horizontal overflow, clipped text, overlapping elements or orphaned
      single words in headings.
- [ ] Headlines wrap to three lines or fewer at every width.
- [ ] Spacing, alignment and type follow the tokens; no one-off values.
- [ ] Images sharp at device pixel ratio 1, 2 and 3; correct crops per width.
- [ ] Art direction and identity rules hold on every template.
- [ ] Empty, loading and error states designed and implemented.

## Accessibility

- [ ] Automated scan run on every template; findings triaged.
- [ ] Full keyboard pass: every control reachable, logical order, no traps,
      skip link works.
- [ ] Focus always visible and never hidden under sticky elements.
- [ ] Contrast checked for text, components and focus indicators.
- [ ] Screen reader pass on one desktop and one mobile pairing: landmarks,
      headings, names, roles, states, live updates.
- [ ] 200 % zoom and 320 px reflow without loss of content or function.
- [ ] Targets at least 24 × 24 CSS px or adequately spaced.
- [ ] Images have appropriate alt text; decorative images are hidden.
- [ ] Video has captions; moving content can be paused.

## Motion and 3D

- [ ] `prefers-reduced-motion: reduce` gives equivalent static or cross-faded
      alternatives on every template.
- [ ] WebGL disabled: fallback content appears and tasks remain possible.
- [ ] Asset failure (blocked 3D model or video) degrades gracefully.
- [ ] Frame rate and memory within budget on the reference mid-range mobile.
- [ ] No flashing above three per second; no scroll trap.

## Cross-browser and device

- [ ] Every browser in the agreed matrix tested on the key journeys.
- [ ] Reference devices tested, including the mid-range Android phone.
- [ ] Touch, mouse, trackpad and keyboard input all work.
- [ ] Orientation changes and browser back/forward behave correctly.

## Functional

- [ ] Every link resolves; no unexpected 404s.
- [ ] Forms: validation, error messages, success state, spam protection,
      delivery to the right destination.
- [ ] CMS: create, edit, preview, publish and unpublish each content type.
- [ ] Integrations exercised, including failure paths.
- [ ] First-party browser console clean on every template.

## Content

- [ ] Final copy in place; no placeholder text, images or lorem ipsum.
- [ ] Proofread by someone other than the author; client content owner signed
      off.
- [ ] Legal pages, privacy notice and cookie information present and approved.
- [ ] Titles, meta descriptions and social cards set per page.

## Result

- [ ] Defects logged with severity, owner and state.
- [ ] No open critical or major defect; minor defects have an agreed
      disposition.
- [ ] Re-inspection done after the last fix.
