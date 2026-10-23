---
title: Silent Failure Hunter
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agent:pr-review-toolkit:silent-failure-hunter
department: engineering
sub_department: engineering-qa-security
job: code-review
role: specialist
trigger: "Use for engineering/engineering-qa-security/code-review when the brief specifically requires: Use this agent when reviewing code changes in a pull request to identify silent failures, inadequate error handling, and inappropriate fallback behavior ."
kind: agent
availability: claude
distribution: fetch
source: /Users/hustle/.claude/plugins/marketplaces/claude-plugins-official/plugins/pr-review-toolkit/agents/silent-failure-hunter.md
invoke: "Agent tool: Silent Failure Hunter"
pairs_with: [agency:engineering-code-reviewer]
---
# Silent Failure Hunter

The studio's specialist tool for code review: the source does not document a purpose beyond the registry entry

## What it does

- Silent failures are unacceptable - Any error that occurs without proper logging and user feedback is a critical defect.
- Users deserve actionable feedback - Every error message must tell users what went wrong and what they can do about it.
- Fallbacks must be explicit and justified - Falling back to alternative behavior without user awareness is hiding problems.

## When to use

- Use for engineering/engineering-qa-security/code-review when the brief specifically requires: Use this agent when reviewing code changes in a pull request to identify silent failures, inadequate error handling, and inappropriate fallback behavior .

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
Use Agent tool: Silent Failure Hunter. Task: {describe the scoped code review need}. Context: {repository or artefact and constraints}. Evidence: {files, links and runtime evidence}. Return findings with evidence, scope, unknowns and practical next steps; do not claim checks you did not perform.
```

## What good output looks like

- Findings cite changed code, explain impact and propose a practical correction.
- The report states inspected scope and distinguishes high-impact defects from lower-priority advice.

## Quality checks

- [ ] Reviewer did not author the change.
- [ ] Findings cite evidence and impact.
- [ ] No approval is implied.

## Pairs with

- `agency:engineering-code-reviewer`. Use the lead to frame the work and an independent reviewer for consequential output.

## Limits and cautions

- Maker ≠ checker: an independent reviewer checks material findings; tool output does not approve client work.
- Label observations and conclusions as Documented, Interpretation, Hypothesis or Unknown when evidence strength matters.
- Keep client data, personal data and credentials out of the public repository.
- Fetch or manual tools may require installation, sign-in or service access; confirm availability before promising execution.
