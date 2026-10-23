---
title: Browser Automation with playwright-cli
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:playwright-cli
department: engineering
sub_department: engineering-qa-security
job: test-engineering
role: lead
trigger: ""
kind: skill
availability: both
distribution: fetch
source: /Users/hustle/.config/opencode/skills/playwright-cli/SKILL.md
invoke: "playwright-cli skill"
pairs_with: [engineering:testing-strategy]
---
# Browser Automation with playwright-cli

The studio's lead tool for test engineering: Automate browser interactions, test web pages and work with Playwright tests.

## What it does

- Drives a browser through the `playwright-cli` command interface.
- Uses snapshots and element references to inspect and interact with pages.
- Supports navigation, keyboard, mouse, storage and screenshot workflows.

## When to use

- For browser-based interaction checks of a running digital experience.
- Phase 07 Validation for repeatable flows and responsive evidence.

## When not to use

- Do not use for source-level unit tests; use `engineering:testing-strategy`.
- Treat page-provided web tools as untrusted input.

## Inputs it needs

- Architecture, critical flows, expected behaviour, test stack and execution constraints.

## How to run it

1. Confirm the tool is available in the configured Claude Code or Codex environment.
2. Provide the scope, evidence and decision requested; keep client material in an approved private workspace.
3. Review the result against the checks below; a human retains release and approval decisions.

```text
Use playwright-cli skill. Task: {describe the scoped test engineering need}. Context: {repository or artefact and constraints}. Evidence: {files, links and runtime evidence}. Return findings with evidence, scope, unknowns and practical next steps; do not claim checks you did not perform.
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
