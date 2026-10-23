---
title: The Creative Technology Handbook — October 2026
type: guide
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Archive provenance

**Documented** — Founder-supplied source received 2026-10-23, dated October
2026 and written with AI-assisted research. **Unknown** — source claims are
not yet verified as a whole. This is an archive, not selection policy.
The original name 3RDWRONGS is retained; the studio is now 3RDWRONG.

Only ephemeral image links (captions retained), favicon image lines, citation
chips, HTML spacing artefacts and ChatGPT URL tracking were removed. The section 10
interactive-selector remnant is rendered as one sentence. All other source
wording is retained, including its recommendations and historical claims.
The [working system](../../methods/creative-technology/README.md) separates
adopted rules from dated verification and untested interpretation.

<!-- markdownlint-disable MD001 MD009 MD012 MD024 MD025 MD029 MD031 MD032 MD034 MD040 MD047 MD049 MD050 MD051 MD055 MD056 MD058 MD060 -->

# The Creative Technology Handbook

How to choose the right tools for world-class website design, motion, 3D, interaction and creative engineering — October 2026.

The goal is not to use Three.js everywhere. It's to understand the entire creative-development ecosystem and select the right combination for each project.

For 3RDWRONGS, I'd structure the technology system around six capabilities:

Parallax Project Page - Awwwards

01 — Layout and visual identity

Typography, composition, responsive systems, interface details, graphic language and brand expression.

HTML · CSS · SVG · Figma

Interactive Typography - Awwwards

02 — Motion and choreography

Scroll narratives, page transitions, kinetic type, reveals, pacing and hover behaviour.

GSAP · Motion · CSS Animations · Lenis

きちんと文脈もあって技術としてもおもしろい流体表現が楽しい OAKSUN Studio のウェブサイト - WebGL 総本山

03 — Creative rendering and shaders

Fluid distortion, organic visuals, generative art, interactive images and particle effects.

OGL · PixiJS · GLSL · WebGPU

A gallery of works in the form of a virtual space - Awwwards

04 — 3D and immersive environments

Spatial navigation, interactive sculptures, real-time materials, depth and cinematic scenes.

Three.js · React Three Fiber · Blender · PlayCanvas

Vodafone / Generative Rebrand — itMatters

05 — Living brand identities

Responsive logos, interactive identity systems, animated graphic assets and dynamic symbols.

Rive · SVG · GSAP · Canvas

Spaace - Awwwards SOTD

06 — Data, physics and simulation

Interactive visualisations, believable physical behaviour, procedural systems and computational art.

D3 · Rapier · Matter.js · Custom shaders

The key distinction is between a tool that creates the visual, one that animates it, one that renders it, and one that manages the wider website. These tools often belong together rather than competing.

## 1. The master task-to-tool selection matrix

This is the first reference I would give an AI developer before it begins a project.

| What you want to create        | Best starting choice                 | Use something else when…                                 |
| ------------------------------ | ------------------------------------ | -------------------------------------------------------- |
| Premium, minimal website       | HTML/CSS + Astro                     | Complex application state requires React                 |
| Kinetic typography             | GSAP + DOM text                      | Simple movement only needs CSS                           |
| Intricate animation timelines  | GSAP                                 | React layout interactions favour Motion                  |
| Scroll-triggered reveals       | CSS or GSAP ScrollTrigger            | Native effects already meet the brief                    |
| Pinned scroll storytelling     | GSAP ScrollTrigger                   | The story requires a 3D camera, so add Three.js          |
| Smooth scrolling               | Native scrolling; Lenis if justified | Accessibility or precise native behaviour takes priority |
| Animated logos                 | Rive or SVG + GSAP                   | Procedural geometry requires shaders                     |
| Icons / microinteractions      | CSS, Motion or Rive                  | Playback-only asset is better as Lottie                  |
| Simple animated illustrations  | Lottie / dotLottie                   | Complex interaction needs Rive                           |
| Fluid image hover distortion   | OGL + GLSL                           | Basic transforms can use CSS                             |
| Full-screen liquid backgrounds | OGL or Three.js shaders              | Pre-rendered video achieves the same outcome             |
| Many interactive 2D sprites    | PixiJS                               | DOM or SVG handles a modest number                       |
| 3D product viewer              | `<model-viewer>`                     | A full configurator needs Three.js                       |
| Interactive 3D hero            | Three.js                             | Spline offers sufficient control, faster                 |
| 3D in React                    | React Three Fiber                    | Existing app uses no React                               |
| Complex 3D game experience     | PlayCanvas / Babylon.js              | A mostly presentational site favours Three.js            |
| Physics-driven 3D objects      | Rapier + Three.js                    | Simple spring animation is sufficient                    |
| Interactive particles          | PixiJS (2D), Three.js (3D)           | Massive GPU simulations justify custom compute           |
| Custom experimental shaders    | OGL / Three.js + GLSL                | WebGPU compute is a core requirement                     |
| Large real-time GPU simulation | WebGPU compute                       | WebGL solution is simpler and adequate                   |
| Video scroll sequence          | Video frames + GSAP                  | True 3D interaction is required                          |
| Interactive charts             | D3 or Observable Plot                | Standard charts can use a charting library               |
| Spatial map experience         | MapLibre GL JS                       | No actual map is needed                                  |
| Immersive AR product preview   | `<model-viewer>`                     | Custom AR behaviour requires WebXR                       |
| Cinematic 3D production        | Blender + Three.js                   | A fixed film can simply be rendered as video             |

These are editorial recommendations, not universal performance rankings. The correct choice depends on asset complexity, browser support, developer expertise, interaction requirements and production deadlines.

## 2. Understand the rendering hierarchy first

Many developers confuse WebGL, WebGPU, Three.js, R3F and shaders. They operate at different levels.

Your visual concept

What should appear and how should it behave?

DOM / SVG

Text, UI, vector

Canvas 2D

Pixel rendering

GPU rendering

WebGL / WebGPU

Libraries and engines

GSAP · PixiJS · OGL · Three.js · Babylon.js · PlayCanvas

Conceptual layers; not every library is a GPU-rendering library. GSAP, for example, animates properties and timelines rather than rendering an entire 3D scene.

Three.js abstracts away much of the low-level graphics programming required to work directly with WebGL or WebGPU.

React Three Fiber then provides a React component model for Three.js. It is not a more powerful renderer than Three.js; it is another way of developing with it.


React Three Fiber



### WebGL vs WebGPU

|                          | WebGL 2                        | WebGPU                              |
| ------------------------ | ------------------------------ | ----------------------------------- |
| Maturity                 | Established                    | Newer, still evolving               |
| Production compatibility | Generally safer                | Requires more compatibility testing |
| Advanced GPU compute     | More limited and indirect      | Major strength                      |
| Shader language          | GLSL                           | WGSL, or TSL through Three.js       |
| Typical application      | Most current creative 3D sites | Advanced rendering and simulations  |
| My default               | Production baseline            | Evaluate for advanced projects      |

Three.js's newer `WebGPURenderer` can fall back to WebGL 2. But its material and post-processing APIs differ from the traditional renderer, and its documentation still identifies some experimental limitations.


Three.js



Rule: Never choose WebGPU just because it sounds newer. Choose it when it enables a particular visual or computational result that warrants the additional development and testing.

## 3. The animation toolkit: which is best?

My preferred choices by animation problem

| Tool                         | Choose it for                                                                  | Don't make it your default for              |
| ---------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------- |
| CSS animations / transitions | Basic fades, transforms, hover, responsive motion                              | Complex, tightly sequenced cinematic scenes |
| Native Web Animations API    | Small imperative animations without a major dependency                         | Large creative timelines                    |
| GSAP                         | Complex choreography, kinetic typography, ScrollTrigger, coordinated sequences | Routine React layout changes                |
| Motion                       | React UI, gestures, layout transitions, springs, dragging                      | Deep GSAP-style scroll storytelling         |
| Anime.js                     | Lightweight, creative DOM/SVG animation, SVG path work                         | Complex 3D scene management                 |
| Lenis                        | Smooth scroll feel and scroll-to-WebGL synchronisation                         | Animating elements independently            |
| Theatre.js                   | Visually authoring cinematic keyframes, cameras, lights and 3D sequences       | Simple microinteractions                    |

GSAP's ScrollTrigger supports pinning, scrubbing, snapping and complex timeline coordination. Motion is especially strong at interruptible React layout and shared-element transitions. Native CSS scroll-driven animation is increasingly capable without JavaScript orchestration.




### GSAP vs Motion

Choose GSAP when the experience should play like a carefully directed film, particularly when scrolling determines the timing.

Choose Motion when the interface should behave like a polished application: cards moving between layouts, components entering and exiting, and controls responding to gestures.

You can use both in the same project, but give them distinct responsibilities. Don't let both libraries animate the same property on the same element simultaneously.

### Lenis vs GSAP ScrollTrigger

They do different jobs.

Lenis affects scroll smoothing and synchronisation. ScrollTrigger maps scroll positions and progress to animations.

You can use ScrollTrigger without Lenis and vice versa. Lenis documents a direct GSAP integration, but also notes limitations around scroll snapping, nested scroll containers and some browser behaviours.


GitHub



Rule: Begin with native scrolling. Add Lenis only when a specific creative or technical reason justifies it.

## 4. Shader and creative-rendering technologies

This category is especially important for the experimental design aesthetic you prefer.

Shaders are small programs that control how geometry, pixels, lighting or other visual data are processed on the GPU.

They're behind effects such as liquid chrome, refractive glass, image warping, procedural noise, generative surfaces and advanced particle systems.

### OGL vs PixiJS vs Three.js

|                        | OGL                            | PixiJS                       | Three.js                                  |
| ---------------------- | ------------------------------ | ---------------------------- | ----------------------------------------- |
| Main specialty         | Minimal WebGL abstraction      | High-performance 2D graphics | General-purpose 3D                        |
| Image displacement     | Excellent                      | Excellent                    | Excellent, but heavier for simple effects |
| Sprite-heavy scenes    | Possible                       | Strongest default            | Often unnecessary                         |
| Custom GLSL effects    | Excellent                      | Excellent                    | Excellent                                 |
| 3D objects and cameras | Basic                          | Primarily 2D                 | Strongest default                         |
| Large scenes           | More manual implementation     | Strong for 2D                | Strong for 3D                             |
| Learning effort        | Requires shader knowledge      | Moderate                     | Moderate to high                          |
| Best fit               | Experimental creative websites | Interactive 2D experiences   | Immersive 3D websites                     |

OGL deliberately exposes a smaller abstraction layer than Three.js. PixiJS focuses on GPU-accelerated 2D rendering and supports WebGL and an evolving WebGPU backend.


oframe/ogl: Minimal WebGL Library · GitHub


### Which one should we choose for specific effects?

| Effect                             | Preferred approach                                  |
| ---------------------------------- | --------------------------------------------------- |
| Magnetic button                    | GSAP or Motion                                      |
| Cursor-following image             | DOM + GSAP                                          |
| Image ripple on hover              | OGL + GLSL                                          |
| Liquid-glass image distortion      | OGL or Three.js shader                              |
| Noise/grain overlay                | CSS/SVG or shader                                   |
| Animated gradient mesh             | CSS, SVG or shader, by complexity                   |
| Procedural organic blobs           | GLSL via OGL or Three.js                            |
| Real-time refraction of 3D objects | Three.js + appropriate material/shader              |
| Interactive halftone               | SVG/CSS for simple cases; shader for dynamic images |
| Thousands of 2D particles          | PixiJS                                              |
| Thousands of 3D particles          | Three.js with instancing/points                     |
| Complex GPU particle simulation    | WebGPU compute or an optimised GPU simulation       |
| Image-to-image transition          | GSAP for simple transforms; OGL for shader morphing |
| Real-time feedback and distortion  | Custom shader pipeline                              |
| Scroll-controlled 3D displacement  | Three.js + GSAP                                     |

Important: Not every beautiful-looking distortion requires GPU programming. For a static or predictable result, a video, SVG filter or CSS effect can sometimes be faster to build and easier to maintain.

## 5. Choosing a 3D engine

The two main questions are: How much 3D complexity does the project require, and how much control do we need?

| Tool               | Strength                                           | Weakness / trade-off                                     | Best use                                           |
| ------------------ | -------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------- |
| Three.js           | Flexible, broad ecosystem, excellent customisation | You assemble many systems yourself                       | Creative 3D websites                               |
| React Three Fiber  | React-native architecture on top of Three.js       | Adds React ecosystem considerations                      | Complex React + 3D sites                           |
| Spline             | Fast visual scene creation and web embedding       | Less low-level control over custom rendering             | 3D concepts and moderate-interaction heroes        |
| Babylon.js         | Integrated features for large interactive 3D apps  | More engine-oriented workflow                            | Advanced configurators and 3D apps                 |
| PlayCanvas         | Integrated editor and engine workflow              | Different tooling and engine architecture                | 3D productions, games and interactive environments |
| A-Frame            | Declarative entity/component VR scene building     | Less suitable for heavily bespoke creative art direction | Accessible WebXR prototyping                       |
| Raw WebGL / WebGPU | Maximum control of rendering                       | Highest engineering cost                                 | Specialised rendering research                     |

### Should we prefer Three.js or Spline?

Spline wins for speed when the required scene can be created visually using its existing capabilities.

Three.js wins for custom control when you require original shaders, extensive scene logic, deeply custom rendering or tightly integrated interaction systems.

Spline supports code export and interaction through its runtime API, so it isn't limited to static embeds.


Spline


### The Three.js ecosystem worth knowing

If you choose a React-based 3D approach, these are the important supporting libraries:

| Technology                                                                                    | Its responsibility                                                     |
| --------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| [React Three Fiber](https://github.com/pmndrs/react-three-fiber)       | Build Three.js scenes with React                                       |
| [Drei](https://github.com/pmndrs/drei)                                 | Cameras, controls, environment helpers, loaders and reusable utilities |
| [React Postprocessing](https://github.com/pmndrs/react-postprocessing) | Bloom, depth of field, noise and other visual treatments               |
| [React Three Rapier](https://github.com/pmndrs/react-three-rapier)     | 3D physics                                                             |
| [GLTFJSX](https://github.com/pmndrs/gltfjsx)                           | Convert 3D assets into reusable React components                       |
| [14islands Scroll Rig](https://github.com/14islands/r3f-scroll-rig)    | Coordinate HTML content and 3D elements during scrolling               |
| [Theatre.js](https://www.theatrejs.com/)                               | Visual editing of animation sequences                                  |

14islands' Scroll Rig is particularly relevant to your references. It tracks DOM elements and synchronises their positions with objects on a shared 3D canvas. This helps solve a notoriously difficult problem in creative development: combining normal accessible HTML layouts with a fluid WebGL visual layer.


GitHub



Compatibility note: React Three Fiber v9 is the stable baseline. v10 is still alpha in its official documentation, and switching to its WebGPU renderer can break existing GLSL-based materials and some post-processing integrations. Test dependencies before committing to v10.


React Three Fiber



## 6. Rive vs Lottie vs SVG vs GSAP for living identities

This is one of the most important decisions for a brand identity studio.

| Requirement                                   | Preferred choice                     |
| --------------------------------------------- | ------------------------------------ |
| A simple looping logo animation               | Lottie / dotLottie                   |
| Logo responds to hover, clicks or user input  | Rive                                 |
| Letterforms distort or transform continuously | SVG + GSAP, or custom rendering      |
| Identity changes according to data            | Rive data binding or generative code |
| Interactive mascot or animated character      | Rive                                 |
| Procedural particle-based identity            | PixiJS or Three.js                   |
| 3D living identity                            | Three.js                             |
| Identity system for web and app interfaces    | Rive, SVG and reusable design tokens |
| Static logo that just needs subtle movement   | CSS or SVG                           |

Rive's state machines, dynamic inputs and data binding make it particularly suited to reusable interactive identity assets. Lottie remains useful for pre-authored motion, while the newer dotLottie ecosystem also supports more advanced state-machine interaction. The distinction is no longer simply “Lottie is static, Rive is interactive”; compare the actual capabilities required.


Rive


A useful 2026 development: Rive now promotes a CLI workflow compatible with AI coding agents including Claude Code, allowing some animation creation to be driven through an agent and refined visually in the editor.


Rive



For 3RDWRONGS, I would establish two identity capabilities:

Art-directed living identities: created using Rive, GSAP and SVG, with deliberately designed states and behaviours.

Generative identity systems: created with Canvas, shaders or Three.js, where rules and data continuously generate variations.

Those are different creative disciplines and shouldn't be treated as interchangeable.

## 7. The additional tools most creative developers should know

The earlier tools cover most 3D and motion work, but a genuinely complete creative-engineering system also needs several specialist categories.

| Category                  | Notable tools                                                                                                               | When they earn their place                                              |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Generative coding         | [p5.js](https://p5js.org/), Canvas API                                                               | Procedural illustration, creative sketches, interactive art             |
| 2D interactive graphics   | [PixiJS](https://pixijs.com/)                                                                        | Sprite systems, particle layers, rich 2D scenes                         |
| SVG animation             | GSAP, Motion, Anime.js                                                                                                      | Vector identity systems, drawings, morphing                             |
| 2D physics                | [Matter.js](https://brm.io/matter-js/)                                                               | Falling, bouncing or colliding interface objects                        |
| 3D physics                | [Rapier](https://rapier.rs/)                                                                         | Accurate collisions and interactive spatial behaviour                   |
| Data visualisation        | [D3.js](https://d3js.org/), [Observable Plot](https://observablehq.com/plot/) | Custom data-driven graphics and interactive storytelling                |
| Maps                      | [MapLibre](https://maplibre.org/)                                                                    | Custom interactive geographic experiences                               |
| 3D model display          | [model-viewer](https://modelviewer.dev/)                                                             | Standard 3D viewers and supported AR previews                           |
| 3D model authoring        | [Blender](https://www.blender.org/), Houdini, Cinema 4D                                              | Modelling, procedural geometry, rigging, lighting                       |
| 3D asset optimisation     | [glTF Transform](https://gltf-transform.dev/), GLTFJSX                                               | Preparing smaller and more efficient web assets                         |
| Cinematic sequencing      | [Theatre.js](https://www.theatrejs.com/)                                                             | Visual timelines controlling 3D camera and scene properties             |
| HTML-to-WebGL integration | [r3f-scroll-rig](https://github.com/14islands/r3f-scroll-rig)                                        | Matching DOM content with a persistent GPU canvas                       |
| Programmatic video        | [Remotion](https://www.remotion.dev/)                                                                | Generating videos, motion assets and reusable compositions through code |
| Smooth scrolling          | [Lenis](https://lenis.darkroom.engineering/)                                                         | Deliberate scroll feel and synchronisation                              |

None of these should be installed automatically. They should be available as approved options in your system.

## 8. Four complete stacks for different kinds of exceptional websites

### Stack A — Editorial excellence

Lower complexity

Studio NAND - Made to Measure

[nand.io](https://www.nand.io/case-studies/made-to-measure)

Astro + CSS + SVG + GSAP + optional Lenis

Designed for exceptional typography, meticulous responsive layouts, dramatic transitions, beautiful image treatment and carefully directed motion.

This is where I'd start for premium branding-studio websites that don't need elaborate 3D.

### Stack B — Experimental digital studio

Medium complexity

Mouse interaction WebGl Liquid Distortion - Awwwards

[awwwards.com](https://www.awwwards.com/inspiration/mouse-interaction-webgl-liquid-distortion-heroine)

Astro / React + GSAP + OGL + GLSL

Designed for fluid image effects, custom cursors, generative transitions, procedural textures and experimental typography.

Excellent when the experience is primarily 2D but needs GPU-powered artistic effects.

### Stack C — Immersive creative experience

High complexity

Campo alle Comete - Awwwards SOTD

[awwwards.com](https://www.awwwards.com/sites/campo-alle-comete)

Next.js / React + Three.js + R3F + Drei + GSAP + Blender

Add post-processing, Scroll Rig, Theatre.js and Rapier only where needed.

Designed for immersive narratives, 3D art direction, spatial interaction, original materials and camera choreography.

### Stack D — Living identity experience

Variable complexity

An interactive identity for York Mediale - Creative Review

[creativereview.co.uk](https://www.creativereview.co.uk/york-mediale-art-festival-branding/)

Astro / React + Rive + SVG + GSAP

Add PixiJS or Three.js for deeply generative identity elements.

Designed for expressive identity systems that carry consistent motion and behaviour across interfaces.

Use Astro when most content can be static HTML with small interactive islands; use Next.js when the wider application genuinely benefits from React-centric architecture, routing and state. Astro's islands model is specifically designed to limit unnecessary client-side JavaScript.


Astro Docs



These are starting architectures, not fixed prescriptions.

## 9. Real project scenarios: what I would actually select

### Scenario A — An interactive studio homepage inspired by Lusion

The concept: a sculptural object changes form as visitors navigate through the brand narrative.

Stack: Three.js + R3F + GSAP + Blender. Consider Theatre.js for art-directed camera sequences and Scroll Rig when DOM elements must align precisely with 3D objects.

Avoid building ordinary navigation, paragraphs and forms inside the 3D scene.

### Scenario B — A Buttermax-style experimental editorial site

The concept: extremely expressive typography, unexpected transitions, fluid image hover and playful cursor behaviour.

Stack: Astro + GSAP + OGL + GLSL + CSS/SVG.

Don't add React or a full Three.js scene unless the interaction architecture requires them. Use HTML typography for actual readable content.

### Scenario C — A product website like a cinematic Apple launch page

The concept: a product appears to rotate and disassemble as the visitor scrolls.

Two valid approaches:

| Approach                           | Advantage                                                | Limitation                                                     |
| ---------------------------------- | -------------------------------------------------------- | -------------------------------------------------------------- |
| Pre-rendered frame sequence + GSAP | High-quality fixed imagery and predictable art direction | Large assets; cannot freely rotate or inspect                  |
| Three.js + GSAP                    | Fully interactive 3D, configurable camera and materials  | Real-time rendering, asset optimisation and device constraints |

For a fully predetermined cinematic reveal, I'd prototype the frame-sequence version first. For a real product configurator, choose 3D.

### Scenario D — Interactive generative brand identity

The concept: the studio's visual identity evolves based on interaction, context or data.

Stack: Rive for bounded animated states; PixiJS, OGL or Three.js for genuinely generated visual outcomes.

This distinction matters. An animation that changes between five designed states is not the same as a system that generates unique forms from a set of rules.

### Scenario E — An immersive portfolio

The concept: project thumbnails subtly distort on hover, expand into case studies and transform smoothly between layouts.

Stack: Astro/React + GSAP or Motion + optional OGL.

Only introduce Three.js if the portfolio includes real 3D material or spatial navigation.

### Scenario F — A high-end e-commerce configurator

The concept: visitors can rotate an object, change materials, select variants and inspect details.

Stack: React + Three.js/R3F + glTF assets + Zustand or equivalent state management.

For a simpler rotate-and-view experience, Google's `<model-viewer>` may remove the need for a custom 3D engine.


Model Viewer



## 10. A decision engine for choosing the stack

Use this every time you begin a new interaction or website.

For an interactive cinematic 3D hero, the selector suggests Three.js + React Three Fiber as the preferred foundation, supported by GSAP + Drei + Blender, with Spline as an alternative for faster visual production, because the visual depends on real-time 3D geometry, lighting and camera control.

This selector gives an initial architecture, not a final dependency list. Before implementation, verify the interaction requirements, chosen framework and supported library versions.

## 11. Performance standards for a world-class website

A website should not sacrifice usability to achieve beautiful effects.

Google's Core Web Vitals establish these targets at the 75th percentile of real visits:


web.dev



LCP · Loading

# ≤2.5s

Largest Contentful Paint

INP · Interaction

# ≤200ms

Interaction to Next Paint

CLS · Stability

# ≤0.1

Cumulative Layout Shift

For creative experiences, also establish frame-rate and responsiveness goals. Aim for 60 FPS on your target devices where appropriate, but measure real frame times rather than assuming that any particular library guarantees that result.

Every production implementation should pass these checks:

- Preserve readable, accessible HTML for meaningful content, and support keyboard navigation and reduced-motion preferences.
- Avoid loading unnecessary 3D engines and assets before they are needed.
- Compress textures, optimise geometry, reuse GPU resources and minimise draw calls.
- Reduce rendering resolution or effects quality on constrained devices; pause rendering when nothing changes.
- Clean up unused geometries, materials, textures and event listeners.
- Test mobile hardware, Safari, touch input, browser resizing and long browsing sessions.

React Three Fiber provides strategies for on-demand rendering, instancing and adaptive performance. Three.js also explicitly requires manual GPU resource disposal for many objects.


React Three Fiber


## 12. How I would organise the entire system

Don't install every technology globally and force Claude to consider all of them on every task.

Instead, create three levels of access.

| Level                | Technologies                                                       | Policy                                            |
| -------------------- | ------------------------------------------------------------------ | ------------------------------------------------- |
| Core                 | HTML, CSS, SVG, TypeScript, Astro/React, GSAP                      | Default knowledge and preferred foundations       |
| Creative specialists | Three.js, R3F, OGL, Rive, PixiJS, GLSL, Blender                    | Activate when the creative brief requires them    |
| Advanced specialists | WebGPU, Rapier, Theatre.js, PlayCanvas, Babylon.js, D3, Scroll Rig | Load only for the corresponding technical problem |

For actual website development, establish a repeatable selection process:

1. Understand the concept. Define the interaction and visual outcome before selecting libraries.
2. Research references. Identify what makes the reference exceptional: composition, animation, depth, shader technique or storytelling.
3. Propose alternatives. Generate at least two viable implementation approaches when the decision is consequential.
4. Prototype the hardest interaction first. Don't develop an entire website around an unproven GPU effect.
5. Art-direct the prototype. Compare visual quality, originality, timing and interaction behaviour.
6. Test on target devices. Measure performance, accessibility and content usability before expanding production.
7. Record the decision. Store the selected stack, rejected alternatives, trade-offs and reusable implementation patterns in the Creative OS.

## 13. Give Claude Code an explicit technology-selection policy

This can become a project-level instruction rather than a one-time prompt.

```

# Creative Technology Selection Policy

ROLE
Act as a senior creative technologist, interactive art director,
graphics engineer, and frontend architect.

OBJECTIVE
Select the simplest technical approach that can faithfully deliver
an exceptional creative result.

SELECTION RULES
1. Start with the visual concept, interaction model, and constraints.
2. Prefer native HTML/CSS/SVG before adding JavaScript animation.
3. Use GSAP for tightly directed timelines and scroll choreography.
4. Use Motion for state-driven React layout and gesture animations.
5. Use Rive for reusable interactive vector and identity assets.
6. Use OGL for focused custom WebGL and shader-driven effects.
7. Use PixiJS for high-volume interactive 2D graphics.
8. Use Three.js for custom real-time 3D environments and objects.
9. Use R3F when Three.js belongs in an existing React architecture.
10. Consider model-viewer or Spline before custom-building simple 3D.
11. Consider Babylon.js or PlayCanvas for game-like 3D applications.
12. Use WebGPU only when advanced rendering or compute justifies it.
13. Never add Lenis, physics, post-processing, or another specialist
    dependency without an explicit reason.

BEFORE IMPLEMENTATION
Provide:
- Desired visual and interaction outcome
- Preferred implementation and why
- Two alternatives with trade-offs
- Required and optional dependencies
- Compatibility and maintenance risks
- Mobile, performance, and accessibility strategy
- A testable prototype plan

EXECUTION
Prototype the riskiest interaction before full-site development.
Review both technical correctness and art-direction quality.
Do not mistake a functioning implementation for an exceptional design.

QUALITY GATE
Evaluate typography, composition, pacing, interaction feel,
mobile behaviour, runtime performance, accessibility, and originality.

LEARNING
Record successful techniques, failed experiments, reusable patterns,
and important technical decisions for future projects.

```

## 14. The learning and reference library I'd prioritise

| Resource                                                                                   | What to learn from it                                            |
| ------------------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| [Three.js Journey](https://threejs-journey.com/)                    | Three.js fundamentals, shaders, physics and advanced 3D concepts |
| [Three.js Examples](https://threejs.org/examples/)                  | Working rendering and interaction techniques                     |
| [OGL Examples](https://oframe.github.io/ogl/examples/)              | Low-level WebGL and shader experimentation                       |
| [GSAP Resources](https://gsap.com/resources/)                       | Choreography, ScrollTrigger and animation architecture           |
| [Codrops](https://tympanus.net/codrops/)                            | Creative coding tutorials and experimental interaction research  |
| [Theatre.js](https://www.theatrejs.com/)                            | Visual sequencing and art-directed animation                     |
| [React Three Fiber](https://r3f.docs.pmnd.rs/)                      | Component architecture and production 3D                         |
| [14islands Scroll Rig](https://github.com/14islands/r3f-scroll-rig) | Integrating traditional HTML and WebGL                           |
| [Rive](https://rive.app/)                                           | Interactive identity, state machines and motion systems          |
| [web.dev](https://web.dev/)                                         | Performance engineering and Core Web Vitals                      |

My priority order for the studio would be GSAP → creative CSS/SVG → shaders/OGL → Three.js/R3F → Rive → advanced rendering and simulation. This is an order of organisational learning, not a ranking of artistic importance.

The most valuable next step is to build a library of small, deeply analysed reference implementations: one excellent typography interaction, one shader transition, one scroll narrative, one interactive 3D scene and one generative identity. Each should be studied, recreated, criticised, improved and documented.

That gives the studio something much more useful than a directory of tools: a continually improving repertoire of proven creative techniques.
