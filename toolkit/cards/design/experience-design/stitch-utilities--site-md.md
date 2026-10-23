---
title: Stitch SITE.md
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: stitch-utilities:site-md
department: design
sub_department: experience-design
job: interaction-architecture
role: specialist
trigger: "Use when the approved work needs this capability: Analyze a project description or site requirements and synthesize a project constitution into SITE.md for the Stitch Build Loop"
kind: plugin-skill
availability: claude
distribution: vendor
source: toolkit/vendor/plugin-google-labs-code-stitch-skills-stitch-utilities-0337446dadde/skills/site-md
invoke: "site-md skill (Claude Code plugin `stitch-utilities`)"
pairs_with: [skill:designing-user-experience, frontend-design:frontend-design]
---
# Stitch SITE.md

The experience-design specialist for `interaction-architecture` is Stitch SITE.md (trigger: “Use when the approved work needs this capability: Analyze a project description or site requirements and synthesize a project constitution into SITE.md for the Stitch Build Loop”), which creates a project constitution file for the stitch build loop from approved requirements or existing site content.

## What it does

- Synthesises core identity and visual language.
- records architecture, live sitemap and roadmap.
- provides a persistent project reference.

## When to use

- Use when the approved work needs a project constitution for the Stitch Build Loop. Use Phase 04 Architecture before Stitch implementation.
- Use when the approved work needs this capability: Analyze a project description or site requirements and synthesize a project constitution into SITE.md for the Stitch Build Loop

## When not to use

- Use `skill:designing-user-experience` to define the experience and `frontend-design:frontend-design` to set visual direction.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- Project description or requirements, approved identity and visual direction, architecture constraints, site content.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use site-md skill (Claude Code plugin `stitch-utilities`). Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce the file states only agreed decisions; gaps remain explicit; sitemap and roadmap reflect the approved scope. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- A scoped `.stitch/SITE.md` aligned to approved project requirements.
- Evidence claims are labelled Documented, Interpretation, Hypothesis or Unknown as applicable.
- The output names open questions, owner and next action.

## Quality checks

- [ ] An independent checker verifies the output against the approved scope and artefact version.
- [ ] No unsupported user, audience, accessibility, performance or business outcome is presented as fact.
- [ ] Responsive, keyboard/focus and reduced-motion needs are included where relevant.

## Pairs with

- Related tools: `skill:designing-user-experience`, `frontend-design:frontend-design`. Use the relevant method or specialist to complete the handoff.
- Engineering owns implementation, general testing, performance and security; Design owns experience intent and craft.

## Limits and cautions

- Claude plugin skill; availability/access may require plugin install. Do not treat a generated constitution as strategy approval.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
