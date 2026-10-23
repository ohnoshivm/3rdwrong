---
title: Loading Feedback
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: vectorlab-ux-skills:loaders
department: design
sub_department: experience-design
job: interaction-architecture
role: specialist
trigger: "A measured asynchronous wait needs the correct feedback pattern for its duration."
kind: plugin-skill
availability: claude
distribution: vendor
source: toolkit/vendor/plugin-account-synced-vectorlab-ux-skills-marketplace/skills/feedback/loaders
invoke: "loaders skill (Claude Code plugin `vectorlab-ux-skills`)"
pairs_with: [design-skills:interaction-design, vectorlab-ux-skills:errors]
---
# Loading Feedback

The experience-design specialist for `interaction-architecture` is Loading Feedback (trigger: “A measured asynchronous wait needs the correct feedback pattern for its duration”), which chooses loading feedback based on measured asynchronous wait duration.

## What it does

- Uses no loader for waits under 100 ms.
- inline feedback for 100 ms–1 s.
- skeletons for longer waits.
- guards against flicker and layout shift.

## When to use

- Use when a measured asynchronous wait needs the correct feedback pattern for its duration. Use Phase 05 Prototype after wait timings are measured.
- A measured asynchronous wait needs the correct feedback pattern for its duration.

## When not to use

- Use `design-skills:interaction-design` for broader state and feedback logic.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- Measured wait durations, layout/content shape, cancellation and error behaviour.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use loaders skill (Claude Code plugin `vectorlab-ux-skills`). Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce feedback matches the wait, avoids flash for very short tasks and keeps layout stable for longer ones. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- A wait-state recommendation tied to measured duration and affected content.
- Evidence claims are labelled Documented, Interpretation, Hypothesis or Unknown as applicable.
- The output names open questions, owner and next action.

## Quality checks

- [ ] An independent checker verifies the output against the approved scope and artefact version.
- [ ] No unsupported user, audience, accessibility, performance or business outcome is presented as fact.
- [ ] Responsive, keyboard/focus and reduced-motion needs are included where relevant.

## Pairs with

- Related tools: `design-skills:interaction-design`, `vectorlab-ux-skills:errors`. Use the relevant method or specialist to complete the handoff.
- Engineering owns implementation, general testing, performance and security; Design owns experience intent and craft.

## Limits and cautions

- Measure the actual wait. A skeleton must match the eventual layout; do not imply progress if none is known.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
