---
title: Chatcut Transcription
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:chatcut-transcription
department: media
sub_department: sound-voice
job: transcription-captions
role: specialist
trigger: "Use for transcript-driven captions or speech cleanup."
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.agents/skills/chatcut-transcription/SKILL.md
invoke: "Claude Code/Codex skill `chatcut-transcription`"
pairs_with: [chatcut-desktop:transcription]
---
# Chatcut Transcription

The studio's specialist for transcription-captions; activate when Use for transcript-driven captions or speech cleanup

## What it does

- track_progress` with `target: "transcription"` for status/wait.
- find_transcript` for query-based transcript lookup.
- read_captions` and `edit_captions` for caption display edits.
- manage_transcript` action `fix` for source transcript repair.

## When to use

- Use for transcript-driven captions or speech cleanup.

## When not to use

- When the task does not match its documented scope, use the job lead or ask the producer to route it.

## Inputs it needs

- Approved brief, intended audience and output format.
- Source assets and rights/consent status where relevant.
- Relevant production environment and constraints stated by the tool file.

## How to run it

1. Read the source file at `/Users/hustle/.agents/skills/chatcut-transcription/SKILL.md` and confirm its prerequisites.
2. Invoke Claude Code/Codex skill `chatcut-transcription` in the supported host.
3. Supply only approved inputs; review the result against the brief.

```text
Use Claude Code/Codex skill `chatcut-transcription` for the transcription-captions task. Brief: {{approved brief}}. Inputs: {{source assets and constraints}}. Return only work supported by the tool instructions, state unknowns, and flag anything that needs human review.
```

## What good output looks like

- Output addresses the supplied brief and requested format.
- Unsupported claims, missing inputs and unresolved rights are identified.

## Quality checks

- [ ] Reviewer other than the maker checks the result against the brief.
- [ ] Claims and provenance are traceable; unknowns are explicit.
- [ ] Accessibility, rights and delivery requirements are checked where applicable.

## Pairs with

- `chatcut-desktop:transcription`

## Limits and cautions

- Source: `/Users/hustle/.agents/skills/chatcut-transcription/SKILL.md`. Verify documented prerequisites and scope before relying on output.
- Distribution and runtime availability are not guaranteed by this card.
- Follow studio rules: maker ≠ checker; motion only when concept-led; honour reduced motion/accessibility; no client data in public repo.
