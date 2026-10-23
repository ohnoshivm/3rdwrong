---
title: Creative Technology — official-source verification
type: guide
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Official-source verification

**Documented** — Checks below were made on 2026-10-23 against official
maintainer documentation or releases. They establish published capabilities
and cautions, not a measured studio implementation. Recheck the chosen versions
before installation; record the exact package versions in the project.

| Claim | Evidence and date checked | Consequence for selection |
| --- | --- | --- |
| R3F v9 is the stable line; v10 remains alpha. v9 pairs with React 19. | **Documented**, 2026-10-23: [current introduction](https://r3f.docs.pmnd.rs/getting-started/introduction) and [v9.8.2 release](https://github.com/pmndrs/react-three-fiber/releases/tag/v9.8.2). | Keep stable and alpha documentation separate; pin compatible versions. v9 is a checked baseline, not an eternal mandate. |
| R3F v10's default Canvas uses WebGPURenderer; GLSL-based materials and WebGL post-processing need the legacy renderer or a port. | **Documented**, 2026-10-23: [official v10 migration guide](https://r3f.docs.pmnd.rs/next/migration/v10), retrieved through official search text; direct reader exceeded its size limit. It also warns that a Drei peer range for v10 is pending. | Prototype the exact material/effect stack. Do not upgrade a GLSL scene on the assumption that backend fallback preserves API compatibility. |
| Three.js WebGPURenderer can use a WebGL 2 backend, but remains experimental in the manual. ShaderMaterial, RawShaderMaterial, onBeforeCompile customisations and EffectComposer passes are not supported there. | **Documented**, 2026-10-23: [renderer manual](https://threejs.org/manual/pages/webgpurenderer) and [API](https://threejs.org/docs/pages/WebGPURenderer.html). The manual recommends WebGLRenderer for pure WebGL 2 work; WebGPU uses node materials/TSL and its own effect stack. | Select the renderer before shader and post-processing APIs; test both backend and no-GPU paths. No universal speed advantage is established. |
| Rive documents an agent-compatible CLI workflow. | **Documented**, 2026-10-23: [maintainer CLI agent guide](https://github.com/rive-app/rive-docs/blob/main/cli/agents.mdx) and [CLI overview](https://github.com/rive-app/rive-docs/blob/main/cli/overview.mdx). The guide describes agent-written RML/scripts, live preview, verification and inspection. The public CLI page was inaccessible to the reader; the maintainer source was readable. | Evaluate authoring and handover in a bounded study; this is not evidence of a connected studio Rive tool. |
| Rive data binding links View Models to scene properties and supports updates from runtime code, editor, state machines or scripting. | **Documented**, 2026-10-23: [data binding overview](https://rive.app/docs/editor/data-binding/overview). | Define data contracts, invalid/missing values and accessible HTML equivalents. Binding data is not by itself generative design. |
| dotLottie supports interactive state machines. | **Documented**, 2026-10-23: [web-player state machines](https://docs.lottiefiles.com/en/runtimes/distributions/js/v0.x/state-machines). Machines are authored in the asset, loaded and driven through runtime inputs/events. | Compare required runtime/export features with Rive; do not call all Lottie playback-only or assume every player supports the same feature set. |
| Lenis does not support CSS scroll-snap directly; it provides lenis/snap. Nested scroll needs configuration. | **Documented**, 2026-10-23: [official README, considerations and limitations](https://github.com/darkroomengineering/lenis#limitations). `allowNestedScroll` can add DOM-check overhead; prevention attributes are another option. The README also lists iframe wheel-event and browser-specific limitations. | Begin with native scroll; test nested panels, anchors, touch, keyboard and chosen browser versions before recording a reason to retain Lenis. |
| Astro islands render most content as HTML and hydrate interactive client islands separately. | **Documented**, 2026-10-23: [islands architecture](https://docs.astro.build/en/concepts/islands/). | Consider Astro for content-led pages; an islands architecture is not proof that a particular site meets its budget. |
| PixiJS provides WebGL and WebGPU renderers. Its v8 guide labels WebGPU experimental and recommends WebGL for production. | **Documented**, 2026-10-23: [v8 renderer guide](https://pixijs.com/8.x/guides/components/renderers). | Evaluate WebGPU deliberately; the backend's existence does not make it a studio default. Recheck the installed release's guide. |
| Spline supports code export and runtime interaction; exports differ in retained behaviour. | **Documented**, 2026-10-23: [code export](https://docs.spline.design/exporting-your-scene/web/exporting-as-code) lists Vanilla JS, Three.js, React, Next.js and R3F; it says animations/events are enabled for Vanilla JS and React. [Web API](https://docs.spline.design/exporting-your-scene/web/code-api-for-web) is the runtime reference. | Prototype the selected export, events and host integration; check plan/licence, asset ownership, runtime delivery and maintenance before adoption. |
| Google's good Core Web Vitals thresholds are p75 LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1, assessed separately for mobile and desktop. | **Documented**, 2026-10-23: [Web Vitals](https://web.dev/articles/vitals). | These are the public floor. D-0023's stricter studio LCP and weight/motion budget still applies. |

## Unknowns and limits

- **Unknown** — Performance, browser coverage, maintenance cost and licence
  suitability of any future project's assets and selected versions. No runtime
  benchmark, authenticated service connection or production capability was
  verified by reading these sources.
- **Unknown** — Whether every Rive CLI output round-trips identically through
  every editor/runtime version. Do not turn the handbook's visual-refinement
  suggestion into a guaranteed compatibility rule; test the actual export.
- **Unknown** — Future stability of the alpha ecosystem and future browser
  support. This document makes no forward guarantee and no claim that WebGPU
  always outperforms WebGL.

The [policy](selection-policy.md) contains studio rules. Matrix recommendations
are **Interpretation**, to test against a brief; unknown technical claims do not
enter those rules. The archive intentionally retains unverified source wording.
