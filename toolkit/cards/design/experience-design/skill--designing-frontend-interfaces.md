---
title: Designing Frontend Interfaces
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:designing-frontend-interfaces
department: design
sub_department: experience-design
job: ui-design
role: specialist
trigger: "When the approved scope specifically requires designing or restyling web interfaces with distinctive visual direction."
kind: skill
availability: both
distribution: manual
source: /Users/hustle/.config/opencode/skills/designing-frontend-interfaces/SKILL.md
invoke: "designing-frontend-interfaces skill"
pairs_with: [frontend-design:frontend-design, skill:designing-user-experience, skill:ceos-motion-direction]
---
# Designing Frontend Interfaces

The experience-design specialist for `ui-design` is Designing Frontend Interfaces (trigger: “When the approved scope specifically requires designing or restyling web interfaces with distinctive visual direction”), which builds or restyles a web interface from an explicit visual brief and locked design tokens.

## What it does

- Requires brief before components.
- commits to one aesthetic and token system.
- works through skeleton, components, self-review and rendered visual verification.

## When to use

- Use when the approved scope specifically requires designing or restyling web interfaces with distinctive visual direction. Use Phase 04 Art Direction before implementation starts.
- When the approved scope specifically requires designing or restyling web interfaces with distinctive visual direction.

## When not to use

- Use `skill:designing-user-experience` for non-trivial flow/state; `building-accessible-interfaces` before shipping.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- Purpose, audience, tone, reference, palette intent, type roles, constraints and content.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use designing-frontend-interfaces skill. Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce css values derive from the chosen tokens; the design is subject-specific; real renders were reviewed. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- A brief, token block and visually inspected responsive UI with purposeful restraint.
- Evidence claims are labelled Documented, Interpretation, Hypothesis or Unknown as applicable.
- The output names open questions, owner and next action.

## Quality checks

- [ ] An independent checker verifies the output against the approved scope and artefact version.
- [ ] No unsupported user, audience, accessibility, performance or business outcome is presented as fact.
- [ ] Responsive, keyboard/focus and reduced-motion needs are included where relevant.

## Pairs with

- Related tools: `frontend-design:frontend-design`, `skill:designing-user-experience`, `skill:ceos-motion-direction`. Use the relevant method or specialist to complete the handoff.
- Engineering owns implementation, general testing, performance and security; Design owns experience intent and craft.

## Limits and cautions

- Do not follow its example palette blindly. Avoid generic visual defaults and D-0006 rejected own-identity look; respect reduced motion and accessibility.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
