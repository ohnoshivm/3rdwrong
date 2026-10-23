---
title: Image QA
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:3w-image-qa
department: media
sub_department: image-photo-direction
job: image-quality-check
role: lead
trigger: ""
kind: repo-skill
availability: repo
distribution: repo
source: skills/3w-image-qa/SKILL.md
invoke: "3w-image-qa skill"
pairs_with: [skill:3w-image-production, skill:3w-brand-consistency-qa]
---
# Image QA

The studio's lead tool for image quality checks: the independent rights, likeness, AI-consent, fit, technical and accessibility gate before release. Registered job lead; the skill remains experimental.

## What it does

- Matches every file to a rights record.
- Checks licence scope, model and property releases, and AI disclosure with written client consent.
- Checks D-0021 anonymity for studio uses, brief fit, technical quality, alt text and web weight.
- Records Pass, Fail or Not testable with evidence.

## When to use

- After image production, before handover, launch or publication, and when any image is replaced or received from a third party.

## When not to use

- Making or selecting images.
- Brand-wide guideline audits — `skill:3w-brand-consistency-qa`.
- Legal advice.

## Inputs it needs

- Files at release version.
- Rights register.
- Art direction and briefs.
- AI consent and release scope.

## How to run it

1. Collect the inputs; keep client and prospect details in the vault.
2. Run the skill and return its exact output structure.
3. Have someone other than the maker review the result.
4. File the output where the skill says; act on blockers first.

```text
Use the 3w-image-qa skill on {{set}} v{{version}} for {{release scope}}. You did not make these images. Register: {{link}}. Return the image QA table, blockers and not-testable items.
```

## What good output looks like

- Evidence cited for each Pass.
- Unknown rights or consent shown as blockers.

## Quality checks

- [ ] Checker is not the maker.
- [ ] Releases cover the real use.
- [ ] AI consent written and dated.

## Pairs with

- Upstream: `skill:3w-image-production`.
- Neighbour: `skill:3w-brand-consistency-qa` for guideline conformance.

## Limits and cautions

- Experimental skill; screens evidence only.
- A live image is not exempt.
