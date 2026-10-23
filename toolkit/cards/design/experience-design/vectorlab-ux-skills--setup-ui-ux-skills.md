---
title: Setup UI/UX Skills
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: vectorlab-ux-skills:setup-ui-ux-skills
department: design
sub_department: experience-design
job: ui-design
role: specialist
trigger: "A digital project explicitly adopts VectorLab and needs its one-time reference and access-target setup."
kind: plugin-skill
availability: claude
distribution: vendor
source: toolkit/vendor/plugin-account-synced-vectorlab-ux-skills-marketplace/skills/setup/setup-ui-ux-skills
invoke: "setup-ui-ux-skills skill (Claude Code plugin `vectorlab-ux-skills`)"
pairs_with: [vectorlab-ux-skills:page-patterns, vectorlab-ux-skills:forms]
---
# Setup UI/UX Skills

The experience-design specialist for `ui-design` is Setup UI/UX Skills (trigger: “A digital project explicitly adopts VectorLab and needs its one-time reference and access-target setup”), which sets up the vectorlab project profile that its other ux skills expect.

## What it does

- Scaffolds a project profile for aesthetic reference, banned anti-patterns, accessibility target, voice and icon library.
- Explores existing project guidance, design tokens, UI libraries and icon signals before proposing values.
- Presents findings and a draft profile for confirmation before writing; does not install packages.

## When to use

- Use when a digital project explicitly adopts VectorLab and needs its one-time reference and access-target setup. Do this before using its other skills.
- A digital project explicitly adopts VectorLab and needs its one-time reference and access-target setup.

## When not to use

- Use `vectorlab-ux-skills:page-patterns` or another specific VectorLab skill only after the profile is agreed.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- Project design references, existing styles, accessibility target, brand tone and icon library.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use setup-ui-ux-skills skill (Claude Code plugin `vectorlab-ux-skills`). Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce profile reflects confirmed project decisions and does not invent preferences. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- A project UX profile with confirmed decisions, suitable to guide later VectorLab work.
- Evidence claims are labelled Documented, Interpretation, Hypothesis or Unknown as applicable.
- The output names open questions, owner and next action.

## Quality checks

- [ ] An independent checker verifies the output against the approved scope and artefact version.
- [ ] No unsupported user, audience, accessibility, performance or business outcome is presented as fact.
- [ ] Responsive, keyboard/focus and reduced-motion needs are included where relevant.

## Pairs with

- Related tools: `vectorlab-ux-skills:page-patterns`, `vectorlab-ux-skills:forms`. Use the relevant method or specialist to complete the handoff.
- Engineering owns implementation, general testing, performance and security; Design owns experience intent and craft.

## Limits and cautions

- The source workflow asks for confirmation before editing. Keep client-specific profiles in an appropriate private project store, not the public repo.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
