---
title: evolving-apis-and-schemas
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:evolving-apis-and-schemas
department: engineering
sub_department: platform-performance
job: data-and-storage
role: specialist
trigger: "Use when changing anything other systems or stored data already depend on — editing a."
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.config/opencode/skills/evolving-apis-and-schemas/SKILL.md
invoke: "evolving-apis-and-schemas skill"
pairs_with: [agency:engineering-database-optimizer]
---
# evolving-apis-and-schemas

Use when changing anything other systems or stored data already depend on — editing a .proto file, writing a database migration, adding or dropping a column, renaming a field, changing a response shape, changing an enum, or altering a queue message format. Triggers include "will this break clients", "is this backward compatible", "buf breaking", "ALTER TABLE", "migration", "deprecate this endpoint", and any change to a published API version.

## What it does

- Use when changing anything other systems or stored data already depend on — editing a .proto file, writing a database migration, adding or dropping a column, renaming a field, changing a response shape, changing an enum, or altering a queue message format. Triggers include "will this break clients", "is this backward compatible", "buf breaking", "ALTER TABLE", "migration", "deprecate this endpoint", and any change to a published API version.
- Not for "the old column is definitely unused" — prove it with a query, not a grep
- Not for "we deploy everything together" — rollouts are not atomic, and rollbacks are not either
- Not for renames. A rename is a drop and an add, and it is the single most common way to take an outage

## When to use

- Use when changing anything other systems or stored data already depend on — editing a.
- Before changing production behaviour, with scope, baseline and decision owner stated.

## When not to use

- When the task is outside `data-and-storage` or its stated trigger; route to the appropriate job lead.
- To approve its own work; use an independent checker.

## Inputs it needs

- The approved scope, relevant repository or system context, and decision requested.
- Baseline evidence, constraints, and acceptance criteria relevant to the task.
- Access and environment details only when required; keep client data outside the public repository.

## How to run it

1. Confirm the brief matches `data-and-storage` and the trigger above.
2. Provide the inputs and ask for findings tied to the supplied evidence.
3. Review the output independently; implement only approved changes and record before/after evidence.

```text
Use evolving-apis-and-schemas skill. Task: {specific task}. Context: {repository/system and approved scope}. Evidence available: {baseline, traces, logs, or constraints}. Return documented capabilities and limits, identify unknowns, and give a proposed next action with evidence. Do not claim unmeasured results.
```

## What good output looks like

- Recommendations map to the stated task and cite supplied evidence.
- Unknowns, assumptions and risks are explicit.
- Any performance or reliability claim has a comparable baseline and follow-up measure.

## Quality checks

- [ ] The work matches the registry job and trigger.
- [ ] Claims trace to supplied evidence; unknowns are labelled.
- [ ] An independent reviewer checks the result.

## Pairs with

- Upstream: `agency:engineering-database-optimizer`.
- Downstream: an independent reviewer and the relevant delivery or QA owner; hand off findings, evidence and unresolved risks.

## Limits and cautions

- The source describes a role or workflow; it does not prove live system access, successful execution or performance outcomes.
- Keep maker and checker separate; label evidence **Documented**, **Interpretation**, **Hypothesis** or **Unknown**.
- Protect client data; do not place confidential or identifying material in this public repository.
