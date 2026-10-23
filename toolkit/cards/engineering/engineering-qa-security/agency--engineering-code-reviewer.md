---
title: Code Reviewer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:engineering-code-reviewer
department: engineering
sub_department: engineering-qa-security
job: code-review
role: lead
trigger: ""
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/engineering-code-reviewer.md
invoke: "Agent tool: Code Reviewer"
pairs_with: [agent:pr-review-toolkit:code-reviewer, agent:pr-review-toolkit:silent-failure-hunter]
---
# Code Reviewer

The studio's lead tool for code review: Expert code reviewer who provides constructive, actionable feedback focused on correctness, maintainability, security, and performance — not style preferences.

## What it does

- Expert code reviewer who provides constructive, actionable feedback focused on correctness, maintainability, security, and performance — not style preferences.
- Correctness — Does it do what it's supposed to?.
- Security — Are there vulnerabilities? Input validation? Auth checks?.
- Maintainability — Will someone understand this in 6 months?.

## When to use

- Phase 06 Development, before hand-off or pull-request readiness.

## When not to use

- Do not use it to implement the reviewed change.
- Do not treat review output as release approval; use `skill:ceos-production-quality` for release readiness.

## Inputs it needs

- Pull request or diff, intended behaviour, acceptance criteria and relevant tests.

## How to run it

1. Confirm the tool is available in the configured Claude Code or Codex environment.
2. Provide the scope, evidence and decision requested; keep client material in an approved private workspace.
3. Review the result against the checks below; a human retains release and approval decisions.

```text
Use Agent tool: Code Reviewer. Task: {describe the scoped code review need}. Context: {repository or artefact and constraints}. Evidence: {files, links and runtime evidence}. Return findings with evidence, scope, unknowns and practical next steps; do not claim checks you did not perform.
```

## What good output looks like

- Findings cite changed code, explain impact and propose a practical correction.
- The report states inspected scope and distinguishes high-impact defects from lower-priority advice.

## Quality checks

- [ ] Reviewer did not author the change.
- [ ] Findings cite evidence and impact.
- [ ] No approval is implied.

## Pairs with

- `agent:pr-review-toolkit:code-reviewer`, `agent:pr-review-toolkit:silent-failure-hunter`. Use the lead to frame the work and an independent reviewer for consequential output.

## Limits and cautions

- Maker ≠ checker: an independent reviewer checks material findings; tool output does not approve client work.
- Label observations and conclusions as Documented, Interpretation, Hypothesis or Unknown when evidence strength matters.
- Keep client data, personal data and credentials out of the public repository.
- Fetch or manual tools may require installation, sign-in or service access; confirm availability before promising execution.
