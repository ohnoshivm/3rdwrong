---
title: Composition system skill evaluation — Stillsoil Atelier
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-23
review_every_days: 180
---
# Composition system skill evaluation — Stillsoil Atelier

**Fictional example for testing methods and skills. Not a client.**

## Skill and version

`3w-composition-system` 0.1.0 was run; findings below produced version 0.1.1 of [the skill](../../../skills/3w-composition-system/SKILL.md). The run was not repeated on 0.1.1.

## Test request and inputs

**Request:** "Use 3w-composition-system on route A for Stillsoil Atelier as a formative run, using the mark, typography and colour runs. Set invariants and variables, test against the brief's labels, line sheet and online shop with stand-in dimensions, and do not approve anything."

Inputs: [fictional brief](brief.md), [discovery synthesis](discovery-synthesis.md), [concept route A](concept-route-a.md) and the [formative critique](identity-system-critique.md), plus the [mark](mark-exploration-test-run.md), [typography](typography-system-test-run.md) and [colour](colour-system-test-run.md) test runs. Route A is not chosen and strategy is not signed, so the run was accepted as formative. No category audit, artwork, dimensions, printer or licences exist in the fiction.

Output: [composition system test run](composition-system-test-run.md).

## Procedure followed

Steps 1–7, 9 and 10 were followed in text. Step 8 used stand-in dimensions and text checks, not built layouts; the unfamiliar-colleague test could not run in a single-agent fiction and is listed as not run.

## Output review

- Three invariants are measurable and tied to the idea; the base unit is derived from format width.
- The motion rule caught a conflict in route A itself: its fade that reveals the variant after the name would hide information the fictional customer needs before purchase (R1), so the variant was made visible without motion.
- Out-of-scope formats were marked out of scope rather than designed.
- Stand-in dimensions were labelled throughout.

## What worked

- Running after the other three skills made the hand-offs concrete: the mark's interval became the held field, the type rule became I2 and the colour finding became I3.
- The "what gives way first" rule gave a testable answer to the dense line-sheet case.

## Gaps and observed failure

- **Fixed content blocks missing.** Mandatory label text, price, size and die lines decide much of a label's composition; the skill did not ask for them.
- **Motion and required information.** The reduced-motion rule did not say that information needed to choose a product must be visible without motion; the run found this only by reading R1.
- **Unfamiliar-colleague test.** The skill gave no route when no human is available; the run could only record "not run".
- **Formative use and stand-ins** were not provided for.

## Skill changes made

- Inputs: fixed content blocks with minimum sizes.
- Step 6 (motion): required information must be visible without motion; check the route's motion against it.
- Step 8: the tester must not be the maker; an AI rebuild from the rule sheet may screen for gaps as a labelled proxy, never as a replacement.
- Failure conditions: formative runs with labelled stand-in dimensions allowed when accepted.

## Remaining limits and next evaluation

- No layout was built, so invariants remain Hypotheses; the next evaluation needs drawn label, shelf-card and mobile applications at real sizes and a human unfamiliar-colleague test.
- Social, environmental and motion behaviours were not exercised because they are out of the fictional scope; test a brief that includes them.
