---
title: Figma Use Motion
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: figma:figma-use-motion
department: design
sub_department: experience-design
job: motion-principles
role: specialist
trigger: "A Figma file/workspace exists or is explicitly requested, and the task requires use motion. Load this prerequisite only for its corresponding Figma operation."
kind: plugin-skill
availability: both
distribution: fetch
source: /Users/hustle/.claude/plugins/cache/claude-plugins-official/figma/2.2.120/skills-figquery/figma-use-motion/SKILL.md
invoke: "figma-use-motion skill (Claude Code plugin `figma`)"
pairs_with: [skill:ceos-motion-direction, skill:animate]
---
# Figma Use Motion

The experience-design specialist for `motion-principles` is Figma Use Motion (trigger: “A Figma file/workspace exists or is explicitly requested, and the task requires use motion. Load this prerequisite only for its corresponding Figma operation”), which supplies motion-specific figma plugin api guidance for inspecting and editing node animations.

## What it does

- Covers manual keyframes, animation styles, easing and timeline duration.
- points to motion references.
- sets preflight and verification rules.

## When to use

- Use when a Figma file/workspace exists or is requested and the task requires use motion. Load with `figma-use` for that operation.
- A Figma file/workspace exists or is explicitly requested, and the task requires use motion. Load this prerequisite only for its corresponding Figma operation.

## When not to use

- Use `skill:ceos-motion-direction` for the motion concept and web implementation specification.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- Figma Design file, target nodes, intended motion behaviour, Figma MCP and `figma-use` guidance.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use figma-use-motion skill (Claude Code plugin `figma`). Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce correct public api names and timeline units; reduced-motion and rendered-frame checks are addressed. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- A motion edit using the public API fields, with duration/easing and frame verification when needed.
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

- Motion API may be gated by the `metronome` user feature flag. Creating a new animation-style preset is explicitly out of scope; fetch distribution and Figma access apply.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
