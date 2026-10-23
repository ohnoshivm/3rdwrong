---
title: Website To Hyperframes
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: hyperframes:website-to-hyperframes
department: media
sub_department: film-motion-graphics
job: programmatic-video
role: specialist
trigger: "Use for the specific Remotion or HyperFrames production task."
kind: plugin-skill
availability: both
distribution: vendor
source: toolkit/vendor/plugin-openai-curated-remote-hyperframes-0.1.2/skills/website-to-hyperframes
invoke: "Claude Code/Codex skill `website-to-hyperframes`"
pairs_with: [remotion:remotion-best-practices]
---
# Website To Hyperframes

The studio's specialist for programmatic-video; activate when Use for the specific Remotion or HyperFrames production task

## What it does

- "Capture https://... and make me a 25-second product launch video"
- "Turn this website into a 15-second social ad for Instagram"
- "Create a 30-second product tour from https://..."
- **Landscape**: 1920x1080 (default)

## When to use

- Use for the specific Remotion or HyperFrames production task.

## When not to use

- When the task does not match its documented scope, use the job lead or ask the producer to route it.

## Inputs it needs

- Approved brief, intended audience and output format.
- Source assets and rights/consent status where relevant.
- Relevant production environment and constraints stated by the tool file.

## How to run it

1. Read the source file at `toolkit/vendor/plugin-openai-curated-remote-hyperframes-0.1.2/skills/website-to-hyperframes` and confirm its prerequisites.
2. Invoke Claude Code/Codex skill `website-to-hyperframes` in the supported host.
3. Supply only approved inputs; review the result against the brief.

```text
Use Claude Code/Codex skill `website-to-hyperframes` for the programmatic-video task. Brief: {{approved brief}}. Inputs: {{source assets and constraints}}. Return only work supported by the tool instructions, state unknowns, and flag anything that needs human review.
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

- Source: `toolkit/vendor/plugin-openai-curated-remote-hyperframes-0.1.2/skills/website-to-hyperframes`. Verify documented prerequisites and scope before relying on output.
- Distribution and runtime availability are not guaranteed by this card.
- Follow studio rules: maker ≠ checker; motion only when concept-led; honour reduced motion/accessibility; no client data in public repo.
