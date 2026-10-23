---
title: "Data visualisation"
type: "tool-card"
status: "proposed"
owner: "founder"
last_reviewed: "2026-10-23"
tool_id: "skill:dataviz"
department: "design"
sub_department: "identity-craft"
job: "composition-layout"
role: "specialist"
trigger: "An approved guidelines or identity application needs charts with supplied, verified data."
kind: "skill"
availability: "claude-managed"
distribution: "manual"
source: "toolkit/sources/managed-tool-descriptions.md"
invoke: "dataviz skill in Claude"
pairs_with: []
---

# Data visualisation

Guides coherent, accessible charts and data displays for 3RDWRONG reports, guidelines and digital products. It is a specialist for composition-layout.

## What it does

- Selects chart forms through a documented form heuristic.
- Defines palette, marks and interactions as a coherent visual system.
- Provides a colour formula, runnable validator and replaceable default palette.

## When to use

- Before writing chart code, choosing chart colours or laying out any dashboard or KPI display.

## When not to use

- For inventing or validating the underlying dataset; use independent data-quality checks.

## Inputs it needs

- The data, question, medium, client identity palette and accessibility constraints.

## How to run it

1. Load the account-managed dataviz skill before the first line of chart code.
2. Read the required palette reference and adapt its values to the approved brand.
3. Validate the palette and inspect the chart’s marks, labels and interactions.

```text
Use dataviz before coding {{chart or dashboard}}. Data: {{source}}. Question: {{question}}. Apply {{approved palette}}, run its documented validation and distinguish supplied facts from interpretation.
```

## What good output looks like

- A legible chart system with validated colours and consistent marks, labels and interactions.

## Quality checks

- [ ] A reviewer other than the maker checks capability claims and output evidence.
- [ ] Access, connectivity and prerequisites are verified before use.
- [ ] Client assets, credentials and personal data stay outside the public repository.

## Pairs with

- The job lead receives the result and unresolved prerequisites before the next production step.

## Limits and cautions

- The reference palette is brand-neutral; replace it with the approved client palette.
- For a document connector with live charts, supply rows rather than a rendered chart image.
- Documented from the founder’s account description dated 2026-10-23; this card remains proposed.
