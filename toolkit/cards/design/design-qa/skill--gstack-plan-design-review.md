---
title: Plan Design Review
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:gstack-plan-design-review
department: design
sub_department: design-qa
job: concept-critique
role: specialist
trigger: "When a design plan needs scored critique before implementation."
kind: skill
availability: both
distribution: fetch
source: /Users/hustle/.config/opencode/skills/gstack-plan-design-review/SKILL.md
invoke: "/plan-design-review"
pairs_with: [skill:gstack-design-review, skill:3w-identity-system-critic]
---
# Plan-design-review

Plan-design-review is a 3RDWRONG design QA specialist for concept-critique, activated when a design plan needs scored critique before implementation.

## What it does

- Reviews a design plan before implementation, scores design dimensions and improves the plan itself.
- Looks for missing design decisions and adds them to the plan.
- Is for plan-stage review; live-site visual audits use `/design-review`.
- Follows a hard scope gate before the review workflow.

## When to use

- When a design plan needs scored critique before implementation. In practice: before implementation, once the exact design plan is named.

## When not to use

- Do not use it to approve work or replace the founder’s decision; use `skill:3w-creative-direction` to develop routes and `skill:3w-identity-system-critic` for identity critique.

## Inputs it needs

- Approved strategy and criteria (or a draft explicitly marked formative), the named decision, artefact version and representative applications.
- Category evidence and source links when distinctiveness is in scope.

## How to run it

1. State the decision, phase, version and strategy status; inventory what can be inspected.
2. Run only the documented review lenses; mark unavailable evidence Unknown or Not testable.
3. Separate observations from interpretation, prioritise consequential findings and name an owner and next check.
4. Return the tool’s stated verdict/report; keep final route or release approval with the founder.

```text
Use skill:gstack-plan-design-review for this concept-critique review. Scope: {{surface, phase and decision}}. Inputs/evidence: {{links, files, versions and states}}. Apply only the documented method. Separate Documented, Interpretation, Hypothesis and Unknown where evidence claims are made; mark untested checks explicitly. Return the tool's required output structure with findings, evidence and concrete next actions.
```

## What good output looks like

- Findings point to the supplied artefact or state and distinguish observation from interpretation.
- Each recommendation names a concrete next action, owner or retest condition.
- Unknowns and unrun checks remain visible; no result is inferred from a filename, mock-up or claim.

## Quality checks

- [ ] Reviewer is independent from the maker; scope and artefact version are explicit.
- [ ] Every finding has evidence appropriate to its claim and a concrete fix or next check.
- [ ] Limits, unverified checks and human approval responsibilities are stated.

## Pairs with

- Work with `skill:gstack-design-review`, `skill:3w-identity-system-critic` at the concept-critique handoff; pass the evidence, unresolved checks and next owner between tools.

## Limits and cautions

- Audience response, preference, memorability and commercial effect remain Unknown without observed research. The reviewer recommends; the founder decides.
- Apply the studio guardrails: no rejected own-identity look (black backgrounds, heavy grotesk, neon; D-0006); motion only when the concept needs it; respect reduced motion and accessibility; keep client data out of the public repository (D-0021).
- Distribution is `fetch`; confirm required installation, sign-in, licence and connectivity before relying on it. Availability records instruction/source presence, not authentication or output quality.
- Fetch/manual tools may require installation or sign-in; do not imply they are already connected.
