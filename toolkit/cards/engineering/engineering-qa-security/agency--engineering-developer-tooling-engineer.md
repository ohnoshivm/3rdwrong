---
title: Developer Tooling Engineer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:engineering-developer-tooling-engineer
department: engineering
sub_department: engineering-qa-security
job: codebase-analysis
role: lead
trigger: ""
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/engineering-developer-tooling-engineer.md
invoke: "Agent tool: Developer Tooling Engineer"
pairs_with: [agency:engineering-codebase-onboarding-engineer]
---
# Developer Tooling Engineer

The studio's lead tool for codebase analysis when a brief concerns developer tooling: designs CLIs and internal platforms around discoverability, actionable errors, scriptability and fast startup.

## What it does

- Expert developer-tooling and CLI engineer — building command-line tools and internal developer platforms with great DX: intuitive command design, helpful errors, shell completions, fast startup, cross-platform distribution, and scriptable, composable interfaces.
- Design command interfaces that are discoverable and consistent: sensible verb-noun structure, predictable flags, and a --help that actually teaches.
- Make failure a feature: error messages that state what went wrong, why, and the exact next step — never a raw stack trace dumped at a human.
- Build for both humans and machines: rich interactive output when attached to a terminal, clean parseable output (JSON, exit codes, quiet mode) when piped or scripted.

## When to use

- When a studio project needs a CLI, internal developer platform or automation tool designed or improved; use the codebase-analysis route only where the brief includes repository context discovery.

## When not to use

- Do not use it to review or refactor code; use `agency:engineering-code-reviewer` for an independent review.
- Do not describe uninspected files or behaviour as understood.

## Inputs it needs

- Current developer workflow, scripts or CLI surface and the recurring user problem.
- Platform, distribution, performance, automation and backwards-compatibility constraints.

## How to run it

1. Confirm the tool is available in the configured Claude Code or Codex environment.
2. Provide the scope, evidence and decision requested; keep client material in an approved private workspace.
3. Review the result against the checks below; a human retains release and approval decisions.

```text
Use Agent tool: Developer Tooling Engineer. Task: {describe the CLI or internal developer platform problem}. Current workflow: {commands, scripts and user pain}. Constraints: {platforms, startup target, distribution and compatibility}. Return a proposed command surface, output and error behaviour, safety controls and trade-offs; do not claim measurements you did not run.
```

## What good output looks like

- The command surface, errors, human and machine output, safety controls and distribution path are specified.
- Decisions account for startup speed and interface compatibility where relevant.

## Quality checks

- [ ] The interface is discoverable and scriptable, with actionable errors.
- [ ] Destructive actions are deliberate and interface changes preserve a migration path.
- [ ] Performance and platform assumptions are explicit.

## Pairs with

- Upstream: `agency:engineering-codebase-onboarding-engineer` can map an existing repository and workflow; this tool uses that context to shape developer tooling. The registry places this tool under codebase analysis, while its source focuses on designing tooling.

## Limits and cautions

- Maker ≠ checker: an independent reviewer checks material findings; tool output does not approve client work.
- Label observations and conclusions as Documented, Interpretation, Hypothesis or Unknown when evidence strength matters.
- Keep client data, personal data and credentials out of the public repository.
- Fetch or manual tools may require installation, sign-in or service access; confirm availability before promising execution.

- Registry placement may be too broad: the source describes developer tooling design and creation, not codebase analysis.
