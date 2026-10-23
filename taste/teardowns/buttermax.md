---
title: "Buttermax — studio teardown"
type: research
status: reference
owner: founder
last_reviewed: 2026-10-23
review_every_days: 180
sources:
  - title: "Buttermax — original website"
    url: https://buttermax.net/
    accessed: 2026-10-20
---
# Buttermax — studio teardown

**Scope:** a consolidated studio study of the captured desktop and mobile experience, visual system, motion, engineering and visitor journey. The source capture was made on 2026-10-20; this is a dated reference, not a current-site audit. See the [original site](https://buttermax.net/).

## Visual system

A tightly controlled butter-yellow and black field lets scale and position do most of the hierarchy work. Oversized display typography, compact labels and a hand-drawn wordmark create a recognisable voice. Portfolio projects appear as crafted physical devices, giving the grid a family resemblance while each object's silhouette signals a different project. The 3D objects, ink-like pointer response and fluid transitions all support the same material metaphor. The capture also found long uppercase copy and some project colour combinations that weakened readability.

## Motion and animation

The opening sequences a branded loader, a halftone reveal, the wordmark and a featured device, with overlapping phases that resolve to a still, readable page. Afterward, autonomous content changes are sparse; pointer and scroll input drive most of the remaining movement. A fluid cursor trail, velocity-sensitive frame treatment and project transitions extend the material idea. The captured experience did not honour reduced-motion preferences, so its motion language is instructive only when considered alongside a reduced-motion alternative.

## Technical approach

The captured build used a Next.js and React shell with a custom WebGL rendering framework. DOM layout supplied text and geometry that a fixed WebGL canvas rendered; a shared state bus connected React interactions with the renderer. The page used Lenis for smoothed scrolling, GSAP and Framer Motion for some UI transitions, and custom shaders for devices, fluid effects and transitions. A capability policy and GPU-tiering logic were present, but the capture also exposed fragile behaviour for unsupported WebGL and an empty server-rendered app shell. The implementation is tightly integrated and expensive to reproduce; the transferable lesson is to define fallback, semantic and performance requirements before committing to a canvas-led page.

## Visitor journey

The loader and signature reveal establish the brand before the hero device introduces selected work. A project grid uses distinct object forms as a scan aid, then case pages expand into each project's identity. Navigation remains available, with direct routes to studio information and contact. The experience makes the portfolio itself feel like a designed collection; however, the initial loader, long display-copy wraps and reliance on WebGL can make access slower or less robust.

## What to learn

- Derive colour, typography, objects and interaction from one ownable identity idea.
- Give portfolio items distinct silhouettes so the collection can be scanned before reading labels.
- Use a small number of meaningful transitions, then let the page settle.
- Treat the DOM as the source of semantic content and layout, even when canvas carries the visual layer.
- Plan readable copy, keyboard access, reduced motion, server output and no-WebGL behaviour as part of the visual system.

## What not to copy

Do not reuse the yellow-and-black identity, emblem, hand motif, device models, fluid effects, page structure or transition choreography. Do not let a loader, canvas or visual metaphor hide content, block navigation or substitute for accessible HTML. Translate the principle of an ownable material world into a different concept and formal language.
