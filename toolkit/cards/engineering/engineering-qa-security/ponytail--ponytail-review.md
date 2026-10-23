---
title: ponytail-review
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: ponytail:ponytail-review
department: engineering
sub_department: engineering-qa-security
job: code-review
role: specialist
trigger: "Use for an independent second review when engineering:code-review did not author the change; keep reviewer separate from maker."
kind: plugin-skill
availability: both
distribution: vendor
source: toolkit/vendor/plugin-ponytail-ponytail-5.3.2/.openclaw/skills/ponytail-review
invoke: "ponytail-review skill (Claude Code plugin)"
pairs_with: [agency:engineering-code-reviewer]
---
# ponytail-review

The studio's specialist tool for code review: Quality review of a diff: bugs, security, real load, missing tests, speed, and what to delete.

## What it does

- Quality review of a diff: bugs, security, real load, missing tests, speed, and what to delete. Each finding says what goes wrong and how to fix it.
- Review what the user names: uncommitted or staged changes, a branch, a PR.
- Read the diff, then the code it touches: callers of every changed function,.
- Trace the real flow: where data comes in, what is stored, what goes out.

## When to use

- Use for an independent second review when engineering:code-review did not author the change; keep reviewer separate from maker.

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
Use ponytail-review skill (Claude Code plugin). Task: {describe the scoped code review need}. Context: {repository or artefact and constraints}. Evidence: {files, links and runtime evidence}. Return findings with evidence, scope, unknowns and practical next steps; do not claim checks you did not perform.
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
