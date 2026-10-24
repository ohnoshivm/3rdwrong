---
title: Impeccable
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-24
tool_id: skill:impeccable
department: design
sub_department: experience-design
job: ui-design
role: lead
trigger: "Use when the user wants to design, redesign, shape, critique, audit, polish, simplify, harden, animate, or otherwise improve a frontend interface."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-pbakaus-impeccable-apache-2.0/skills/impeccable
invoke: "impeccable skill (Claude Code: /impeccable; Codex: skill name impeccable)"
pairs_with: [frontend-design:frontend-design, skill:web-design-guidelines, skill:emil-design-eng, skill:designing-frontend-interfaces]
---
# Impeccable

The experience-design lead for `ui-design`: a frontend design and critique skill that sets a mode (persuade, operate or read), works through a set of design commands, and checks the rendered result before it is called finished.

## What it does

- Works as an award-level design director: production-grade code, a clear point of view and a deliberate visual world.
- Chooses a mode for the surface (Persuade, Operate, Read or Experience) and scales ambition to it.
- Runs named commands for shaping, critique, audit, polish, hardening, animation and design-system documentation (per its own command table).
- Loads a craft floor before any UI edit and asks for a rendered look at the sizes the work ships at.
- Respects a pinned brief: a clear brief wins over the skill's own taste.

## When to use

- Phase 05 Prototype and Phase 06 Development, for a web or app interface that needs a designed, not templated, result.
- Critique or audit of an existing studio digital touchpoint before a visual sign-off.
- Making a bland screen bolder, or a loud screen quieter, against an approved direction.

## When not to use

- Backend-only or non-UI work.
- Brand identity, mark or colour-system decisions: use the identity-craft specialists first.
- Accessibility certification or production readiness: use `skill:web-design-guidelines` (bench) or engineering QA, and report unverified checks as unverified.
- When the brief or approved direction is missing: stop and ask.

## Inputs it needs

- Surface, audience, goal and mode, plus the approved brief or strategy version.
- Real content, real references and the target sizes or devices.
- Existing project design context (tokens, DESIGN.md) if it exists.

## How to run it

1. Run the skill's context step once per session, as its own `SKILL.md` instructs.
2. Pick the command that matches the request, or follow the new-work playbook for a new surface.
3. Build, then look at the rendered result at desktop, tablet and mobile widths. Fix what one look shows before looking again.
4. Hand the result to an independent checker (maker is not checker).

```text
Use the impeccable skill. Mode: {persuade|operate|read|experience}. Surface: {page or screen}. Approved brief: {link, version}. Goal: {task or decision}. Constraints: {devices, accessibility, motion, performance}. Run the context step, then produce the change, render it at the shipped sizes and report what you verified and what you did not.
```

## What good output looks like

- A mode-appropriate design decision trail that traces back to the brief.
- Rendered evidence (screenshots at the shipped widths) and a list of visual defects found and fixed.
- Unknowns and unverified checks named openly.

## Quality checks

- [ ] An independent reviewer checks the output against the approved brief.
- [ ] Rendered at desktop, tablet and mobile widths, with the console checked.
- [ ] No generic template look, no rejected own-identity vocabulary (D-0006).
- [ ] Motion serves hierarchy or feedback and honours reduced motion.

## Pairs with

- `frontend-design:frontend-design`: specialist for distinctive visual direction on new or reshaped UI.
- `skill:emil-design-eng`: interface polish and motion craft.
- `skill:web-design-guidelines`: bench; consistency review when explicitly requested.
- `skill:designing-frontend-interfaces`: the interface-quality route for building UI.

## Limits and cautions

- Its command launcher runs `npx impeccable` at run time. Review the package and version before running it on client material.
- Apache-2.0 licence; the vendored copy keeps its upstream notice (see `THIRD_PARTY_NOTICES.md`).
- Its own rules forbid loaded symbols as decoration. Apply the same rule in studio work.
- References inspire only; never copy layouts, assets or copy (AGENTS.md).
