---
title: Brief Generator
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:brief-generator
department: outbound
sub_department: partnerships-referrals
job: creator-partnerships
role: specialist
trigger: "Use only when the named content, channel, lifecycle, or campaign task is explicitly in the approved marketing scope."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/brief-generator/SKILL.md
invoke: "Claude Code skill: brief-generator; Codex skill: brief-generator."
pairs_with: [skill:influencer-marketing, skill:trend-spotter]
---
# Brief Generator

The studio specialist for `creator-partnerships`: Use only when the named content, channel, lifecycle, or campaign task is explicitly in the approved marketing scope.

## What it does

- Brief Generator.
- **Reads**: campaign/product/platform/deliverable/CTA/timeline/compensation inputs; stable opaque `creator_ref`, `brand_ref`, `page_ref`, `shipping_ref`, `contact_ref`, `brand_asset_ref`, `hashtag_ref`, `promo_code_ref`, and (when voice is used) `voice_source_ref`; plus `memory/projections/narrative.json`, `memory/projections/claims.json`, and relevant creator/channel projections. HOT is only an index to those sources. Raw creator/brand names and handles, page/asset-folder URLs, shipping addresses, contact names/emails/phones, hashtags, promo codes, and voice-source locators are transient rendering/dispatch inputs only.
- **Writes**: return a reference-safe creator brief inline by default; save it to `memory/influencer/brief-generator/YYYY-MM-DD-<topic>.md` only with exact authorization. Saved artifacts and handoffs represent creator, brand, landing destination, shipping destination, contact path, assets, hashtags, promo terms, and voice provenance only with `creator_ref`, `brand_ref`, `page_ref`, `shipping_ref`, `contact_ref`, `brand_asset_ref`, `hashtag_ref`, `promo_code_ref`, and `voice_source_ref`; never persist their raw identity/address/URL/contact/content values or a hidden mapping. Each unresolved-claim proposal is a separate exact `operation: propose` authorization; a brief-save approval does not cover it.
- The brief covers all required sections (overview, key messages, deliverables, creative direction, timeline, compliance, compensation, contact).
- Disclosure requirements and usage rights are stated explicitly, with no placeholder left unresolved that the user gave input for.

## When to use

- Use only when the named content, channel, lifecycle, or campaign task is explicitly in the approved marketing scope.

## When not to use

- Outside `creator-partnerships`; route to the matching job lead when another job owns the work.
- Do not use it to send or automate outreach; studio outbound is limited to 20 personalised, hand-written first messages per week.
- Do not use it to approve its own work or make an unapproved commercial commitment.

## Inputs it needs

- Approved scope, intended decision and the minimum relevant source material.
- The target, account, call, pricing context or pipeline data required by this job; redact or keep personal data in a private store.

## How to run it

1. Confirm the job, trigger and desired output; provide only approved, necessary inputs.
2. Invoke the tool with the prompt below and request evidence labels where claims or recommendations are made.
3. Review the draft against the source material; route decisions, external actions and approvals to the responsible human.

```text
Use skill:brief-generator for creator partnerships at 3RDWRONG. Scope: {{approved scope}}. Inputs: {{private source references or redacted facts}}. Return a concise, source-grounded draft for human review. Mark unsupported items Unknown; do not invent facts, approvals, outcomes or claims.
```

## What good output looks like

- Answers the stated `creator-partnerships` question with a clearly scoped result.
- Distinguishes documented inputs from interpretation and unknowns; gives a practical next step.
- Contains no unsupported claim, invented result or unapproved commitment.

## Quality checks

- [ ] A separate reviewer checked the output against the supplied evidence.
- [ ] Scope and assumptions are visible; unknowns are stated rather than filled in.
- [ ] No sensitive client or prospect information entered the public repository.

## Pairs with

- skill:influencer-marketing
- skill:trend-spotter

Use the lead for routing and hand off only the relevant, reviewed artefact; keep human approval with the founder.

## Limits and cautions

- The tool source is a prompt/instruction file; this card does not establish live connectivity, performance, or approval.
- Distribution is `vendor`; verify installation or sign-in requirements before relying on runtime access.

- Outbound is 20 personalised, hand-written first messages per week; do not automate or batch-send. Check consent, suppression and opt-out rules before any contact. Keep prospect names, contact details, notes and other personal data out of this public repository.
- Separate sourced facts from interpretation and label evidence Documented, Interpretation, Hypothesis or Unknown. A maker cannot be the sole checker; the founder retains approval.
