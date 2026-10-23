---
title: Music
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: chatcut-desktop:music
department: media
sub_department: sound-voice
job: voice-and-sound
role: specialist
trigger: "Use for an approved voiceover, audio cleanup, music, or speech workflow."
kind: skill
availability: both
distribution: fetch
source: /Users/hustle/.agents/skills/chatcut-music/SKILL.md
invoke: "Claude Code/Codex skill `music`"
pairs_with: [chatcut-desktop:voice]
---
# Music

The studio's specialist for voice-and-sound; activate when Use for an approved voiceover, audio cleanup, music, or speech workflow

## What it does

- generationType` — `instrumental` (default) for no-vocals BGM, or `song` for
- prompt` — required for instrumental mode and optional music/vocal direction
- lyrics` — required for song mode and invalid for instrumental mode; maximum
- gender` — optional `female` or `male` preference for song mode only;

## When to use

- Use for an approved voiceover, audio cleanup, music, or speech workflow.

## When not to use

- When the task does not match its documented scope, use the job lead or ask the producer to route it.

## Inputs it needs

- Approved brief, intended audience and output format.
- Source assets and rights/consent status where relevant.
- Relevant production environment and constraints stated by the tool file.

## How to run it

1. Read the source file at `/Users/hustle/.agents/skills/chatcut-music/SKILL.md` and confirm its prerequisites.
2. Invoke Claude Code/Codex skill `music` in the supported host.
3. Supply only approved inputs; review the result against the brief.

```text
Use Claude Code/Codex skill `music` for the voice-and-sound task. Brief: {{approved brief}}. Inputs: {{source assets and constraints}}. Return only work supported by the tool instructions, state unknowns, and flag anything that needs human review.
```

## What good output looks like

- Output addresses the supplied brief and requested format.
- Unsupported claims, missing inputs and unresolved rights are identified.

## Quality checks

- [ ] Reviewer other than the maker checks the result against the brief.
- [ ] Claims and provenance are traceable; unknowns are explicit.
- [ ] Accessibility, rights and delivery requirements are checked where applicable.

## Pairs with

- `chatcut-desktop:voice`

## Limits and cautions

- Source: `/Users/hustle/.agents/skills/chatcut-music/SKILL.md`. Verify documented prerequisites and scope before relying on output.
- Fetch/manual distribution may require installation or sign-in.
- Follow studio rules: maker ≠ checker; motion only when concept-led; honour reduced motion/accessibility; no client data in public repo.
