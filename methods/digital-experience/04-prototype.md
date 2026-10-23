---
title: 04 Prototype
type: method
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# 04 Prototype

## Purpose

Build the critical slice in a real browser on target hardware before the full
build: the hardest interaction or scene, one key template, real content and
real tokens. The prototype sets the budgets the rest of the project is held to.

## Roles and sign-off

- **Engineering** (creative-engineering, platform-performance): builds and
  measures the slice.
- **Design** (experience-design, direction): judges craft, feel and motion in
  the browser, not in a mock-up.
- **Sign-off:** founder and `C1` accept the prototype; Design and Engineering
  leads jointly agree budgets and fallbacks (gate DX-04).

## Inputs

- DX-03 tokens, key templates and motion language.
- Signature-moment list with feasibility notes.
- Reference device and network profile agreed at kickoff
  ([web standards](../quality/web-standards.md#devices-and-browsers)).

## Steps

1. Choose the slice: the riskiest signature moment plus the template it lives
   in.
2. Set up the agreed stack with one smooth-scroll engine, tokens wired in and
   a production build from day one.
3. Build the slice with real content and assets at production formats.
4. Measure on the reference mid-range mobile and a desktop: LCP, CLS, input
   responsiveness, JavaScript and asset weight, draw calls, texture memory and
   frame time.
5. Implement and test the reduced-motion and no-WebGL fallbacks.
6. Inspect at desktop, tablet and mobile widths; screenshot and record.
7. Set explicit numerical budgets for the full build from these measurements,
   starting from the defaults in [web standards](../quality/web-standards.md),
   and record any approved exception.

## Outputs

- Running prototype on a private preview URL (URL recorded in the vault).
- Measurement record and agreed budgets in `qa/README.md`.
- Fallback behaviour notes; updated risks and estimate.

## Quality gate

- [ ] The slice runs in a production build on the reference devices.
- [ ] Measured values, device, network profile and date are recorded.
- [ ] Budgets are set as numbers; exceptions are approved in `decisions.md`.
- [ ] Reduced-motion and no-WebGL paths work and keep content usable.
- [ ] Design accepts the feel in the browser; Engineering accepts the cost.

## Evidence required

Screenshots and a short recording at three widths (vault), measurement output,
budget table, and the joint acceptance logged with version.

## Failure modes

- Prototyping the easy part and discovering the hard part in production.
- Measuring only on a fast laptop.
- Setting budgets after the build, to match what was built.
- Treating the prototype as throwaway when its architecture is kept, or keeping
  prototype shortcuts in production code.

## Related

[03 Art direction & design system](03-art-direction-and-design-system.md) ·
[05 Production build](05-production-build.md) ·
[Web standards](../quality/web-standards.md)
