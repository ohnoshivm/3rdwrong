---
title: Icon Buttons
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: vectorlab-ux-skills:icon-buttons
department: design
sub_department: experience-design
job: interaction-architecture
role: specialist
trigger: "A supplied toolbar needs icon-only controls with labels, tooltips and shortcuts."
kind: plugin-skill
availability: claude
distribution: vendor
source: toolkit/vendor/plugin-account-synced-vectorlab-ux-skills-marketplace/skills/interaction/icon-buttons
invoke: "icon-buttons skill (Claude Code plugin `vectorlab-ux-skills`)"
pairs_with: [vectorlab-ux-skills:labels, skill:building-accessible-interfaces]
---
# Icon Buttons

The experience-design specialist for `interaction-architecture` is Icon Buttons (trigger: “A supplied toolbar needs icon-only controls with labels, tooltips and shortcuts”), which specifies when a toolbar control can become icon-only and requires an accessible name and tooltip.

## What it does

- Checks whether the icon is conventional.
- requires tooltip and focus visibility.
- includes a shortcut label when one exists.

## When to use

- Use when a supplied toolbar needs icon-only controls with labels, tooltips and shortcuts. Use Phase 05 Prototype when refining dense toolbar chrome.
- A supplied toolbar needs icon-only controls with labels, tooltips and shortcuts.

## When not to use

- Use `skill:building-accessible-interfaces` for broader accessibility review.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- Existing toolbar, actions, icon library, shortcuts and input modes.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use icon-buttons skill (Claude Code plugin `vectorlab-ux-skills`). Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce each icon-only control is understandable by sight, keyboard and assistive technology. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- A toolbar mapping with icon, accessible name, tooltip and shortcut where applicable.
- Evidence claims are labelled Documented, Interpretation, Hypothesis or Unknown as applicable.
- The output names open questions, owner and next action.

## Quality checks

- [ ] An independent checker verifies the output against the approved scope and artefact version.
- [ ] No unsupported user, audience, accessibility, performance or business outcome is presented as fact.
- [ ] Responsive, keyboard/focus and reduced-motion needs are included where relevant.

## Pairs with

- Related tools: `vectorlab-ux-skills:labels`, `skill:building-accessible-interfaces`. Use the relevant method or specialist to complete the handoff.
- Engineering owns implementation, general testing, performance and security; Design owns experience intent and craft.

## Limits and cautions

- Do not remove visible text if the icon is ambiguous. Tooltips must also be available on keyboard focus.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
