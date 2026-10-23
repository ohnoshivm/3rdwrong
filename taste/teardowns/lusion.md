---
title: "Lusion — studio teardown"
type: research
status: reference
owner: founder
last_reviewed: 2026-10-23
review_every_days: 180
sources:
  - title: "Lusion — original website"
    url: https://lusion.co/
    accessed: 2026-10-20
---
# Lusion — studio teardown

**Scope:** a consolidated studio study of the captured desktop and mobile experience, visual system, motion, engineering and visitor journey. The source capture was made on 2026-10-20; this is a dated reference, not a current-site audit. See the [original site](https://lusion.co/).

## Visual system

The homepage pairs a restrained editorial interface with a changing sequence of highly rendered 3D worlds. A mostly achromatic UI and limited action colour give work imagery room to carry saturation. Large display type, small labels, generous section-scale spacing and repeated registration-like marks create a clean frame. Continuity comes from recurring objects and movement, while scenes can change their material and palette. The measured capture also showed contrast and type-size weaknesses in some sections and at intermediate widths.

## Motion and animation

Motion links the page's DOM layout and 3D scene through a shared scroll position. A short, eased scroll response makes ordinary sections feel direct; selected sections shift into a cinematic, time-based sequence. The hero's pointer response makes the object cluster feel physical, while section entrances, menu cards and route wipes use distinct, staged transitions. Some interaction affordances are subtle, and the captured build did not honour reduced-motion preferences; keyboard focus and scroll control also had observed gaps.

## Technical approach

The capture showed a vanilla JavaScript application using Three.js r158, custom interaction and tween utilities, raw shader materials, a fixed WebGL canvas and DOM content coordinated against the same virtual scroll. Page content remained in readable HTML while project imagery and the visual environment were rendered in WebGL. Route transitions used a 2D canvas overlay. This separation is useful to study as an architecture choice; the captured site did not provide a visitor-facing WebGL fallback, so the rendering dependency created a resilience concern.

## Visitor journey

The first view states the offer before the 3D scene asks for attention. A sequence of selected work then provides proof, followed by longer manifesto and cinematic sections and a practical footer. A persistent header keeps contact and navigation close. The journey's strongest editorial move is to let practical content establish meaning before extended spectacle; its weakest moments reduce direct control and make some interactive rewards difficult to discover.

## What to learn

- Keep the offer legible before the visitor enters an immersive sequence.
- Give interface and imagery separate jobs: a quiet frame can help rich work read clearly.
- Let recurring materials, objects or motion rules connect distinct scenes to one idea.
- Coordinate DOM and canvas from a shared layout clock, and preserve semantic content in the DOM.
- Measure load cost, input latency, contrast, keyboard access and reduced-motion behaviour alongside visual quality.

## What not to copy

Do not reproduce the distinctive 3D objects, visual motifs, exact palette, layout, transitions or interaction sequence. Do not treat long auto-advancing scenes, invisible focus, weak contrast or missing reduced-motion support as acceptable costs of spectacle. Extract an abstract principle and express it through original forms.
