---
title: UI styling (shadcn/ui and Tailwind)
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-24
tool_id: ui-ux-pro-max:ui-styling
department: design
sub_department: experience-design
job: ui-design
role: specialist
trigger: "Use when building user interfaces, implementing design systems, creating responsive layouts, adding accessible components, or customising themes and dark mode."
kind: plugin-skill
availability: both
distribution: vendor
source: toolkit/vendor/plugin-ui-ux-pro-max-skill-ui-ux-pro-max-2.13.0/.claude/skills/ui-styling
invoke: "ui-styling skill (from the ui-ux-pro-max plugin)"
pairs_with: [skill:impeccable, frontend-design:frontend-design, ui-ux-pro-max:ui-ux-pro-max, skill:building-accessible-interfaces]
---
# UI styling (shadcn/ui and Tailwind)

A specialist for implementing UI with shadcn/ui components on Radix primitives and Tailwind utility styling, including tokens, themes, dark mode and responsive layout. Use it when the design is decided and the build must be consistent.

## What it does

- Builds accessible components (dialogs, forms, tables, navigation) from shadcn/ui and Radix.
- Sets up Tailwind utility styling and a token-based theme, including dark mode.
- Covers responsive, mobile-first layout and reusable styling patterns.
- Points to the upstream shadcn/ui and Tailwind references for current APIs.

## When to use

- Phase 06 Development, when a React-based front end needs a consistent component layer.
- Establishing or extending a design-system token set for a client web app, from an approved direction.
- Rapid prototypes that need accessible primitives rather than hand-built controls.

## When not to use

- Choosing the visual direction itself: use `skill:impeccable` or `frontend-design:frontend-design` first.
- Projects that do not use React-based frameworks.
- Accessibility certification: use `building-accessible-interfaces` and report results with evidence.

## Inputs it needs

- The approved direction and token values, or a note that tokens are still open.
- The framework and existing component conventions in the repository.

## How to run it

1. Read the project's existing components and tokens before adding anything.
2. Use the shadcn/ui primitives for controls; do not rebuild them.
3. Verify in the browser at mobile, tablet and desktop widths, including dark mode if it ships.

```text
Use the ui-styling skill. Framework: {Next.js/Vite}. Approved tokens: {file or link}. Components needed: {list}. Reuse the project's existing components first. Report each new dependency, the widths and themes checked, and any component that does not meet the accessibility checks.
```

## What good output looks like

- Components built from the project's existing primitives, with token-driven styling.
- Browser evidence at the shipped widths and themes; console clean.
- A list of new dependencies, each justified.

## Quality checks

- [ ] No new dependency added without a stated reason (shadcn/ui only where it fits).
- [ ] Keyboard, focus and label behaviour verified, not assumed.
- [ ] Tokens, not hard-coded values, carry colour and spacing.

## Pairs with

- `skill:impeccable` and `frontend-design:frontend-design`: the design decisions this implements.
- `skill:building-accessible-interfaces`: accessibility checks during build.
- `ui-ux-pro-max:ui-ux-pro-max`: broader design-system reference.

## Limits and cautions

- The plugin's own text cites upstream docs that change; verify current APIs before use.
- MIT licence; the vendored copy keeps its upstream notice.
- Generic component styling is the default the studio bans. Use the approved direction, not the library's default look.
