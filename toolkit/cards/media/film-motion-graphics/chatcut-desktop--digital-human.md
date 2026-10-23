---
title: Digital Human
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: chatcut-desktop:digital-human
department: media
sub_department: film-motion-graphics
job: brand-film
role: specialist
trigger: "Use when an approved deliverable requires a synthetic presenter or avatar."
kind: skill
availability: both
distribution: fetch
source: /Users/hustle/.agents/skills/chatcut-digital-human/SKILL.md
invoke: "Claude Code/Codex skill `digital-human`"
pairs_with: [anthropic-skills:motionmaxxing]
---
# Digital Human

The studio's specialist for brand-film; activate when Use when an approved deliverable requires a synthetic presenter or avatar

## What it does

- Make an official or saved AI avatar, talking avatar, or virtual presenter speak.
- Turn a consented portrait into a reusable digital-human identity.
- Use a representative still from an imported video as a photo avatar.
- Create a synthetic AI presenter from a description, when live capabilities allow it.

## When to use

- Use when an approved deliverable requires a synthetic presenter or avatar.

## When not to use

- When the task does not match its documented scope, use the job lead or ask the producer to route it.

## Inputs it needs

- Approved brief, intended audience and output format.
- Source assets and rights/consent status where relevant.
- Relevant production environment and constraints stated by the tool file.

## How to run it

1. Read the source file at `/Users/hustle/.agents/skills/chatcut-digital-human/SKILL.md` and confirm its prerequisites.
2. Invoke Claude Code/Codex skill `digital-human` in the supported host.
3. Supply only approved inputs; review the result against the brief.

```text
Use Claude Code/Codex skill `digital-human` for the brand-film task. Brief: {{approved brief}}. Inputs: {{source assets and constraints}}. Return only work supported by the tool instructions, state unknowns, and flag anything that needs human review.
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

- Source: `/Users/hustle/.agents/skills/chatcut-digital-human/SKILL.md`. Verify documented prerequisites and scope before relying on output.
- Fetch/manual distribution may require installation or sign-in.
- Follow studio rules: maker ≠ checker; motion only when concept-led; honour reduced motion/accessibility; no client data in public repo.
- The studio discloses AI use in its process; AI-generated material in final deliverables requires the client's written consent (D-0023).
- Check rights, likeness and source permissions before use.
- Do not send client data in prompts to third-party services without permission.
