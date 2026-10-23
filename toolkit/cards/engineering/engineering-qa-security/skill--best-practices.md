---
title: Best practices
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:best-practices
department: engineering
sub_department: engineering-qa-security
job: code-review
role: specialist
trigger: "Use for tasks involving Apply modern web development best practices for security, compatibility, and code quality."
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.config/opencode/skills/best-practices/SKILL.md
invoke: "best-practices skill"
pairs_with: [agency:engineering-code-reviewer]
---
# Best practices

The studio's specialist tool for code review: Apply modern web development best practices for security, compatibility, and code quality.

## What it does

- Apply modern web development best practices for security, compatibility, and code quality. Use when asked to "apply best practices", "security audit", "modernize code", "code quality review", or "check for vulnerabilities".
- Run a live Lighthouse Best Practices audit when that capability is available; with Chrome DevTools MCP, use lighthouseaudit. Use navigation mode for a normal page load or snapshot mode when the current state must be preserved.
- Inspect the listed console and network failures and fetch individual details only when they support a finding.
- Supplement runtime evidence with dependency, header, configuration, and source inspection; Lighthouse is not a complete security assessment.

## When to use

- Use for tasks involving Apply modern web development best practices for security, compatibility, and code quality.

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
Use best-practices skill. Task: {describe the scoped code review need}. Context: {repository or artefact and constraints}. Evidence: {files, links and runtime evidence}. Return findings with evidence, scope, unknowns and practical next steps; do not claim checks you did not perform.
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
