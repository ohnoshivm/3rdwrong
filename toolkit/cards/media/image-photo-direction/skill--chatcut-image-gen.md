---
title: Chatcut Image Gen
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:chatcut-image-gen
department: media
sub_department: image-photo-direction
job: brand-image-assets
role: specialist
trigger: "Use when the task explicitly calls for this image generation workflow or host."
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.agents/skills/chatcut-image-gen/SKILL.md
invoke: "Claude Code/Codex skill `chatcut-image-gen`"
pairs_with: [skill:imagegen]
---
# Chatcut Image Gen

The studio's specialist for brand-image-assets; activate when Use when the task explicitly calls for this image generation workflow or host

## What it does

- gpt-image-2.5-flare` is the default. Honor the image model attached to the user prompt or explicitly requested.
- Use `gpt-image-2.5-sunburst` when the user selects it for precise editing.
- nano-banana` is the reference-heavy choice. Use it when reference-image fidelity matters more than text rendering, or when the user needs more than 10 reference images.
- Image 2.5 Flare / Sunburst → references/gpt-image-2.5.md (upstream reference `references/gpt-image-2.5.md`)

## When to use

- Use when the task explicitly calls for this image generation workflow or host.

## When not to use

- When the task does not match its documented scope, use the job lead or ask the producer to route it.

## Inputs it needs

- Approved brief, intended audience and output format.
- Source assets and rights/consent status where relevant.
- Relevant production environment and constraints stated by the tool file.

## How to run it

1. Read the source file at `/Users/hustle/.agents/skills/chatcut-image-gen/SKILL.md` and confirm its prerequisites.
2. Invoke Claude Code/Codex skill `chatcut-image-gen` in the supported host.
3. Supply only approved inputs; review the result against the brief.

```text
Use Claude Code/Codex skill `chatcut-image-gen` for the brand-image-assets task. Brief: {{approved brief}}. Inputs: {{source assets and constraints}}. Return only work supported by the tool instructions, state unknowns, and flag anything that needs human review.
```

## What good output looks like

- Output addresses the supplied brief and requested format.
- Unsupported claims, missing inputs and unresolved rights are identified.

## Quality checks

- [ ] Reviewer other than the maker checks the result against the brief.
- [ ] Claims and provenance are traceable; unknowns are explicit.
- [ ] Accessibility, rights and delivery requirements are checked where applicable.

## Pairs with

- `skill:imagegen`

## Limits and cautions

- Source: `/Users/hustle/.agents/skills/chatcut-image-gen/SKILL.md`. Verify documented prerequisites and scope before relying on output.
- Distribution and runtime availability are not guaranteed by this card.
- Follow studio rules: maker ≠ checker; motion only when concept-led; honour reduced motion/accessibility; no client data in public repo.
- Client consent is required for AI-generated material in final deliverables (studio contract default).
- Check rights, likeness and source permissions before use.
- Do not send client data in prompts to third-party services without permission.
