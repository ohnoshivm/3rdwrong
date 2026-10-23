---
title: Design Review
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:gstack-design-review
department: design
sub_department: design-qa
job: concept-critique
role: specialist
trigger: "When reviewing a visual artifact for hierarchy, generic patterns, consistency, or actionable design defects."
kind: skill
availability: both
distribution: fetch
source: /Users/hustle/creative-engineering-os/library/skills/design-review/SKILL.md
invoke: "Claude Code: /design-review (gstack; skill:gstack-design-review)"
pairs_with: [skill:3w-creative-direction, skill:3w-identity-system-critic, skill:3w-brand-consistency-qa]
---
# Design-review

Design-review is a 3RDWRONG design QA specialist for concept-critique, activated when reviewing a visual artifact for hierarchy, generic patterns, consistency, or actionable design defects.

## What it does

- Reviews a live site for visual inconsistency, spacing, hierarchy, generic patterns and slow interactions.
- Iteratively fixes issues in source code, commits each fix atomically and re-verifies with before/after screenshots.
- Routes plan-stage design review to `/plan-design-review`.

## When to use

- When reviewing a visual artifact for hierarchy, generic patterns, consistency, or actionable design defects. In practice: after a visual change on a live site and before calling the interface done; for a plan-stage review use `/plan-design-review`.

## When not to use

- Do not use it as a read-only independent gate: its workflow fixes source code and commits each fix. Use `agent:creative-auditor` or `agent:visual-qa-engineer` for a read-only independent review. Use `skill:3w-identity-system-critic` for identity-route critique.

## Inputs it needs

- A live site or running URL, target route and local source in the working directory.
- The UI changes and art direction/reference to review, plus permission for the skill’s source-edit and commit workflow.

## How to run it

1. Start the gstack `design-review` workflow and confirm the installation/runtime preamble succeeds.
2. Open the live site, capture before evidence and inspect the visual defects in scope.
3. Apply the workflow’s fixes to source, commit each fix atomically and capture/re-check after evidence.
4. Use `/plan-design-review` for plan-stage work; keep a separate reviewer for its completed changes.

```text
Use `/design-review` (gstack) on {{live route}} after {{UI change}}. Compare against {{art direction/reference}}. Capture before and after screenshots, fix the observed issues in source, commit each fix atomically and report any findings that remain. For a plan rather than a live site, use `/plan-design-review`.
```

## What good output looks like

- Findings point to the live site and are backed by before/after screenshots.
- Fixes are made in source and re-verified; the plan review is routed separately.
- The reviewer’s changes do not count as an independent check of its own work.

## Quality checks

- [ ] Reviewer is independent from the maker; scope and artefact version are explicit.
- [ ] Every finding has evidence appropriate to its claim and a concrete fix or next check.
- [ ] Limits, unverified checks and human approval responsibilities are stated.

## Pairs with

- Work with `skill:3w-creative-direction`, `skill:3w-identity-system-critic`, `skill:3w-brand-consistency-qa` at the concept-critique handoff; pass the evidence, unresolved checks and next owner between tools.

## Limits and cautions

- Registry job `concept-critique` is broader than the source workflow, which is live-interface QA and source editing; use it at the visual QA stage.
- Audience response, preference, memorability and commercial effect remain Unknown without observed research. The reviewer recommends; the founder decides.
- Apply the studio guardrails: no rejected own-identity look (black backgrounds, heavy grotesk, neon; D-0006); motion only when the concept needs it; respect reduced motion and accessibility; keep client data out of the public repository (D-0021).
- Distribution is `fetch`; confirm required installation, sign-in, licence and connectivity before relying on it. Availability records instruction/source presence, not authentication or output quality.
- Fetch/manual tools may require installation or sign-in; do not imply they are already connected.
