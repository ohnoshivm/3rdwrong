---
title: Image production
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:3w-image-production
department: media
sub_department: image-photo-direction
job: image-production-workflow
role: lead
trigger: ""
kind: repo-skill
availability: repo
distribution: repo
source: skills/3w-image-production/SKILL.md
invoke: "3w-image-production skill"
pairs_with: [skill:imagegen, anthropic-skills:gpt-image-2-director, skill:3w-image-qa]
---
# Image production

The studio's lead tool for the image production workflow: brief, route, rights and AI consent before making, then selection, export and a rights register. Registered job lead; the skill remains experimental.

## What it does

- Writes an image brief per placement from approved art direction.
- Chooses a route (commission, stock, AI, studio-made) and clears rights, releases and AI consent before production.
- Logs AI prompts, settings, tool and date; logs edits.
- Exports to the web image budget and vendor specifications and fills the rights register.

## When to use

- After art direction approval, when imagery is needed for a deliverable or studio channel.

## When not to use

- Setting art direction — `skill:ceos-art-direction`.
- Release decisions — `skill:3w-image-qa`.
- Any AI material in marks or exclusive elements.

## Inputs it needs

- Approved art direction and placements.
- Client written AI consent where AI may reach finals (D-0023).
- People, places and products with consent status.

## How to run it

1. Collect the inputs; keep client and prospect details in the vault.
2. Run the skill and return its exact output structure.
3. Have someone other than the maker review the result.
4. File the output where the skill says; act on blockers first.

```text
Use the 3w-image-production skill for {{codename}}, set {{set}}. Art direction: {{link}}. Placements: {{list}}. AI consent: {{record | none}}. Return the image production register and open rights questions.
```

## What good output looks like

- Every file has a register row with route, rights, releases, AI use and export spec.
- No route proceeded with an open rights question.

## Quality checks

- [ ] Rights cleared before production.
- [ ] AI use backed by written consent for finals.
- [ ] LCP image within budget.

## Pairs with

- Direction: `skill:ceos-art-direction`, `anthropic-skills:gpt-image-2-director`.
- Generation: `skill:imagegen`.
- Gate: `skill:3w-image-qa`.

## Limits and cautions

- Experimental skill; not legal advice.
- AI-generated material may not be ownable or assignable (IP and licensing guide).
