---
title: Creative Technology selection policy
type: policy
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Creative Technology selection policy

**Documented** — Adopted by [D-0025](../../studio/decisions/0025-creative-technology-selection-policy.md),
2026-10-23. Adapted from sections 12–13 of the
[founder-supplied handbook](../../studio/archive/creative-technology-handbook-2026-10.md).
**Interpretation** — The selection rules are studio judgement, not claims that
one library is always faster or artistically better. Technical facts and
version-sensitive limits are separated in the [verification ledger](verification.md).

## Role and objective

Act as a senior creative technologist, interactive art director, graphics
engineer and frontend architect. Select the simplest technical approach that
can faithfully deliver an exceptional creative result. Design leads the intent;
Engineering owns implementation and maintenance. All agents and humans use the
same rules; tool availability does not decide the concept.

## Selection rules

1. Start with the visual concept, interaction model, real content, target
   devices and constraints. Prefer native HTML, CSS and SVG before JavaScript
   animation or GPU rendering. Use readable, accessible HTML for real content,
   navigation and forms; canvas must not be their only representation.
2. Use GSAP for directed timelines and scroll choreography. Use Motion for
   React state, layout and gestures. Give them separate ownership: never both
   animate the same property on the same element. Record the owner and cleanup
   of every shared timeline, frame loop and animated property.
3. Begin with native scrolling. Add Lenis only for a recorded creative or
   technical reason that the prototype demonstrates. Use one scroll engine;
   never stack Lenis, ScrollSmoother, ScrollControls or other competing scroll
   owners. ScrollTrigger works without a smoothing engine.
4. Use Rive for reusable interactive vector and identity assets when designed
   states and data contracts earn a runtime. Compare SVG/CSS/GSAP and
   Lottie/dotLottie against the actual interaction requirements; do not treat
   dotLottie as playback-only. Static identity is a valid outcome.
5. Consider OGL for focused custom shader effects; PixiJS for high-volume
   interactive 2D. First test whether CSS, SVG, Canvas 2D, a fixed image or
   video can deliver the same intended result.
6. Use Three.js for custom real-time 3D. Use R3F only inside a React architecture,
   with compatible React, Three.js, renderer and ecosystem versions recorded.
   Consider model-viewer or Spline before custom-building simple 3D. Evaluate
   exported behaviour, ownership, runtime weight and ongoing maintenance.
7. Consider Babylon.js or PlayCanvas for game-like 3D applications. Raw WebGL
   or WebGPU requires a specialised problem that a smaller abstraction cannot
   satisfy. Never select an engine simply because it is already installed.
8. Use WebGPU only when advanced rendering or compute justifies it. Prove
   renderer, materials, post-processing and device support together; a WebGL 2
   backend fallback does not make WebGL shader APIs compatible with a WebGPU
   renderer. Provide a useful no-GPU path independently.
9. Add no physics, post-processing, smooth scrolling, sequencing package or
   other specialist dependency without an explicit reason in the stack record.
   Required and optional dependencies must be separate; optional means omitted
   until the prototype proves the need. Ignore upstream full-stack presets
   where they conflict with this policy. Do not edit vendored skills to do so.
10. Preserve keyboard support, visible focus and useful touch input. Always
    implement and test `prefers-reduced-motion`, with the same information and
    tasks available. Avoid motion that obstructs reading or navigation.

## Seven-step selection process

1. **Understand the concept.** Define the visual and interaction outcome,
   audience tasks, content and constraints before choosing libraries.
2. **Research references.** Read the relevant sources in `taste/`; extract
   composition, pacing, depth and engineering principles. Never copy their
   layout, assets, code or identity. Apply the Taste Graph workflow before
   creative output, as [AGENTS.md](../../AGENTS.md) requires.
3. **Propose alternatives.** State a preferred approach and two viable
   alternatives with trade-offs. Include a native or pre-rendered option where
   feasible; explain when an alternative cannot meet a requirement.
4. **Prototype the riskiest interaction first.** Build the smallest slice with
   real content and production assets. Do not build a whole site around an
   unproven GPU effect. Define pass/fail thresholds before the prototype.
5. **Art-direct the prototype.** Critique typography, composition, timing,
   originality and interaction feel. A functioning effect is not a craft pass.
6. **Test on target devices.** Check performance, keyboard, touch, reduced
   motion, browser compatibility and content usability before scaling up.
7. **Record the decision.** Complete the stack record with rejected
   alternatives, versions, prototype results, device evidence, trade-offs,
   owners and final decision. Link it from the project's `decisions.md`.

## Before implementation

For every digital project, prepare the
[stack decision record](../../templates/bundles/project-digital/workspace/stack-decision.md.tmpl)
with:

- Desired visual and interaction outcome, content and success criteria.
- Preferred implementation and why it is sufficient.
- Two alternatives with trade-offs and reasons for rejection or further testing.
- Required and optional dependencies with versions, licences and ownership.
- Compatibility and maintenance risks, including framework/renderer boundaries.
- Mobile, performance and accessibility strategy, including keyboard,
  reduced-motion, asset failure and no-GPU fallbacks.
- A testable prototype plan, reference devices, measurements and pass/fail criteria.

The plan authorises a bounded prototype only within existing project approvals.
DX-04 requires the prototype result, device tests and final recorded decision
before the production build. A scope, architecture or dependency change that
invalidates the evidence reopens the decision and relevant gate.
Use codenames and roles; confidential URLs, captures, assets and client detail
stay in the vault under [D-0021](../../studio/decisions/0021-client-work-public-anonymised.md).

## Performance and accessibility contract

**Documented** — Google's public “good” Core Web Vitals floor is p75 LCP
≤ 2.5 s, INP ≤ 200 ms and CLS ≤ 0.1, segmented by mobile and desktop
([official Web Vitals](https://web.dev/articles/vitals), checked 2026-10-23).
[D-0023](../../studio/decisions/0023-commercial-and-delivery-defaults.md) is the
binding 3RDWRONG budget: mobile p75 LCP ≤ 2.0 s, INP ≤ 200 ms, CLS ≤ 0.1,
≤ 2 MB transferred before first interaction, a 60 fps target on a mid-range
phone, and a complete reduced-motion fallback. Projects can be stricter;
only a founder-approved, recorded exception can loosen the budget.

Measure the production slice with device, browser, network, date and run count.
Lab measurements guide the prototype; they do not establish field p75 INP or
Core Web Vitals compliance. Record absent field data as **Unknown** and name
its post-launch owner. Apply [web standards](../quality/web-standards.md) and
run `bin/3w qa run <url>` using the [Web QA harness guide](../../docs/web-qa-harness.md)
and [default budget](../digital-experience/qa-budget.yaml); retain raw reports
outside the public repository. Acceptance requires verdict PASS, or INCOMPLETE
only with the named founder sign-offs `FIELD-DATA-DEFERRED` and, where needed,
`REAL-PHONE-TEST-DEFERRED` under the
[conditional QA gate](../playbooks/digital-experience.md#mandatory-harness-report-and-conditional-gate).
The current harness never emits overall PASS: require `lab_status: PASS`, no
unresolved Blocker/Major defect, complete manual accessibility, functional and
equivalent reduced-motion/fallback checks, and account for every `NOT_MEASURED`
item. Only field data and the named real-phone checks may be deferred; missing
collection or required manual evidence holds the gate. Missing prerequisites
block collection; exit 2 alone is never success. Inspect three widths,
keyboard/focus, reduced motion and real mobile behaviour.

**Interpretation** — For GPU work, set draw-call, texture-memory, pixel-ratio
and frame-time budgets in the prototype. Compress assets, load progressively,
reuse resources, pause idle rendering and dispose resources on teardown.
Measure after adding an effect; reduce quality or choose a simpler medium when
it fails the budget. No library guarantees a frame rate.

## Quality gate

A separate checker reviews the actual artefact; the maker does not approve it.
Record defects, fixes, evidence and verdict for typography, composition, pacing,
interaction feel, mobile behaviour, runtime performance, accessibility and
originality. Honour the [critique protocol](../quality/critique-protocol.md).
A build pass or an award reference cannot replace rendered evidence and device
tests. Founder sign-off remains distinct from technical and craft review.

## Learning rule

Record successful techniques, failed experiments, reusable patterns and important
decisions with versions, evidence, limits and a re-test trigger. Route original
non-client studies through the [Labs repertoire](../../experiments/creative-technology-repertoire.md),
then validate a reusable kit before project use. Do not turn a single successful
demo into a universal rule. Use the [learning library](learning-library.md)
and [learning loop](../learning-loop.md); paid courses require founder approval.
