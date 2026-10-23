---
title: Effect study
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:3w-effect-study
department: labs
sub_department: experiments
job: effect-studies
role: lead
trigger: ""
kind: repo-skill
availability: repo
distribution: repo
source: skills/3w-effect-study/SKILL.md
invoke: "3w-effect-study skill"
pairs_with: [skill:audit-reference-originality, skill:3w-engine-validation]
---
# Effect study

The studio's lead tool for effect studies: re-authors a parked effect recipe or captured technique as an original technique card, measured against the D-0023 budget. Proposed lead; the registry change is pending.

## What it does

- Separates a source's underlying technique from its expression (assets, palette, sequence, layout) and carries forward only the technique.
- Builds the reduced-motion and no-WebGL path first.
- Measures frame time, draw calls, texture memory and transfer on the reference phone and desktop.
- Writes a technique card with budget fit, degradation ladder, risks and an adopt / iterate / drop decision.

## When to use

- A parked recipe in `effect-studies` or a Taste Graph capture names a technique worth understanding before a project needs it.
- Before a technique is proposed to the house engine.
- Labs time between client projects.

## When not to use

- Inside a client build — follow digital stage 06 Motion, 3D and interaction.
- To copy a reference's look or sequence.
- To justify motion the concept does not need.

## Inputs it needs

- Study question and the design problem it might serve.
- Source recipe id or reference link with access date.
- Reference devices from the web standards.
- An `experiments/<study>/` folder from the experiment template.

## How to run it

1. Collect the inputs; keep client and prospect details in the vault.
2. Run the skill and return its exact output structure.
3. Have someone other than the maker review the result.
4. File the output where the skill says; act on blockers first.

```text
Use the 3w-effect-study skill. Question: can {{technique}} serve {{design problem}} inside the D-0023 budget? Source: {{recipe id or reference, accessed date}}. Build in experiments/{{study}}/ with neutral placeholder content, reduced-motion path first. Return the technique card.
```

## What good output looks like

- A technique card whose technique section names what was deliberately not carried over.
- Measurements with device, tool and run conditions; a clear budget-fit line.
- A decision with a named reviewer who is not the maker.

## Quality checks

- [ ] No source asset, palette, layout or sequence survives.
- [ ] Reduced-motion and no-WebGL states convey the same information.
- [ ] Measurements cite device, tool and version.
- [ ] Study styling avoids the rejected own-identity look (D-0006).
- [ ] Originality reviewed by a non-maker.

## Pairs with

- Upstream: `skill:3w-taste-graph` (captured references), parked recipes in `effect-studies`.
- Review: `skill:audit-reference-originality`.
- Downstream: `skill:3w-engine-validation` when adopted.

## Limits and cautions

- Experimental skill; outputs are drafts for human review.
- Lab measurements only; no field data or audience effect is established.
- Client reuse needs a concept-specific choice, independent originality review and project performance evidence (Labs operating contract).
