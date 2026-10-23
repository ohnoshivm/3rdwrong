---
title: Software Architect
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:engineering-software-architect
department: engineering
sub_department: engineering-qa-security
job: technical-architecture
role: lead
trigger: ""
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/engineering-software-architect.md
invoke: "Agent tool: Software Architect"
pairs_with: [agency:specialized-master-plan-architect]
---
# Software Architect

The studio's lead tool for technical architecture: Expert software architect specializing in system design, domain-driven design, architectural patterns, and technical decision-making for scalable, maintainable systems.

## What it does

- Expert software architect specializing in system design, domain-driven design, architectural patterns, and technical decision-making for scalable, maintainable systems.
- Domain modeling — Bounded contexts, aggregates, domain events.
- Architectural patterns — When to use layered, hexagonal, onion, modular monolith, microservices, or event-driven architecture.
- Trade-off analysis — Consistency vs availability, coupling vs duplication, simplicity vs flexibility.

## When to use

- Phase 03 Technical Architecture, before choosing major boundaries or implementation approach.

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
Use Agent tool: Software Architect. Task: {describe the scoped technical architecture need}. Context: {repository or artefact and constraints}. Evidence: {files, links and runtime evidence}. Return findings with evidence, scope, unknowns and practical next steps; do not claim checks you did not perform.
```

## What good output looks like

- Options and trade-offs are explicit; decision rationale is recorded.
- Assumptions and residual risks are visible.

## Quality checks

- [ ] Domain and constraints precede technology choices.
- [ ] Trade-offs are named.
- [ ] Complexity is justified.

## Pairs with

- `agency:specialized-master-plan-architect`. Use the lead to frame the work and an independent reviewer for consequential output.

## Limits and cautions

- Maker ≠ checker: an independent reviewer checks material findings; tool output does not approve client work.
- Label observations and conclusions as Documented, Interpretation, Hypothesis or Unknown when evidence strength matters.
- Keep client data, personal data and credentials out of the public repository.
- Fetch or manual tools may require installation, sign-in or service access; confirm availability before promising execution.
