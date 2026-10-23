---
title: Audit Reference Originality
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:audit-reference-originality
department: design
sub_department: design-qa
job: originality-audit
role: lead
trigger: ""
kind: skill
availability: both
distribution: fetch
source: /Users/hustle/.agents/skills/audit-reference-originality/SKILL.md
invoke: "/audit-reference-originality"
pairs_with: [skill:3w-category-code-audit, skill:3w-identity-system-critic]
---
# Audit-reference-originality

Audit-reference-originality is a 3RDWRONG design QA tool for originality-audit: lead for originality-audit.

## What it does

- Builds a source registry and inventories current output and history.
- Compares text, brands, numbers, images, assets, video, structure, motion and history.
- Triangulates each red flag with exact current-site and reference evidence.
- Reports originality risk without declaring legal plagiarism or clearing unchecked scope.

## When to use

- Before any route or digital experience leaves the studio, when the actual reference corpus and current output can be inspected.

## When not to use

- Do not use it as legal clearance or a general visual polish review; use `skill:3w-identity-system-critic` for identity concept critique.

## Inputs it needs

- The current site/output and complete reference corpus: URLs, captures, prompts, assets, copy and licences as applicable.
- Project scope, known source history and provenance records; use cleared/non-confidential materials only.

## How to run it

1. Register every supplied reference and identify any missing promised material before judging.
2. Inspect current rendered output and relevant history across the documented categories.
3. Pair each red flag with exact current and reference evidence; separate observation, inference and unknown access.
4. Report originality risks and smallest differentiating fixes; do not make legal conclusions.

```text
Use skill:audit-reference-originality for this originality-audit review. Scope: {{surface, phase and decision}}. Inputs/evidence: {{links, files, versions and states}}. Apply only the documented method. Separate Documented, Interpretation, Hypothesis and Unknown where evidence claims are made; mark untested checks explicitly. Return the tool's required output structure with findings, evidence and concrete next actions.
```

## What good output looks like

- Every red flag cites exact current and reference evidence; common visual grammar is separated from distinctive overlap.
- All relevant categories and history are covered or marked unverified.
- Verdict and proposed fixes do not claim legal plagiarism or clearance beyond checked scope.

## Quality checks

- [ ] Reference registry is complete for the promised scope; missing evidence is recorded.
- [ ] Every red flag cites both current and reference evidence.
- [ ] Similarity is not presented as a legal plagiarism finding.

## Pairs with

- Work with `skill:3w-category-code-audit`, `skill:3w-identity-system-critic` at the originality-audit handoff; pass the evidence, unresolved checks and next owner between tools.

## Limits and cautions

- Similarity is an originality risk, not a legal plagiarism determination. Client data must stay outside the public repository unless cleared and anonymised under D-0021.
- Distribution is `fetch`; confirm required installation, sign-in, licence and connectivity before relying on it. Availability records instruction/source presence, not authentication or output quality.
- Fetch/manual tools may require installation or sign-in; do not imply they are already connected.
