---
title: Image to Code
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:image-to-code-skill
department: engineering
sub_department: product-frontend
job: ui-implementation
role: specialist
trigger: "When the approved scope specifically requires building a web interface from generated design references."
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.config/opencode/skills/image-to-code-skill/SKILL.md
invoke: "image-to-code-skill skill"
pairs_with: [agent:frontend-architect, skill:building-accessible-interfaces]
---
# Image to Code

Image to Code is the studio's specialist for `ui-implementation`; use it when the registry trigger below applies.

## What it does

- Guides web interface implementation from supplied generated references
- Uses visible layout/styling as implementation input
- Works within project stack

## When to use

- When the approved scope specifically requires building a web interface from generated design references.
- When approved scope specifically builds interface from generated reference
- Phase 05 after reference is approved

## When not to use

- For Figma source use `figma:figma-design-to-code`
- Image does not specify hidden behaviours
- Do not use to approve its own work; assign a separate checker.

## Inputs it needs

- Reference images and target states
- Explicit content/interaction requirements
- Framework, tokens and assets

## How to run it

1. Confirm the task matches the job and, for a specialist, the registry trigger.
2. Invoke `image-to-code-skill skill` and provide the approved brief, artefacts, constraints and source context.
3. Ask for the documented deliverable; inspect assumptions and verification before handoff.

```text
Use `skill:image-to-code-skill` for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform/version: {links and versions}. Constraints: {accessibility, performance, delivery}. Work within the documented scope and registry trigger. Label evidence Documented, Interpretation, Hypothesis or Unknown; return the requested artefact, assumptions, limitations, verification actually performed and a concrete next action.
```

## What good output looks like

- Working UI aligned to reference and project conventions
- Unseen states labelled as assumptions

## Quality checks

- [ ] Work matches the approved brief and the maker is not its checker.
- [ ] Claims are supported by source or supplied evidence; label uncertainty explicitly.
- [ ] Responsive behaviour, accessibility and performance are checked where they apply.
- [ ] Verification lists only commands, tests or browser checks actually run.

## Pairs with

- `agent:frontend-architect` — coordinate the artefacts and handoff at the relevant stage.
- `skill:building-accessible-interfaces` — coordinate the artefacts and handoff at the relevant stage.

## Limits and cautions

- Do not infer hidden interaction, responsiveness or semantics from pixels
- mark unknowns
- Keep client data and credentials out of the public repository (D-0021); check licence and distribution prerequisites, including installation or sign-in when required.
