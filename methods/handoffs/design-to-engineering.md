---
title: "Handoff: design to engineering (pod contract)"
type: checklist
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Handoff: design to engineering (pod contract)

Design and Engineering are one pod from day one; this contract names what Design supplies so Engineering can build without guessing, and what Engineering returns so Design can judge in the browser. It is first signed before the prototype (DX-03 → DX-04, or identity 06 when digital applications are in scope) and kept live through DX-06: every change to an item is versioned and re-acknowledged. The [Digital Experience offer](../../studio/digital-experience-offer.md#proposed-phases-and-paired-pods) names the same contents.

- **Design side:** `agent:creative-director` (intent), `agent:visual-designer` (tokens, type), `agent:ui-ux-architect` (layouts, states).
- **Engineering side:** `agent:frontend-architect` (architecture, token mapping), `agent:motion-director` and `agent:3d-webgl-engineer` (motion and scenes), `agent:performance-engineer` (budgets).
- **Acceptance checker:** `agent:frontend-architect` checks buildability; `agent:creative-auditor` checks that Engineering's prototype matches the intent. Neither checks its own side.

## Artefact checklist (Design supplies)

### Spec

- [ ] Concept sentence and the signature-moment list, each moment with its purpose, reduced-motion alternative and no-WebGL alternative (from DX-02).
- [ ] Sitemap, template inventory and key templates at desktop, tablet and mobile widths with real content.
- [ ] Component inventory with every state: default, hover, focus, active, disabled, loading, error, empty.
- [ ] Responsive rules: breakpoints, reflow behaviour, what changes and what stays fixed.
- [ ] Content and UX writing for every state; CMS-editable fields marked.

### Tokens

- [ ] Design tokens as data (JSON), versioned: spacing scale, type scale, colour roles with contrast pairs, radii, shadows or materials, motion durations and easings, breakpoints.
- [ ] Contrast results for every text and interface pair against [web standards](../quality/web-standards.md#accessibility).
- [ ] Fonts with licence terms for web use; subsets and weights actually needed.
- [ ] Human-led typography, colour and composition decisions checked through [`skill:3w-typography-system`](../../toolkit/cards/design/identity-craft/skill--3w-typography-system.md), [`skill:3w-colour-system`](../../toolkit/cards/design/identity-craft/skill--3w-colour-system.md) and [`skill:3w-composition-system`](../../toolkit/cards/design/identity-craft/skill--3w-composition-system.md); mark variants through [`skill:3w-mark-exploration`](../../toolkit/cards/design/identity-craft/skill--3w-mark-exploration.md) where scoped. `agent:visual-designer` translates the chosen system into digital tokens.

### Motion principles

- [ ] Motion language: what motion means in this experience, which properties move, durations and easings by role.
- [ ] Choreography notes per signature moment: trigger, sequence, end state.
- [ ] Reduced-motion behaviour that keeps the same information and order.

### Interaction intent

- [ ] For each interaction: what it helps the user understand or do (one line), input methods (pointer, touch, keyboard), and focus behaviour.
- [ ] Error, empty and loading behaviour.
- [ ] What must never happen: scroll traps, broken browser find, colour-only meaning.

### Assets

- [ ] Image, video, 3D and sound assets in production formats, with rights and AI-consent status (D-0023).

## Artefact checklist (Engineering returns)

- [ ] Feasibility rating and cost note per signature moment (at DX-02).
- [ ] Token mapping: how each token is named and consumed in code.
- [ ] Stack decision with native scrolling or the single smooth-scroll engine named; no engine is required by default.
- [ ] The prototype (DX-04) on a private preview URL, screenshots at three widths and a recording.
- [ ] Measured numbers and the proposed budget table in `qa/README.md`, at or under [D-0023](../../studio/decisions/0023-commercial-and-delivery-defaults.md): mobile p75 LCP ≤ 2.0 s, INP ≤ 200 ms, CLS ≤ 0.1, ≤ 2 MB before first interaction, 60 fps target on a mid-range phone, complete reduced-motion fallback. Any looser value is flagged for a founder exception.

## Acceptance checks

- [ ] Engineering can build every template and state without inventing a missing rule.
- [ ] Tokens are frozen for the prototype; later changes go through change control.
- [ ] Design has judged the prototype in a real browser on target hardware, not in a mock-up.
- [ ] Design and Engineering leads jointly agree budgets and fallbacks (gate DX-04).
- [ ] Quality Lab's paired `creative-prototyping`, `interaction-architecture` and `web-vitals` cases have pre-client results; judge differs from every maker and the human spot-check is recorded. Stage-specific pilot output is inspected under `evals/pilot/README.md`.

## Return conditions

Return to Design when a state, breakpoint, token or interaction intent is missing, or contrast fails. Return to Engineering when the prototype misses intent, exceeds budget without a proposed exception, or lacks a working fallback.

## Record

One handoff row in `decisions.md` per version of this contract ([format](README.md#handoff-record)).
