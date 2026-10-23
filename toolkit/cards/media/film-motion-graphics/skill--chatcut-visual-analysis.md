---
title: Chatcut Visual Analysis
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:chatcut-visual-analysis
department: media
sub_department: film-motion-graphics
job: media-quality-check
role: specialist
trigger: "Use when validating an edit with timeline structure or rendered-frame evidence."
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.agents/skills/chatcut-visual-analysis/SKILL.md
invoke: "Claude Code/Codex skill `chatcut-visual-analysis`"
pairs_with: [chatcut-desktop:verification]
---
# Chatcut Visual Analysis

The studio's specialist for media-quality-check; activate when Use when validating an edit with timeline structure or rendered-frame evidence

## What it does

- Never describe an asset source timestamp as a timeline timestamp. To relate a placed clip to its source, read that item's timeline start, source-start offset, playback rate, and timeline FPS first.
- sourceFrameCount` for a coarse overview across the original asset.
- sourceTimes` for exact source-media moments after narrowing.
- --output <path>` is required and must end in `.jpg`,`.jpeg`,`.png`, or`.webp`.

## When to use

- Use when validating an edit with timeline structure or rendered-frame evidence.

## When not to use

- When the task does not match its documented scope, use the job lead or ask the producer to route it.

## Inputs it needs

- Approved brief, intended audience and output format.
- Source assets and rights/consent status where relevant.
- Relevant production environment and constraints stated by the tool file.

## How to run it

1. Read the source file at `/Users/hustle/.agents/skills/chatcut-visual-analysis/SKILL.md` and confirm its prerequisites.
2. Invoke Claude Code/Codex skill `chatcut-visual-analysis` in the supported host.
3. Supply only approved inputs; review the result against the brief.

```text
Use Claude Code/Codex skill `chatcut-visual-analysis` for the media-quality-check task. Brief: {{approved brief}}. Inputs: {{source assets and constraints}}. Return only work supported by the tool instructions, state unknowns, and flag anything that needs human review.
```

## What good output looks like

- Output addresses the supplied brief and requested format.
- Unsupported claims, missing inputs and unresolved rights are identified.

## Quality checks

- [ ] Reviewer other than the maker checks the result against the brief.
- [ ] Claims and provenance are traceable; unknowns are explicit.
- [ ] Accessibility, rights and delivery requirements are checked where applicable.

## Pairs with

- `chatcut-desktop:verification`

## Limits and cautions

- Source: `/Users/hustle/.agents/skills/chatcut-visual-analysis/SKILL.md`. Verify documented prerequisites and scope before relying on output.
- Distribution and runtime availability are not guaranteed by this card.
- Follow studio rules: maker ≠ checker; motion only when concept-led; honour reduced motion/accessibility; no client data in public repo.
