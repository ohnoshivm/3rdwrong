---
title: Identity system critic
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:3w-identity-system-critic
department: design
sub_department: design-qa
job: concept-critique
role: lead
trigger: ""
kind: repo-skill
availability: repo
distribution: repo
source: skills/3w-identity-system-critic/SKILL.md
invoke: "3w-identity-system-critic skill"
pairs_with: [skill:3w-creative-direction, skill:3w-brand-consistency-qa, skill:3w-category-code-audit]
---
# Identity system critic

The studio's lead tool for concept critique: an independent, evidence-labelled review of an identity route or system before route selection or visual sign-off.

## What it does

- Reviews a route in four modes: concept, formal, audience and implementation.
- Tests whether the idea survives being described without visual adjectives.
- Checks distinctiveness against a linked category sample, and marks it Unknown when no sample exists.
- Checks system repeatability across the supplied applications, sizes and scripts.
- Ends with exactly one written verdict and a concrete next design action — never an approval.

## When to use

- Phase 04 Concept, before the founder chooses between routes.
- Phase 07 Validation, before visual sign-off.
- Formative review of a draft route, as long as the strategy's draft status is stated.

## When not to use

- To invent strategy or choose a route for the founder.
- To certify accessibility or production readiness — use `skill:3w-brand-consistency-qa` and engineering QA for that.
- When the route, artefacts or decision requested are missing: stop and ask.

## Inputs it needs

- Approved strategy and criteria (or a draft marked formative).
- The concept route, the decision requested and the artefact version.
- Representative applications at stated sizes and contexts.
- The category audit and source links if distinctiveness is to be judged.

## How to run it

1. Collect the inputs above in one folder or message.
2. Run the skill with someone other than the route's maker (maker ≠ checker).
3. Read the verdict and findings table; act on the next design action.
4. File the critique in the project's critique folder.

```text
Use the 3w-identity-system-critic skill. Decision requested: choose between routes A and B for {{project}}. Strategy: {{link, approved v1.0}}. Inspect: {{files and applications}}. Category sample: {{audit link}}. Return the skill's exact output structure.
```

## What good output looks like

- One exact verdict from the protocol, a findings table with severity and evidence labels, and an "idea without style adjectives" sentence.
- Unknowns listed instead of guessed; a specific next action with owner.

## Quality checks

- [ ] The reviewer is not the route's maker.
- [ ] Every finding has an evidence label and a source.
- [ ] Distinctiveness is Unknown unless a category sample was supplied.
- [ ] No claim of audience response, memorability or sales from inspection alone.

## Pairs with

- Upstream: `skill:3w-category-code-audit` (category sample), `skill:3w-creative-direction` (routes).
- Downstream: `skill:3w-brand-consistency-qa` once a route is approved.

## Limits and cautions

- Visual inspection documents what is present; it cannot document meaning, preference or results.
- Never records approval; the founder decides.
