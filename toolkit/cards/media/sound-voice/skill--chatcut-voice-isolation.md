---
title: Chatcut Voice Isolation
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:chatcut-voice-isolation
department: media
sub_department: sound-voice
job: voice-and-sound
role: specialist
trigger: "Use for an approved voiceover, audio cleanup, music, or speech workflow."
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.agents/skills/chatcut-voice-isolation/SKILL.md
invoke: "Claude Code/Codex skill `chatcut-voice-isolation`"
pairs_with: [chatcut-desktop:voice]
---
# Chatcut Voice Isolation

The studio's specialist for voice-and-sound; activate when Use for an approved voiceover, audio cleanup, music, or speech workflow

## What it does

- User wants cleaner or more isolated spoken voice.
- User complains about hiss, hum, fan/AC noise, or room tone **around speech**.
- User asks to reduce room echo / reverb / reverberation / echoey or distant speech
- A talking-head / interview / voiceover clip needs cleaner speech before export.

## When to use

- Use for an approved voiceover, audio cleanup, music, or speech workflow.

## When not to use

- When the task does not match its documented scope, use the job lead or ask the producer to route it.

## Inputs it needs

- Approved brief, intended audience and output format.
- Source assets and rights/consent status where relevant.
- Relevant production environment and constraints stated by the tool file.

## How to run it

1. Read the source file at `/Users/hustle/.agents/skills/chatcut-voice-isolation/SKILL.md` and confirm its prerequisites.
2. Invoke Claude Code/Codex skill `chatcut-voice-isolation` in the supported host.
3. Supply only approved inputs; review the result against the brief.

```text
Use Claude Code/Codex skill `chatcut-voice-isolation` for the voice-and-sound task. Brief: {{approved brief}}. Inputs: {{source assets and constraints}}. Return only work supported by the tool instructions, state unknowns, and flag anything that needs human review.
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

- Source: `/Users/hustle/.agents/skills/chatcut-voice-isolation/SKILL.md`. Verify documented prerequisites and scope before relying on output.
- Distribution and runtime availability are not guaranteed by this card.
- Follow studio rules: maker ≠ checker; motion only when concept-led; honour reduced motion/accessibility; no client data in public repo.
