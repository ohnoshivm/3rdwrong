---
title: Creative Technology selection matrix
type: method
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Creative Technology selection matrix

**Interpretation** — Working recommendations adapted from handbook sections
1–9; “preferred”, “excellent”, “strongest” and complexity labels in the source
tables are editorial judgements, not measured rankings. Test the smallest
approach against the brief using the [policy](selection-policy.md). No table
installs a package, activates a library tool or approves a visual direction.
[D-0023](../../studio/decisions/0023-commercial-and-delivery-defaults.md) governs
performance. [Official-source checks](verification.md) govern dated facts.

## Studio tool routes

**Documented** — IDs, roles, loads and card paths below were checked against
[registry.json](../../toolkit/sources/registry.json) and source cards on
2026-10-23. Route codes in every following table refer here. Read the job lead
first; a specialist needs its registry trigger. Bench/parked requires explicit
request and source review. No dedicated tool is invented for a gap; general
coverage is distinguished from a dedicated implementation method.

| Route | Registry ID and card | Role / load | Selection boundary |
| --- | --- | --- | --- |
| N | [`agent:frontend-architect`](../../toolkit/cards/engineering/product-frontend/agent--frontend-architect.md) | lead / active | HTML/CSS/SVG, TypeScript and application architecture; no dedicated Astro method. |
| N | [`skill:ceos-frontend-architecture`](../../toolkit/cards/engineering/product-frontend/skill--ceos-frontend-architecture.md) | specialist / active | HTML/CSS/SVG, TypeScript and application architecture; no dedicated Astro method. |
| N | [`skill:building-accessible-interfaces`](../../toolkit/cards/engineering/product-frontend/skill--building-accessible-interfaces.md) | lead / active | HTML/CSS/SVG, TypeScript and application architecture; no dedicated Astro method. |
| G | [`skill:gsap-core`](../../toolkit/cards/engineering/creative-engineering/skill--gsap-core.md) | lead / active | Directed choreography; choose only the needed GSAP specialist. |
| G | [`skill:gsap-timeline`](../../toolkit/cards/engineering/creative-engineering/skill--gsap-timeline.md) | specialist / active | Directed choreography; choose only the needed GSAP specialist. |
| G | [`skill:gsap-scrolltrigger`](../../toolkit/cards/engineering/creative-engineering/skill--gsap-scrolltrigger.md) | specialist / active | Directed choreography; choose only the needed GSAP specialist. |
| G | [`skill:gsap-react`](../../toolkit/cards/engineering/creative-engineering/skill--gsap-react.md) | specialist / active | Directed choreography; choose only the needed GSAP specialist. |
| G | [`skill:gsap-frameworks`](../../toolkit/cards/engineering/creative-engineering/skill--gsap-frameworks.md) | specialist / active | Directed choreography; choose only the needed GSAP specialist. |
| G | [`skill:gsap-plugins`](../../toolkit/cards/engineering/creative-engineering/skill--gsap-plugins.md) | specialist / active | Directed choreography; choose only the needed GSAP specialist. |
| G | [`skill:gsap-utils`](../../toolkit/cards/engineering/creative-engineering/skill--gsap-utils.md) | specialist / active | Directed choreography; choose only the needed GSAP specialist. |
| G | [`skill:gsap-performance`](../../toolkit/cards/engineering/platform-performance/skill--gsap-performance.md) | specialist / active | Directed choreography; choose only the needed GSAP specialist. |
| G | [`agent:motion-director`](../../toolkit/cards/engineering/creative-engineering/agent--motion-director.md) | specialist / active | Directed choreography; choose only the needed GSAP specialist. |
| M | [`skill:motion`](../../toolkit/cards/engineering/creative-engineering/skill--motion.md) | specialist / active | React state/layout/gestures; separate property ownership from GSAP. |
| L | [`skill:cinematic-gsap-lenis-motion-system`](../../toolkit/cards/engineering/creative-engineering/skill--cinematic-gsap-lenis-motion-system.md) | specialist / active | Lenis coverage; native first and a recorded reason. |
| L | [`skill:cinematic-scroll-storytelling`](../../toolkit/cards/engineering/creative-engineering/skill--cinematic-scroll-storytelling.md) | specialist / active | Lenis coverage; native first and a recorded reason. |
| S | [`skill:ceos-shader-engineering`](../../toolkit/cards/engineering/creative-engineering/skill--ceos-shader-engineering.md) | lead / active | GLSL, WGSL/TSL and GPU effects; renderer-specific APIs. |
| T | [`skill:ceos-realtime-3d`](../../toolkit/cards/engineering/creative-engineering/skill--ceos-realtime-3d.md) | lead / active | Three.js/R3F and OGL architecture; React only when justified. |
| T | [`skill:threejs`](../../toolkit/cards/engineering/creative-engineering/skill--threejs.md) | specialist / active | Three.js/R3F and OGL architecture; React only when justified. |
| T | [`agent:3d-webgl-engineer`](../../toolkit/cards/engineering/creative-engineering/agent--3d-webgl-engineer.md) | specialist / active | Three.js/R3F and OGL architecture; React only when justified. |
| T | [`skill:scaffold-3d-site`](../../toolkit/cards/engineering/creative-engineering/skill--scaffold-3d-site.md) | specialist / active | Three.js/R3F and OGL architecture; React only when justified. |
| T | [`skill:scroll-3d-scene`](../../toolkit/cards/engineering/creative-engineering/skill--scroll-3d-scene.md) | specialist / active | Three.js/R3F and OGL architecture; React only when justified. |
| A | [`skill:ceos-3d-asset-pipeline`](../../toolkit/cards/engineering/creative-engineering/skill--ceos-3d-asset-pipeline.md) | specialist / active | Blender/glTF delivery and optimisation; authoring competence is not established by a card. |
| A | [`skill:optimize-3d-assets`](../../toolkit/cards/engineering/creative-engineering/skill--optimize-3d-assets.md) | specialist / active | Blender/glTF delivery and optimisation; authoring competence is not established by a card. |
| P | [`skill:add-postprocessing`](../../toolkit/cards/engineering/creative-engineering/skill--add-postprocessing.md) | specialist / active | Optional post-processing only; prove renderer compatibility and cost. |
| C | [`skill:ceos-creative-coding`](../../toolkit/cards/engineering/creative-engineering/skill--ceos-creative-coding.md) | lead / active | Canvas/SVG/WebGL generative methods; algorithmic-art also covers p5.js. |
| C | [`skill:creating-algorithmic-art`](../../toolkit/cards/engineering/creative-engineering/skill--creating-algorithmic-art.md) | specialist / active | Canvas/SVG/WebGL generative methods; algorithmic-art also covers p5.js. |
| Q | [`skill:ceos-performance-engineering`](../../toolkit/cards/engineering/platform-performance/skill--ceos-performance-engineering.md) | lead / active | Performance and release evidence; a checker must be independent. |
| Q | [`skill:ceos-production-quality`](../../toolkit/cards/engineering/engineering-qa-security/skill--ceos-production-quality.md) | lead / active | Performance and release evidence; a checker must be independent. |
| V | [`remotion:remotion-best-practices`](../../toolkit/cards/media/film-motion-graphics/remotion--remotion-best-practices.md) | lead / active | Programmatic video, under Media; not a website animation runtime. |
| D | [`figma:figma-use`](../../toolkit/cards/design/identity-craft/figma--figma-use.md) | specialist / active | Design authoring prerequisite for the corresponding Figma operation; no runtime renderer. |
| F | `skill:matterjs` (no active card) | parked / library | Matter.js study only; parked/library, explicit request required. |

### Coverage and gaps by technology

Each technology mentioned below resolves to one or more route codes or an
explicit gap. A covered option still requires version-specific official docs.

| Technology | Studio route or gap | Coverage limit |
| --- | --- | --- |
| HTML, CSS, SVG, TypeScript, native scroll, WAAPI | N; G when directed animation is needed | General frontend coverage; begin with native features. |
| React / Next.js | N | Architecture support; no framework is automatically required. |
| Astro | **Gap: no dedicated tool**; N supplies architecture judgement | Verify islands/framework integration from official docs. |
| GSAP / ScrollTrigger / SVG animation / frame sequencing | G | ScrollTrigger does not require Lenis. |
| Motion | M | React interaction specialist. |
| Anime.js | **Gap: no dedicated tool** | Do not substitute a similarly named animation tool. |
| Lenis | L; T for the scroll-3d recipe | Gated coverage; legacy source recipes require current-version checks. |
| Theatre.js | **Gap: no dedicated tool** | Optional visual sequencing only. |
| OGL | T + S | Explicitly covered by CEOS realtime-3d; no dedicated OGL-only skill. |
| GLSL, WGSL, TSL, raw WebGL/WebGPU | S + T | Advanced rendering/compute requires a reason; no automatic WebGPU migration. |
| PixiJS | **Gap: no dedicated tool** | General C/S advice is not a PixiJS implementation method. |
| Three.js / R3F / Drei | T | Record React/renderer/ecosystem compatibility. |
| Spline | **Gap: no dedicated tool** | Evaluate export/runtime from official docs. |
| Babylon.js / PlayCanvas / A-Frame / WebXR | **Gap: no dedicated engine method** | An immersive specialist is not proof of coverage for these engines. |
| model-viewer | **Gap: no dedicated tool** | Still compare before building a simple custom viewer. |
| Rive | **Gap: no dedicated tool** | CLI availability is not studio installation or a tested workflow. |
| Lottie / dotLottie | **Gap: no dedicated tool** | Compare exact player/state-machine support. |
| Canvas 2D / p5.js | C | Generative study support; preserve semantic HTML. |
| Matter.js | F | Parked; not an active delivery default. |
| Rapier / React Three Rapier | **Gap: no dedicated tool**; T scaffold mentions it | Explicit physics reason; a preset installation recipe is not lead coverage. |
| D3 / Observable Plot | **Gap: no dedicated tool** | General data-visualisation expertise is not a library method. |
| MapLibre | **Gap: no dedicated tool** | Use only when geographic data is a requirement. |
| Blender / glTF Transform / GLTFJSX | A + T | Asset pipeline support; GLTFJSX belongs in a justified React stack. |
| Houdini / Cinema 4D | **Gap: no dedicated tool** | External authoring and export/rights workflow needs a human owner. |
| React Postprocessing / postprocessing | P | Optional; WebGL EffectComposer is not WebGPURenderer-compatible. |
| 14islands r3f-scroll-rig | **Gap: no dedicated tool** | T covers DOM/canvas principles, not this integration package. |
| Remotion | V | Media asset production; not a page rendering foundation. |
| Figma | D | Read the prerequisite and select the corresponding authoring operation; it is not a renderer. |
| Zustand / equivalent state store | N + T | Add a store only for state that requires it; no automatic dependency. |

## 1. Task to tool

**Interpretation** — Start here, then read the relevant technology table and
route. These are candidates, never universal “best” choices.

| What you want to create | Starting candidate | Use something else when… | Studio route / gap |
| ------------------------------ | ------------------------------------ | -------------------------------------------------------- | --- |
| Content-led, minimal website | HTML/CSS + Astro | Complex application state requires React | N; Astro gap |
| Kinetic typography | GSAP + DOM text | Simple movement only needs CSS | G / N |
| Intricate animation timelines | GSAP | React layout interactions favour Motion | G / M |
| Scroll-triggered reveals | CSS or GSAP ScrollTrigger | Native effects already meet the brief | N / G |
| Pinned scroll storytelling | GSAP ScrollTrigger | The story requires a 3D camera, so add Three.js | G; T if 3D |
| Smooth scrolling | Native scrolling; Lenis if justified | Accessibility or precise native behaviour takes priority | N; L only with reason |
| Animated logos | Rive or SVG + GSAP | Procedural geometry requires shaders | Rive gap / G / S |
| Icons / microinteractions | CSS, Motion or Rive | Playback-only asset is better as Lottie | N / M; Rive/Lottie gap |
| Simple animated illustrations | Lottie / dotLottie | Complex interaction needs Rive | Lottie/dotLottie gap |
| Fluid image hover distortion | OGL + GLSL | Basic transforms can use CSS | T + S (OGL) |
| Full-screen liquid backgrounds | OGL or Three.js shaders | Pre-rendered video achieves the same outcome | T + S; N for video |
| Many interactive 2D sprites | PixiJS | DOM or SVG handles a modest number | PixiJS gap; N for modest volume |
| 3D product viewer | `<model-viewer>` | A full configurator needs Three.js | model-viewer gap; T if custom |
| Interactive 3D hero | Three.js | Spline offers sufficient control, faster | T; Spline gap |
| 3D in React | React Three Fiber | Existing app uses no React | T + N |
| Complex 3D game experience | PlayCanvas / Babylon.js | A mostly presentational site favours Three.js | PlayCanvas/Babylon.js gap |
| Physics-driven 3D objects | Rapier + Three.js | Simple spring animation is sufficient | Rapier gap; T for scene |
| Interactive particles | PixiJS (2D), Three.js (3D) | Massive GPU simulations justify custom compute | PixiJS gap / T / S |
| Custom experimental shaders | OGL / Three.js + GLSL | WebGPU compute is a core requirement | T + S |
| Large real-time GPU simulation | WebGPU compute | WebGL solution is simpler and adequate | S, advanced reason |
| Video scroll sequence | Video frames + GSAP | True 3D interaction is required | G + N |
| Interactive charts | D3 or Observable Plot | Standard charts can use a charting library | D3/Plot gap |
| Spatial map experience | MapLibre GL JS | No actual map is needed | MapLibre gap |
| Immersive AR product preview | `<model-viewer>` | Custom AR behaviour requires WebXR | model-viewer/WebXR gap |
| Cinematic 3D production | Blender + Three.js | A fixed film can simply be rendered as video | A + T; N for video |

## Rendering and WebGPU

**Interpretation** — Concept → medium → renderer → authoring/component model
is the hierarchy. WebGL 2 is a conservative candidate for a WebGL scene;
WebGPU earns selection through a demonstrated requirement, not its age.

| Layer | WebGL path | WebGPU path | Studio route |
| --- | --- | --- | --- |
| Browser graphics API | WebGL 2 | WebGPU | S; advanced justification for raw APIs |
| Shader authoring | GLSL | WGSL, or TSL in Three.js | S; match material APIs to renderer |
| 3D abstraction | Three.js WebGLRenderer | Three.js WebGPURenderer, with WebGL 2 backend fallback | T + S; verify APIs, not just backend availability |
| React component model | Compatible R3F stable line | v10 alpha path, or a version-specific custom renderer integration | N + T; do not mix v9/v10 recipes |
| No-GPU failure path | HTML content plus designed poster/static state | HTML content plus designed poster/static state | N + Q |

**Documented** — Current renderer status, fallback and breaking APIs are in the
[verification ledger](verification.md). A fallback backend is not a fallback
for unsupported shader or effect APIs. **Unknown** — which path performs better
for a particular unbuilt scene; benchmark its actual content and target devices.

## 3. Animation toolkit

**Interpretation** — Choose by the responsibility, not a global library ranking.

| Tool | Choose it for | Don't make it your default for | Studio route / gap |
| ---------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------- | --- |
| CSS animations / transitions | Basic fades, transforms, hover, responsive motion | Complex, tightly sequenced cinematic scenes | N |
| Native Web Animations API | Small imperative animations without a major dependency | Large creative timelines | N |
| GSAP | Complex choreography, kinetic typography, ScrollTrigger, coordinated sequences | Routine React layout changes | G |
| Motion | React UI, gestures, layout transitions, springs, dragging | Deep GSAP-style scroll storytelling | M |
| Anime.js | Creative DOM/SVG animation, SVG path work | Complex 3D scene management | Anime.js gap |
| Lenis | Smooth scroll feel and scroll-to-WebGL synchronisation | Animating elements independently | L with recorded reason |
| Theatre.js | Visually authoring cinematic keyframes, cameras, lights and 3D sequences | Simple microinteractions | Theatre.js gap |

GSAP owns directed sequences; Motion owns React layout/state/gestures. Never
give them the same animated property. Native scroll is the starting point;
Lenis is not an element-animation library. Its snapping and nested-container
limits are [documented separately](verification.md).

## 4. Shader and creative rendering comparison

**Interpretation** — Qualitative source comparison, not benchmark results.
OGL routes to T + S, PixiJS is a dedicated-tool gap, Three.js routes to T + S.

| Criterion | OGL | PixiJS | Three.js |
| ---------------------- | ------------------------------ | ---------------------------- | ----------------------------------------- |
| Main specialty | Minimal WebGL abstraction | GPU-rendered 2D graphics | General-purpose 3D |
| Image displacement | Capable | Capable | Capable; more scene machinery |
| Sprite-heavy scenes | Possible | Primary candidate | Often unnecessary |
| Custom GLSL effects | Capable | Capable | Capable |
| 3D objects and cameras | Basic | Primarily 2D | Primary candidate |
| Large scenes | More manual implementation | Strong for 2D | Strong for 3D |
| Learning effort | Requires shader knowledge | Moderate | Moderate to high |
| Best fit | Experimental creative websites | Interactive 2D experiences | Immersive 3D websites |

### Effect choices

**Interpretation** — Try the simplest medium that preserves the idea.

| Effect | Preferred approach | Studio route / gap |
| ---------------------------------- | --------------------------------------------------- | --- |
| Magnetic button | GSAP or Motion | G / M |
| Cursor-following image | DOM + GSAP | N + G |
| Image ripple on hover | OGL + GLSL | T + S (OGL) |
| Liquid-glass image distortion | OGL or Three.js shader | T + S |
| Noise/grain overlay | CSS/SVG or shader | N / S |
| Animated gradient mesh | CSS, SVG or shader, by complexity | N / S |
| Procedural organic blobs | GLSL via OGL or Three.js | T + S |
| Real-time refraction of 3D objects | Three.js + appropriate material/shader | T + S |
| Interactive halftone | SVG/CSS for simple cases; shader for dynamic images | N / S |
| Thousands of 2D particles | PixiJS | PixiJS gap |
| Thousands of 3D particles | Three.js with instancing/points | T |
| Complex GPU particle simulation | WebGPU compute or an optimised GPU simulation | S, advanced reason |
| Image-to-image transition | GSAP for simple transforms; OGL for shader morphing | G / T + S |
| Real-time feedback and distortion | Custom shader pipeline | S |
| Scroll-controlled 3D displacement | Three.js + GSAP | T + G |

A fixed image, video, SVG filter or CSS effect can be a valid alternative.
Compare fidelity, interaction and maintenance in the prototype. Do not add
a full engine for an effect that does not need its scene model.

## 5. 3D engines

**Interpretation** — Compare control, authoring and the maintenance owner.
The source's A-Frame description refers to declarative authoring, not proven
assistive-technology accessibility. All paths need accessible content.

| Tool | Strength | Weakness / trade-off | Best use | Studio route / gap |
| ------------------ | -------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------- | --- |
| Three.js | Flexible, broad ecosystem, customisation | You assemble many systems yourself | Creative 3D websites | T |
| React Three Fiber | React-native architecture on top of Three.js | Adds React ecosystem considerations | Complex React + 3D sites | N + T |
| Spline | Fast visual scene creation and web embedding | Less low-level control over custom rendering | 3D concepts and moderate-interaction heroes | Spline gap |
| Babylon.js | Integrated features for large interactive 3D apps | More engine-oriented workflow | Advanced configurators and 3D apps | Babylon.js gap |
| PlayCanvas | Integrated editor and engine workflow | Different tooling and engine architecture | 3D productions, games and interactive environments | PlayCanvas gap |
| A-Frame | Declarative entity/component VR scene building | Less suitable for heavily bespoke creative art direction | Declarative WebXR prototyping | A-Frame gap |
| Raw WebGL / WebGPU | Maximum control of rendering | Highest engineering cost | Specialised rendering research | S + T, advanced reason |

### React 3D ecosystem

**Interpretation** — Supporting packages have distinct jobs; none is an
automatic bundle. Spline and model-viewer should be compared for simple scenes.

| Technology | Its responsibility | Studio route / gap |
| --------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | --- |
| [React Three Fiber](https://github.com/pmndrs/react-three-fiber) | Build Three.js scenes with React | T |
| [Drei](https://github.com/pmndrs/drei) | Cameras, controls, environment helpers, loaders and reusable utilities | T |
| [React Postprocessing](https://github.com/pmndrs/react-postprocessing) | Bloom, depth of field, noise and other visual treatments | P, only with reason |
| [React Three Rapier](https://github.com/pmndrs/react-three-rapier) | 3D physics | Rapier gap |
| [GLTFJSX](https://github.com/pmndrs/gltfjsx) | Convert 3D assets into reusable React components | A + T |
| [14islands Scroll Rig](https://github.com/14islands/r3f-scroll-rig) | Coordinate HTML content and 3D elements during scrolling | Scroll Rig gap |
| [Theatre.js](https://www.theatrejs.com/) | Visual editing of animation sequences | Theatre.js gap |

**Documented** — R3F v9/stable, v10/alpha, renderer/material and Spline
export boundaries were checked on 2026-10-23; see [verification](verification.md).
Record compatible React, Three.js, R3F, Drei and post-processing versions rather
than copying a latest-version preset.

## 6. Living identities

**Interpretation** — Art-directed living identities use deliberately designed
states and behaviours (Rive, SVG, GSAP). Generative identity systems use rules
and inputs to produce variations (Canvas, shaders, Three.js). A state machine
with five authored states is not equivalent to a generative grammar. Neither
is intrinsically better: choose against purpose, invariants and handover.

| Requirement | Preferred choice | Studio route / gap |
| --------------------------------------------- | ------------------------------------ | --- |
| A simple looping logo animation | Lottie / dotLottie | Lottie/dotLottie gap |
| Logo responds to hover, clicks or user input | Rive | Rive gap |
| Letterforms distort or transform continuously | SVG + GSAP, or custom rendering | G / S |
| Identity changes according to data | Rive data binding or generative code | Rive gap / C |
| Interactive mascot or animated character | Rive | Rive gap |
| Procedural particle-based identity | PixiJS or Three.js | PixiJS gap / T |
| 3D living identity | Three.js | T |
| Identity system for web and app interfaces | Rive, SVG and reusable design tokens | Rive gap / N |
| Static logo that just needs subtle movement | CSS or SVG | N |

**Documented** — Rive data binding and CLI agent workflow, and dotLottie
state machines, are verified in the [ledger](verification.md). Compare the
actual editor/runtime/export requirements. Essential text and controls stay
in accessible HTML; test keyboard, reduced motion and missing input.

## 7. Specialist tools

**Interpretation** — Each specialist must earn a recorded reason. No row
authorises automatic installation.

| Category | Notable tools | When they earn their place | Studio route / gap |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- | --- |
| Generative coding | [p5.js](https://p5js.org/), Canvas API | Procedural illustration, creative sketches, interactive art | C |
| 2D interactive graphics | [PixiJS](https://pixijs.com/) | Sprite systems, particle layers, rich 2D scenes | PixiJS gap |
| SVG animation | GSAP, Motion, Anime.js | Vector identity systems, drawings, morphing | G / M; Anime.js gap |
| 2D physics | [Matter.js](https://brm.io/matter-js/) | Falling, bouncing or colliding interface objects | F, parked |
| 3D physics | [Rapier](https://rapier.rs/) | Accurate collisions and interactive spatial behaviour | Rapier gap |
| Data visualisation | [D3.js](https://d3js.org/), [Observable Plot](https://observablehq.com/plot/) | Custom data-driven graphics and interactive storytelling | D3/Plot gap |
| Maps | [MapLibre](https://maplibre.org/) | Custom interactive geographic experiences | MapLibre gap |
| 3D model display | [model-viewer](https://modelviewer.dev/) | Standard 3D viewers and supported AR previews | model-viewer gap |
| 3D model authoring | [Blender](https://www.blender.org/), Houdini, Cinema 4D | Modelling, procedural geometry, rigging, lighting | A; Houdini/Cinema 4D gaps |
| 3D asset optimisation | [glTF Transform](https://gltf-transform.dev/), GLTFJSX | Preparing smaller and more efficient web assets | A + T |
| Cinematic sequencing | [Theatre.js](https://www.theatrejs.com/) | Visual timelines controlling 3D camera and scene properties | Theatre.js gap |
| HTML-to-WebGL integration | [r3f-scroll-rig](https://github.com/14islands/r3f-scroll-rig) | Matching DOM content with a persistent GPU canvas | Scroll Rig gap |
| Programmatic video | [Remotion](https://www.remotion.dev/) | Generating videos, motion assets and reusable compositions through code | V |
| Smooth scrolling | [Lenis](https://lenis.darkroom.engineering/) | Deliberate scroll feel and synchronisation | L only with reason |

## 8. Four starting stacks

**Interpretation** — Starting architectures adapted from the source, not fixed
prescriptions or studio defaults. Existing project conventions come first.

| Stack | Minimum candidate | Conditional additions and reason | Studio route / gap |
| --- | --- | --- | --- |
| A — Editorial | HTML/CSS/SVG, Astro when content architecture warrants it | GSAP for directed choreography; Lenis only after native scroll fails a stated need | N + G; L gated; Astro gap |
| B — Experimental | HTML/CSS/SVG with GSAP and OGL/GLSL for the signature effect | React only for state/component architecture that needs it | N + G + T + S; Astro gap if chosen |
| C — Immersive | Three.js with HTML content; React/Next + R3F only inside justified React architecture; Blender for assets | Drei helpers as needed; P, Scroll Rig, Theatre.js or Rapier only for a named effect, alignment, sequencing or collision requirement | N + T + G + A; P gated; Scroll Rig/Theatre.js/Rapier gaps |
| D — Living identity | SVG and tokens; GSAP or Rive for authored interactive assets | Canvas, PixiJS or Three.js for genuinely generated forms; choose Astro/React for the wider site needs | N + G + C + T; Rive/PixiJS/Astro gaps |

**Documented** — Astro's separately hydrated islands can limit client JavaScript
([official architecture](https://docs.astro.build/en/concepts/islands/), checked
2026-10-23). **Interpretation** — Use it where most content can remain HTML;
use a React-centric application when routing/state/integration warrants that
architecture. Neither framework proves performance on its own.

## 9. Six project scenarios

**Interpretation** — These source-inspired briefs describe candidate techniques,
not permission to reproduce Lusion, Buttermax, Apple or another identity.
References teach principles; all production composition, assets and code must
be original or explicitly licensed dependencies.

| Scenario | Preferred prototype | Alternative and trade-off | Studio route / gap |
| --- | --- | --- | --- |
| A — Sculptural studio narrative | Three.js + GSAP + Blender; R3F only within React | Spline can simplify visual authoring if export/control meets the brief; Theatre.js for justified camera sequencing, Scroll Rig for proven DOM alignment need | T + G + A; Spline/Theatre.js/Scroll Rig gaps |
| B — Experimental editorial | HTML/CSS/SVG + GSAP; OGL/GLSL for a focused image effect; Astro if appropriate | Native transforms avoid a GPU pipeline; React/full Three.js only if architecture/scene requirements demand them | N + G + T + S; Astro gap |
| C — Cinematic product reveal | Prototype a pre-rendered frame sequence + GSAP for fixed choreography | Three.js for free camera/material interaction; sequence trades real-time interaction for fixed art direction and potentially heavy assets | N + G + T + A |
| D — Generative brand identity | Rive for bounded designed states; Canvas for rule-generated forms | PixiJS/OGL/Three.js only when visual scale or geometry requires them; separate data binding from generating forms | C + T + S; Rive/PixiJS gaps |
| E — Portfolio transitions | HTML + GSAP or React + Motion, with distinct property owners if both are used | Add OGL for a necessary distortion; Three.js only for real spatial/material content; Astro is a content-led candidate | N + G / M + T + S; Astro gap |
| F — Product configurator | React + Three.js/R3F + glTF, with explicit state ownership | model-viewer for rotate-and-view; a state store such as Zustand only when needed; custom 3D adds asset/runtime maintenance cost | N + T + A; model-viewer gap |

Ordinary navigation, forms and paragraphs remain HTML in every scenario.
Compare two alternatives in the stack record, prototype the riskiest interaction
first and pass [the quality gate](selection-policy.md#quality-gate) before scaling.
