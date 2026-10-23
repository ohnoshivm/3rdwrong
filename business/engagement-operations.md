---
title: Project operations
type: method
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Project operations

The studio's standard for running a client project day to day, from kickoff
(L5) to close-out (L9) in the [client lifecycle](../methods/lifecycle.md).
Offer methods say what to make; this page says how the project is run around
them. Commercial terms, proposals, change orders and invoices belong to the
Business engine; this page hands off to them by name.

## Purpose

Clients always know where the project stands, what is needed from them and
what happens next. The studio never absorbs unagreed scope, never treats
silence as approval and never loses a decision.

## When it applies

Every client engagement from L5 Onboard & kickoff onwards, for both pillars.
Internal projects use the ceremonies and logs they find useful.

## Roles

| Role | Department | Responsibility |
| --- | --- | --- |
| Founder | Studio | Strategic, creative and release approval; escalation point |
| Producer | Production (producing-pm) | Plan, status, risks, changes, client communication |
| Design lead | Design | What and why; design gates and design QA |
| Engineering lead | Engineering | How; technical gates, engineering QA and security |
| Strategy lead | Strategy | Research and positioning inputs, when scoped |
| Client decision-maker `C1` | Client | Approvals and consolidated feedback |
| Client contributors `C2`… | Client | Content, access and subject knowledge |

On a founder-led project the founder may also act as producer; name that
explicitly in the RACI so the checks still happen.

### RACI

R = responsible, A = accountable, C = consulted, I = informed.

| Activity | Founder | Producer | Design lead | Eng. lead | `C1` |
| --- | --- | --- | --- | --- | --- |
| Plan and milestones | A | R | C | C | C |
| Weekly status | I | A/R | C | C | I |
| Method gate review | A | R | R | R | C |
| Client approval at a gate | C | R | C | C | A |
| Change request | A | R | C | C | C |
| Risk and issue log | I | A/R | C | C | I |
| QA sign-off | A | I | R (design QA) | R (engineering QA) | I |
| Launch go/no-go | A | R | C | R | A |
| Handover and receipt | C | A/R | C | R | A |
| Retrospective | A | R | C | C | C |

## Inputs

- Signed contract and clearance (L4), recorded in the vault.
- The project workspace from `bin/3w new` ([template bundles](../templates/bundles/README.md)).
- The offer method: [identity engagement](../methods/identity-engagement/README.md)
  or [digital experience](../methods/digital-experience/README.md).

## Steps

### Kickoff

Hold within five working days of L4. Agenda:

1. Goals, success criteria and what is out of scope, read back to the client.
2. Method stages, gates, and what each client approval does and does not
   approve.
3. Plan: milestones, review dates, client input dates and holidays.
4. Roles and RACI; `C1` confirmed as the single feedback consolidator.
5. Communication channels, status day and response times.
6. Inputs and access: what the studio needs, from whom, by when; access is
   granted through the vault process.
7. Feedback rounds and change control, in plain words.
8. Risks the client sees.

Outcomes go into `decisions.md`; the plan and brief go into the workspace.

### Weekly status report

Every week on the agreed day, even when nothing visible moved. Use the format
in the workspace's `status/README.md`: overall state (on track, at risk, off
track) with one reason, stage and next gate, done, next, decisions needed with
dates and consequences of delay, risk changes and change requests. Send it to
the client and file it in `status/YYYY-MM-DD.md`. Hold a short call only when
a decision needs discussion.

### Client reviews

- One review per method gate, with the artefact version and **the question
  being asked** stated in the invitation.
- Present the work against the brief and criteria; show options only with
  their consequences.
- Strategy, concept, art direction and launch are separate approvals.
- Close each review with the decision, or a date for `C1`'s consolidated
  feedback.

### Internal critiques

Before every client review, run an internal crit with the
[critique protocol](../methods/quality/critique-protocol.md): stated phase and
decision, approved criteria, evidence labels and severity. No department
reviews its own work alone. Fix critical and major findings before the client
sees the work.

### Timeline and milestones

- The plan lists milestones per method gate, each with a date, an owner and the
  client inputs it depends on.
- Client input dates are part of the plan. When an input is late, the producer
  states the effect on the plan in that week's status report; do not compress
  studio quality time to absorb it silently.
- Re-plan formally when a milestone moves by more than a week; log it in
  `decisions.md`.

### Communication rules

- One agreed written channel for decisions; calls are summarised in writing
  within one working day.
- Respond to client messages within one working day, even if only to say when
  an answer will come.
- No decisions in private messages to individuals; they go to the agreed
  channel and the log.
- Bad news early: raise a risk the day it is seen.
- Explain what the next decision enables and what remains open; label
  evidence, interpretation, hypothesis and unknown.
- Keep critique about the work, criteria and evidence rather than taste or
  status.

### Feedback rounds and revision limits

- Each method gate includes a set number of consolidated feedback rounds,
  agreed in the proposal. The studio's default number is a founder decision
  still to be made.
- `C1` sends one consolidated set of comments per round, by the agreed date.
  Contradictory comments go back to `C1` to resolve before work starts.
- Every comment is logged in `feedback.md` as a fix, refinement or new
  direction, with the studio's response.
- A new direction after sign-off, a change to approved strategy, or a round
  beyond the limit goes to change control.

### Change control

1. Anyone may raise a change; the producer logs it in `decisions.md` with what
   changes and why.
2. The producer and leads assess the effect on scope, timeline, quality and
   risk.
3. The Business engine issues a change order covering scope, fee and schedule.
4. No work on the change starts until the change order is signed; the original
   plan continues meanwhile.
5. The plan, brief and gate log are updated; the change-order reference (not
   its fee) is logged.

### Risk and issue log

Kept in the workspace's `risks.md`. A risk may happen; an issue has happened.
Each entry has an ID, description, likelihood, impact, owner role, response,
trigger or due date and state. Review it in every weekly status; escalate any
high-likelihood, high-impact item to the founder the same day.

### Approvals log

Kept in the workspace's `decisions.md`. Each approval records the date, the
artefact and version, the approver role or code, what was approved and what
was not, and any conditions. Silence is never logged as approval. Every gate
also appears in the README's gate log.

### File and version naming

- Pattern: `<codename>_<deliverable>_<variant>_v<major>.<minor>.<ext>`, for
  example `quiet-harbour_logo_primary-rgb_v2.1.svg`. Lowercase, hyphens inside
  parts, underscores between parts, no spaces.
- Minor versions for internal iterations, major versions for client-reviewed
  issues. The approved version is named in the approvals log.
- Never `final`, `final-final` or dates as the only version marker.
- Client-facing exports may use the client's name only inside the vault or the
  client's own systems, never in the public repository.

### Access and credentials

- Credentials are exchanged only through a password manager share or the
  client's own system, never by email or chat, and are never written in the
  repository.
- The vault records which access the studio holds, where it is kept and when
  it is removed; see the [publication rules](../docs/public-private-boundary.md#the-vault).
- Request least privilege and time-bound access; remove it at offboarding
  ([handover and care](../methods/handover-and-care.md#offboarding-and-access-removal)).

## Outputs

Plan; RACI; kickoff record; weekly status reports; review and crit records;
feedback log; risk and issue log; approvals log; change-order references; a
consistently named, versioned file set.

## Quality gate

- [ ] Kickoff held and recorded before any method work.
- [ ] A status report exists for every project week.
- [ ] Every gate has a recorded approval with version and approver role.
- [ ] Every scope change has a change-order reference before work started.
- [ ] No credentials, names, money or client files in the public record.

## Metrics

Proposed, with no baselines yet: on-time milestones; status reports sent on
the agreed day; rounds used against limits; change requests raised and
accepted; risks that became issues.

## Failure modes

- A new brief folded into the old fee because the client is pleasant.
- Feedback from several people with no consolidator.
- Status reports that only report activity, not decisions needed.
- Decisions made in calls and never written down.
- Credentials pasted into chat "just this once".

## Related

- [Client lifecycle](../methods/lifecycle.md) and
  [handover and care](../methods/handover-and-care.md)
- [Critique protocol](../methods/quality/critique-protocol.md)
- [Publication rules](../docs/public-private-boundary.md)
- Business engine: proposal, change order, contract and invoicing templates.
- The [AIGA Standard Form of Agreement for Design Services](https://www.aiga.org/sites/default/files/2023-11/Standardformofagreement_2022update.pdf)
  is a professional reference for contract architecture; adapt any agreement
  with an Indian legal professional.
