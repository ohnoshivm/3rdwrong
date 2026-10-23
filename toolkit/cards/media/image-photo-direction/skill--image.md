---
title: Image
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:image
department: media
sub_department: image-photo-direction
job: brand-image-assets
role: specialist
trigger: "Use when the task explicitly calls for this image generation workflow or host."
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.codex/skills/image/SKILL.md
invoke: "Claude Code/Codex skill `image`"
pairs_with: [skill:imagegen]
---
# Image

The studio's specialist for brand-image-assets; activate when Use when the task explicitly calls for this image generation workflow or host

## What it does

- What type of image? (Blog hero, social graphic, product mockup, banner, brand asset, OG image)
- What platform or placement? (Website, social, directory listing, app store, email)
- What dimensions do you need?
- Do you have existing brand assets? (Logo, colors, fonts, style guide)

## When to use

- Use when the task explicitly calls for this image generation workflow or host.

## When not to use

- When the task does not match its documented scope, use the job lead or ask the producer to route it.

## Inputs it needs

- Approved brief, intended audience and output format.
- Source assets and rights/consent status where relevant.
- Relevant production environment and constraints stated by the tool file.

## How to run it

1. Read the source file at `/Users/hustle/.codex/skills/image/SKILL.md` and confirm its prerequisites.
2. Invoke Claude Code/Codex skill `image` in the supported host.
3. Supply only approved inputs; review the result against the brief.

```text
Use Claude Code/Codex skill `image` for the brand-image-assets task. Brief: {{approved brief}}. Inputs: {{source assets and constraints}}. Return only work supported by the tool instructions, state unknowns, and flag anything that needs human review.
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

- Source: `/Users/hustle/.codex/skills/image/SKILL.md`. Verify documented prerequisites and scope before relying on output.
- Distribution and runtime availability are not guaranteed by this card.
- Follow studio rules: maker ≠ checker; motion only when concept-led; honour reduced motion/accessibility; no client data in public repo.
- The studio discloses AI use in its process; AI-generated material in final deliverables requires the client's written consent (D-0023).
- Check rights, likeness and source permissions before use.
- Do not send client data in prompts to third-party services without permission.
