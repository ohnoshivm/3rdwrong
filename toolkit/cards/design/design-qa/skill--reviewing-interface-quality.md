---
title: Reviewing Interface Quality
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:reviewing-interface-quality
department: design
sub_department: design-qa
job: ux-audit
role: lead
trigger: ""
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.config/opencode/skills/reviewing-interface-quality/SKILL.md
invoke: "/reviewing-interface-quality"
pairs_with: [skill:reviewing-interface-quality, skill:accessibility, skill:cognitive-load-conversion]
---
# Reviewing-interface-quality

Reviewing-interface-quality is a 3RDWRONG design QA tool for ux-audit: lead for ux-audit.

## What it does

- Requires rendered evidence at desktop and mobile plus computed values for claims.
- Reviews first impression, system consistency, typography, responsive layout, states, accessibility, motion and performance.
- Reports severity-graded findings with location, cause and concrete replacement.
- Marks visual claims plausible or unverified if the interface cannot be rendered.

## When to use

- As the lead UX/interface-quality review during Phase 07 Validation or before frontend work is declared complete, when a running interface can be rendered.

## When not to use

- Do not use it to certify accessibility or production readiness; use `skill:accessibility` for design-level access risks and `skill:reviewing-interface-quality` for rendered interface quality.

## Inputs it needs

- The named interface or flow, user/task, current design intent and constraints.
- Relevant screenshots, URL, prototype or source artefact; state what evidence is absent.

## How to run it

1. Confirm the exact surface, task, scope and evidence before judging.
2. Apply only the source tool’s relevant method and record concrete observations.
3. Prioritise findings by user consequence and pair each with a usable next action.
4. State evidence gaps and route any specialist checks to the relevant owner.

```text
Use skill:reviewing-interface-quality for this ux-audit review. Scope: {{surface, phase and decision}}. Inputs/evidence: {{links, files, versions and states}}. Apply only the documented method. Separate Documented, Interpretation, Hypothesis and Unknown where evidence claims are made; mark untested checks explicitly. Return the tool's required output structure with findings, evidence and concrete next actions.
```

## What good output looks like

- A real 1440px and 390px render plus computed values support the review.
- Findings name location, cause and concrete replacement; severity reflects user impact.
- Visual or interaction claims without a browser remain unverified.

## Quality checks

- [ ] Reviewer is independent from the maker; scope and artefact version are explicit.
- [ ] Every finding has evidence appropriate to its claim and a concrete fix or next check.
- [ ] Limits, unverified checks and human approval responsibilities are stated.

## Pairs with

- Work with `skill:reviewing-interface-quality`, `skill:accessibility`, `skill:cognitive-load-conversion` at the ux-audit handoff; pass the evidence, unresolved checks and next owner between tools.

## Limits and cautions

- Apply the studio guardrails: no rejected own-identity look (black backgrounds, heavy grotesk, neon; D-0006); motion only when the concept needs it; respect reduced motion and accessibility; keep client data out of the public repository (D-0021).
- Distribution is `manual`; confirm required installation, sign-in, licence and connectivity before relying on it. Availability records instruction/source presence, not authentication or output quality.
- Fetch/manual tools may require installation or sign-in; do not imply they are already connected.
