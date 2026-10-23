---
title: Figma Generate Design
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: figma:figma-generate-design
department: design
sub_department: experience-design
job: ui-design
role: specialist
trigger: "A Figma file/workspace exists or is explicitly requested, and the task requires generate design. Load this prerequisite only for its corresponding Figma operation."
kind: plugin-skill
availability: both
distribution: fetch
source: /Users/hustle/.claude/plugins/cache/claude-plugins-official/figma/2.2.120/skills-figquery/figma-generate-design/SKILL.md
invoke: "figma-generate-design skill (Claude Code plugin `figma`)"
pairs_with: [frontend-design:frontend-design, skill:designing-frontend-interfaces]
---
# Figma Generate Design

The experience-design specialist for `ui-design` is Figma Generate Design (trigger: “A Figma file/workspace exists or is explicitly requested, and the task requires generate design. Load this prerequisite only for its corresponding Figma operation”), which builds or updates a composed figma screen by reusing the published design system.

## What it does

- Discovers components, variables and styles from Code Connect, screens and library search.
- assembles views incrementally.
- supports web-app generation workflow when available.

## When to use

- Use when a Figma file/workspace exists or is requested and the operation is generate design. Load only for that Figma operation.
- A Figma file/workspace exists or is explicitly requested, and the task requires generate design. Load this prerequisite only for its corresponding Figma operation.

## When not to use

- Use `frontend-design:frontend-design` to establish visual direction before transfer; use Figma’s base `figma-use` skill for Plugin API operations.
- Do not use it to approve its own work; have an independent reviewer check the artefact.

## Inputs it needs

- Figma Design file, code or view description, published components/variables/styles, access to relevant Figma tools.
- Versioned approved brief/strategy and source links; mark draft material as formative.

## How to run it

1. Confirm the trigger, stage and source material; keep client data in the approved private store.
2. Run it using the invocation above and provide the required inputs.
3. Check the output against the quality checks; hand unresolved decisions to the named human owner.

```text
Use figma-generate-design skill (Claude Code plugin `figma`). Studio phase: {phase}. Project: {project}. Approved goal/strategy: {goal and source}. Scope: {screen, flow or interaction}. Inputs/evidence: {links and versions}. Constraints: {platform, accessibility, motion, privacy}. Produce existing system assets are reused; hard-coded primitives are avoided where system assets exist; changed nodes are inspectable. Keep documented facts separate from interpretation and hypothesis; list unknowns and the next human decision.
```

## What good output looks like

- A Figma screen or view composed with system tokens and reusable components, plus a clear gap list.
- Evidence claims are labelled Documented, Interpretation, Hypothesis or Unknown as applicable.
- The output names open questions, owner and next action.

## Quality checks

- [ ] An independent checker verifies the output against the approved scope and artefact version.
- [ ] No unsupported user, audience, accessibility, performance or business outcome is presented as fact.
- [ ] Responsive, keyboard/focus and reduced-motion needs are included where relevant.

## Pairs with

- Related tools: `frontend-design:frontend-design`, `skill:designing-frontend-interfaces`. Use the relevant method or specialist to complete the handoff.
- Engineering owns implementation, general testing, performance and security; Design owns experience intent and craft.

## Limits and cautions

- Fetch distribution requires installation and Figma sign-in/MCP access. Source specifies `figma-use` as a prerequisite; this skill alone is not the API connection.
- Respect the tool distribution: vendor copies are repo snapshots; fetch/manual sources need their stated install or sign-in.
- Client data, personal data and credentials stay out of the public repository.
- Motion is purposeful and honours reduced motion; avoid the rejected own-identity vocabulary in D-0006.
