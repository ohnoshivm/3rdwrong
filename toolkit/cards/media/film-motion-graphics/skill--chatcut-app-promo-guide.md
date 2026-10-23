---
title: Chatcut App Promo Guide
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:chatcut-app-promo-guide
department: media
sub_department: film-motion-graphics
job: video-editing
role: specialist
trigger: "Use for the named production workflow when its format or host matches the brief."
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.agents/skills/chatcut-app-promo-guide/SKILL.md
invoke: "Claude Code/Codex skill `chatcut-app-promo-guide`"
pairs_with: [chatcut-desktop:chatcut-plugin-basics]
---
# Chatcut App Promo Guide

The studio's specialist for video-editing; activate when Use for the named production workflow when its format or host matches the brief

## What it does

- **Motion Graphics (MG)** - Author segmented editable MG clips, TTS voiceover, background music, and timeline assembly. Best for high information density, text emphasis, and strict brand consistency.
- **Seedance 2.0** - Generate a one-shot AI video, up to 15s, with visuals, voiceover, and music. Best when visual impact matters most, a realistic scene texture is needed, and text requirements are light.
- **A. Product website URL** - The agent uses Firecrawl to extract information and assets automatically.
- **B. User-provided materials** - The agent asks for product information and has the user upload assets.

## When to use

- Use for the named production workflow when its format or host matches the brief.

## When not to use

- When the task does not match its documented scope, use the job lead or ask the producer to route it.

## Inputs it needs

- Approved brief, intended audience and output format.
- Source assets and rights/consent status where relevant.
- Relevant production environment and constraints stated by the tool file.

## How to run it

1. Read the source file at `/Users/hustle/.agents/skills/chatcut-app-promo-guide/SKILL.md` and confirm its prerequisites.
2. Invoke Claude Code/Codex skill `chatcut-app-promo-guide` in the supported host.
3. Supply only approved inputs; review the result against the brief.

```text
Use Claude Code/Codex skill `chatcut-app-promo-guide` for the video-editing task. Brief: {{approved brief}}. Inputs: {{source assets and constraints}}. Return only work supported by the tool instructions, state unknowns, and flag anything that needs human review.
```

## What good output looks like

- Output addresses the supplied brief and requested format.
- Unsupported claims, missing inputs and unresolved rights are identified.

## Quality checks

- [ ] Reviewer other than the maker checks the result against the brief.
- [ ] Claims and provenance are traceable; unknowns are explicit.
- [ ] Accessibility, rights and delivery requirements are checked where applicable.

## Pairs with

- `chatcut-desktop:chatcut-plugin-basics`

## Limits and cautions

- Source: `/Users/hustle/.agents/skills/chatcut-app-promo-guide/SKILL.md`. Verify documented prerequisites and scope before relying on output.
- Distribution and runtime availability are not guaranteed by this card.
- Follow studio rules: maker ≠ checker; motion only when concept-led; honour reduced motion/accessibility; no client data in public repo.
