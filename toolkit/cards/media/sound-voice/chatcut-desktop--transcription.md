---
title: Transcription
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: chatcut-desktop:transcription
department: media
sub_department: sound-voice
job: transcription-captions
role: lead
trigger: ""
kind: plugin-skill
availability: both
distribution: fetch
source: /Users/hustle/.codex/plugins/cache/openai-curated-remote/chatcut-desktop/1.10.14/skills/transcription/SKILL.md
invoke: "Claude Code/Codex skill `transcription`"
pairs_with: []
---
# Transcription

The studio's lead tool for transcription-captions: use it for the documented workflow in media production.

## What it does

- 1. Use `browse_assets` to identify the video/audio asset and its transcription state.
- 1. For newly imported local media, complete the `asset-import` workflow first.
- 1. Check `track_progress` with target `transcription`. It returns current status; follow the returned check-back guidance and do not busy-loop.

## When to use

- At the point in a studio engagement when `transcription-captions` is required.
- Use after Design direction and required inputs are agreed; keep the human accountable for creative decisions.

## When not to use

- When the task does not match its documented scope, use the job lead or ask the producer to route it.

## Inputs it needs

- Approved brief, intended audience and output format.
- Source assets and rights/consent status where relevant.
- Relevant production environment and constraints stated by the tool file.

## How to run it

1. Read the source file at `/Users/hustle/.codex/plugins/cache/openai-curated-remote/chatcut-desktop/1.10.14/skills/transcription/SKILL.md` and confirm its prerequisites.
2. Invoke Claude Code/Codex skill `transcription` in the supported host.
3. Supply only approved inputs; review the result against the brief.

```text
Use Claude Code/Codex skill `transcription` for the transcription-captions task. Brief: {{approved brief}}. Inputs: {{source assets and constraints}}. Return only work supported by the tool instructions, state unknowns, and flag anything that needs human review.
```

## What good output looks like

- Output addresses the supplied brief and requested format.
- Unsupported claims, missing inputs and unresolved rights are identified.

## Quality checks

- [ ] Reviewer other than the maker checks the result against the brief.
- [ ] Claims and provenance are traceable; unknowns are explicit.
- [ ] Accessibility, rights and delivery requirements are checked where applicable.

## Pairs with

- No same-job pair recorded in the registry; use the department lead for hand-off.

## Limits and cautions

- Source: `/Users/hustle/.codex/plugins/cache/openai-curated-remote/chatcut-desktop/1.10.14/skills/transcription/SKILL.md`. Verify documented prerequisites and scope before relying on output.
- Fetch/manual distribution may require installation or sign-in.
- Follow studio rules: maker ≠ checker; motion only when concept-led; honour reduced motion/accessibility; no client data in public repo.
