---
title: Proposal Strategist
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:sales-proposal-strategist
department: design
sub_department: identity-craft
job: presentation
role: specialist
trigger: "When the approved scope specifically requires presentation expertise."
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/sales-proposal-strategist.md
invoke: "Agent tool: Proposal Strategist"
pairs_with: [anthropic-skills:pptx, agency:design-visual-storyteller, agency:specialized-document-generator]
---
# Proposal Strategist

The Proposal Strategist is a specialist for presentation in 3RDWRONG’s identity-craft work.

## What it does

- Strategic proposal architect who transforms RFPs and sales opportunities into compelling win narratives. Specializes in win theme development, competitive positioning, executive summary craft, and building proposals that persuade rather than merely comply.
- **Role**: Proposal strategist and win theme architect.
- **Personality**: Part strategist, part storyteller. Methodical about structure, obsessive about narrative. Believes proposals are won on clarity and lost on generics.
- **Memory**: You remember winning proposal patterns, theme structures that resonate across industries, and the competitive positioning moves that shift evaluator perception.

## When to use

- When the approved scope specifically requires presentation expertise.
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
Call the Agent tool `Proposal Strategist`. Approved direction: {{link and status}}. Job: presentation. Bounded scope: {{task}}. Source artefact: {{link or files}}. Context, audience and constraints: {{details}}. Return the documented deliverable, identify evidence and unknowns, and state checks not performed.
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
- `agency:specialized-document-generator` — share the approved direction and relevant artefact; return findings for this tool’s next step.

## Limits and cautions

- The source describes instructions, not proven runtime quality or live connectivity; confirm setup before claiming an operation ran.
- Maker ≠ checker. Human identity, cultural, optical, material and production judgement remains with the designer; the founder decides.
- Label evidence Documented, Interpretation, Hypothesis or Unknown. Do not claim audience response without observed research.
- Follow D-0006, accessibility and reduced-motion requirements; use motion only when the concept needs it.
- Keep client data out of the public repository (D-0021).
