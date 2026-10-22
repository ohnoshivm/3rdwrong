---
title: Identity system critic skill evaluation — Stillsoil Atelier
type: guide
status: experimental
owner: founder
last_reviewed: 2026-10-22
review_every_days: 180
---
# Identity system critic skill evaluation — Stillsoil Atelier

**Fictional example for testing methods and skills. Not a client.**

## Skill and version

The first pass used `3w-identity-system-critic` 0.1.0 and prompted version 0.1.1.
The blueprint integration added four critique modes and fixed verdicts in
version 0.2.0; the output below was rerun against that version.

## Test request and inputs

**Request:** “Use 3w-identity-system-critic to give a formative critique of route A against the fictional brief and discovery synthesis. Identify the next checks. Do not approve the route or make real-market claims.”

Inputs: [fictional brief](brief.md), [discovery synthesis](discovery-synthesis.md)
and [concept route A](concept-route-a.md). Strategy is not signed. No category
audit, finished artwork or application prototypes were supplied; the test was
explicitly formative.

## Procedure followed

1. Marked the review formative and named the decision: evidence and checks needed before route selection.
2. Inventoried the brief, synthesis and text-only route; recorded that no visual artwork, user-test evidence or dimensions were inspectable.
3. Compared route A with the fictional brief's provisional goal, not an approved strategy.
4. Reviewed concept, formal, audience and implementation modes; marked audience response and visual implementation Not testable where evidence was absent.
5. Stated the underlying idea without visual adjectives and noted it addresses tone more clearly than variant wayfinding.
6. Checked distinctiveness against supplied category evidence; none existed, so it remained Unknown / Not testable.
7. Recorded that one label description cannot demonstrate system repeatability; noted the missing line sheet and mobile screen.
8. Marked contrast, font licence, script support, small-size and print craft checks unrun.
9. Used one permitted verdict, severity matched to consequence, and findings with source, owner, next check and no taste-score average.
10. Recommended further exploration rather than approval, named the human decisions and ended with a concrete next design action.

## Output review

The [formative critique](identity-system-critique.md) distinguishes fictional
facts from interpretations, hypotheses and unknowns. It covers the four modes,
uses an exact protocol verdict and ends with an owner-led action. It does not
infer market conventions from the description or treat missing evidence as a
visual defect.

## What worked

- The formative status prevented an unapproved draft from being treated as a signed strategy.
- Strategy fit, idea, system and craft were all discussed with evidence limits.
- Findings distinguish an actual observation from a risk and from a missing test.
- The route's idea is tested separately from its type, paper and motion cues.

## Gaps and observed failure

The first output schema grouped findings in one table but did not give
distinctiveness its own required field. Without a category audit, an evaluator
could omit the lens rather than explicitly report that it was not testable.
The four-mode schema needed a clear boundary between intended audience
interpretation and observed response; otherwise a fictional brief could read
as audience evidence. That gap was identified while preparing the final test.

## Skill changes made

After the first pass, updated `skills/3w-identity-system-critic/SKILL.md` from
0.1.0 to 0.1.1: no category sample now means **Unknown / Not testable**, and
the schema has a dedicated distinctiveness field. Version 0.2.0 adds concept,
formal, audience and implementation modes, exact non-scored verdicts, and a
mandatory next action. During preparation of the current run, clarified that
the audience mode separates intended interpretation from observed response
and requires Unknown when no audience test exists. The current output follows
that wording; no post-run skill change is claimed.

## Remaining limits and next evaluation

This test reviewed text only. Next, evaluate approved files with a linked
category sample and actual application dimensions; check whether the skill
identifies defects accurately without over-weighting taste. Accessibility and
production checks remain unverified here. The run does not approve the strategy
or route.
