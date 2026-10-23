---
title: Pricing Packaging Planner
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:pricing-packaging-planner
department: sales
sub_department: pricing-deal-desk
job: pricing-models
role: specialist
trigger: "Use for sales/pricing-deal-desk/pricing-models when the brief specifically requires: Use when the user asks to \"plan launch pricing\", \"design pricing tiers / packaging\", or \"set up a launch discount / early-bird offer\"; produces a launch pricing and packaging plan — tier structure and naming, a value-to-price map aligned to the message house, a launch-offer ladder with a true deadline reason, beta / early-adopter pricing with a post-launch graduation path, and guarantee / refund terms — with every price claim and offer term submitted to memory/events/claims.ndjson ."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/pricing-packaging-planner/SKILL.md
invoke: "Claude Code skill: pricing-packaging-planner; Codex skill: pricing-packaging-planner."
pairs_with: [agency:specialized-pricing-analyst, skill:pricing]
---
# Pricing Packaging Planner

The studio specialist for `pricing-models`: Use for sales/pricing-deal-desk/pricing-models when the brief specifically requires: Use when the user asks to "plan launch pricing", "design pricing tiers / packaging", or "set up a launch discount / early-bird offer"; produces a launch pricing and packaging plan — tier structure and naming, a value-to-price map aligned to the message house, a launch-offer ladder with a true deadline reason, beta / early-adopter pricing with a post-launch graduation path, and guarantee / refund terms — with every price claim and offer term submitted to memory/events/claims.ndjson .

## What it does

- Pricing Packaging Planner.
- **Reads**: product, ICP, launch type/access model; current pricing/history; unit economics if known; accepted message-house pillars; competitor public pricing; and launch projection stage/date.
- **Writes**: a user-facing pricing plan + a reusable summary to `memory/launch/pricing-packaging-planner/`; every price claim, offer term, and guarantee wording to `memory/events/claims.ndjson` via an authorized `operation: propose` request to `registry-events.py` for offer-claims-registry (upstream reference `../../../protocol/offer-claims-registry/SKILL.md`) to formalize; stage-linked pricing facts (e.g. "pricing page goes live at GA") to `memory/events/launches.ndjson` via an authorized `operation: propose` request to `registry-events.py` — this skill never writes `memory/claims/` or `memory/launch-registry/` directly.
- **Promotes**: the chosen tier structure, launch-offer terms + deadline rationale, and the beta→GA price path (ask before writing); durable pricing decisions proposed as pending-decision items — never written to `decisions.md` directly.
- **Done when**: tiers are named with per-tier contents and each maps to a message-house pillar; the launch offer states a true deadline reason (or no offer, stated explicitly); the beta / early-adopter price and its graduation path are declared; guarantee / refund terms are drafted; and every price claim and offer term is submitted as a candidate — nothing is presented as a live offer.

## When to use

- Use for sales/pricing-deal-desk/pricing-models when the brief specifically requires: Use when the user asks to "plan launch pricing", "design pricing tiers / packaging", or "set up a launch discount / early-bird offer"; produces a launch pricing and packaging plan — tier structure and naming, a value-to-price map aligned to the message house, a launch-offer ladder with a true deadline reason, beta / early-adopter pricing with a post-launch graduation path, and guarantee / refund terms — with every price claim and offer term submitted to memory/events/claims.ndjson .

## When not to use

- Outside `pricing-models`; route to the matching job lead when another job owns the work.
- Do not use it to approve its own work or make an unapproved commercial commitment.

## Inputs it needs

- Approved scope, intended decision and the minimum relevant source material.
- The target, account, call, pricing context or pipeline data required by this job; redact or keep personal data in a private store.

## How to run it

1. Confirm the job, trigger and desired output; provide only approved, necessary inputs.
2. Invoke the tool with the prompt below and request evidence labels where claims or recommendations are made.
3. Review the draft against the source material; route decisions, external actions and approvals to the responsible human.

```text
Use skill:pricing-packaging-planner for pricing models at 3RDWRONG. Scope: {{approved scope}}. Inputs: {{private source references or redacted facts}}. Return a concise, source-grounded draft for human review. Mark unsupported items Unknown; do not invent facts, approvals, outcomes or claims.
```

## What good output looks like

- Answers the stated `pricing-models` question with a clearly scoped result.
- Distinguishes documented inputs from interpretation and unknowns; gives a practical next step.
- Contains no unsupported claim, invented result or unapproved commitment.

## Quality checks

- [ ] A separate reviewer checked the output against the supplied evidence.
- [ ] Scope and assumptions are visible; unknowns are stated rather than filled in.
- [ ] No sensitive client or prospect information entered the public repository.

## Pairs with

- agency:specialized-pricing-analyst
- skill:pricing

Use the lead for routing and hand off only the relevant, reviewed artefact; keep human approval with the founder.

## Limits and cautions

- The tool source is a prompt/instruction file; this card does not establish live connectivity, performance, or approval.
- Distribution is `vendor`; verify installation or sign-in requirements before relying on runtime access.

- Keep client and prospect personal data out of this public repository; use an approved private store.
- Separate sourced facts from interpretation and label evidence Documented, Interpretation, Hypothesis or Unknown. A maker cannot be the sole checker; the founder retains approval.
