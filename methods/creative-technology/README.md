---
title: Creative Technology system
type: method
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Creative Technology system

Choose the simplest technology that faithfully delivers an exceptional creative
result. Engineering's creative-engineering sub-department owns this system;
Design owns creative intent and critique; Labs owns the non-client repertoire.

**Documented** — [D-0025](../../studio/decisions/0025-creative-technology-selection-policy.md)
adopts the selection policy, access levels and stack decision record. Supporting
method documents retain proposed metadata for review; this does not make the
adopted rules optional. The [founder-supplied handbook](../../studio/archive/creative-technology-handbook-2026-10.md)
is the source, not proof of performance or production readiness.

## Six capabilities

**Interpretation** — Organise the handbook's capabilities as questions, not a
shopping list. A project need not use all six.

| Capability | Outcome to define | Candidate medium |
| --- | --- | --- |
| Layout and visual identity | Legible hierarchy, composition, responsive brand expression | HTML, CSS, SVG; design tools for authoring |
| Motion and choreography | Pacing, kinetic type, meaningful feedback and scroll narratives | CSS, WAAPI, GSAP, Motion |
| Creative rendering and shaders | Interactive image treatment, distortion, procedural surfaces | OGL, PixiJS, GLSL; WebGPU only with justification |
| 3D and immersive environments | Spatial interaction, materials, lighting and camera direction | Three.js, R3F, Blender; an engine when needed |
| Living brand identities | Recognisable states, responsive assets or generated variations | SVG, Rive, GSAP, Canvas |
| Data, physics and simulation | Information or physical rules that explain a real idea | D3, Rapier, Matter.js, custom rendering |

## Rendering hierarchy

**Interpretation** — Start at the concept, then choose the medium: DOM/SVG for
text, UI and vector content; Canvas 2D for pixel drawing; WebGL/WebGPU for
justified GPU rendering. Select an abstraction only after that choice: OGL for
a focused effect, PixiJS for rich 2D, Three.js or a scene engine for 3D.
GSAP animates properties; it does not replace a renderer. R3F supplies the React
component model for Three.js; it is not an upgrade in rendering power.
See the [matrix](selection-matrix.md#rendering-and-webgpu) and
[dated official-source checks](verification.md).

## Three access levels

**Interpretation** — Access levels describe when to consider a technology, not
installation, competence, approval or registry activation.

| Level | Repertoire | Access rule |
| --- | --- | --- |
| Core | HTML, CSS, SVG, TypeScript, Astro/React, GSAP | Begin here; use only what the brief needs. GSAP and a framework are not mandatory dependencies. |
| Creative specialists | Three.js, R3F, OGL, Rive, PixiJS, GLSL, Blender | Activate for a named creative requirement after comparing a simpler approach. |
| Advanced specialists | WebGPU, Rapier, Theatre.js, PlayCanvas, Babylon.js, D3, Scroll Rig | Load for the corresponding technical problem with a recorded reason and compatibility proof. |

[D-0019](../../studio/decisions/0019-organisation-and-loading-policy.md) and the
[registry](../../toolkit/sources/registry.json) still own role, load and trigger.
A technology in Core may have no dedicated studio tool. Bench and parked tools
remain library entries requiring explicit request; this method cannot activate them.

## Delivery integration

| Stage | Required use |
| --- | --- |
| [02 Experience strategy](../digital-experience/02-experience-strategy-and-concept.md) | Define the concept and signature moments; open the stack record with preferred approach, two alternatives and risks. |
| [04 Prototype](../digital-experience/04-prototype.md) | Own architecture proof: prototype the riskiest interaction first, compare craft and cost, test target devices, record the final stack before production build. |
| [05 Production build](../digital-experience/05-production-build.md) | Implement the recorded stack, versions and boundaries; revisit the record when assumptions change. |
| [06 Motion, 3D and interaction](../digital-experience/06-motion-3d-and-interaction.md) | Apply motion/property ownership, one scroll engine and measured optional effects. |
| [08 Launch readiness](../digital-experience/08-performance-and-launch-readiness.md) | Check D-0023 budgets, accessibility, fallbacks and compatibility against the actual build. |
| [Living identities](../living-identities.md) | Apply the decision test and distinguish authored states from generative rules before choosing a runtime. |

Run `bin/3w qa run <url>` against the production build using the
[Web QA harness guide](../../docs/web-qa-harness.md), [implementation](../../scripts/web_qa.py),
[browser probe](../../scripts/web_qa_browser.js) and [default budget](../digital-experience/qa-budget.yaml).
Acceptance requires PASS, or INCOMPLETE only with the named founder sign-offs
under the [conditional QA gate](../playbooks/digital-experience.md#mandatory-harness-report-and-conditional-gate).
The current harness never emits overall PASS; `lab_status: PASS` alone is not
acceptance. Keep raw evidence outside the public repository.

## Working documents

- [Selection policy](selection-policy.md): the rules and seven-step process.
- [Selection matrix](selection-matrix.md): tasks, techniques, tool routes and gaps.
- [Verification ledger](verification.md): dated official claims and limits.
- [Stack decision template](../../templates/bundles/project-digital/workspace/stack-decision.md.tmpl): created by `bin/3w new project-digital` for every digital project.
- [Learning library](learning-library.md) and [Labs starter repertoire](../../experiments/creative-technology-repertoire.md).

Keep real content readable in HTML, preserve keyboard access and always supply
a reduced-motion path. Follow [creative guardrails](../creative-guardrails.md),
[taste references](../../taste/studio-websites.md) and
[publication rules](../../docs/public-private-boundary.md). No studio aesthetic
is implied; [D-0006](../../studio/decisions/0006-rejected-own-identity-direction.md)
remains rejected.
