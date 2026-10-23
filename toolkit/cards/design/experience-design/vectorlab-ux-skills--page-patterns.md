---
title: Page Patterns
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: vectorlab-ux-skills:page-patterns
department: design
sub_department: experience-design
job: ui-design
role: specialist
trigger: "A digital screen lacks a named structural pattern and the adopted product system needs one."
kind: plugin-skill
availability: claude
distribution: vendor
source: toolkit/vendor/plugin-account-synced-vectorlab-ux-skills-marketplace/skills/interaction/page-patterns
invoke: "page-patterns skill (Claude Code plugin `vectorlab-ux-skills`)"
pairs_with: [design-superpowers:design, skill:designing-user-experience]
---
# Page Patterns

The experience-design specialist for `ui-design` is Page Patterns (trigger: “A digital screen lacks a named structural pattern and the adopted product system needs one”), which names one structural page pattern before a new digital screen is built.

## What it does

- Names one of ten product page patterns or a marketing route type before markup.
- Distinguishes page structure from app chrome, widgets, empty states and view modes.
- Requires a pattern-specific anatomy and preserves that pattern in empty/loading/error states.

## When to use

- Use when a digital screen lacks a named structural pattern and the adopted product system needs one. Use Phase 05 Prototype before page markup.
- A digital screen lacks a named structural pattern and the adopted product system needs one.

## When not to use

- Use `design-superpowers:design` when choosing existing system components and patterns.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- Screen goal, content density, primary task, system conventions and responsive context.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use page-patterns skill (Claude Code plugin `vectorlab-ux-skills`). Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce a single pattern fits the page’s main job; widgets do not become the structure by accident. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- One named page pattern with a rationale before markup begins.
- Evidence claims are labelled Documented, Interpretation, Hypothesis or Unknown as applicable.
- The output names open questions, owner and next action.

## Quality checks

- [ ] An independent checker verifies the output against the approved scope and artefact version.
- [ ] No unsupported user, audience, accessibility, performance or business outcome is presented as fact.
- [ ] Responsive, keyboard/focus and reduced-motion needs are included where relevant.

## Pairs with

- Related tools: `design-superpowers:design`, `skill:designing-user-experience`. Use the relevant method or specialist to complete the handoff.
- Engineering owns implementation, general testing, performance and security; Design owns experience intent and craft.

## Limits and cautions

- Only use when the project adopts this toolkit. Confirm `.ux-profile.md` exists or read the setup guidance; avoid ungrounded layout choices.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
