---
title: Dieter Rams Principles
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:dieter-rams-principles
department: design
sub_department: direction
job: concept-direction
role: specialist
trigger: "When the approved scope specifically requires evaluating or refining a design through Dieter Rams’ principles."
kind: skill
availability: codex
distribution: manual
source: /Users/hustle/.agents/skills/dieter-rams-principles/SKILL.md
invoke: "/dieter-rams-principles skill"
pairs_with: [skill:design-analysis, ui-ux-pro-max:ui-ux-pro-max, agent:visual-qa-engineer]
---

# Dieter Rams Principles

A principle-based reviewer for evaluating and refining a digital product or interface. For 3RDWRONG, use this specialist when the registry trigger applies: “When the approved scope specifically requires evaluating or refining a design through Dieter Rams’ principles.”

## What it does

- Applies ten Rams principles translated for software.
- Scores each as Strong, Adequate or Weak, focusing on relevant principles.
- Names the top two or three violations and gives a concrete change for each.
- Preserves strong decisions and concludes with the one edit that matters most.

## When to use

- When the approved scope specifically requires evaluating or refining a design through Dieter Rams’ principles.
- For a product, screen, flow or feature critique where core utility and restraint are clear.

## When not to use

- A measured visual analysis when exact dimensions are unknown; use `skill:design-analysis` first.
- A concept-generation request; use `skill:3w-creative-direction` or the relevant concept tool.

## Inputs it needs

- The screen/product and its primary job.
- A screenshot, flow or accessible product view.

## How to run it

1. Invoke `/dieter-rams-principles` in Codex.
2. Provide the product’s core job and inspectable screen/flow.
3. Ask for the source’s scorecard, top violations, keep list and one edit.

```text
Use /dieter-rams-principles skill. Task: {specific decision or output}. Context: {approved strategy, source links, version and constraints}. Return the documented format, label evidence and unknowns, and stop where required inputs or approval are missing.
```

## What good output looks like

- Scores are tied to observed details and relevant principles.
- Each priority finding names a concrete change, and useful existing decisions are preserved.

## Quality checks

- [ ] The output answers the registry job and, for a specialist, the exact trigger.
- [ ] Every factual claim comes from supplied evidence or the tool’s documented method.
- [ ] An independent reviewer checks the output; the maker does not approve their own work.
- [ ] Accessibility, reduced motion and responsive behaviour are checked where relevant.

## Pairs with

- `skill:design-analysis` — upstream context or hand-off.
- `ui-ux-pro-max:ui-ux-pro-max` — downstream review or delivery.
- `agent:visual-qa-engineer` — downstream review or delivery.

## Limits and cautions

- Codex skill; it is a critique lens, not a user study.
- Do not infer preference, performance or accessibility conformance from the scorecard alone.
- Keep the maker and final reviewer separate.
- Manual distribution: installation, account access or sign-in may be required before invocation; verify availability in the target host.
