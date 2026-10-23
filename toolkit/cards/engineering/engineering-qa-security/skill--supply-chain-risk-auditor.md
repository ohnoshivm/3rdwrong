---
title: Supply Chain Risk Auditor
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:supply-chain-risk-auditor
department: engineering
sub_department: engineering-qa-security
job: dependency-audit
role: lead
trigger: ""
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.config/opencode/skills/supply-chain-risk-auditor/SKILL.md
invoke: "supply-chain-risk-auditor skill"
pairs_with: [skill:semgrep, skill:codeql]
---
# Supply Chain Risk Auditor

The studio's lead tool for dependency audit: Audits a project's dependencies for supply-chain risk: version-matched advisories for direct dependencies and the full lockfile tree, abandoned or archived upstreams, npm publisher concentration, and install-time script execution.

## What it does

- Measures direct dependency risks and sweeps resolved lockfile dependencies for advisories.
- Produces a report using deterministic collection.
- Distinguishes unavailable data from measured risk and no measurement from a clean result.

## When to use

- Before release or dependency upgrades when supply-chain exposure is in scope.
- During due diligence of a supported package ecosystem.

## When not to use

- Do not use for code-level vulnerability scanning; use `skill:semgrep` or `skill:codeql`.
- Missing registry data is neither risk nor a clean conclusion.

## Inputs it needs

- Project manifests and lockfiles, decision context and a private-safe report location.

## How to run it

1. Confirm the tool is available in the configured Claude Code or Codex environment.
2. Provide the scope, evidence and decision requested; keep client material in an approved private workspace.
3. Review the result against the checks below; a human retains release and approval decisions.

```text
Use supply-chain-risk-auditor skill. Task: {describe the scoped dependency audit need}. Context: {repository or artefact and constraints}. Evidence: {files, links and runtime evidence}. Return findings with evidence, scope, unknowns and practical next steps; do not claim checks you did not perform.
```

## What good output looks like

- The report prioritises evidenced actions and identifies unavailable measurements.
- Upgrade or replacement suggestions are supported and compatibility is checked.

## Quality checks

- [ ] Measured ecosystems and lockfiles are named.
- [ ] Missing data is not labelled safe.
- [ ] Advice is compatible with project constraints.

## Pairs with

- `skill:semgrep`, `skill:codeql`. Use the lead to frame the work and an independent reviewer for consequential output.

## Limits and cautions

- Maker ≠ checker: an independent reviewer checks material findings; tool output does not approve client work.
- Label observations and conclusions as Documented, Interpretation, Hypothesis or Unknown when evidence strength matters.
- Keep client data, personal data and credentials out of the public repository.
- Fetch or manual tools may require installation, sign-in or service access; confirm availability before promising execution.
- Security output is not certification, legal advice or authorisation to test a system.
