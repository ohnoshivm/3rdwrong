---
title: Claude Security
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: claude-security:claude-security
department: engineering
sub_department: engineering-qa-security
job: security-analysis
role: lead
trigger: ""
kind: plugin-skill
availability: claude
distribution: fetch
source: /Users/hustle/.claude/plugins/marketplaces/claude-plugins-official/plugins/claude-security/skills/claude-security/SKILL.md
invoke: "claude-security skill (Claude Code plugin)"
pairs_with: [agent:claude-security:explore, agent:claude-security:scan-researcher, agent:claude-security:scan-verifier]
---
# Claude Security

The studio's lead tool for security analysis: Claude Security: scan the codebase (the whole repository or a scoped part of it), scan changes (this branch's or a pull request's diff, or one commit), or suggest patches (findings turned into targeted patch files, each verified by a panel of.

## What it does

- Claude Security: scan the codebase (the whole repository or a scoped part of it), scan changes (this branch's or a pull request's diff, or one commit), or suggest patches (findings turned into targeted patch files, each verified by a panel of agents, that you apply when you choose). Use when the user asks to scan, audit or check code with Claude Security, to scan their changes with Claude Security, or to fix or patch Claude Security findings.
- SCRIPTS — helper scripts directory (upstream reference `${CLAUDEPLUGINROOT}/scripts`).
- REPORT SPEC (the report's shape) (upstream reference `${CLAUDESKILLDIR}/specs/report-spec.md`).
- PATCH SPEC (the patch products contract) (upstream reference `${CLAUDESKILLDIR}/specs/patch-spec.md`).

## When to use

- Phase 07 Validation, when a scoped security check is required before hand-over.

## When not to use

- Do not use it outside the stated scope or without authorisation for active testing.
- Do not treat a scan as proof that no vulnerabilities exist.

## Inputs it needs

- Repository or system scope, evidence, authorisation where relevant and the requested security question.

## How to run it

1. Confirm the tool is available in the configured Claude Code or Codex environment.
2. Provide the scope, evidence and decision requested; keep client material in an approved private workspace.
3. Review the result against the checks below; a human retains release and approval decisions.

```text
Use claude-security skill (Claude Code plugin). Task: {describe the scoped security analysis need}. Context: {repository or artefact and constraints}. Evidence: {files, links and runtime evidence}. Return findings with evidence, scope, unknowns and practical next steps; do not claim checks you did not perform.
```

## What good output looks like

- Findings identify evidence, impact, remediation direction and unknowns.
- The report distinguishes observation from assessment.

## Quality checks

- [ ] Scope matches the request and any authorisation.
- [ ] Findings cite evidence.
- [ ] Limitations and untested areas are stated.

## Pairs with

- `agent:claude-security:explore`, `agent:claude-security:scan-researcher`, `agent:claude-security:scan-verifier`. Use the lead to frame the work and an independent reviewer for consequential output.

## Limits and cautions

- Maker ≠ checker: an independent reviewer checks material findings; tool output does not approve client work.
- Label observations and conclusions as Documented, Interpretation, Hypothesis or Unknown when evidence strength matters.
- Keep client data, personal data and credentials out of the public repository.
- Fetch or manual tools may require installation, sign-in or service access; confirm availability before promising execution.
- Security output is not certification, legal advice or authorisation to test a system.
