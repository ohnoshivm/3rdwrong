---
title: Rust Refactoring Specialist
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:engineering-rust-refactoring-specialist
department: engineering
sub_department: product-frontend
job: code-modernization
role: specialist
trigger: "Use for repository-scale Rust refactors, safe renames, ownership improvements, and compiler or Clippy-driven cleanup."
kind: upstream-agent
availability: claude-managed
distribution: vendor
source: .claude/agents/engineering-rust-refactoring-specialist.md
invoke: "Claude Code agent: Rust Refactoring Specialist Agent"
pairs_with: [agency:engineering-minimal-change-engineer, agent:implementer]
---
# Rust Refactoring Specialist

Rust Refactoring Specialist is the studio's specialist for `code-modernization`; use it when the registry trigger below applies.

## What it does

- Performs repository-scale Rust refactors and safe renames
- Improves ownership patterns
- Uses compiler and Clippy feedback for cleanup

## When to use

- Use for repository-scale Rust refactors, safe renames, ownership improvements, and compiler or Clippy-driven cleanup.
- For repository-scale Rust refactors, safe renames, ownership improvements, and compiler or Clippy-driven cleanup

## When not to use

- For frontend code use `agent:frontend-architect`
- For minimal non-Rust fixes use `agency:engineering-minimal-change-engineer`
- Do not use to approve its own work; assign a separate checker.

## Inputs it needs

- Rust workspace and toolchain
- Refactor goal and compatibility constraints
- Compiler/Clippy output and relevant tests

## How to run it

1. Confirm the task matches the job and, for a specialist, the registry trigger.
2. Invoke `Claude Code agent: Rust Refactoring Specialist Agent` and provide the approved brief, artefacts, constraints and source context.
3. Ask for the documented deliverable; inspect assumptions and verification before handoff.

```text
Use `agency:engineering-rust-refactoring-specialist` for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform/version: {links and versions}. Constraints: {accessibility, performance, delivery}. Work within the documented scope and registry trigger. Label evidence Documented, Interpretation, Hypothesis or Unknown; return the requested artefact, assumptions, limitations, verification actually performed and a concrete next action.
```

## What good output looks like

- Reviewable Rust refactor with compiler, Clippy and test results

## Quality checks

- [ ] Work matches the approved brief and the maker is not its checker.
- [ ] Claims are supported by source or supplied evidence; label uncertainty explicitly.
- [ ] Responsive behaviour, accessibility and performance are checked where they apply.
- [ ] Verification lists only commands, tests or browser checks actually run.

## Pairs with

- `agency:engineering-minimal-change-engineer` — coordinate the artefacts and handoff at the relevant stage.
- `agent:implementer` — coordinate the artefacts and handoff at the relevant stage.

## Limits and cautions

- Registry places Rust-focused work under product-frontend
- source scope appears inconsistent with that placement
- Keep client data and credentials out of the public repository (D-0021); check licence and distribution prerequisites, including installation or sign-in when required.
