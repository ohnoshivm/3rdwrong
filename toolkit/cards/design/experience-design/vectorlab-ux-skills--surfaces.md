---
title: Interaction Surfaces
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: vectorlab-ux-skills:surfaces
department: design
sub_department: experience-design
job: interaction-architecture
role: specialist
trigger: "A specified edit flow needs a decision between inline editing, a drawer or a dedicated page."
kind: plugin-skill
availability: claude
distribution: vendor
source: toolkit/vendor/plugin-account-synced-vectorlab-ux-skills-marketplace/skills/interaction/surfaces
invoke: "surfaces skill (Claude Code plugin `vectorlab-ux-skills`)"
pairs_with: [vectorlab-ux-skills:page-patterns, skill:ceos-interaction-architecture]
---
# Interaction Surfaces

The experience-design specialist for `interaction-architecture` is Interaction Surfaces (trigger: “A specified edit flow needs a decision between inline editing, a drawer or a dedicated page”), which chooses between inline editing, a drawer or a dedicated page for a defined edit flow.

## What it does

- Routes quick edits to inline surfaces and longer work to a page.
- requires named confirmation for destructive actions.
- protects layout stability.

## When to use

- Use when a specified edit flow needs a decision between inline editing, a drawer or a dedicated page. Use Phase 05 Prototype before building the surface.
- A specified edit flow needs a decision between inline editing, a drawer or a dedicated page.

## When not to use

- Use `vectorlab-ux-skills:page-patterns` if the decision is a page; use `skill:ceos-interaction-architecture` for full focus/route rules.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- Task length, amount of context needed, edit reversibility, destructive risk and route structure.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use surfaces skill (Claude Code plugin `vectorlab-ux-skills`). Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce surface preserves context appropriately, returns focus and confirms destructive actions by name. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- A surface decision with entry, exit, focus and destructive-action behaviour.
- Evidence claims are labelled Documented, Interpretation, Hypothesis or Unknown as applicable.
- The output names open questions, owner and next action.

## Quality checks

- [ ] An independent checker verifies the output against the approved scope and artefact version.
- [ ] No unsupported user, audience, accessibility, performance or business outcome is presented as fact.
- [ ] Responsive, keyboard/focus and reduced-motion needs are included where relevant.

## Pairs with

- Related tools: `vectorlab-ux-skills:page-patterns`, `skill:ceos-interaction-architecture`. Use the relevant method or specialist to complete the handoff.
- Engineering owns implementation, general testing, performance and security; Design owns experience intent and craft.

## Limits and cautions

- Check focus management and escape/return path; page pattern must be named before writing a page.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
