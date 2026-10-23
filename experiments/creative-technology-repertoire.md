---
title: Labs — Creative Technology starter repertoire
type: guide
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Labs — Creative Technology starter repertoire

**Interpretation** — Proposed non-client practice backlog before the first client,
adapted from handbook section 14. No study has been built, benchmarked or
validated. Labs owns the backlog under [its charter](../studio/departments/labs.md);
Engineering's creative-engineering sub-department owns the
[selection policy](../methods/creative-technology/selection-policy.md).
These exercises establish inspectable practice, not client results.

## Study workflow and owners

Each study gets `experiments/<study>/README.md` only when work begins, following
the [experiment template](../templates/learning/experiment.md) and
[experiments guide](README.md). Study a reference, recreate the technique
internally, critique it, improve it through an original application and document
what changed. Pick the smallest stack through the policy and record a preferred
approach plus two alternatives before coding. Prototype the riskiest interaction
first. A valid result may be iterate or drop.

**Documented** — Four experimental Labs lead skills are integrated and registered.
Read each source method and its linked card before the matching study step:

- [`skills/3w-effect-study/SKILL.md`](../skills/3w-effect-study/SKILL.md): study and isolate a technique with provenance.
- [`skills/3w-labs-benchmark/SKILL.md`](../skills/3w-labs-benchmark/SKILL.md): compare two options on a fixed fixture,
  at least five alternating runs per environment; report median and spread.
- [`skills/3w-engine-validation/SKILL.md`](../skills/3w-engine-validation/SKILL.md): a different engineer validates an
  original reusable kit, its API, licences, clean install and degradation.
- [`skills/3w-demo-publishing/SKILL.md`](../skills/3w-demo-publishing/SKILL.md): check rights, data, disclosure, evidence
  and founder approval before publication.

A named human Labs owner checks prerequisites before applying the methods;
registration does not establish execution or a completed handoff.
Maker and checker are separate. Founder review decides house-engine adoption
and publication. Do not run the publishing step as part of studying a reference.

## Common acceptance contract

Every study below must supply all of this evidence before it can pass:

- Run `bin/3w qa run <url>` against its production build; record tool/version,
  device, browser, network profile, date, raw output and what the command could
  not test. If unavailable, mark **Unknown**, never pass it silently.
- Meet [D-0023](../studio/decisions/0023-commercial-and-delivery-defaults.md):
  mobile p75 LCP ≤ 2.0 s, INP ≤ 200 ms, CLS ≤ 0.1, ≤ 2 MB before first
  interaction, 60 fps target on a mid-range phone and a complete reduced-motion
  path. Lab runs guide budget assessment; they do not prove field p75 data.
  Record field p75 as **Unknown** until sufficient field data exists. A looser
  budget needs a founder-approved exception, not a changed threshold.
- Record desktop, tablet and mobile screenshots; real mid-range-phone frame
  times; the browser matrix in [web standards](../methods/quality/web-standards.md).
  For comparative claims, use at least five runs and report median and spread.
- Exercise keyboard, visible focus, touch, zoom/reflow, contrast and screen-reader
  access to meaningful content; no task may require a mouse, sound or GPU.
- Test reduced motion, no-WebGL/WebGPU, missing assets and route teardown.
  Preserve the same content and tasks; record memory/resource cleanup for GPU work.
- Obtain an independent art-direction critique of typography, composition,
  pacing, interaction feel, mobile behaviour and originality, with defects,
  improvements and a verdict. The maker cannot approve their own work.
- Record provenance, licences, source URLs and never-copy rules. Studying or
  recreating a reference stays internal and rights-compliant. Anything published
  must be original, never a copy of a reference's layout, assets or code;
  licensed library dependencies retain attribution and notices. D-0006's rejected
  visual vocabulary is not a default study style. No client data belongs here.

Client URLs, captures and identifying data never enter this public backlog.
Use original, non-client fixtures and open-licence assets, with recorded rights.

## CT-01 — Typography interaction

**Goal / Hypothesis** — Express an original typographic idea through one legible
interaction without sacrificing reading order or selection.

**Chosen candidate stack / Interpretation** — HTML/CSS/SVG first; GSAP only for
choreography CSS cannot express clearly. Compare CSS-only and WAAPI against the
GSAP slice. Native scroll; no GPU renderer or smooth-scroll dependency.

**Acceptance** — Common contract plus readable DOM text at all three widths,
no six-line headline wraps, selectable/copyable text, focus equivalent to hover,
and final meaningful text immediately available with reduced motion. Critique
letter spacing, line breaks, hierarchy and whether timing supports reading.

## CT-02 — Shader transition

**Goal / Hypothesis** — Make an original image-to-image transition whose
material behaviour communicates a stated idea.

**Chosen candidate stack / Interpretation** — OGL + GLSL for a focused plane,
with HTML content and a static image fallback. Compare CSS/SVG masking and a
pre-rendered transition; keep OGL only if the effect needs dynamic distortion.
The CEOS shader and realtime-3D routes cover OGL; no OGL-only skill is assumed.

**Acceptance** — Common contract plus progress 0/1, resize, extreme aspect ratio,
precision and asset-failure tests; measured frame times at the selected DPR;
no black frame, stranded canvas or inaccessible slide control. Reduced motion
shows the selected image directly. Critique transition pacing, image integrity
and concept-specific material choices, not resemblance to a reference.

## CT-03 — Scroll narrative

**Goal / Hypothesis** — Explain one idea through three short narrative beats
whose order and content remain useful without animation.

**Chosen candidate stack / Interpretation** — HTML/CSS + GSAP ScrollTrigger
with native scrolling. Compare CSS sticky/scroll-driven animation and a static
editorial sequence. Add Lenis only if the recorded prototype proves a necessary
scroll-feel/synchronisation requirement; use one scroll engine.

**Acceptance** — Common contract plus anchor links, browser find, keyboard
scroll, nested panel, touch and resize tests. Reduced motion preserves story
order without scrubbing or pin traps. Critique pacing, reading time, transitions
and the relationship between text and movement. Record scroll ownership.

## CT-04 — Interactive 3D scene

**Goal / Hypothesis** — Let a user inspect one original object and change one
meaningful property, keeping its explanation and controls in HTML.

**Chosen candidate stack / Interpretation** — Three.js + a small optimised glTF
asset, with a designed poster. Compare model-viewer and Spline first; retain
custom Three.js only for the required interaction/material control. R3F is an
alternative only if the surrounding fixture justifies React. No default physics
or post-processing; use Blender only where asset authoring requires it.

**Acceptance** — Common contract plus keyboard/touch controls, object-load
failure, GPU-context failure, bounded DPR, draw calls/texture memory and resource
return after teardown. Reduced motion is an inspectable still with equivalent
controls/content. Critique composition, lighting, materials and useful depth.
Test renderer/material versions as a unit before proposing any WebGPU path.

## CT-05 — Generative identity

**Goal / Hypothesis** — Generate recognisable variations from a documented
invariant and bounded synthetic inputs, rather than switching authored states.

**Chosen candidate stack / Interpretation** — Canvas 2D or SVG with seeded
rules and HTML controls. Compare SVG/GSAP authored states and a Rive state/data
system to prove whether generation is needed. PixiJS, OGL or Three.js earns
selection only when measured scale or geometry exceeds the simpler approach.

**Acceptance** — Common contract plus deterministic replay from seed,
missing/invalid/extreme input tests, bounded variation, export and maintenance
notes, and a useful static identity when motion is reduced. Critique recognition,
invariants, meaningful variation and coherent composition across samples.
Do not claim audience recognition without a separate audience study.

## Promotion and learning

Record technique, failures, improvements, measurements, art-direction verdict,
limits and next owner. Useful outcomes link back to the
[learning library](../methods/creative-technology/learning-library.md).
House-engine validation and public release are separate later gates; no backlog
entry is evidence of a validated kit or a published original demo.
