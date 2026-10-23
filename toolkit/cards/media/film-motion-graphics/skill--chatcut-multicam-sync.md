---
title: Chatcut Multicam Sync
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:chatcut-multicam-sync
department: media
sub_department: film-motion-graphics
job: video-editing
role: specialist
trigger: "Use for the named production workflow when its format or host matches the brief."
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.agents/skills/chatcut-multicam-sync/SKILL.md
invoke: "Claude Code/Codex skill `chatcut-multicam-sync`"
pairs_with: [chatcut-desktop:chatcut-plugin-basics]
---
# Chatcut Multicam Sync

The studio's specialist for video-editing; activate when Use for the named production workflow when its format or host matches the brief

## What it does

- Parts 1–3 always run: they produce the synced master, a verifiable fact that every
- later edit is rebuilt from. Part 4 cuts a draft from it by default; skip it only for an explicit sync-only request.
- Transcripts do almost all of the work. AI locates; arithmetic decides frames.

## When to use

- Use for the named production workflow when its format or host matches the brief.

## When not to use

- When the task does not match its documented scope, use the job lead or ask the producer to route it.

## Inputs it needs

- Approved brief, intended audience and output format.
- Source assets and rights/consent status where relevant.
- Relevant production environment and constraints stated by the tool file.

## How to run it

1. Read the source file at `/Users/hustle/.agents/skills/chatcut-multicam-sync/SKILL.md` and confirm its prerequisites.
2. Invoke Claude Code/Codex skill `chatcut-multicam-sync` in the supported host.
3. Supply only approved inputs; review the result against the brief.

```text
Use Claude Code/Codex skill `chatcut-multicam-sync` for the video-editing task. Brief: {{approved brief}}. Inputs: {{source assets and constraints}}. Return only work supported by the tool instructions, state unknowns, and flag anything that needs human review.
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

- Source: `/Users/hustle/.agents/skills/chatcut-multicam-sync/SKILL.md`. Verify documented prerequisites and scope before relying on output.
- Distribution and runtime availability are not guaranteed by this card.
- Follow studio rules: maker ≠ checker; motion only when concept-led; honour reduced motion/accessibility; no client data in public repo.
