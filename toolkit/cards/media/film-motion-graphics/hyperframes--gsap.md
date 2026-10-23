---
title: Gsap
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: hyperframes:gsap
department: media
sub_department: film-motion-graphics
job: video-effects
role: specialist
trigger: "Use when the video needs custom effects or transitions."
kind: plugin-skill
availability: both
distribution: vendor
source: toolkit/vendor/plugin-openai-curated-remote-hyperframes-0.1.2/skills/gsap
invoke: "Claude Code/Codex skill `gsap`"
pairs_with: [chatcut-desktop:shader-gen]
---
# Gsap

The studio's specialist for video-effects; activate when Use when the video needs custom effects or transitions

## What it does

- **gsap.to(targets, vars)** — animate from current state to `vars`. Most common.
- **gsap.from(targets, vars)** — animate from `vars` to current state (entrances).
- **gsap.fromTo(targets, fromVars, toVars)** — explicit start and end.
- **gsap.set(targets, vars)** — apply immediately (duration 0).

## When to use

- Use when the video needs custom effects or transitions.

## When not to use

- When the task does not match its documented scope, use the job lead or ask the producer to route it.

## Inputs it needs

- Approved brief, intended audience and output format.
- Source assets and rights/consent status where relevant.
- Relevant production environment and constraints stated by the tool file.

## How to run it

1. Read the source file at `toolkit/vendor/plugin-openai-curated-remote-hyperframes-0.1.2/skills/gsap` and confirm its prerequisites.
2. Invoke Claude Code/Codex skill `gsap` in the supported host.
3. Supply only approved inputs; review the result against the brief.

```text
Use Claude Code/Codex skill `gsap` for the video-effects task. Brief: {{approved brief}}. Inputs: {{source assets and constraints}}. Return only work supported by the tool instructions, state unknowns, and flag anything that needs human review.
```

## What good output looks like

- Output addresses the supplied brief and requested format.
- Unsupported claims, missing inputs and unresolved rights are identified.

## Quality checks

- [ ] Reviewer other than the maker checks the result against the brief.
- [ ] Claims and provenance are traceable; unknowns are explicit.
- [ ] Accessibility, rights and delivery requirements are checked where applicable.

## Pairs with

- `chatcut-desktop:shader-gen`

## Limits and cautions

- Source: `toolkit/vendor/plugin-openai-curated-remote-hyperframes-0.1.2/skills/gsap`. Verify documented prerequisites and scope before relying on output.
- Distribution and runtime availability are not guaranteed by this card.
- Follow studio rules: maker ≠ checker; motion only when concept-led; honour reduced motion/accessibility; no client data in public repo.
