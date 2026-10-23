---
title: AI Tuners
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:ai-tuners
department: design
sub_department: experience-design
job: interaction-architecture
role: specialist
trigger: "When the approved scope specifically requires designing AI inputs, controls, onboarding, or discoverability in an AI product."
kind: skill
availability: codex
distribution: manual
source: /Users/hustle/.agents/skills/ai-tuners/SKILL.md
invoke: "ai-tuners skill"
pairs_with: [skill:ai-inputs, skill:ai-wayfinders]
---
# AI Tuners

The experience-design specialist for `interaction-architecture` is AI Tuners (trigger: “When the approved scope specifically requires designing AI inputs, controls, onboarding, or discoverability in an AI product”), which designs controls that let users shape how an ai feature interprets input and produces output.

## What it does

- Covers attachments, connectors, filters, model management, modes, parameters, preset/saved styles and voice/tone.
- makes active constraints visible.
- identifies connector trust and recovery risks.

## When to use

- Use when the approved scope specifically requires designing AI inputs, controls, onboarding, or discoverability in an AI product. Use Phase 04 Concept before controls are implemented.
- When the approved scope specifically requires designing AI inputs, controls, onboarding, or discoverability in an AI product.

## When not to use

- Use `skill:ai-inputs` for the input surface and `skill:ai-wayfinders` for discovery and first interaction.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- User intent, data sources, available model choices, permissions, risk and desired degree of control.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use ai-tuners skill. Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce controls are understandable and visible; connectors are scoped/revocable; failures and empty results have recovery. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- A control model that exposes relevant settings without requiring prompt-engineering knowledge.
- Evidence claims are labelled Documented, Interpretation, Hypothesis or Unknown as applicable.
- The output names open questions, owner and next action.

## Quality checks

- [ ] An independent checker verifies the output against the approved scope and artefact version.
- [ ] No unsupported user, audience, accessibility, performance or business outcome is presented as fact.
- [ ] Responsive, keyboard/focus and reduced-motion needs are included where relevant.

## Pairs with

- Related tools: `skill:ai-inputs`, `skill:ai-wayfinders`. Use the relevant method or specialist to complete the handoff.
- Engineering owns implementation, general testing, performance and security; Design owns experience intent and craft.

## Limits and cautions

- Connected data is untrusted and may contain prompt injection. Do not imply integrations or model choices exist unless product facts confirm them.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
