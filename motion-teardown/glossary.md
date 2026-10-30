---
title: "Glossary"
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-31
review_every_days: 180
---

# Glossary

Terms used across the playbook and the tracks, in alphabetical order. Numbers quoted for oryzo.ai (by [Lusion](https://oryzo.ai)) were measured on the live page or read in its shipped code during our study. Where a term has a lab, it is linked.

**`.buf`.** The custom binary container the original uses for models and baked animation clips, in place of glTF. We describe the idea and publish none of its details. See [custom binary models](tracks/dev/deep-dives/custom-binary-models.md).

**Acceptance.** The part of a brief or spec that says how to prove the work is done, as commands, files and screenshots rather than adjectives. See [directing agents](tracks/ai-builder/directing-agents.md).

**Animation ratio.** A 0 to 1 number that says how far along a baked animation is, computed from scroll. On oryzo.ai the coaster and camera used `fit(r, 0, 5.5)`, so the ratio ran across the first 4,950 px of scroll at 1440×900. The hand began to pose at a ratio of about 0.617 (3,056 px).

**Anti-aliasing pass (FXAA, SMAA).** Smoothing of jagged edges done as a post pass, because the renderer's own anti-aliasing is off. The original sets `antialias: false` and runs one of these passes instead.

**Baked animation.** A motion recorded once, offline, as one pose per frame, and played back by looking up a frame. Scrubbing backwards is free. See [L2](tracks/dev/lab-l2-fixed-stage.md).

**Band (hover band).** A horizontal slice of the screen's height. Each finger of the original's hand responds to the pointer's height through one of four bands, with a spring. No raycasting is involved. See [L3](tracks/dev/lab-l3-character-and-post.md).

**Bloom.** A glow around bright areas, made by keeping the bright pixels, blurring them at several widths and adding the result back. The original used five levels with blur sigmas of 3, 5, 7, 9 and 11.

**Brief.** The written instruction given to an agent: Objective, Context, Files, Constraints, Implementation, Acceptance, Output. See [directing agents](tracks/ai-builder/directing-agents.md).

**Bundle.** The single JavaScript file (or a few) a site ships. oryzo.ai's was 1,097,812 bytes raw with no source maps. See [reading a minified bundle](tracks/dev/deep-dives/reading-a-minified-bundle.md).

**CLS (cumulative layout shift).** A web-vitals measure of unexpected layout movement. The original measured 0.

**Contract (file).** A typed interface shared by agents, written once from the spec's exact text and never edited. In our rebuild it carried the per-frame state from the DOM layer to the GL layer. See [stage 5](playbook/05-spec.md).

**Corrections table.** The table in the reconcile report: earlier claim, corrected claim, evidence. See [stage 4](playbook/04-reconcile.md).

**Dither.** A tiny amount of noise added in the last pass so smooth gradients do not show bands. Re-seed it each frame.

**DPR (device pixel ratio) and DPR cap.** The ratio of device pixels to CSS pixels. Rendering at DPR 3 costs nine times the pixels of DPR 1. A cap limits the ratio the renderer uses: the original used `min(1.5, devicePixelRatio)`, and so did our rebuild. See [L3](tracks/dev/lab-l3-character-and-post.md).

**Draw call.** One request from the CPU to the GPU to draw something. The capture hook in the [deep dive](tracks/dev/deep-dives/capturing-scenes-and-shaders.md) counts them.

**Edge glow.** A coloured glow around the edge of the viewport, made in a full-screen post pass. On oryzo.ai it follows scroll, not hover: it switches on between 4,950 and 5,400 px, off between 6,750 and 7,200 px, and pulses every 2 seconds.

**Effect inventory.** The table of every effect in scope, with hypothesis, evidence and status. See the [worksheet](worksheets/byo-site.md).

**Evidence order.** When sources disagree: code > measured data > video. See [the playbook](playbook/README.md).

**Evidence tags.** `[code]` (read from the shipped code), `[measured]` (read from the live page), `[inferred]` (reasoned; say what would confirm it).

**`fit()`.** The function every effect is built from: it maps a number from one range to another, clamped and eased. `fit(x, a, b, c, d, ease)`. See [L1](tracks/dev/lab-l1-scroll-is-a-number.md).

**Frosted card.** A blurred, tinted panel behind text. On oryzo.ai it is a post pass in the renderer, not CSS `backdrop-filter`.

**Gobo.** A stencil placed in front of a light to shape the shadow it casts. In a render, a greyscale texture that fakes dappled light, such as leaf shadows. Our image agent made two 512×512 ones.

**GPU skinning.** Deforming a mesh by its bones on the graphics card. The original's hand has 36 bones; bone data goes to the shader in textures. See [L3](tracks/dev/lab-l3-character-and-post.md).

**Height map.** A greyscale image where brightness stands for height; used to fake relief or relighting. For each prop we derived one from its alpha channel.

**LCP (largest contentful paint).** A web-vitals measure of when the main content appears. 6.5 to 7.2 s on oryzo.ai, because the preloader gates it.

**Ledger.** A file an agent appends to after each milestone, so a crash loses nothing. See [routing and fallbacks](tracks/ai-builder/routing-and-fallbacks.md).

**LUT (lookup table).** A small image used by a shader to map one value to another, such as the SMAA lookup tables or a colour grade.

**Mask (rounded-rectangle).** A signed-distance shape used to restrict an effect to a region. Our blur is masked to the text block's rectangle. See [L2](tracks/dev/lab-l2-fixed-stage.md).

**Mirror (local asset mirror).** A private copy of a site's in-scope files, served locally during capture, so that one blocked or hanging third-party request cannot stall the page. Git-ignored and never published. See [stage 2](playbook/02-map.md).

**MRT (multiple render targets).** Drawing to several textures in one pass. The original draws colour and velocity at once.

**MSDF (multi-channel signed distance field).** A texture format for sharp, scalable text in 3D. The original uses an Inter MSDF for 3D text.

**Post pass / post chain.** A full-screen draw that reads the rendered picture and writes a new one (blur, glow, grade). The chain is their order. The original's: anti-aliasing, glow, bloom, final grade, card blur. See [L3](tracks/dev/lab-l3-character-and-post.md).

**Preloader.** The screen shown while a site loads. On oryzo.ai, finishing requires loaded weight to exactly equal total weight, and a failed file is never handled. See [the resilient loader](tracks/dev/deep-dives/resilient-loader.md).

**Prop sprite.** A 2D image of an object placed on a 2D layered scene. The hero desk on oryzo.ai is a base photo plus seven prop sprites, a 2.5D composite rather than a 3D scene.

**`r` (section progress).** One number per section: `r = 1 + (scrollY − sectionTop) / viewportHeight`. Every effect in the section is a `fit()` of it. See [L1](tracks/dev/lab-l1-scroll-is-a-number.md).

**Reconcile.** The stage where conflicting findings are resolved by evidence and written into one report. See [stage 4](playbook/04-reconcile.md).

**Reduced motion.** The `prefers-reduced-motion` setting. A page should honour it by removing blur, slides and idle motion.

**Render target.** A texture you draw into instead of the screen. The basis of every post pass. See [L2](tracks/dev/lab-l2-fixed-stage.md).

**Resume note.** The opening block of a replacement agent's brief: what is done and must not be redone, and what is not done. See [routing and fallbacks](tracks/ai-builder/routing-and-fallbacks.md).

**Scripted scroll.** Moving a page with `window.scrollTo(0, y)` from a test script instead of wheel events, then waiting two animation frames. Reproducible, and it works when an app cancels native wheel input but mirrors the page's scroll position. See [stage 2](playbook/02-map.md).

**Scrub.** To drive an animation directly from a position (here, scroll) so that it plays forwards and backwards with the position. An effect is **scrubbed** if its state is a function of scroll, **triggered** if it plays on a clock after a threshold. On oryzo.ai the effects in scope were scrubbed.

**Second-order dynamics (spring).** A small simulation that chases a target with a chosen response, damping and anticipation. Used for the hand's fingers. See [L3](tracks/dev/lab-l3-character-and-post.md).

**Shader / uniform.** A shader is a small program that runs on the GPU. A uniform is a value the CPU hands to it each frame, such as an amount that comes from scroll.

**Source map.** A file that maps shipped code back to the original source. oryzo.ai ships none, which is why we pretty-printed the bundle instead.

**SplitText.** A GSAP plugin that splits text into lines, words and characters for animation. The only third-party animation code in oryzo.ai's bundle (version 3.14.2).

**Stagger window.** Each item in a group gets its own slice of the group's progress, starting a little later than the one before. On the live site, items start at about 0.3 times their normalised index, in a window 0.4 to 0.6 wide. See [L1](tracks/dev/lab-l1-scroll-is-a-number.md).

**Tone mapping.** Compressing bright scene values into the range a screen can show. The original turns it off in the renderer and grades in its final shader.

**Triggered.** See *Scrub*.

**Vignette.** Darkening toward the corners of the frame, done in the final grade.

**Virtual scroll.** A scroll model run in JavaScript: it takes input, smooths it, and moves the page itself. The original's drives the real `window.scrollTo`, and cancels native wheel scrolling. See [L1](tracks/dev/lab-l1-scroll-is-a-number.md).
