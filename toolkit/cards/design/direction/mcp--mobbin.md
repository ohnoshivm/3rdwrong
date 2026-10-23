---
title: Mobbin MCP
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: mcp:mobbin
department: design
sub_department: direction
job: inspiration-taste
role: specialist
trigger: "A digital interaction question needs source-backed interface reference research; record it under taste/."
kind: mcp
availability: mcp
distribution: manual
source: https://api.mobbin.com/mcp
invoke: "Mobbin MCP server `mobbin`"
pairs_with: [skill:taste-skill, skill:daily-ui-inspiration-capture, skill:3w-category-code-audit]
---

# Mobbin MCP

A declared Mobbin MCP endpoint for interface reference work; server capabilities are not documented in the available declaration. For 3RDWRONG, use this specialist when the registry trigger applies: “A digital interaction question needs source-backed interface reference research; record it under taste/.”

## What it does

- The local declaration identifies an HTTP MCP server named `mobbin` at `https://api.mobbin.com/mcp`.
- Server operations and returned data: Not documented.
- Authentication and account requirements: Not documented.

## When to use

- A digital interaction question needs source-backed interface reference research; record it under taste/.
- Use only after the Mobbin MCP connection exposes its actual tools and a relevant operation has been confirmed.

## When not to use

- General concept development without a digital interaction question; use `skill:3w-creative-direction`.
- When no live Mobbin tool schema or service connection is available; use documented reference sources instead.

## Inputs it needs

- A defined interface question and the relevant category/platform.
- A connected Mobbin MCP tool schema; its exact input requirements are Not documented.

## How to run it

1. Select the connected `mobbin` MCP server in the host.
2. Inspect its available operation schema before making a call.
3. Record the source page and what was observed in the taste/ record; extract principles, never copy a screen.

```text
Use Mobbin MCP server `mobbin`. Task: {specific decision or output}. Context: {approved strategy, source links, version and constraints}. Return the documented format, label evidence and unknowns, and stop where required inputs or approval are missing.
```

## What good output looks like

- A source-linked observation that answers the stated interaction question.
- Limitations and unavailable details are labelled Unknown.

## Quality checks

- [ ] The output answers the registry job and, for a specialist, the exact trigger.
- [ ] Every factual claim comes from supplied evidence or the tool’s documented method.
- [ ] An independent reviewer checks the output; the maker does not approve their own work.
- [ ] Accessibility, reduced motion and responsive behaviour are checked where relevant.

## Pairs with

- `skill:taste-skill` — upstream context or hand-off.
- `skill:daily-ui-inspiration-capture` — downstream review or delivery.
- `skill:3w-category-code-audit` — downstream review or delivery.

## Limits and cautions

- The declaration exposes the server endpoint only; tool operations, outputs and licence terms are Not documented.
- Manual server setup/connection; an endpoint declaration does not establish authentication or access.
- Reference material is inspiration only; do not copy layouts, assets, copy or identity.
