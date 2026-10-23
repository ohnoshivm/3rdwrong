---
title: explore
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agent:claude-security:explore
department: engineering
sub_department: engineering-qa-security
job: security-analysis
role: specialist
trigger: "only when dispatched by the Claude Security scan workflow to map code; read-only and not a direct scanner."
kind: agent
availability: claude
distribution: fetch
source: /Users/hustle/.claude/plugins/marketplaces/claude-plugins-official/plugins/claude-security/agents/explore.md
invoke: "Agent tool: explore"
pairs_with: [claude-security:claude-security]
---
# explore

The studio's specialist tool for security analysis: Read-only code explorer that the plugin's other agents dispatch to map a codebase — locate files, trace how a flow is wired, find every caller of a symbol, answer "where does X happen".

## What it does

- Read-only code explorer that the plugin's other agents dispatch to map a codebase — locate files, trace how a flow is wired, find every caller of a symbol, answer "where does X happen".
- Match the depth to the request: a targeted lookup is one or two searches; a "how does X flow end to end" question means tracing across files. Honour a thoroughness the dispatch names ("quick", "medium", "very thorough").
- Be efficient: find for filename patterns, grep for symbols and strings, Read once you know the file. Fan out independent searches in parallel.
- Read enough of a file to answer correctly. If a conclusion rests on lines you did not read, say so rather than guessing.

## When to use

- only when dispatched by the Claude Security scan workflow to map code; read-only and not a direct scanner.

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
Within the Claude Security workflow, dispatch Agent tool: explore. Task: {describe the scoped security analysis need}. Context: {repository or artefact and constraints}. Evidence: {files, links and runtime evidence}. Return findings with evidence, scope, unknowns and practical next steps; do not claim checks you did not perform.
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
