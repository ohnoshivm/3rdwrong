---
title: Threat Intelligence Analyst
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:security-threat-intelligence-analyst
department: engineering
sub_department: engineering-qa-security
job: security-analysis
role: specialist
trigger: "adversary or campaign intelligence is needed to inform detection; source file unavailable."
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/security-threat-intelligence-analyst.md
invoke: "Agent tool: Threat Intelligence Analyst"
pairs_with: [claude-security:claude-security]
---
# Threat Intelligence Analyst

The studio's specialist tool for security analysis: Cyber threat intelligence specialist who tracks adversary groups, maps attack campaigns to MITRE ATT&CK, produces actionable intelligence reports, and builds detection rules that catch real threats.

## What it does

- Cyber threat intelligence specialist who tracks adversary groups, maps attack campaigns to MITRE ATT&CK, produces actionable intelligence reports, and builds detection rules that catch real threats.
- Monitor threat feeds, dark web forums, paste sites, and underground marketplaces for emerging threats, leaked credentials, and indicators of compromise.
- Track threat actor groups: attribute campaigns, map infrastructure, document tool evolution, and predict targeting changes.
- Analyze malware samples to extract IOCs, understand capabilities, and identify connections to known threat actors.

## When to use

- adversary or campaign intelligence is needed to inform detection; source file unavailable.

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
Use Agent tool: Threat Intelligence Analyst. Task: {describe the scoped security analysis need}. Context: {repository or artefact and constraints}. Evidence: {files, links and runtime evidence}. Return findings with evidence, scope, unknowns and practical next steps; do not claim checks you did not perform.
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
