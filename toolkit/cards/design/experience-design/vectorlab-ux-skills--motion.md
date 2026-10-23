---
title: Motion Tokens
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: vectorlab-ux-skills:motion
department: design
sub_department: experience-design
job: motion-principles
role: specialist
trigger: "An approved digital interaction needs consistent duration/easing tokens."
kind: plugin-skill
availability: claude
distribution: vendor
source: toolkit/vendor/plugin-account-synced-vectorlab-ux-skills-marketplace/skills/animation/motion
invoke: "motion skill (Claude Code plugin `vectorlab-ux-skills`)"
pairs_with: [skill:ceos-motion-direction, skill:animate]
---
# Motion Tokens

The experience-design specialist for `motion-principles` is Motion Tokens (trigger: “An approved digital interaction needs consistent duration/easing tokens”), which defines consistent duration/easing tokens and allowed animation properties for an approved interaction.

## What it does

- Sets reusable timing and easing.
- recommends animatable properties.
- discourages layout animation and decorative motion.

## When to use

- Use when an approved digital interaction needs consistent duration/easing tokens. Use Phase 05 Motion before implementation.
- An approved digital interaction needs consistent duration/easing tokens.

## When not to use

- Use `skill:ceos-motion-direction` for coordinated motion and `skill:animate` for a bounded movement.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- Approved interaction, existing token conventions, property changes and reduced-motion needs.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use motion skill (Claude Code plugin `vectorlab-ux-skills`). Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce tokens are reused; motion clarifies change; expensive layout animation is avoided. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- A token set and application rules aligned to the interaction and reduced-motion behaviour.
- Evidence claims are labelled Documented, Interpretation, Hypothesis or Unknown as applicable.
- The output names open questions, owner and next action.

## Quality checks

- [ ] An independent checker verifies the output against the approved scope and artefact version.
- [ ] No unsupported user, audience, accessibility, performance or business outcome is presented as fact.
- [ ] Responsive, keyboard/focus and reduced-motion needs are included where relevant.

## Pairs with

- Related tools: `skill:ceos-motion-direction`, `skill:animate`. Use the relevant method or specialist to complete the handoff.
- Engineering owns implementation, general testing, performance and security; Design owns experience intent and craft.

## Limits and cautions

- Use motion only where it serves the concept or feedback; honour reduced motion and test performance.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
