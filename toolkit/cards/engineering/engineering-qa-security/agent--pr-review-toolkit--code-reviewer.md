---
title: code-reviewer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agent:pr-review-toolkit:code-reviewer
department: engineering
sub_department: engineering-qa-security
job: code-review
role: specialist
trigger: "Use for an independent second review when engineering:code-review did not author the change; keep reviewer separate from maker."
kind: agent
availability: claude
distribution: fetch
source: /Users/hustle/.claude/plugins/marketplaces/claude-plugins-official/plugins/pr-review-toolkit/agents/code-reviewer.md
invoke: "Agent tool: code-reviewer"
pairs_with: [agency:engineering-code-reviewer]
---
# code-reviewer

The studio's specialist tool for code review: Use this agent when you need to review code for adherence to project guidelines, style guides, and best practices.

## What it does

- Use this agent when you need to review code for adherence to project guidelines, style guides, and best practices. This agent should be used proactively after writing or modifying code, especially before committing changes or creating pull requests. It will check for style violations, potential issues, and ensure code follows the established patterns in CLAUDE.md. Also the agent needs to know which files to focus on for the review. In most cases this will be recently completed work which is unstaged in git (can be retrieved by running git diff). However there can be cases where this is different, make sure to specify this as the agent input when calling the agent. Typical triggers include the user asking for a review of a feature they just implemented, the assistant proactively reviewing its own newly-written code before declaring a task done, and a final pre-PR check before opening a pull request. See "When to invoke" in the agent body for worked scenarios.
- User-requested review after a feature lands. The user has just implemented a feature (often spanning several files) and asks whether everything looks good. Run a review of the recent diff and report findings.
- Proactive review of newly-written code. The assistant has just written new code (e.g. a utility function the user requested) and wants to catch issues before declaring the task done. Spawn this agent on the freshly written files.
- Pre-PR sanity check. The user signals they're ready to open a pull request. Run a review of the full diff first to avoid round-trips on the PR itself.

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
Use Agent tool: code-reviewer. Task: {describe the scoped code review need}. Context: {repository or artefact and constraints}. Evidence: {files, links and runtime evidence}. Return findings with evidence, scope, unknowns and practical next steps; do not claim checks you did not perform.
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
