---
title: Heygen Workflows
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: heygen:heygen-workflows
department: media
sub_department: film-motion-graphics
job: brand-film
role: specialist
trigger: "Use when an approved deliverable requires a synthetic presenter or avatar."
kind: plugin-skill
availability: both
distribution: manual
source: /Users/hustle/.codex/plugins/cache/openai-curated-remote/heygen/4.1.0/skills/heygen-workflows/SKILL.md
invoke: "Claude Code/Codex skill `heygen-workflows`"
pairs_with: [anthropic-skills:motionmaxxing]
---
# Heygen Workflows

The studio's specialist for brand-film; activate when Use when an approved deliverable requires a synthetic presenter or avatar

## What it does

- description: Use HeyGen for talking-avatar videos, general AI clips with HeyGen Video 1, and video, avatar, voice, translation and media workflows.
- Use the connected server's available tools and current schemas. Never claim a capability that the connection does not expose.

## When to use

- Use when an approved deliverable requires a synthetic presenter or avatar.

## When not to use

- When the task does not match its documented scope, use the job lead or ask the producer to route it.

## Inputs it needs

- Approved brief, intended audience and output format.
- Source assets and rights/consent status where relevant.
- Relevant production environment and constraints stated by the tool file.

## How to run it

1. Read the source file at `/Users/hustle/.codex/plugins/cache/openai-curated-remote/heygen/4.1.0/skills/heygen-workflows/SKILL.md` and confirm its prerequisites.
2. Invoke Claude Code/Codex skill `heygen-workflows` in the supported host.
3. Supply only approved inputs; review the result against the brief.

```text
Use Claude Code/Codex skill `heygen-workflows` for the brand-film task. Brief: {{approved brief}}. Inputs: {{source assets and constraints}}. Return only work supported by the tool instructions, state unknowns, and flag anything that needs human review.
```

## What good output looks like

- Output addresses the supplied brief and requested format.
- Unsupported claims, missing inputs and unresolved rights are identified.

## Quality checks

- [ ] Reviewer other than the maker checks the result against the brief.
- [ ] Claims and provenance are traceable; unknowns are explicit.
- [ ] Accessibility, rights and delivery requirements are checked where applicable.

## Pairs with

- `anthropic-skills:motionmaxxing`

## Limits and cautions

- Source: `/Users/hustle/.codex/plugins/cache/openai-curated-remote/heygen/4.1.0/skills/heygen-workflows/SKILL.md`. Verify documented prerequisites and scope before relying on output.
- Distribution and runtime availability are not guaranteed by this card.
- Follow studio rules: maker ≠ checker; motion only when concept-led; honour reduced motion/accessibility; no client data in public repo.
- Client consent is required for AI-generated material in final deliverables (studio contract default).
- Check rights, likeness and source permissions before use.
- Do not send client data in prompts to third-party services without permission.
