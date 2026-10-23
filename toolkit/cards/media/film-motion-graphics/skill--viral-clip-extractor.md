---
title: Viral Clip Extractor
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:viral-clip-extractor
department: media
sub_department: film-motion-graphics
job: short-form-editing
role: specialist
trigger: "Use when extracting short-form clip candidates from source video."
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.claude/skills/synced/88e7af4e-a2cf-4b40-8488-91a856697e04_aa2d1473-adba-46ff-9558-93fbf2ea6240/viral-clip-extractor/SKILL.md
invoke: "Claude Code/Codex skill `viral-clip-extractor`"
pairs_with: [agency:marketing-short-video-editing-coach]
---
# Viral Clip Extractor

The studio's specialist for short-form-editing; activate when Use when extracting short-form clip candidates from source video

## What it does

- Retrieve the auto-generated transcript with timestamps from the YouTube video
- If no transcript exists: attempt to reconstruct from video description, comments, or available metadata
- If transcript quality is too poor: return `"Transcript quality insufficient for extraction."
- Minimum 30 seconds, maximum 3 minutes per clip

## When to use

- Use when extracting short-form clip candidates from source video.

## When not to use

- When the task does not match its documented scope, use the job lead or ask the producer to route it.

## Inputs it needs

- Approved brief, intended audience and output format.
- Source assets and rights/consent status where relevant.
- Relevant production environment and constraints stated by the tool file.

## How to run it

1. Read the source file at `/Users/hustle/.claude/skills/synced/88e7af4e-a2cf-4b40-8488-91a856697e04_aa2d1473-adba-46ff-9558-93fbf2ea6240/viral-clip-extractor/SKILL.md` and confirm its prerequisites.
2. Invoke Claude Code/Codex skill `viral-clip-extractor` in the supported host.
3. Supply only approved inputs; review the result against the brief.

```text
Use Claude Code/Codex skill `viral-clip-extractor` for the short-form-editing task. Brief: {{approved brief}}. Inputs: {{source assets and constraints}}. Return only work supported by the tool instructions, state unknowns, and flag anything that needs human review.
```

## What good output looks like

- Output addresses the supplied brief and requested format.
- Unsupported claims, missing inputs and unresolved rights are identified.

## Quality checks

- [ ] Reviewer other than the maker checks the result against the brief.
- [ ] Claims and provenance are traceable; unknowns are explicit.
- [ ] Accessibility, rights and delivery requirements are checked where applicable.

## Pairs with

- `agency:marketing-short-video-editing-coach`

## Limits and cautions

- Source: `/Users/hustle/.claude/skills/synced/88e7af4e-a2cf-4b40-8488-91a856697e04_aa2d1473-adba-46ff-9558-93fbf2ea6240/viral-clip-extractor/SKILL.md`. Verify documented prerequisites and scope before relying on output.
- Distribution and runtime availability are not guaranteed by this card.
- Follow studio rules: maker ≠ checker; motion only when concept-led; honour reduced motion/accessibility; no client data in public repo.
