---
title: "Dev track: build the mechanisms yourself"
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
---

# Dev track: build the mechanisms yourself

This track teaches the front-end techniques behind award-level scroll sites, with code you can run. It is for developers who want to understand a mechanism well enough to write it from a blank file, with or without an AI agent.

**Case credit.** The mechanisms are modelled on what we measured and read in oryzo.ai, a site by [Lusion](https://oryzo.ai). The labs use our own TypeScript and GLSL, written fresh for this guide. We do not publish their code, shaders, models or textures, and the labs never need them.

## Start here

1. Read the [level ladder](level-ladder.md): three levels and what each teaches.
2. Do [L1](lab-l1-scroll-is-a-number.md), then [L2](lab-l2-fixed-stage.md), then [L3](lab-l3-character-and-post.md).
3. Read a deep dive when you are ready to study a real site:
   - [Reading a minified bundle](deep-dives/reading-a-minified-bundle.md)
   - [Capturing three.js scenes and shaders](deep-dives/capturing-scenes-and-shaders.md)
   - [Custom binary models](deep-dives/custom-binary-models.md)
   - [The resilient loader](deep-dives/resilient-loader.md)

If you would rather direct agents than write the code, go to the [AI-builder track](../ai-builder/README.md). The two tracks share the same [playbook](../../playbook/README.md).

## What each lab contains

Each lab file has the same parts: a goal, the concepts, the code, exercises, common traps, and a "you're done when" checklist. The checklist is pass or fail.

## Setup

- Node 20 or later.
- A bundler. The labs assume [Vite](https://vite.dev) with TypeScript; any bundler that handles `.ts` will do.
- `three` for L2 and L3 (`npm i three`). We tested against three.js r180.
- A browser with WebGL2.

Each snippet starts with a comment such as `// lab/math.ts`: that is the file name to save it under. Imports between them are relative and match those names.

## How the code was tested

The snippets were extracted from these files and run. The test files are in [`tests/`](tests/README.md), with instructions for running them yourself:

- **Node:** `fit`, the easings, section maths, the scroll model (including frame-rate independence and the 200 px wheel clamp), stagger windows, the baked-clip sampler, bone pose maths, the spring, band weights, the gaussian kernel, frame statistics, the mesh container's round trip and error bound, the resilient loader (success, failure, synchronous throw, a hung item, the total deadline), and the call scanner on a small fixture.
- **TypeScript:** all snippets type-check under `strict` against three.js r180.
- **Headless Chrome with Playwright:**
  - L1's whole page: letters at set scroll positions, reversibility, the wheel path.
  - L2's stage: pixel statistics inside and outside the glass.
  - L3's shaders: skinning against known poses, finger lift, the edge glow, grade, bright-pass and blur, and the three.js wiring.
  - The capture hook against a small three.js page.
- **Not tested:** real-device behaviour on phones, Firefox and Safari, the L3 bloom pyramid as a full chain (its three shaders are tested one by one, the ping-pong plumbing is not), and the `prefers-reduced-motion` branch in a browser. The GPU tests ran in headless Chrome; frame-time targets in the labs are for you to measure on your machine.

## Rules for this track

- Write your own code. Describe measured behaviour (windows, formulas, numbers) in your own words and write your own shader.
- Study for yourself. Do not publish captured models, textures or shader sources from a site you study.
- Credit the work you studied, and say clearly what you measured and what you inferred.
