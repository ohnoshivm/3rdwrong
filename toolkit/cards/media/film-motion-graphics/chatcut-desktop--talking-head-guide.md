---
title: Talking Head Guide
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: chatcut-desktop:talking-head-guide
department: media
sub_department: film-motion-graphics
job: video-editing
role: specialist
trigger: "Use for the named production workflow when its format or host matches the brief."
kind: skill
availability: both
distribution: fetch
source: /Users/hustle/.agents/skills/chatcut-talking-head-guide/SKILL.md
invoke: "Claude Code/Codex skill `talking-head-guide`"
pairs_with: [chatcut-desktop:chatcut-plugin-basics]
---
# Talking Head Guide

The studio's specialist for video-editing; activate when Use for the named production workflow when its format or host matches the brief

## What it does

- **B-roll** (industry term — keep as "B-roll" in any language, do not translate) — cover jump cuts or visualize what's being said
- **Background music** (Chinese product term: **背景音乐**) — set mood and smooth micro-gaps
- **Captions** (Chinese product term: **字幕**) — on-screen text for accessibility
- **AI Voice Isolation** (Chinese product term: **AI 人声隔离**) — clean or isolate spoken human voice with MossFormer2, picture untouched. See the `voice-isolation` skill.

## When to use

- Use for the named production workflow when its format or host matches the brief.

## When not to use

- When the task does not match its documented scope, use the job lead or ask the producer to route it.

## Inputs it needs

- Approved brief, intended audience and output format.
- Source assets and rights/consent status where relevant.
- Relevant production environment and constraints stated by the tool file.

## How to run it

1. Read the source file at `/Users/hustle/.agents/skills/chatcut-talking-head-guide/SKILL.md` and confirm its prerequisites.
2. Invoke Claude Code/Codex skill `talking-head-guide` in the supported host.
3. Supply only approved inputs; review the result against the brief.

```text
Use Claude Code/Codex skill `talking-head-guide` for the video-editing task. Brief: {{approved brief}}. Inputs: {{source assets and constraints}}. Return only work supported by the tool instructions, state unknowns, and flag anything that needs human review.
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

- Source: `/Users/hustle/.agents/skills/chatcut-talking-head-guide/SKILL.md`. Verify documented prerequisites and scope before relying on output.
- Fetch/manual distribution may require installation or sign-in.
- Follow studio rules: maker ≠ checker; motion only when concept-led; honour reduced motion/accessibility; no client data in public repo.
