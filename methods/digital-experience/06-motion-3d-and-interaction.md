---
title: 06 Motion, 3D & interaction
type: method
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# 06 Motion, 3D & interaction

## Purpose

Implement the motion system, scenes and interactions so that each one carries
meaning, stays within budget and has a usable alternative.

## Roles and sign-off

- **Design** (experience-design: motion-principles; direction): choreography,
  timing, easing and the intent of each moment.
- **Engineering** (creative-engineering, platform-performance: animation
  runtime): implementation, GPU cost, fallbacks.
- **Media:** scoped 3D, film or sound assets under Design's direction.
- **Sign-off:** Design and Engineering leads jointly; founder logs gate DX-06.

## Inputs

- Motion language and tokens (DX-03); budgets and fallbacks (DX-04).
- Production assets in agreed formats with rights.

## Steps

1. For each motion or interaction, write one line: what it helps the user
   understand or do. Remove any that have no answer.
2. Follow the [selection policy](../creative-technology/selection-policy.md)
   and stack record: native scroll first, one scroll engine at most, separate
   GSAP/Motion property ownership. Use motion tokens; record the reason for
   Lenis, physics, post-processing, WebGPU or any other specialist addition.
3. Animate compositor-friendly properties (transform, opacity); avoid layout
   thrash and long tasks on input.
4. Build scenes within the draw-call, texture-memory and frame-time budgets;
   compress geometry and textures; load progressively.
5. Implement `prefers-reduced-motion`: replace movement with fades or static
   states that keep the same information and order.
6. Implement and test the no-WebGL and asset-failure fallbacks.
7. Check flashing content against the three-flashes rule and give users
   control over any movement longer than five seconds.
8. Review in the browser at three widths and on the reference mobile.

## Outputs

- Motion and scene implementation; motion specification (durations, easings,
  triggers); fallback notes; frame-time and memory measurements.

## Quality gate

- [ ] Every motion has a stated purpose.
- [ ] Reduced-motion mode keeps all content and tasks available.
- [ ] No essential task depends on animation, pointer effects, sound or WebGL.
- [ ] Frame time, draw calls and texture memory meet budget on the reference
      device, with graceful degradation below it.
- [ ] No content flashes more than three times per second.

## Evidence required

Recordings with and without reduced motion (vault), frame-time and memory
measurements with device and date, fallback test notes.

## Failure modes

- Motion for its own sake, or the same easing everywhere.
- Two scroll engines fighting each other.
- Scroll-jacking that breaks keyboard, screen-reader or browser find.
- Scenes that look right on a desktop GPU and stall on a mid-range phone.

## Related

[05 Production build](05-production-build.md) · [07 QA](07-qa.md) ·
[Web standards](../quality/web-standards.md#motion-standards) ·
[Living identities](../living-identities.md)

[Motion Teardown](../../motion-teardown/README.md) records an experimental eight-stage motion study, learning tracks and evidence tools for original rebuilds.
