---
title: Scroll World Storytelling
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:scroll-world-storytelling
department: design
sub_department: experience-design
job: motion-principles
role: specialist
trigger: "The approved concept specifically calls for this effect: scroll-world-storytelling."
kind: skill
availability: claude
distribution: manual
source: /Users/hustle/.claude/skills-library/master-of-20261021/effects-3d/scroll-world-storytelling/SKILL.md
invoke: "scroll-world-storytelling skill"
pairs_with: [skill:ceos-motion-direction, skill:ceos-interaction-architecture]
---
# Scroll World Storytelling

The experience-design specialist for `motion-principles` is Scroll World Storytelling (trigger: “The approved concept specifically calls for this effect: scroll-world-storytelling”), which develops a scroll-led narrative scene when the approved concept depends on spatial or world-like progression.

## What it does

- Turns source material into a connected scroll-driven journey with deliberate story beats.
- Selects one primary renderer: scrubbed video, a Three.js world, or semantic HTML/SVG/data/type.
- Requires a source-preserving story map, one action and fallbacks for native scroll, mobile and reduced motion.

## When to use

- Use only when the approved concept specifically calls for this effect: scroll-world-storytelling. Use Phase 05 Prototype after the story and non-scroll route are clear.
- The approved concept specifically calls for this effect: scroll-world-storytelling.

## When not to use

- Use `skill:ceos-motion-direction` for motion engineering and `skill:ceos-interaction-architecture` to keep navigation and scroll operable.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- Approved narrative, content order, scene concept, target devices and accessibility requirements.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use scroll-world-storytelling skill. Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce scroll progression clarifies the story; native scroll, keyboard and reduced-motion alternatives remain usable. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- A scroll sequence with content purpose, progression, interaction and fallback.
- Evidence claims are labelled Documented, Interpretation, Hypothesis or Unknown as applicable.
- The output names open questions, owner and next action.

## Quality checks

- [ ] An independent checker verifies the output against the approved scope and artefact version.
- [ ] No unsupported user, audience, accessibility, performance or business outcome is presented as fact.
- [ ] Responsive, keyboard/focus and reduced-motion needs are included where relevant.

## Pairs with

- Related tools: `skill:ceos-motion-direction`, `skill:ceos-interaction-architecture`. Use the relevant method or specialist to complete the handoff.
- Engineering owns implementation, general testing, performance and security; Design owns experience intent and craft.

## Limits and cautions

- This is a specialised effect, not a default site treatment. Do not hijack scrolling or create a second scroll engine; local manual source.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
