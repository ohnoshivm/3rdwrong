---
title: CEO
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agent:ceo
department: design
sub_department: direction
job: concept-direction
role: specialist
trigger: "A flagship assignment or the studio own identity needs a consequential concept or critique decision; use Opus/max."
kind: agent
availability: claude
distribution: vendor
source: toolkit/vendor/pack-founder-local-agents/agents/ceo.md
invoke: "ceo agent in the Agent tool"
pairs_with: [skill:3w-creative-direction, agent:creative-director, agent:visual-qa-engineer]
---

# CEO

The flagship direction and critique specialist for consequential brand or experience decisions. For 3RDWRONG, use this specialist when the registry trigger applies: “A flagship assignment or the studio own identity needs a consequential concept or critique decision; use Opus/max.”

## What it does

- Decides what deserves to exist, what makes it distinctive and what separates outstanding work from generic work.
- Names limiting assumptions and ideas to reject; challenges derivative aesthetics and weak strategy.
- Makes trade-offs explicit and converts a decision into an executable spec with constraints, acceptance criteria and risks.
- Ends with a report containing Decision, Why, Rejected, Spec for executor and Open questions.

## When to use

- A flagship assignment or the studio’s own identity needs a consequential concept or critique decision; the registry trigger specifies Opus at max effort.
- Phase 04 Concept, when the founder needs a high-stakes decision translated into a buildable spec.

## When not to use

- Routine coding, formatting or research; use the relevant production or research tool.
- Routine route development; use `skill:3w-creative-direction`.

## Inputs it needs

- The decision, brief, relevant strategy and only the context files needed.
- Constraints, assets and the intended executor or next owner.

## How to run it

1. Open the `ceo` agent in Claude Code and supply the decision brief.
2. Request the agent’s stated report shape and keep the founder’s decision explicit.
3. Hand the executable spec to the named maker; obtain an independent review.

```text
Use ceo agent in the Agent tool. Task: {specific decision or output}. Context: {approved strategy, source links, version and constraints}. Return the documented format, label evidence and unknowns, and stop where required inputs or approval are missing.
```

## What good output looks like

- A decisive recommendation with explicit trade-offs and rejected options.
- An executable spec with acceptance criteria, risks and open questions.

## Quality checks

- [ ] The output answers the registry job and, for a specialist, the exact trigger.
- [ ] Every factual claim comes from supplied evidence or the tool’s documented method.
- [ ] An independent reviewer checks the output; the maker does not approve their own work.
- [ ] Accessibility, reduced motion and responsive behaviour are checked where relevant.

## Pairs with

- `skill:3w-creative-direction` — upstream context or hand-off.
- `agent:creative-director` — downstream review or delivery.
- `agent:visual-qa-engineer` — downstream review or delivery.

## Limits and cautions

- Use Opus at max effort for the registry trigger; the source file specifies Opus/max.
- The agent does not claim approval; founder sign-off remains the gate.
- Do not put client-confidential data in the public repository.
