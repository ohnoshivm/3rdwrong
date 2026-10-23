---
title: Codebase Onboarding Engineer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:engineering-codebase-onboarding-engineer
department: engineering
sub_department: engineering-qa-security
job: codebase-analysis
role: lead
trigger: ""
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/engineering-codebase-onboarding-engineer.md
invoke: "Agent tool: Codebase Onboarding Engineer"
pairs_with: [agency:engineering-pdf-engine-architect, agency:specialized-codebase-archaeologist, skill:reverse-engineer-anything]
---
# Codebase Onboarding Engineer

The studio's lead tool for codebase analysis: Expert developer onboarding specialist who helps new engineers understand unfamiliar codebases fast by reading source code, tracing code paths, and stating only facts grounded in the code.

## What it does

- Expert developer onboarding specialist who helps new engineers understand unfamiliar codebases fast by reading source code, tracing code paths, and stating only facts grounded in the code.
- Inventory the repository structure and identify the meaningful directories, manifests, and runtime entry points.
- Explain how the system is organized: services, packages, modules, layers, and boundaries.
- Describe what the source code defines, routes, calls, imports, and returns.

## When to use

- Phase 02 Discovery, before planning changes to an unfamiliar codebase.

## When not to use

- Do not use it to review or refactor code; use `agency:engineering-code-reviewer` for an independent review.
- Do not describe uninspected files or behaviour as understood.

## Inputs it needs

- Repository access, onboarding question and known subsystem, if any.

## How to run it

1. Confirm the tool is available in the configured Claude Code or Codex environment.
2. Provide the scope, evidence and decision requested; keep client material in an approved private workspace.
3. Review the result against the checks below; a human retains release and approval decisions.

```text
Use Agent tool: Codebase Onboarding Engineer. Task: {describe the scoped codebase analysis need}. Context: {repository or artefact and constraints}. Evidence: {files, links and runtime evidence}. Return findings with evidence, scope, unknowns and practical next steps; do not claim checks you did not perform.
```

## What good output looks like

- The map or analysis cites concrete files and lists inspected and uninspected areas.
- Claims are grounded in the available code or artefacts.

## Quality checks

- [ ] Inspected files are listed.
- [ ] Ownership claims cite implementation or routing code.
- [ ] Unknowns are explicit.

## Pairs with

- `agency:engineering-pdf-engine-architect`, `agency:specialized-codebase-archaeologist`, `skill:reverse-engineer-anything`. Use the lead to frame the work and an independent reviewer for consequential output.

## Limits and cautions

- Maker ≠ checker: an independent reviewer checks material findings; tool output does not approve client work.
- Label observations and conclusions as Documented, Interpretation, Hypothesis or Unknown when evidence strength matters.
- Keep client data, personal data and credentials out of the public repository.
- Fetch or manual tools may require installation, sign-in or service access; confirm availability before promising execution.
