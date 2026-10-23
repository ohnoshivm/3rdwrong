---
title: pr-test-analyzer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agent:pr-review-toolkit:pr-test-analyzer
department: engineering
sub_department: engineering-qa-security
job: test-engineering
role: specialist
trigger: "Use for engineering/engineering-qa-security/test-engineering when the brief specifically requires: Use this agent when you need to review a pull request for test coverage quality and completeness ."
kind: agent
availability: claude
distribution: fetch
source: /Users/hustle/.claude/plugins/marketplaces/claude-plugins-official/plugins/pr-review-toolkit/agents/pr-test-analyzer.md
invoke: "Agent tool: pr-test-analyzer"
pairs_with: [engineering:testing-strategy]
---
# pr-test-analyzer

The studio's specialist tool for test engineering: Use this agent when you need to review a pull request for test coverage quality and completeness.

## What it does

- Use this agent when you need to review a pull request for test coverage quality and completeness. This agent should be invoked after a PR is created or updated to ensure tests adequately cover new functionality and edge cases. Typical triggers include the user asking whether tests on a freshly-created PR are thorough, an updated PR adding new logic that needs coverage analysis, and a final pre-merge double-check before marking a PR ready. See "When to invoke" in the agent body for worked scenarios.
- Fresh PR, thoroughness check. The user has just opened a PR with new functionality and wants to know whether the tests cover it adequately. Analyze the diff and report critical gaps.
- PR updated with new logic. A PR has been pushed with new validation, parsing, or business logic. Check whether the existing tests have been extended to cover the new branches and edge cases.
- Pre-ready double-check. Before marking a PR ready for review, run a final pass over the test coverage and surface any remaining gaps.

## When to use

- Use for engineering/engineering-qa-security/test-engineering when the brief specifically requires: Use this agent when you need to review a pull request for test coverage quality and completeness .

## When not to use

- Do not claim coverage or runtime verification from a plan alone.
- Do not treat aggregate coverage as proof of behaviour.

## Inputs it needs

- Architecture, critical flows, expected behaviour, test stack and execution constraints.

## How to run it

1. Confirm the tool is available in the configured Claude Code or Codex environment.
2. Provide the scope, evidence and decision requested; keep client material in an approved private workspace.
3. Review the result against the checks below; a human retains release and approval decisions.

```text
Use Agent tool: pr-test-analyzer. Task: {describe the scoped test engineering need}. Context: {repository or artefact and constraints}. Evidence: {files, links and runtime evidence}. Return findings with evidence, scope, unknowns and practical next steps; do not claim checks you did not perform.
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
