---
title: Audit
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: product-design:audit
department: design
sub_department: design-qa
job: ux-audit
role: specialist
trigger: "when auditing product flows or interface usability"
kind: plugin-skill
availability: codex
distribution: manual
source: /Users/hustle/.codex/plugins/cache/openai-curated-remote/product-design/0.1.56/skills/audit/SKILL.md
invoke: "/audit"
pairs_with: [skill:reviewing-interface-quality, skill:accessibility, skill:cognitive-load-conversion]
---
# Audit

Audit is a 3RDWRONG design QA specialist for ux-audit, activated when auditing product flows or interface usability.

## What it does

- Captures and inspects each step of a supplied product flow before writing findings.
- Ties UX, design and accessibility findings to accepted screenshots and observed behaviour.
- Reports capture gaps and what screenshots alone cannot verify.
- Defaults to a concise inline report; a canvas walkthrough follows the user’s stated preference.

## When to use

- when auditing product flows or interface usability. In practice: during experience design or validation, against the named user task and flow.

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
Use product-design:audit for this ux-audit review. Scope: {{surface, phase and decision}}. Inputs/evidence: {{links, files, versions and states}}. Apply only the documented method. Separate Documented, Interpretation, Hypothesis and Unknown where evidence claims are made; mark untested checks explicitly. Return the tool's required output structure with findings, evidence and concrete next actions.
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

- Work with `skill:reviewing-interface-quality`, `skill:accessibility`, `skill:cognitive-load-conversion` at the ux-audit handoff; pass the evidence, unresolved checks and next owner between tools.

## Limits and cautions

- Apply the studio guardrails: no rejected own-identity look (black backgrounds, heavy grotesk, neon; D-0006); motion only when the concept needs it; respect reduced motion and accessibility; keep client data out of the public repository (D-0021).
- Distribution is `manual`; confirm required installation, sign-in, licence and connectivity before relying on it. Availability records instruction/source presence, not authentication or output quality.
- Fetch/manual tools may require installation or sign-in; do not imply they are already connected.
