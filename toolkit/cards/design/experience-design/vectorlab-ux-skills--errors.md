---
title: Error Recovery Copy
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: vectorlab-ux-skills:errors
department: design
sub_department: experience-design
job: ux-writing
role: specialist
trigger: "A defined failure state needs blame-free recovery copy."
kind: plugin-skill
availability: claude
distribution: vendor
source: toolkit/vendor/plugin-account-synced-vectorlab-ux-skills-marketplace/skills/voice/errors
invoke: "errors skill (Claude Code plugin `vectorlab-ux-skills`)"
pairs_with: [design-skills:ux-writing, vectorlab-ux-skills:verbs]
---
# Error Recovery Copy

The experience-design specialist for `ux-writing` is Error Recovery Copy (trigger: “A defined failure state needs blame-free recovery copy”), which writes blame-free error messages with a clear recovery action.

## What it does

- Distinguishes failure context.
- avoids blaming users.
- makes the next step explicit and preserves trust.

## When to use

- Use when a defined failure state needs blame-free recovery copy. Use Phase 05 Prototype while failure states and copy are being designed.
- A defined failure state needs blame-free recovery copy.

## When not to use

- Use `design-skills:ux-writing` for consistent multi-state copy or `vectorlab-ux-skills:forms` for validation behaviour.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- Failure cause, what user was attempting, available recovery and voice.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use errors skill (Claude Code plugin `vectorlab-ux-skills`). Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce message explains what failed and what the user can do; no false promise or user blame. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- An error string with cause/context and a concrete recovery action.
- Evidence claims are labelled Documented, Interpretation, Hypothesis or Unknown as applicable.
- The output names open questions, owner and next action.

## Quality checks

- [ ] An independent checker verifies the output against the approved scope and artefact version.
- [ ] No unsupported user, audience, accessibility, performance or business outcome is presented as fact.
- [ ] Responsive, keyboard/focus and reduced-motion needs are included where relevant.

## Pairs with

- Related tools: `design-skills:ux-writing`, `vectorlab-ux-skills:verbs`. Use the relevant method or specialist to complete the handoff.
- Engineering owns implementation, general testing, performance and security; Design owns experience intent and craft.

## Limits and cautions

- Do not fabricate causes. If the system cannot identify the cause, say so clearly; review alongside support and privacy needs.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
