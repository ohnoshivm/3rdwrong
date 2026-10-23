---
title: Find Animation Opportunities
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:find-animation-opportunities
department: design
sub_department: experience-design
job: motion-principles
role: specialist
trigger: "When identifying motion opportunities, auditing existing motion, or extracting interaction patterns from a supplied reference."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-emilkowalski-skills-mit/skills/find-animation-opportunities
invoke: "find-animation-opportunities skill"
pairs_with: [skill:ceos-motion-direction, skill:improve-animations]
---
# Find Animation Opportunities

The experience-design specialist for `motion-principles` is Find Animation Opportunities (trigger: “When identifying motion opportunities, auditing existing motion, or extracting interaction patterns from a supplied reference”), which identifies where motion could improve hierarchy, feedback or continuity in a supplied interface/reference.

## What it does

- Audits existing motion.
- extracts interaction patterns from references.
- identifies possible motion opportunities and their purpose.

## When to use

- Use when identifying motion opportunities, auditing existing motion, or extracting interaction patterns from a supplied reference. Use Phase 05 Motion after interaction states are known.
- When identifying motion opportunities, auditing existing motion, or extracting interaction patterns from a supplied reference.

## When not to use

- Use `skill:ceos-motion-direction` to specify and govern selected motion.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- Working interface or named reference, user action, approved concept and accessibility constraints.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use find-animation-opportunities skill. Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce each proposed move answers what it communicates; unnecessary movement is omitted. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- A prioritised opportunity list tied to a user action or communication need.
- Evidence claims are labelled Documented, Interpretation, Hypothesis or Unknown as applicable.
- The output names open questions, owner and next action.

## Quality checks

- [ ] An independent checker verifies the output against the approved scope and artefact version.
- [ ] No unsupported user, audience, accessibility, performance or business outcome is presented as fact.
- [ ] Responsive, keyboard/focus and reduced-motion needs are included where relevant.

## Pairs with

- Related tools: `skill:ceos-motion-direction`, `skill:improve-animations`. Use the relevant method or specialist to complete the handoff.
- Engineering owns implementation, general testing, performance and security; Design owns experience intent and craft.

## Limits and cautions

- A reference is inspiration, not a template. Respect the approved concept, reduced motion and studio originality rules.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
