---
title: Testing Web Applications
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:testing-webapps
department: engineering
sub_department: engineering-qa-security
job: test-engineering
role: specialist
trigger: "a local web app specifically needs native Python Playwright test scripts or a local test server workflow."
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.config/opencode/skills/testing-webapps/SKILL.md
invoke: "testing-webapps skill"
pairs_with: [engineering:testing-strategy, skill:playwright-cli]
---
# Testing Web Applications

The studio's specialist tool for test engineering: Use when testing local web applications using Playwright.

## What it does

- Provides a Playwright workflow for local web application testing.
- Chooses an approach with a decision tree and reconnaissance before action.
- Uses server lifecycle helpers and recommends closing the browser.

## When to use

- a local web app specifically needs native Python Playwright test scripts or a local test server workflow.

## When not to use

- Do not use if app server or test prerequisites cannot run.
- Do not claim coverage beyond the exercised flow.

## Inputs it needs

- Architecture, critical flows, expected behaviour, test stack and execution constraints.

## How to run it

1. Confirm the tool is available in the configured Claude Code or Codex environment.
2. Provide the scope, evidence and decision requested; keep client material in an approved private workspace.
3. Review the result against the checks below; a human retains release and approval decisions.

```text
Use testing-webapps skill. Task: {describe the scoped test engineering need}. Context: {repository or artefact and constraints}. Evidence: {files, links and runtime evidence}. Return findings with evidence, scope, unknowns and practical next steps; do not claim checks you did not perform.
```

## What good output looks like

- Test choices map to risk and critical behaviour.
- Uncovered paths and execution limits are explicit.

## Quality checks

- [ ] Critical and failure paths are considered.
- [ ] Test layers are proportionate.
- [ ] Execution evidence is distinguished from plans.

## Pairs with

- `engineering:testing-strategy`, `skill:playwright-cli`. Use the lead to frame the work and an independent reviewer for consequential output.

## Limits and cautions

- Maker ≠ checker: an independent reviewer checks material findings; tool output does not approve client work.
- Label observations and conclusions as Documented, Interpretation, Hypothesis or Unknown when evidence strength matters.
- Keep client data, personal data and credentials out of the public repository.
- Fetch or manual tools may require installation, sign-in or service access; confirm availability before promising execution.
