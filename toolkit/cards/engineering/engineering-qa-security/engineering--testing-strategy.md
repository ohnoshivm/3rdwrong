---
title: Testing Strategy
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: engineering:testing-strategy
department: engineering
sub_department: engineering-qa-security
job: test-engineering
role: specialist
trigger: "Use for engineering/engineering-qa-security/test-engineering when the brief specifically requires: Design test strategies and test plans ."
kind: plugin-skill
availability: claude
distribution: manual
source: /Users/hustle/.claude/plugins/synced/88e7af4e-a2cf-4b40-8488-91a856697e04_aa2d1473-adba-46ff-9558-93fbf2ea6240/2da0c8d9-1e96-4394-b0f4-3249613186f8/skills/testing-strategy/SKILL.md
invoke: "testing-strategy skill (Claude Code plugin)"
pairs_with: [agent:code-modernization:test-engineer, agent:pr-review-toolkit:pr-test-analyzer, mcp:chrome-devtools]
---
# Testing Strategy

The studio's specialist tool for test engineering: Design test strategies and test plans. Trigger with "how should we test", "test strategy for", "write tests for", "test plan", "what tests do we need", or when the user needs help with testing approaches, coverage, or test architecture.

## What it does

- Design test strategies and test plans. Trigger with "how should we test", "test strategy for", "write tests for", "test plan", "what tests do we need", or when the user needs help with testing approaches, coverage, or test architecture.
- API endpoints: Unit tests for business logic, integration tests for HTTP layer, contract tests for consumers.
- Data pipelines: Input validation, transformation correctness, idempotency tests.
- Frontend: Component tests, interaction tests, visual regression, accessibility.

## When to use

- Use for engineering/engineering-qa-security/test-engineering when the brief specifically requires: Design test strategies and test plans .

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
Use testing-strategy skill (Claude Code plugin). Task: {describe the scoped test engineering need}. Context: {repository or artefact and constraints}. Evidence: {files, links and runtime evidence}. Return findings with evidence, scope, unknowns and practical next steps; do not claim checks you did not perform.
```

## What good output looks like

- Test choices map to risk and critical behaviour.
- Uncovered paths and execution limits are explicit.

## Quality checks

- [ ] Critical and failure paths are considered.
- [ ] Test layers are proportionate.
- [ ] Execution evidence is distinguished from plans.

## Pairs with

- `agent:code-modernization:test-engineer`, `agent:pr-review-toolkit:pr-test-analyzer`, `mcp:chrome-devtools`. Use the lead to frame the work and an independent reviewer for consequential output.

## Limits and cautions

- Maker ≠ checker: an independent reviewer checks material findings; tool output does not approve client work.
- Label observations and conclusions as Documented, Interpretation, Hypothesis or Unknown when evidence strength matters.
- Keep client data, personal data and credentials out of the public repository.
- Fetch or manual tools may require installation, sign-in or service access; confirm availability before promising execution.
