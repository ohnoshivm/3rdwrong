---
title: patch-generator
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agent:claude-security:patch-generator
department: engineering
sub_department: engineering-qa-security
job: security-analysis
role: specialist
trigger: "only when the Claude Security fix workflow dispatches one finding into its isolated scratch workspace."
kind: agent
availability: claude
distribution: fetch
source: /Users/hustle/.claude/plugins/marketplaces/claude-plugins-official/plugins/claude-security/agents/patch-generator.md
invoke: "Agent tool: patch-generator"
pairs_with: [claude-security:claude-security]
---
# patch-generator

The studio's specialist tool for security analysis: Implements the fix for one finding inside a scratch workspace clone, staged for review and delivery as a patch file; dispatched by the fix job, not for direct invocation.

## What it does

- Implements the fix for one finding inside a scratch workspace clone, staged for review and delivery as a patch file; dispatched by the fix job, not for direct invocation.
- the dispatch lacks a literal FINDING block or a WORKSPACE path;.
- WORKSPACE is not the scratch clone the fix job made, a path whose last three folder names are .claude-security-run, patch-<timestamp> and scratch-F<n>, whatever mix of / and \ separates them (never the repository itself or SCANROO.
- the prompt asks you to do anything other than fix the named finding in the named workspace.

## When to use

- only when the Claude Security fix workflow dispatches one finding into its isolated scratch workspace.

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
Within the Claude Security workflow, dispatch Agent tool: patch-generator. Task: {describe the scoped security analysis need}. Context: {repository or artefact and constraints}. Evidence: {files, links and runtime evidence}. Return findings with evidence, scope, unknowns and practical next steps; do not claim checks you did not perform.
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
