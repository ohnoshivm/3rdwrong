---
title: Launch Asset Packager
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:launch-asset-packager
department: marketing
sub_department: pr-awards
job: launch-assets
role: lead
trigger: ""
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/launch-asset-packager/SKILL.md
invoke: "Claude Code: `/launch-asset-packager`; Codex: `launch-asset-packager` skill"
pairs_with: []
---
# Launch Asset Packager

Launch Asset Packager is 3RDWRONG’s lead for launch assets in pr awards.

## What it does

- Assembles the tier-scoped asset manifest for a launch — every artifact the moment needs, its owner, its spec source, and its production status — in the Assemble phase of the RAMP loop (Research → Assemble → Mobilize → Prove). It feeds the RAMP A sub-items directly: *press kit complete*, *per-channel asset kits complete per tier to each surface's documented spec* (store listing character budgets included), and the *technical go-live pass* — and the manifest tracks the localization-variant and message-match rows the auditor later checks. It works one lever — the kit — and hands off: only launch-readiness-auditor computes the RAMP profile result or runs the A1 veto.
- Expected output: a tier-scoped asset manifest (artifact · owner · spec source · status) frozen under launch_ref / manifest_version / manifest_hash with dependency offsets, a press kit section spec, demo script + screenshot specs, a launch FAQ outline, dual-store listing drafts with Measured character counts, a technical go-live checklist (manifest only), and the standard handoff summary.
- Writes: the manifest/specs to memory/launch/launch-asset-packager/ with permission; frozen manifest and unresolved claim facts become separate authorized operation: propose events through registry-events.py.

## When to use

- Use as lead for launch assets when the studio has an approved brief for this deliverable.
- For awards, work only on free entries and keep the final submission for founder review.

## When not to use

- Do not pay for award entries or submit without founder review.
- Do not use to make unsupported claims about recognition, results or approval.

## Inputs it needs

- A specific brief and requested decision or deliverable.
- The source file’s required evidence and context, with links/paths and date or version where relevant.
- Award criteria, deadline, cleared project evidence and confirmation that entry is free.

## How to run it

1. Check the registry role, job and trigger against the request.
2. Gather the required inputs from approved sources; keep client data outside the public repository.
3. Invoke the tool using the host-specific name above and give it the brief and evidence paths.
4. Have someone other than the maker review the output against the checks below.

```text
Use Launch Asset Packager for launch assets at 3RDWRONG. Context: {studio or specifically approved project}. Brief and decision: {brief}. Source material: {links/files}. Follow the tool's documented deliverable, separate sourced facts from interpretation, and mark unknowns. Do not invent evidence or approval.
```

## What good output looks like

- a tier-scoped asset manifest (artifact · owner · spec source · status) frozen under launch_ref / manifest_version / manifest_hash with dependency offsets, a press kit section spec, demo script + screenshot specs, a launch FAQ outline, dual-store listing drafts with Measured character counts, a technical go-live checklist (manifest only), and the standard handoff summary.
- each tier channel has owner/spec/status, required kit sections and character counts are explicit, the go-live checklist names executors, the current manifest version/hash and optional supersedes ref are recorded, the manifest proposal is recorded, and the Narrative/claims dependency tuple matches the source message house. A later asset/claim/channel/owner change produces a new manifest version.
- Evidence and assumptions are distinguishable; missing facts remain Unknown.
- A human owner can review the result and decide the next action.

## Quality checks

- [ ] The request matches the registry job and, for a specialist, its trigger.
- [ ] Claims, numbers and decisions have traceable evidence; unknowns are labelled.
- [ ] A reviewer other than the maker checks the result before use.
- [ ] Any award entry is free and the founder reviews the final submission.

## Pairs with

- No same-job peer appears in this scoped registry slice.

## Limits and cautions

- Only capabilities and restrictions documented in the tool file are attributed to it; anything else is Not documented.
- Keep evidence labels distinct: Documented, Interpretation, Hypothesis and Unknown. Maker ≠ checker.
- Award submissions are free-only for now; do not recommend or incur entry fees.
