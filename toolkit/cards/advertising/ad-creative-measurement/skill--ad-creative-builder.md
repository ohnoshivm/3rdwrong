---
title: Ad Creative Builder
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:ad-creative-builder
department: advertising
sub_department: ad-creative-measurement
job: ad-creative
role: specialist
trigger: "Use for advertising/ad-creative-measurement/ad-creative when the brief specifically requires: Use when the user asks to \"write ad copy\", \"generate RSA headlines\", or \"build ad creative at volume\"; produces ad units — RSA headlines/descriptions, hooks, and an angle matrix — message-matched to the destination landing page ."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/ad-creative-builder/SKILL.md
invoke: "Claude Code: `/ad-creative-builder`; Codex: `ad-creative-builder` skill"
pairs_with: [agency:marketing-growth-hacker, agency:marketing-livestream-commerce-coach, agency:paid-media-creative-strategist]
---
# Ad Creative Builder

Ad Creative Builder is a 3RDWRONG specialist for ad creative, activated only when its registry trigger applies.

## What it does

- Generates and iterates paid-ad creative at volume — RSA headlines and descriptions, hooks, and an angle matrix — each message-matched to the destination landing page. This is the build skill that produces the ROAS O (Offer) units; it does not score them (that is ad-account-auditor) and does not touch the post-click page (that is landing-optimizer).
- Expected output: a ready-to-import creative set (RSA headlines/descriptions, hooks, angle matrix) with a per-unit message-match note to the destination URL, plus the standard handoff summary for memory/ad/ad-creative-builder/.
- Writes: a user-facing creative set and, with permission, a WARM artifact; unresolved claims become authorized operation: propose events through registry-events.py.

## When to use

- Use for advertising/ad-creative-measurement/ad-creative when the brief specifically requires: Use when the user asks to "write ad copy", "generate RSA headlines", or "build ad creative at volume"; produces ad units — RSA headlines/descriptions, hooks, and an angle matrix — message-matched to the destination landing page .
- Limit use to studio demand or campaign creative/review tied to a specifically approved client launch; founder approval is required before any spend.

## When not to use

- Do not treat this tool as authority to launch, change or fund a campaign.
- Do not use without a defined studio-demand or approved client-launch scope and the source data required by the tool.

## Inputs it needs

- A specific brief and requested decision or deliverable.
- The source file’s required evidence and context, with links/paths and date or version where relevant.
- An approved campaign scope; founder approval before spend.

## How to run it

1. Check the registry role, job and trigger against the request.
2. Gather the required inputs from approved sources; keep client data outside the public repository.
3. Invoke the tool using the host-specific name above and give it the brief and evidence paths.
4. Have someone other than the maker review the output against the checks below.

```text
Use Ad Creative Builder to Prepare the documented campaign creative or test deliverable. Scope: {studio demand or named client launch}. Brief and decision: {brief}. Evidence/assets: {links or paths}. Founder approval is required before any spend; do not initiate or authorise spend. Mark missing evidence Unknown and follow the tool's documented output format.
```

## What good output looks like

- a ready-to-import creative set (RSA headlines/descriptions, hooks, angle matrix) with a per-unit message-match note to the destination URL, plus the standard handoff summary for memory/ad/ad-creative-builder/.
- every unit fits current format limits, maps to an accepted destination-page claim, contains no unsupported/policy-prohibited wording, covers at least two angles, and reports the full Narrative/claims dependency tuple.
- Evidence and assumptions are distinguishable; missing facts remain Unknown.
- A human owner can review the result and decide the next action.

## Quality checks

- [ ] The request matches the registry job and, for a specialist, its trigger.
- [ ] Claims, numbers and decisions have traceable evidence; unknowns are labelled.
- [ ] A reviewer other than the maker checks the result before use.
- [ ] No spend action occurs without founder approval.

## Pairs with

- `agency:marketing-growth-hacker` — same job; use when its own role or trigger applies.
- `agency:marketing-livestream-commerce-coach` — same job; use when its own role or trigger applies.
- `agency:paid-media-creative-strategist` — same job; use when its own role or trigger applies.

## Limits and cautions

- Only capabilities and restrictions documented in the tool file are attributed to it; anything else is Not documented.
- Keep evidence labels distinct: Documented, Interpretation, Hypothesis and Unknown. Maker ≠ checker.
- Advertising covers studio demand and creative/review work for specifically approved client launches; it is not standalone ads management.
- No spend without founder approval. Treat campaign exports and client information as confidential; never put client data in the public repository.
