---
title: Archify
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-24
tool_id: skill:archify
department: engineering
sub_department: engineering-qa-security
job: technical-architecture
role: specialist
trigger: "Use when creating validated architecture, workflow, sequence, data-flow, lifecycle, ERD or class diagrams as explorable standalone HTML."
kind: skill
availability: both
distribution: fetch
source: ~/.3rdwrong/fetch/pack-tt-a1i-archify-mit/archify (pinned 25cf37080fc8b1dbe758a4efc3935b55f3327083)
invoke: "archify skill; for a native diagram ask: Use the archify skill to draw {type} for {system}"
pairs_with: [skill:karpathy-guidelines, engineering:architecture, skill:frontend-slides]
---
# Archify

A specialist for drawing technical diagrams as checked, standalone HTML: architecture, workflow, sequence, data-flow, lifecycle, ERD, class, tree, timeline and waterfall. Use it to explain how a system is wired before or during a build, not to decide the architecture.

## What it does

- Writes a native diagram from a stated question, then runs its own validation gates before delivery.
- Traces a real codebase's behaviour from source evidence when asked for a diagram of existing code.
- Produces a dark and light themed HTML artefact with motion and image or SVG export.
- Can also produce a one-page explainer when the user asks for a page.

## When to use

- Technical architecture or data-flow diagrams for a client or internal build, before implementation starts.
- Explaining an existing system's workflow or data model to a non-engineer reviewer.
- Documenting a sequence or lifecycle where a static diagram would hide the state changes.

## When not to use

- Architecture decisions or trade-offs: use `engineering:architecture` and the strategic review route.
- A diagram of client data, names or contracts in the public repository (D-0021): render it in the private store.
- Brand or marketing illustration: use the design specialists.

## Inputs it needs

- The question the diagram must answer, and the scope (system, flow or data model).
- Access to the relevant source files if the diagram describes real code.

## How to run it

1. Choose the diagram type from the question; the skill's type router lists the schema per type.
2. For real code, read the relevant source first and cite the files the diagram depends on.
3. Run the skill's finalize step, then check the HTML in a real browser at desktop and mobile widths.

```text
Use the archify skill to draw a {type} diagram of {system}, scoped to {files or flow}. Cite the source file for each node. Run the finalize gate, open the result in the browser, and report the gates that passed, anything unverified, and any node you could not trace.
```

## What good output looks like

- A validated standalone HTML diagram, each node traceable to a named source file or stated assumption.
- Gate results from the finalize step, reported as they ran.
- Open questions where the code did not show the behaviour.

## Quality checks

- [ ] Every node or edge traces to source or is labelled as an assumption.
- [ ] Finalize gates ran and their result is reported.
- [ ] Rendered in a real browser at desktop and mobile widths; console clean.
- [ ] No client names, data or credentials in the diagram.

## Pairs with

- `engineering:architecture`: the architecture decision that the diagram documents.
- `skill:karpathy-guidelines`: keep the diagram scope surgical.
- `skill:frontend-slides`: when the diagram goes into a web deck.

## Limits and cautions

- MIT licence; only the `archify/` folder is installed. The pinned checkout also carries `bin/`, `renderers/` and `package.json`. These run only when invoked; the install does not run `npm install`.
- The skill may run a bounded update check when it delivers an artefact (its receipt includes an update notice). Review that before using it on client work.
- The repository also holds an `archify.zip` at its root. It is not installed here and has not been reviewed.
- Its own references and examples are not evidence about the studio's systems.
