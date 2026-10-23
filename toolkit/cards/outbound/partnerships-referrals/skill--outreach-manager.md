---
title: Outreach Manager
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:outreach-manager
department: outbound
sub_department: partnerships-referrals
job: partner-outreach
role: lead
trigger: ""
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/outreach-manager/SKILL.md
invoke: "Claude Code skill: outreach-manager; Codex skill: outreach-manager."
pairs_with: []
---
# Outreach Manager

The studio lead for `partner-outreach`: use this tool to handle partner outreach work with a source-grounded draft for human review.

## What it does

- Outreach Manager.
- **Reads**: a stable opaque `creator_ref` when one is carried by an authorized upstream artifact, plus transient target handle/profile locator(s), platform, follower count, niche; campaign and product context; compensation type and budget; deliverables and timeline; jurisdiction, intended channel, lawful-basis reference, contact-source/eligibility evidence, and pseudonymous consent subject ID; any prior contact history supplied by the user or loaded from memory. For a rostered creator, reuse a creator-registry aggregate ID only when its identity link is verified, resolve it through the authorized artifact or verified registry link, then check `memory/creators/<aggregate-id>.md` — the creator-registry (upstream reference `../../../protocol/creator-registry/SKILL.md`) projection — for the confirmed contact path, last agreed rate, and negotiation/response history. Never derive the path from a raw handle.
- **Writes**: return the outreach artifact inline by default; save it to `memory/influencer/outreach-manager/YYYY-MM-DD-<topic>.md` only with exact WARM-save authorization. Reuse an explicitly carried opaque `creator_ref`, or a verified creator-registry aggregate ID; otherwise generate one random `creator-<UUIDv4>` once for this lineage. Never derive `creator_ref` from a raw handle, name, profile URL, email, provider ID, or deterministic hash. Before saving, replace raw locators and resolved recipient identities with the stable `creator_ref` and resolvable opaque `recipient_ref`, `contact_source_ref`, `handle_ref`, and evidence/approval references. A raw URL or handle is never a persisted `source_ref`. When no authorized source artifact or verified registry link can resolve an opaque identity/contact ref, set `identity_status: unresolved`, save no hidden raw-locator mapping, set `cross_session_locator_required: true`, and request the transient locator again at dispatch. Never persist a raw handle, name, profile URL, email, phone, postal address, provider ID, or credential. When a cycle closes, each outcome update (final agreed rate, response history, confirmed contact-path reference) requires a separate exact authorization for an `operation: propose` request to `memory/events/creators.ndjson`; only `creator-registry` writes canonical roster records.
- **Promotes**: only with separate exact authorization, promote durable facts (confirmed partners, agreed rates, top objection patterns, response-rate baselines) to `memory/hot-cache.md`.
- A personalized pitch (plus at least one variation) exists for each target influencer.

## When to use

- Start with this lead for the `partner-outreach` job in outbound/partnerships-referrals.
- Use when the studio needs partner outreach during a live opportunity or internal commercial decision.

## When not to use

- Outside `partner-outreach`; route to the matching job lead when another job owns the work.
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
Use skill:outreach-manager for partner outreach at 3RDWRONG. Scope: {{approved scope}}. Inputs: {{private source references or redacted facts}}. Return a concise, source-grounded draft for human review. Mark unsupported items Unknown; do not invent facts, approvals, outcomes or claims.
```

## What good output looks like

- Answers the stated `partner-outreach` question with a clearly scoped result.
- Distinguishes documented inputs from interpretation and unknowns; gives a practical next step.
- Contains no unsupported claim, invented result or unapproved commitment.

## Quality checks

- [ ] A separate reviewer checked the output against the supplied evidence.
- [ ] Scope and assumptions are visible; unknowns are stated rather than filled in.
- [ ] No sensitive client or prospect information entered the public repository.

## Pairs with

- No same-job peer is listed in the eligible registry scope.

Use the lead for routing and hand off only the relevant, reviewed artefact; keep human approval with the founder.

## Limits and cautions

- The tool source is a prompt/instruction file; this card does not establish live connectivity, performance, or approval.
- Distribution is `vendor`; verify installation or sign-in requirements before relying on runtime access.

- Outbound is 20 personalised, hand-written first messages per week; do not automate or batch-send. Check consent, suppression and opt-out rules before any contact. Keep prospect names, contact details, notes and other personal data out of this public repository.
- Separate sourced facts from interpretation and label evidence Documented, Interpretation, Hypothesis or Unknown. A maker cannot be the sole checker; the founder retains approval.
