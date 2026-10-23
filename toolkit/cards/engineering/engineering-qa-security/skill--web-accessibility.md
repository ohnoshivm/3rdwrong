---
title: Accessibility (a11y)
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:web-accessibility
department: engineering
sub_department: engineering-qa-security
job: test-engineering
role: specialist
trigger: "Use for engineering/engineering-qa-security/test-engineering when the brief specifically requires: Audit and improve web accessibility following WCAG 2.2 guidelines ."
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.config/opencode/skills/web-accessibility/SKILL.md
invoke: "web-accessibility skill"
pairs_with: [engineering:testing-strategy]
---
# Accessibility (a11y)

The studio's specialist tool for test engineering: Audit and improve web accessibility following WCAG 2.2 guidelines.

## What it does

- Applies WCAG principles and conformance guidance to an interface.
- Uses evidence-led inspection and audit results when available.
- Checks perceivability and interaction requirements.

## When to use

- Use for engineering/engineering-qa-security/test-engineering when the brief specifically requires: Audit and improve web accessibility following WCAG 2.2 guidelines .

## When not to use

- Do not claim conformance from source review alone.
- Automated checks do not constitute a complete accessibility evaluation.

## Inputs it needs

- Architecture, critical flows, expected behaviour, test stack and execution constraints.

## How to run it

1. Confirm the tool is available in the configured Claude Code or Codex environment.
2. Provide the scope, evidence and decision requested; keep client material in an approved private workspace.
3. Review the result against the checks below; a human retains release and approval decisions.

```text
Use web-accessibility skill. Task: {describe the scoped test engineering need}. Context: {repository or artefact and constraints}. Evidence: {files, links and runtime evidence}. Return findings with evidence, scope, unknowns and practical next steps; do not claim checks you did not perform.
```

## What good output looks like

- Test choices map to risk and critical behaviour.
- Uncovered paths and execution limits are explicit.

## Quality checks

- [ ] Critical and failure paths are considered.
- [ ] Test layers are proportionate.
- [ ] Execution evidence is distinguished from plans.

## Pairs with

- `engineering:testing-strategy`. Use the lead to frame the work and an independent reviewer for consequential output.

## Limits and cautions

- Maker ≠ checker: an independent reviewer checks material findings; tool output does not approve client work.
- Label observations and conclusions as Documented, Interpretation, Hypothesis or Unknown when evidence strength matters.
- Keep client data, personal data and credentials out of the public repository.
- Fetch or manual tools may require installation, sign-in or service access; confirm availability before promising execution.
