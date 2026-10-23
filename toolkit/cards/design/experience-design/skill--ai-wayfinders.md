---
title: AI Wayfinders
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:ai-wayfinders
department: design
sub_department: experience-design
job: interaction-architecture
role: specialist
trigger: "When the approved scope specifically requires designing AI inputs, controls, onboarding, or discoverability in an AI product."
kind: skill
availability: codex
distribution: manual
source: /Users/hustle/.agents/skills/ai-wayfinders/SKILL.md
invoke: "ai-wayfinders skill"
pairs_with: [skill:ai-inputs, skill:ai-tuners]
---
# AI Wayfinders

The experience-design specialist for `interaction-architecture` is AI Wayfinders (trigger: “When the approved scope specifically requires designing AI inputs, controls, onboarding, or discoverability in an AI product”), which designs first-use guidance that helps people discover and start useful ai interactions.

## What it does

- Covers initial CTAs, example galleries, suggestions, templates, nudges, follow-ups, prompt details and randomise.
- keeps suggestions contextual.
- makes examples actionable.

## When to use

- Use when the approved scope specifically requires designing AI inputs, controls, onboarding, or discoverability in an AI product. Use Phase 04 Concept for blank-slate or discoverability problems.
- When the approved scope specifically requires designing AI inputs, controls, onboarding, or discoverability in an AI product.

## When not to use

- Use `skill:ai-inputs` for the actual input pattern or `skill:ai-tuners` for configuration controls.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- AI feature capability, user task/context, examples grounded in real product behaviour and available data.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use ai-wayfinders skill. Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce users can start without inventing a prompt; examples are usable and the interaction is scoped. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- A first-use surface with a clear entry point and relevant next steps.
- Evidence claims are labelled Documented, Interpretation, Hypothesis or Unknown as applicable.
- The output names open questions, owner and next action.

## Quality checks

- [ ] An independent checker verifies the output against the approved scope and artefact version.
- [ ] No unsupported user, audience, accessibility, performance or business outcome is presented as fact.
- [ ] Responsive, keyboard/focus and reduced-motion needs are included where relevant.

## Pairs with

- Related tools: `skill:ai-inputs`, `skill:ai-tuners`. Use the relevant method or specialist to complete the handoff.
- Engineering owns implementation, general testing, performance and security; Design owns experience intent and craft.

## Limits and cautions

- Do not promise capabilities unsupported by the product or show ungrounded example outcomes. Keep nudges optional and non-coercive.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
