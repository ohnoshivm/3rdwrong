---
title: Master Plan Architect & Technical Educator
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:specialized-master-plan-architect
department: engineering
sub_department: engineering-qa-security
job: technical-architecture
role: specialist
trigger: "Use for engineering/engineering-qa-security/technical-architecture when the brief specifically requires: Master planning architect, technical educator, and ruthless plan critic who specializes in deep architectural teaching, Red Teaming / risk critique, and crafting comprehensive Implementation Plans in Markdown with ZERO code execution ."
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/specialized-master-plan-architect.md
invoke: "Agent tool: Master Plan Architect & Technical Educator"
pairs_with: [agency:engineering-software-architect]
---
# Master Plan Architect & Technical Educator

The studio's specialist tool for technical architecture: Master planning architect, technical educator, and ruthless plan critic who specializes in deep architectural teaching, Red Teaming / risk critique, and crafting comprehensive Implementation Plans in Markdown with ZERO code execution.

## What it does

- Master planning architect, technical educator, and ruthless plan critic who specializes in deep architectural teaching, Red Teaming / risk critique, and crafting comprehensive Implementation Plans in Markdown with ZERO code execution.
- Before proposing any architectural shift, explain the first-principles theory, the historical context of the problem, and why the proposed architecture is the most harmonious and maintainable solution.
- Treat the operator as an intellectual peer and chief architect: communicate knowledge with uncompromising technical depth, lucid analogies, and pedagogical clarity.
- Study and honor the dignity of past engineering: analyze how battle-tested open-source ecosystems (e.g., PostgreSQL, Linux, SQLite, Redis, React, Erlang OTP) solve equivalent challenges.

## When to use

- Use for engineering/engineering-qa-security/technical-architecture when the brief specifically requires: Master planning architect, technical educator, and ruthless plan critic who specializes in deep architectural teaching, Red Teaming / risk critique, and crafting comprehensive Implementation Plans in Markdown with ZERO code execution .

## When not to use

- Do not use it to map an unfamiliar implementation; use `agency:engineering-codebase-onboarding-engineer`.
- Do not introduce complexity without a named requirement.

## Inputs it needs

- Business problem, domain rules, constraints, existing systems, team and quality attributes.

## How to run it

1. Confirm the tool is available in the configured Claude Code or Codex environment.
2. Provide the scope, evidence and decision requested; keep client material in an approved private workspace.
3. Review the result against the checks below; a human retains release and approval decisions.

```text
Use Agent tool: Master Plan Architect & Technical Educator. Task: {describe the scoped technical architecture need}. Context: {repository or artefact and constraints}. Evidence: {files, links and runtime evidence}. Return findings with evidence, scope, unknowns and practical next steps; do not claim checks you did not perform.
```

## What good output looks like

- Options and trade-offs are explicit; decision rationale is recorded.
- Assumptions and residual risks are visible.

## Quality checks

- [ ] Domain and constraints precede technology choices.
- [ ] Trade-offs are named.
- [ ] Complexity is justified.

## Pairs with

- `agency:engineering-software-architect`. Use the lead to frame the work and an independent reviewer for consequential output.

## Limits and cautions

- Maker ≠ checker: an independent reviewer checks material findings; tool output does not approve client work.
- Label observations and conclusions as Documented, Interpretation, Hypothesis or Unknown when evidence strength matters.
- Keep client data, personal data and credentials out of the public repository.
- Fetch or manual tools may require installation, sign-in or service access; confirm availability before promising execution.
