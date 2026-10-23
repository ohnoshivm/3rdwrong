---
title: Specialized Focus Music Architect
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:specialized-focus-music-architect
department: media
sub_department: sound-voice
job: music-composition
role: lead
trigger: ""
kind: upstream-agent
availability: claude
distribution: vendor
source: .claude/agents/specialized-focus-music-architect.md
invoke: "Claude Code Agent tool: `specialized-focus-music-architect`"
pairs_with: []
---
# Specialized Focus Music Architect

The studio's lead tool for music-composition: use it for the documented workflow in media production.

## What it does

- **Role**: Architect of instrumental focus music, neuroacoustic soundscapes, and production-grade generative audio prompts (Suno v3.5/v4, Udio, Stable Audio, MusicLM, native Web Audio DSP).
- **Personality**: Acoustically rigorous, scientifically grounded, detail-obsessed, anti-distraction, and deeply appreciative of minimalist musical aesthetics.
- Map the user's immediate workload to the optimal neuroacoustic profile:
- **Deep Analytical & Architecture (Felt Piano / Neo-Classical)**: 58–72 BPM, contemplative, felt-damped strings, no percussion.

## When to use

- At the point in a studio engagement when `music-composition` is required.
- Use after Design direction and required inputs are agreed; keep the human accountable for creative decisions.

## When not to use

- When the task does not match its documented scope, use the job lead or ask the producer to route it.

## Inputs it needs

- Approved brief, intended audience and output format.
- Source assets and rights/consent status where relevant.
- Relevant production environment and constraints stated by the tool file.

## How to run it

1. Read the source file at `.claude/agents/specialized-focus-music-architect.md` and confirm its prerequisites.
2. Invoke Claude Code Agent tool: `specialized-focus-music-architect` in the supported host.
3. Supply only approved inputs; review the result against the brief.

```text
Use Claude Code Agent tool: `specialized-focus-music-architect` for the music-composition task. Brief: {{approved brief}}. Inputs: {{source assets and constraints}}. Return only work supported by the tool instructions, state unknowns, and flag anything that needs human review.
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

- Source: `.claude/agents/specialized-focus-music-architect.md`. Verify documented prerequisites and scope before relying on output.
- Distribution and runtime availability are not guaranteed by this card.
- Follow studio rules: maker ≠ checker; motion only when concept-led; honour reduced motion/accessibility; no client data in public repo.
