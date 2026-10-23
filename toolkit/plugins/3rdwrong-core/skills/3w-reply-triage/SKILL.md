---
name: 3w-reply-triage
description: Classify and handle replies to 3RDWRONG outbound messages within one working day using the outbound reply rules — interested, not now, wrong person or referral, objection or question, no or unsubscribe, auto-reply — honouring opt-outs the same day and turning positive replies into L0 leads. Use for replies to studio outreach; do not use for inbound enquiries, social comment moderation or auto-sending replies.
metadata:
  type: skill
  status: experimental
  owner: founder
  last_reviewed: 2026-10-23
  version: 0.1.0
---
# 3w-reply-triage

## Purpose

Answer every reply quickly and honestly, stop every sequence at the first reply, and never contact someone again after they say no.

## When to use

Use whenever a reply arrives to a studio outbound message (email, LinkedIn, Instagram DM), and at the start of each working day to clear the queue.

## When not to use

Do not use for inbound enquiries (they go straight to the pipeline as L0 leads) or for comments and DMs on studio social posts (`skill:engagement-inbox-manager`). Never auto-send a reply; this skill drafts and records.

## Inputs

- The reply, the original message and the sequence state (vault).
- The suppression list.
- The account's qualification record from `skill:3w-prospect-qualification`.

## Dependencies

[Tool card](../../toolkit/cards/outbound/outreach-sequences/skill--3w-reply-triage.md) records routing, invocation and independent checks.

Read the [outbound system](../../growth/outbound/README.md#5-reply-handling) reply table, [compliance basics](../../growth/outbound/compliance.md), [pipeline](../../growth/sales/pipeline.md) and [growth metrics](../../growth/metrics.md).

## Procedure

1. **Stop the sequence** for this person at once, whatever the reply says.
2. **Classify** into exactly one class: interested; not now; wrong person or referral; objection or question; no, unsubscribe or annoyed; auto-reply. When unsure between "no" and anything else, treat it as no.
3. **Act by class:**
   - Interested: thank them, propose times, create the L0 lead with source `outbound`.
   - Not now: ask once whether a later date suits; set a "not yet" check-back; no further sequence.
   - Wrong person or referral: thank them; contact the named person only if introduced or clearly appropriate, and qualify that person first.
   - Objection or question: answer honestly and briefly; offer a call only if useful.
   - No, unsubscribe or annoyed: apologise briefly if appropriate, confirm they will not hear again, add them to the suppression list the same day.
   - Auto-reply: pause; resume after the stated return date, still within the sequence limits.
4. **Draft** the reply in the studio voice: short, specific, no pressure, no fake familiarity. A human sends it.
5. **Respond within one working day** of receipt.
6. **Log** the class, action, date and next step in the vault; update monthly counts (reply rate, positive replies, opt-outs).
7. **Watch stop signals.** Rising opt-outs, "irrelevant" replies or spam complaints → pause outbound and flag for review.

## Evidence requirements

Quote the reply's own words for the classification. Record the date the suppression list was updated. Do not infer interest from politeness.

## Output

```markdown
# Reply triage: {{date}}

| Account ref | Channel | Class | Quote (short) | Action | Draft ready | Suppression updated | Next step / date |
| --- | --- | --- | --- | --- | --- | --- | --- |

**Stop signals this week:** {{none | which}}
```

## Quality checks

- Every reply received a response or a recorded reason within one working day.
- Sequences stopped at the first reply.
- Every opt-out was added to the suppression list the same day.
- Positive replies became L0 leads with source `outbound`.
- No names or contact details in the public repository.

## Failure conditions

Stop and escalate to the founder when a reply alleges a legal breach, complains of spam, or asks for data deletion; honour the request first, then review.

## Human review

A person sends every reply. The founder reviews stop signals and any complaint.

## Example

**Fictional example.** A fictional founder replies, "Not this year — maybe after our autumn launch." Class: not now. The draft thanks them and asks whether February suits a short call; the sequence stops and a check-back is set for February.
