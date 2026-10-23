---
title: Apple Design Motion Patterns
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:apple-design
department: design
sub_department: experience-design
job: motion-principles
role: specialist
trigger: "When defining motion purpose, timing, easing, choreography, and reduced-motion behavior."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-emilkowalski-skills-mit/skills/apple-design
invoke: "apple-design skill"
pairs_with: [skill:ceos-motion-direction, skill:animate]
---
# Apple Design Motion Patterns

The experience-design specialist for `motion-principles` is Apple Design Motion Patterns (trigger: “When defining motion purpose, timing, easing, choreography, and reduced-motion behavior”), which applies apple-platform motion guidance and spring behaviour to interface interactions.

## What it does

- Describes damping and response for spring motion.
- recommends critically damped defaults.
- explains velocity handoff and momentum projection for gestures.

## When to use

- Use when defining motion purpose, timing, easing, choreography, and reduced-motion behavior for an Apple-platform interaction.
- When defining motion purpose, timing, easing, choreography, and reduced-motion behavior.

## When not to use

- Use `skill:ceos-motion-direction` for cross-platform motion direction and reduced-motion system.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- Target Apple platform, interaction, gesture velocity/target and system constraints.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use apple-design skill. Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce spring parameters match the interaction’s physical cause and avoid gratuitous bounce. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- A platform-aware motion proposal with spring behaviour tied to how the gesture ends.
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

- Use Apple-specific recommendations only where platform-appropriate. Verify current platform behaviour and provide reduced-motion alternatives.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
