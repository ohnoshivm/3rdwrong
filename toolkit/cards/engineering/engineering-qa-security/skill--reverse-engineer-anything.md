---
title: REA
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:reverse-engineer-anything
department: engineering
sub_department: engineering-qa-security
job: codebase-analysis
role: specialist
trigger: "Use for tasks involving Reverse engineer native, managed, Electron/JavaScript, packaged, firmware, and browser targets with REA."
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.agents/skills/reverse-engineer-anything/SKILL.md
invoke: "reverse-engineer-anything skill"
pairs_with: [agency:engineering-codebase-onboarding-engineer]
---
# REA

The studio's specialist tool for codebase analysis: Reverse engineer native, managed, Electron/JavaScript, packaged, firmware, and browser targets with REA.

## What it does

- Reverse engineer native, managed, Electron/JavaScript, packaged, firmware, and browser targets with REA. Use shipped-artifact or requested runtime evidence to explain features, compare versions, decompile code, or guide a reconstruction. Skip REA for ordinary source-repository architecture analysis.
- Diagnose without changing REA or client configuration. npx may download.
- Distinguish the reason. Missing, malformed, or stale registration needs a.
- For a configuration repair, prepare the read-only plan:.

## When to use

- Use for tasks involving Reverse engineer native, managed, Electron/JavaScript, packaged, firmware, and browser targets with REA.

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
Use reverse-engineer-anything skill. Task: {describe the scoped codebase analysis need}. Context: {repository or artefact and constraints}. Evidence: {files, links and runtime evidence}. Return findings with evidence, scope, unknowns and practical next steps; do not claim checks you did not perform.
```

## What good output looks like

- The map or analysis cites concrete files and lists inspected and uninspected areas.
- Claims are grounded in the available code or artefacts.

## Quality checks

- [ ] Inspected files are listed.
- [ ] Ownership claims cite implementation or routing code.
- [ ] Unknowns are explicit.

## Pairs with

- `agency:engineering-codebase-onboarding-engineer`. Use the lead to frame the work and an independent reviewer for consequential output.

## Limits and cautions

- Maker ≠ checker: an independent reviewer checks material findings; tool output does not approve client work.
- Label observations and conclusions as Documented, Interpretation, Hypothesis or Unknown when evidence strength matters.
- Keep client data, personal data and credentials out of the public repository.
- Fetch or manual tools may require installation, sign-in or service access; confirm availability before promising execution.
