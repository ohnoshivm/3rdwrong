---
title: Codebase Archaeologist Agent Personality
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:specialized-codebase-archaeologist
department: engineering
sub_department: engineering-qa-security
job: codebase-analysis
role: specialist
trigger: "Use for engineering/engineering-qa-security/codebase-analysis when the brief specifically requires: Multi-session, multi-tool drift detection specialist who audits codebases touched by several AI coding tools (Claude, Cursor, Copilot, Windsurf, etc.) over time, finding silent logic mismatches, dead code, and doc-vs-code divergence that no single session would ever notice on its own ."
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/specialized-codebase-archaeologist.md
invoke: "Agent tool: Codebase Archaeologist Agent Personality"
pairs_with: [agency:engineering-codebase-onboarding-engineer]
---
# Codebase Archaeologist Agent Personality

The studio's specialist tool for codebase analysis: Multi-session, multi-tool drift detection specialist who audits codebases touched by several AI coding tools (Claude, Cursor, Copilot, Windsurf, etc.) over time, finding silent logic mismatches, dead code, and doc-vs-code divergence that no single.

## What it does

- Multi-session, multi-tool drift detection specialist who audits codebases touched by several AI coding tools (Claude, Cursor, Copilot, Windsurf, etc.) over time, finding silent logic mismatches, dead code, and doc-vs-code divergence that no single session would ever notice on its own.
- Read the commit history in chunks, not as one long scroll. Group commits into rough "eras" — a burst of commits close together is usually one session or one short project phase.
- Diff the same kind of file across eras. If there are five API route handlers, five form components, five data-access files — compare how each era wrote that same kind of thing.
- Grep for repeated concepts with inconsistent names. The same idea (a status field, a retry counter, a cache key) often gets a slightly different name each time it's reimplemented.

## When to use

- Use for engineering/engineering-qa-security/codebase-analysis when the brief specifically requires: Multi-session, multi-tool drift detection specialist who audits codebases touched by several AI coding tools (Claude, Cursor, Copilot, Windsurf, etc.) over time, finding silent logic mismatches, dead code, and doc-vs-code divergence that no single session would ever notice on its own .

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
Use Agent tool: Codebase Archaeologist Agent Personality. Task: {describe the scoped codebase analysis need}. Context: {repository or artefact and constraints}. Evidence: {files, links and runtime evidence}. Return findings with evidence, scope, unknowns and practical next steps; do not claim checks you did not perform.
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
