---
title: CEOS Creative Direction
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:ceos-creative-direction
department: design
sub_department: direction
job: concept-direction
role: specialist
trigger: "The studio own digital touchpoint needs a concept narrative; the 3w creative-direction method remains the identity gate."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-ohnoshivm-creative-engineering-os-mit/skills/ceos-creative-direction
invoke: "/ceos-creative-direction skill"
pairs_with: [skill:3w-creative-direction, skill:ceos-art-direction, skill:taste-skill]
---

# CEOS Creative Direction

A digital concept specialist that turns a website brief into distinct, original concept narratives. For 3RDWRONG, use this specialist when the registry trigger applies: “The studio own digital touchpoint needs a concept narrative; the 3w creative-direction method remains the identity gate.”

## What it does

- Tests whether the idea comes from a subject-specific fact rather than a shared category style.
- Researches references for principle, mechanism, transfer and never-copy rules.
- Generates three concepts with different form, motion and pacing, then tests each against competitor, screenshot, phone, no-animation and honesty checks.
- Recommends one concept and writes `CONCEPT.md`, stopping for owner approval before large implementation.

## When to use

- The studio own digital touchpoint needs a concept narrative; the 3w creative-direction method remains the identity gate.
- When a website concept feels generic or a brief references a famous site.

## When not to use

- Identity route development or approval; use `skill:3w-creative-direction` as the identity gate.
- Starting a large implementation before the owner approves the concept.

## Inputs it needs

- Brief, audience, one conversion action, real assets and constraints.
- Named benchmarks and client vocabulary.

## How to run it

1. Invoke `/ceos-creative-direction` in Claude Code or Codex.
2. Ask for three materially different website concepts with cited reference principles and never-copy lists.
3. Review and approve a `CONCEPT.md` before large implementation.

```text
Use /ceos-creative-direction skill. Task: {specific decision or output}. Context: {approved strategy, source links, version and constraints}. Return the documented format, label evidence and unknowns, and stop where required inputs or approval are missing.
```

## What good output looks like

- The idea passes a competitor substitution test and works at phone size without animation.
- Reference observations are cited; approval is recorded separately from the recommendation.

## Quality checks

- [ ] The output answers the registry job and, for a specialist, the exact trigger.
- [ ] Every factual claim comes from supplied evidence or the tool’s documented method.
- [ ] An independent reviewer checks the output; the maker does not approve their own work.
- [ ] Accessibility, reduced motion and responsive behaviour are checked where relevant.

## Pairs with

- `skill:3w-creative-direction` — upstream context or hand-off.
- `skill:ceos-art-direction` — downstream review or delivery.
- `skill:taste-skill` — downstream review or delivery.

## Limits and cautions

- Digital website concept work; the studio’s identity gate is still `skill:3w-creative-direction`.
- Do not imitate layouts, objects, copy, shaders, assets or brand signatures.
- Founder approval is required before major implementation.
