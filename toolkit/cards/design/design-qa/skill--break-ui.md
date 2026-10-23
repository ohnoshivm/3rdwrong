---
title: Break UI
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:break-ui
department: design
sub_department: design-qa
job: consistency-qa
role: specialist
trigger: "When verifying a web touchpoint across responsive layouts, interactions, accessibility, and edge cases."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-emilkowalski-skills-mit/skills/break-ui
invoke: "/break-ui"
pairs_with: [skill:3w-brand-consistency-qa, skill:reviewing-interface-quality, skill:accessibility]
---
# Break UI

Break UI is a 3RDWRONG design QA specialist for consistency-qa, activated when verifying a web touchpoint across responsive layouts, interactions, accessibility, and edge cases.

## What it does

- Feeds plausible worst-case data through the same fixture, mock, props or API boundary as demo data.
- Covers realistic long/short names, unbreakable strings, missing fields, counts, empty/one/large lists, translations and scripts.
- Adds a dev-only “Demo data / Worst case” toggle, then inspects the component at its real width, 320px and its widest supported layout.
- Reports each break and proposed fix, then stops; it does not redesign or fix unless asked.

## When to use

- When verifying a web touchpoint across responsive layouts, interactions, accessibility, and edge cases. In practice: after the web touchpoint is implemented and can be exercised.

## When not to use

- Do not use it to critique taste, motion or user flows; use `skill:craft`, `skill:review-animations` or `skill:ux-heuristics-review` for those reviews. Report first and do not fix unless asked.

## Inputs it needs

- The component and its existing demo fixture/props/API boundary, plus field sources and validation limits.
- Intended container sizes, supported breakpoints, and support expectations for zoom, dark mode and RTL.

## How to run it

1. Map every rendered value to its source and schema/API limit; mark missing limits “unbounded”.
2. Build realistic worst-case, empty, one-item and large-list fixtures at the data boundary; add a dev-only toggle.
3. Inspect at the real component width, 320px, the widest supported width and 200% zoom; include RTL/dark mode when supported.
4. Report reproducible breaks and proposed fixes, then stop; only fix when asked.

```text
Use /break-ui on {{component and route}}. Map each rendered value to its source and known limit. Build realistic worst-case, empty, one-item and large-list data at the existing data boundary; expose it only in development. Inspect {{container width}}, 320px, the widest supported width and 200% zoom. Report each observed break and a concrete fix; do not edit the component.
```

## What good output looks like

- Every rendered value has a realistic test value and a documented limit or “unbounded” note.
- The worst-case data enters through the same boundary as demo data; the toggle is dev-only.
- Breaks are evidenced at the component’s real width plus required edge widths; fixes are proposed, not applied.

## Quality checks

- [ ] Worst-case values are plausible or schema-backed; missing limits are marked unbounded.
- [ ] Worst-case fixture enters at the same data boundary as demo data; toggle is development-only.
- [ ] Report distinguishes observed breaks from inferred risks and proposes fixes without applying them.

## Pairs with

- Work with `skill:3w-brand-consistency-qa`, `skill:reviewing-interface-quality`, `skill:accessibility` at the consistency-qa handoff; pass the evidence, unresolved checks and next owner between tools.

## Limits and cautions

- This skill reports breaks and stops before fixing. Respect real backend limits; do not use nonsense values that users could never produce.
- Apply the studio guardrails: no rejected own-identity look (black backgrounds, heavy grotesk, neon; D-0006); motion only when the concept needs it; respect reduced motion and accessibility; keep client data out of the public repository (D-0021).
- Distribution is `vendor`; confirm required installation, sign-in, licence and connectivity before relying on it. Availability records instruction/source presence, not authentication or output quality.
