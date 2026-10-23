---
title: Cold Outbound Sequencer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:cold-outbound-sequencer
department: outbound
sub_department: outreach-sequences
job: sequence-design
role: specialist
trigger: "Use for outbound/outreach-sequences/sequence-design when the brief specifically requires: Use when the user asks to \"build a B2B cold-outbound sequence\", \"design reply-triage branching\", \"plan a domain warmup / sending throttle\", or \"make my outbound CAN-SPAM / opt-in compliant\"; produces a multi-step outbound sequence with reply-triage branches (positive / objection / referral / not-now / opt-out), a warmup + send-throttle ramp schedule, jurisdiction opt-in/CAN-SPAM guardrails (guidance, not legal advice), and a SEND S-dimension read ."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/pack-aaron-he-zhu-aaron-marketing-skills-apache-2.0/skills/cold-outbound-sequencer/SKILL.md
invoke: "Claude Code skill: cold-outbound-sequencer; Codex skill: cold-outbound-sequencer."
pairs_with: [agency:sales-outbound-strategist, skill:cold-email]
---
# Cold Outbound Sequencer

The studio specialist for `sequence-design`: Use for outbound/outreach-sequences/sequence-design when the brief specifically requires: Use when the user asks to "build a B2B cold-outbound sequence", "design reply-triage branching", "plan a domain warmup / sending throttle", or "make my outbound CAN-SPAM / opt-in compliant"; produces a multi-step outbound sequence with reply-triage branches (positive / objection / referral / not-now / opt-out), a warmup + send-throttle ramp schedule, jurisdiction opt-in/CAN-SPAM guardrails (guidance, not legal advice), and a SEND S-dimension read .

## What it does

- Cold Outbound Sequencer.
- **Reads**: the sequence goal or ICP, the sending-domain/mailbox setup (how many mailboxes, domain age, current warmup state), the target list source and its jurisdiction mix, current bounce/spam-complaint signals from a `~~email platform` sending report when available, and the SEND `cold-outbound` profile (`S=.35 E=.25 N=.15 D=.25`) from send-benchmark.md (upstream reference `../../../references/send-benchmark.md`).
- **Writes**: a user-facing sequence map + warmup/throttle schedule + guardrail block, and a reusable handoff summary to `memory/email/cold-outbound-sequencer/YYYY-MM-DD-<sequence-or-icp>.md`.
- **Promotes**: chosen sequence structure, warmup/throttle schedule, the jurisdictions in scope, the S-dimension read, and missing exports/consent-basis gaps to `memory/hot-cache.md` and `memory/open-loops.md`; propose durable outbound-cadence or list-source decisions as `pending-decision` items — never write `decisions.md` directly.
- **Done when**: every sequence step has timing, a goal, and an explicit exit rule; reply-triage routes positive / objection / referral / not-now / opt-out; a per-mailbox warmup ramp and daily send throttle are specified; the CAN-SPAM required elements and any opt-in-jurisdiction flags are stated as guidance with a "confirm with counsel" caveat; and the SEND **S** read is emitted with the Cold-outbound typed profile named.

## When to use

- Use for outbound/outreach-sequences/sequence-design when the brief specifically requires: Use when the user asks to "build a B2B cold-outbound sequence", "design reply-triage branching", "plan a domain warmup / sending throttle", or "make my outbound CAN-SPAM / opt-in compliant"; produces a multi-step outbound sequence with reply-triage branches (positive / objection / referral / not-now / opt-out), a warmup + send-throttle ramp schedule, jurisdiction opt-in/CAN-SPAM guardrails (guidance, not legal advice), and a SEND S-dimension read .

## When not to use

- Outside `sequence-design`; route to the matching job lead when another job owns the work.
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
Use skill:cold-outbound-sequencer for sequence design at 3RDWRONG. Scope: {{approved scope}}. Inputs: {{private source references or redacted facts}}. Return a concise, source-grounded draft for human review. Mark unsupported items Unknown; do not invent facts, approvals, outcomes or claims.
```

## What good output looks like

- Answers the stated `sequence-design` question with a clearly scoped result.
- Distinguishes documented inputs from interpretation and unknowns; gives a practical next step.
- Contains no unsupported claim, invented result or unapproved commitment.

## Quality checks

- [ ] A separate reviewer checked the output against the supplied evidence.
- [ ] Scope and assumptions are visible; unknowns are stated rather than filled in.
- [ ] No sensitive client or prospect information entered the public repository.

## Pairs with

- agency:sales-outbound-strategist
- skill:cold-email

Use the lead for routing and hand off only the relevant, reviewed artefact; keep human approval with the founder.

## Limits and cautions

- The tool source is a prompt/instruction file; this card does not establish live connectivity, performance, or approval.
- Distribution is `vendor`; verify installation or sign-in requirements before relying on runtime access.

- Outbound is 20 personalised, hand-written first messages per week; do not automate or batch-send. Check consent, suppression and opt-out rules before any contact. Keep prospect names, contact details, notes and other personal data out of this public repository.
- Separate sourced facts from interpretation and label evidence Documented, Interpretation, Hypothesis or Unknown. A maker cannot be the sole checker; the founder retains approval.
