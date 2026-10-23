---
title: Hyperframes
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: hyperframes:hyperframes
department: media
sub_department: film-motion-graphics
job: programmatic-video
role: specialist
trigger: "Use for the specific Remotion or HyperFrames production task."
kind: plugin-skill
availability: both
distribution: vendor
source: toolkit/vendor/plugin-openai-curated-remote-hyperframes-0.1.2/skills/hyperframes
invoke: "Claude Code/Codex skill `hyperframes`"
pairs_with: [remotion:remotion-best-practices]
---
# Hyperframes

The studio's specialist for programmatic-video; activate when Use for the specific Remotion or HyperFrames production task

## What it does

- What's the mood? (explosive / cinematic / fluid / technical / chaotic / warm)
- Light or dark canvas?
- Any specific brand colors, fonts, or visual references?

## When to use

- Use for the specific Remotion or HyperFrames production task.

## When not to use

- When the task does not match its documented scope, use the job lead or ask the producer to route it.

## Inputs it needs

- Approved brief, intended audience and output format.
- Source assets and rights/consent status where relevant.
- Relevant production environment and constraints stated by the tool file.

## How to run it

1. Read the source file at `toolkit/vendor/plugin-openai-curated-remote-hyperframes-0.1.2/skills/hyperframes` and confirm its prerequisites.
2. Invoke Claude Code/Codex skill `hyperframes` in the supported host.
3. Supply only approved inputs; review the result against the brief.

```text
Use Claude Code/Codex skill `hyperframes` for the programmatic-video task. Brief: {{approved brief}}. Inputs: {{source assets and constraints}}. Return only work supported by the tool instructions, state unknowns, and flag anything that needs human review.
```

## What good output looks like

- Output addresses the supplied brief and requested format.
- Unsupported claims, missing inputs and unresolved rights are identified.

## Quality checks

- [ ] Reviewer other than the maker checks the result against the brief.
- [ ] Claims and provenance are traceable; unknowns are explicit.
- [ ] Accessibility, rights and delivery requirements are checked where applicable.

## Pairs with

- `remotion:remotion-best-practices`

## Limits and cautions

- Source: `toolkit/vendor/plugin-openai-curated-remote-hyperframes-0.1.2/skills/hyperframes`. Verify documented prerequisites and scope before relying on output.
- Distribution and runtime availability are not guaranteed by this card.
- Follow studio rules: maker ≠ checker; motion only when concept-led; honour reduced motion/accessibility; no client data in public repo.
