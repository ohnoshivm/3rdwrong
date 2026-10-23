---
title: "Claude Docs"
type: "tool-card"
status: "proposed"
owner: "founder"
last_reviewed: "2026-10-23"
tool_id: "mcp:claude-docs"
department: "design"
sub_department: "identity-craft"
job: "handover-specs"
role: "specialist"
trigger: "Approved guidelines or handover specifications must be authored or exchanged through the Claude Docs connector."
kind: "mcp"
availability: "claude-managed"
distribution: "manual"
source: "toolkit/sources/managed-tool-descriptions.md"
invoke: "Claude Docs connector"
pairs_with: []
---

# Claude Docs

Creates and edits living documents in the founder’s Claude account for explicitly requested briefs, critiques or reports. It is a specialist for handover-specs.

## What it does

- Creates a document skeleton and fills its sections through atomic batch operations.
- Reads, queries, edits and exports documents; supports tabs, comments and stored values.
- Provides topic guides for editing, sharing, charts and diagrams.

## When to use

- When the user explicitly requests a living document outside the repository.

## When not to use

- For an unrequested document or as a replacement for the repository source of truth.

## Inputs it needs

- The requested document, approved source material and access to the founder’s Claude account.

## How to run it

1. Open the Claude Docs connector in the signed-in Claude account and read the relevant guide.
2. Create the title, byline and pending section skeleton before filling the sections.
3. Keep findings in the document and answer document comments with document comments.

```text
Use Claude Docs to create the requested {{document}} from {{approved sources}}. Create the skeleton first, then fill each section. Keep findings in the document and identify unsupported claims.
```

## What good output looks like

- A complete, shareable living document with sources and clearly labelled unresolved findings.

## Quality checks

- [ ] A reviewer other than the maker checks capability claims and output evidence.
- [ ] Access, connectivity and prerequisites are verified before use.
- [ ] Client assets, credentials and personal data stay outside the public repository.

## Pairs with

- The job lead receives the result and unresolved prerequisites before the next production step.

## Limits and cautions

- Requires Claude account sign-in; collaborators need their own access.
- Use connector guides for details; availability does not establish current connectivity.
- Documented from the founder’s account description dated 2026-10-23; this card remains proposed.
