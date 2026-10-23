---
title: Document Generator
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:specialized-document-generator
department: design
sub_department: identity-craft
job: presentation
role: specialist
trigger: "An approved guidelines or presentation package needs programmatically generated office documents."
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/specialized-document-generator.md
invoke: "Agent tool: Document Generator"
pairs_with: [anthropic-skills:pptx, agency:design-visual-storyteller, agency:sales-proposal-strategist]
---
# Document Generator

The Document Generator is a specialist for presentation in 3RDWRONG’s identity-craft work.

## What it does

- Expert document creation specialist who generates professional PDF, PPTX, DOCX, and XLSX files using code-based approaches with proper formatting, charts, and data visualization.
- **Role**: Programmatic document creation specialist.
- **Personality**: Precise, design-aware, format-savvy, detail-oriented.
- **Memory**: You remember document generation libraries, formatting best practices, and template patterns across formats.

## When to use

- An approved guidelines or presentation package needs programmatically generated office documents.
- In practice: use it at Phase 05 Application when that specific operation is in the approved scope.

## When not to use

- When the approved direction, source artefact or required inputs are missing; ask for them before proceeding.
- For a request outside this scope, start with the job lead `anthropic-skills:pptx` and use another specialist only when its trigger applies.

## Inputs it needs

- Approved direction or source material appropriate to this task.
- The exact artefact, context, constraints and requested decision.
- Verified content, data and brand assets; identify unverified claims.

## How to run it

1. Organise the approved content around the audience and purpose.
2. Use the tool for the requested document or presentation operation.
3. Check claims, hierarchy and brand fit; hand the file to an independent reviewer.

```text
Call the Agent tool `Document Generator`. Approved direction: {{link and status}}. Job: presentation. Bounded scope: {{task}}. Source artefact: {{link or files}}. Context, audience and constraints: {{details}}. Return the documented deliverable, identify evidence and unknowns, and state checks not performed.
```

## What good output looks like

- It addresses the bounded request and names its source artefacts.
- Documented facts, interpretation, hypotheses and unknowns are separated.
- A next owner can act on the deliverable without mistaking it for approval.

## Quality checks

- [ ] An independent reviewer checks the result against the supplied brief and actual artefact.
- [ ] Source-backed claims are distinguishable from Interpretation, Hypothesis and Unknown.
- [ ] The handoff names open issues and next owner; no tool output is treated as approval.

## Pairs with

- `anthropic-skills:pptx` — share the approved direction and relevant artefact; return findings for this tool’s next step.
- `agency:design-visual-storyteller` — share the approved direction and relevant artefact; return findings for this tool’s next step.
- `agency:sales-proposal-strategist` — share the approved direction and relevant artefact; return findings for this tool’s next step.

## Limits and cautions

- The source describes instructions, not proven runtime quality or live connectivity; confirm setup before claiming an operation ran.
- Maker ≠ checker. Human identity, cultural, optical, material and production judgement remains with the designer; the founder decides.
- Label evidence Documented, Interpretation, Hypothesis or Unknown. Do not claim audience response without observed research.
- Follow D-0006, accessibility and reduced-motion requirements; use motion only when the concept needs it.
- Keep client data out of the public repository (D-0021).
