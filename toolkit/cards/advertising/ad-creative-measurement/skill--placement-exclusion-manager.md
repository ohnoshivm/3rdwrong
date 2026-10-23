---
title: Placement Exclusion Manager
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:placement-exclusion-manager
department: advertising
sub_department: ad-creative-measurement
job: ad-creative
role: specialist
trigger: "Use for advertising/ad-creative-measurement/ad-creative when the brief specifically requires: Use when the user asks to \"build my brand-safety exclusion lists\", \"set placement / topic / content exclusions before launch\", \"add network and audience exclusions\", or \"prep the A1 brand-safety evidence for the auditor\"; produces a placement/network exclusion list, a content-suitability & sensitive-topic block list, an audience/negative-audience exclusion set, and a packaged A1 brand/placement-safety evidence file for the gate ."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/placement-exclusion-manager/SKILL.md
invoke: "Claude Code: `/placement-exclusion-manager`; Codex: `placement-exclusion-manager` skill"
pairs_with: [agency:marketing-growth-hacker, agency:marketing-livestream-commerce-coach, agency:paid-media-creative-strategist]
---
# Placement Exclusion Manager

Placement Exclusion Manager is a 3RDWRONG specialist for ad creative, activated only when its registry trigger applies.

## What it does

- Builds the brand-safety and exclusion lists that gate spend before a campaign goes live — placement/site/app/channel exclusions, network opt-outs, and content-suitability and sensitive-topic blocks — then references the audience exclusion set from audience-segment-builder and packages the placements evidence the auditor reads to judge ROAS A1 (brand/placement safety). It hardens where ads are *not* allowed to run; it does not build the audiences you *do* target or the audience exclusions themselves, and it does not score the account or issue the A1 verdict.
- Expected output: a placement/network exclusion list (sites, apps, channels, network opt-outs), a content-suitability & sensitive-topic block list, a reference to the audience exclusion set consumed from audience-segment-builder (not re-derived here), a packaged A1 evidence file (placements report + exclusion decisions with rationale), and the standard handoff summary.
- Writes: a user-facing exclusion plan, the A1 evidence file, and a reusable summary to memory/ad/placement-exclusion-manager/.

## When to use

- Use for advertising/ad-creative-measurement/ad-creative when the brief specifically requires: Use when the user asks to "build my brand-safety exclusion lists", "set placement / topic / content exclusions before launch", "add network and audience exclusions", or "prep the A1 brand-safety evidence for the auditor"; produces a placement/network exclusion list, a content-suitability & sensitive-topic block list, an audience/negative-audience exclusion set, and a packaged A1 brand/placement-safety evidence file for the gate .
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
Use Placement Exclusion Manager to Prepare the documented campaign creative or test deliverable. Scope: {studio demand or named client launch}. Brief and decision: {brief}. Evidence/assets: {links or paths}. Founder approval is required before any spend; do not initiate or authorise spend. Mark missing evidence Unknown and follow the tool's documented output format.
```

## What good output looks like

- a placement/network exclusion list (sites, apps, channels, network opt-outs), a content-suitability & sensitive-topic block list, a reference to the audience exclusion set consumed from audience-segment-builder (not re-derived here), a packaged A1 evidence file (placements report + exclusion decisions with rationale), and the standard handoff summary.
- placement/network exclusions are specified against a named goal; content-suitability + sensitive-topic blocks are listed; the audience exclusion set is referenced or noted as a dependency; and the A1 evidence file is packaged, or absent placements evidence leaves qualified A1 evidence Unknown and the run NEEDS_INPUT.
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
