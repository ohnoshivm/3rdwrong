---
title: test-engineer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agent:code-modernization:test-engineer
department: engineering
sub_department: engineering-qa-security
job: test-engineering
role: specialist
trigger: "Use for engineering/engineering-qa-security/test-engineering when the brief specifically requires: Writes characterization, contract, and equivalence tests that pin down legacy behavior so transformation can be proven correct ."
kind: agent
availability: claude
distribution: vendor
source: toolkit/vendor/plugin-claude-plugins-official-code-modernization-marketplace/agents/test-engineer.md
invoke: "Agent tool: test-engineer"
pairs_with: [engineering:testing-strategy]
---
# test-engineer

The studio's specialist tool for test engineering: Writes characterization, contract, and equivalence tests that pin down legacy behavior so transformation can be proven correct.

## What it does

- Writes characterisation, contract and equivalence tests for legacy behaviour.
- Pins observed behaviour before transformation or refactor.
- Supports proof that a migration preserved the supplied contract.

## When to use

- Use for engineering/engineering-qa-security/test-engineering when the brief specifically requires: Writes characterization, contract, and equivalence tests that pin down legacy behavior so transformation can be proven correct .

## When not to use

- Do not use it to decide product behaviour that has not been observed.
- Do not claim equivalence until tests have run and passed.

## Inputs it needs

- Architecture, critical flows, expected behaviour, test stack and execution constraints.

## How to run it

1. Confirm the tool is available in the configured Claude Code or Codex environment.
2. Provide the scope, evidence and decision requested; keep client material in an approved private workspace.
3. Review the result against the checks below; a human retains release and approval decisions.

```text
Use Agent tool: test-engineer. Task: {describe the scoped test engineering need}. Context: {repository or artefact and constraints}. Evidence: {files, links and runtime evidence}. Return findings with evidence, scope, unknowns and practical next steps; do not claim checks you did not perform.
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
