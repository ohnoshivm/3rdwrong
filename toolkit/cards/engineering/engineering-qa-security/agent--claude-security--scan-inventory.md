---
title: scan-inventory
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agent:claude-security:scan-inventory
department: engineering
sub_department: engineering-qa-security
job: security-analysis
role: specialist
trigger: "only when the Claude Security workflow partitions a repository for scanning."
kind: agent
availability: claude
distribution: fetch
source: /Users/hustle/.claude/plugins/marketplaces/claude-plugins-official/plugins/claude-security/agents/scan-inventory.md
invoke: "Agent tool: scan-inventory"
pairs_with: [claude-security:claude-security]
---
# scan-inventory

The studio's specialist tool for security analysis: Restricted read-only repository cartographer dispatched by the Claude Security scan workflow to partition the tree into components and account for every top-level directory; not for direct invocation or vulnerability research.

## What it does

- Restricted read-only repository cartographer dispatched by the Claude Security scan workflow to partition the tree into components and account for every top-level directory; not for direct invocation or vulnerability research.
- Returns work within the documented scope.
- States evidence and scope limits where relevant.

## When to use

- only when the Claude Security workflow partitions a repository for scanning.

## When not to use

- Do not use it outside the stated scope or without authorisation for active testing.
- Do not treat a scan as proof that no vulnerabilities exist.

## Inputs it needs

- Repository or system scope, evidence, authorisation where relevant and the requested security question.

## How to run it

1. Start the Claude Security workflow; this agent is dispatched only for its assigned workflow stage.
2. Provide the scope, evidence and decision requested; keep client material in an approved private workspace.
3. Review the result against the checks below; a human retains release and approval decisions.

```text
Within the Claude Security workflow, dispatch Agent tool: scan-inventory. Task: {describe the scoped security analysis need}. Context: {repository or artefact and constraints}. Evidence: {files, links and runtime evidence}. Return findings with evidence, scope, unknowns and practical next steps; do not claim checks you did not perform.
```

## What good output looks like

- Findings identify evidence, impact, remediation direction and unknowns.
- The report distinguishes observation from assessment.

## Quality checks

- [ ] Scope matches the request and any authorisation.
- [ ] Findings cite evidence.
- [ ] Limitations and untested areas are stated.

## Pairs with

- `claude-security:claude-security`. Use the lead to frame the work and an independent reviewer for consequential output.

## Limits and cautions

- Maker ≠ checker: an independent reviewer checks material findings; tool output does not approve client work.
- Label observations and conclusions as Documented, Interpretation, Hypothesis or Unknown when evidence strength matters.
- Keep client data, personal data and credentials out of the public repository.
- Fetch or manual tools may require installation, sign-in or service access; confirm availability before promising execution.
- Security output is not certification, legal advice or authorisation to test a system.
