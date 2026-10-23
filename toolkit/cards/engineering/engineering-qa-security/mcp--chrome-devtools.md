---
title: Chrome DevTools
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: mcp:chrome-devtools
department: engineering
sub_department: engineering-qa-security
job: test-engineering
role: specialist
trigger: "a running page needs browser-level inspection, traces, console/network diagnostics, or Lighthouse via the configured DevTools MCP."
kind: mcp
availability: mcp
distribution: fetch
source: /Users/hustle/.claude.json
invoke: "Chrome DevTools MCP server"
pairs_with: [engineering:testing-strategy]
---
# Chrome DevTools

The studio's specialist tool for test engineering: the source does not document a purpose beyond the registry entry

## What it does

- Tool-specific capabilities are Not documented in the available source.
- Returns work within the documented scope.
- States evidence and scope limits where relevant.

## When to use

- a running page needs browser-level inspection, traces, console/network diagnostics, or Lighthouse via the configured DevTools MCP.

## When not to use

- Do not claim coverage or runtime verification from a plan alone.
- Do not treat aggregate coverage as proof of behaviour.

## Inputs it needs

- Architecture, critical flows, expected behaviour, test stack and execution constraints.

## How to run it

1. Confirm the tool is available in the configured Claude Code or Codex environment.
2. Provide the scope, evidence and decision requested; keep client material in an approved private workspace.
3. Review the result against the checks below; a human retains release and approval decisions.

```text
Use Chrome DevTools MCP server. Task: {describe the scoped test engineering need}. Context: {repository or artefact and constraints}. Evidence: {files, links and runtime evidence}. Return findings with evidence, scope, unknowns and practical next steps; do not claim checks you did not perform.
```

## What good output looks like

- Test choices map to risk and critical behaviour.
- Uncovered paths and execution limits are explicit.

## Quality checks

- [ ] Critical and failure paths are considered.
- [ ] Test layers are proportionate.
- [ ] Execution evidence is distinguished from plans.

## Pairs with

- `engineering:testing-strategy`. Use the lead to frame the work and an independent reviewer for consequential output.

## Limits and cautions

- Maker ≠ checker: an independent reviewer checks material findings; tool output does not approve client work.
- Label observations and conclusions as Documented, Interpretation, Hypothesis or Unknown when evidence strength matters.
- Keep client data, personal data and credentials out of the public repository.
- Fetch or manual tools may require installation, sign-in or service access; confirm availability before promising execution.
- Tool-owned MCP capabilities are Not documented in the available connector configuration.
