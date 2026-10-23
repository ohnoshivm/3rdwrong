---
title: AI Inputs
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:ai-inputs
department: design
sub_department: experience-design
job: interaction-architecture
role: specialist
trigger: "When the approved scope specifically requires designing AI inputs, controls, onboarding, or discoverability in an AI product."
kind: skill
availability: codex
distribution: manual
source: /Users/hustle/.agents/skills/ai-inputs/SKILL.md
invoke: "ai-inputs skill"
pairs_with: [skill:ai-tuners, skill:ai-wayfinders, skill:designing-user-experience]
---
# AI Inputs

The experience-design specialist for `interaction-architecture` is AI Inputs (trigger: “When the approved scope specifically requires designing AI inputs, controls, onboarding, or discoverability in an AI product”), which chooses and designs the input pattern through which users direct or refine an ai feature.

## What it does

- Maps use cases to 13 patterns including open input, Madlibs, auto-fill and inline action.
- defines scope and user control.
- recommends previews and confirmation for bulk or replacement actions.

## When to use

- Use when the approved scope specifically requires designing AI inputs, controls, onboarding, or discoverability in an AI product. Use Phase 04 Concept before building the AI interaction surface.
- When the approved scope specifically requires designing AI inputs, controls, onboarding, or discoverability in an AI product.

## When not to use

- Use `skill:ai-tuners` for controls that configure generation; `skill:ai-wayfinders` for first-use discovery.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- AI task and target content, user expertise, editing scope, existing data and risk of overwriting.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use ai-inputs skill. Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce users know what the model will act on; generated changes are previewed and accepted; bulk actions have a sample/check. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- A selected input pattern with scope, interaction and acceptance rules.
- Evidence claims are labelled Documented, Interpretation, Hypothesis or Unknown as applicable.
- The output names open questions, owner and next action.

## Quality checks

- [ ] An independent checker verifies the output against the approved scope and artefact version.
- [ ] No unsupported user, audience, accessibility, performance or business outcome is presented as fact.
- [ ] Responsive, keyboard/focus and reduced-motion needs are included where relevant.

## Pairs with

- Related tools: `skill:ai-tuners`, `skill:ai-wayfinders`, `skill:designing-user-experience`. Use the relevant method or specialist to complete the handoff.
- Engineering owns implementation, general testing, performance and security; Design owns experience intent and craft.

## Limits and cautions

- Not a model capability guarantee. Do not allow overwrite without confirmation; consider privacy, provenance and human verification.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
