---
title: Client lifecycle
type: method
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Client lifecycle

The backbone every client engagement runs on, from first contact to case
study: ten stages, each closed by a gate with a named decision. Offer methods
run inside L6; commercial documents and invoicing belong to the Business
engine; lead generation belongs to the Growth engine. This page owns the
sequence, the gates and the client's view of them.

## Purpose

Make every engagement predictable for the client and the studio: the same
stages, the same gate discipline and one gate log per project, whatever the
offer. A gate is a decision with evidence, not a date on a calendar.

## When it applies

Every client engagement for either pillar: the Identity System (core offer)
and Digital Experience (second pillar, approved in D-0018). Internal and
speculative projects use L5–L9 only. Fictional examples in
`projects/examples/` may use any stage to exercise methods.

## Roles

Departments follow D-0019 (Craft: Design, Engineering, Labs; Delivery:
Strategy, Production, Media; Growth: Marketing, Advertising, Outbound, Sales;
Studio: Operations). The founder holds strategic, creative and release
approval on every project. The client names one decision-maker, recorded as
`C1`; further client roles are `C2`, `C3` and so on. Roles, never names, go into
public records ([D-0021](../studio/decisions/0021-client-work-public-anonymised.md)).

## Stage overview

Durations are **Hypothesis** planning ranges for a single, founder-led
engagement; they are not commitments. Agree real dates in the plan at L5.

| Stage | Purpose | Owner departments | Studio sign-off | Client sign-off | Typical duration |
| --- | --- | --- | --- | --- | --- |
| L0 Lead | Capture and route a potential client | Outbound, Marketing | — | — | Continuous |
| L1 Qualify | Decide whether to pursue | Sales | Founder: pursue or decline | — | 1–5 working days |
| L2 Discover & scope | Understand the problem enough to scope it | Sales, Strategy; Design and Engineering for feasibility | Founder: scope is deliverable | Confirms problem and scope summary | 1–3 weeks |
| L3 Propose | Offer a scoped, priced plan | Sales (proposals, pricing desk) | Founder: approves proposal | Accepts or negotiates | 3–10 working days |
| L4 Contract & deposit | Make the commitment binding | Sales, Operations (finance-legal) | Founder: signs | Signs, pays deposit, sets clearance | 1–10 working days |
| L5 Onboard & kickoff | Set up the project and align everyone | Production | Founder: plan and team | Confirms plan, roles, access and inputs | 3–5 working days |
| L6 Deliver | Run the offer method to accepted work | Design + Engineering pod; Strategy, Media as scoped; Production coordinates | Founder at every method gate | Approves at each method gate | Per offer; identity 4–6 weeks proposed |
| L7 Launch & handover | Release and transfer ownership | Production, Engineering, Design | Founder: release | Final acceptance and receipt | 1–2 weeks |
| L8 Care | Warranty, then an optional care plan | Production (handover-retention), Engineering | Founder: care scope | Reports issues; approves care work | Warranty period, then per plan |
| L9 Close-out & case study | Learn, close and, if permitted, publish | Production, Marketing, Operations | Founder: retro actions, publication | Final invoice; case-study permission | 1–3 weeks after acceptance |

The identity duration comes from the [identity system offer](../studio/identity-system-offer.md).
No Digital Experience duration is established; estimate it from the stage 04
prototype.

## Steps: stage by stage

Each stage lists its entry condition, the exit gate checklist and the
artefacts. A stage cannot start until the previous exit gate is logged as
`pass` or `pass with conditions`.

### L0 Lead

- **Owner:** Growth engine (Outbound, Marketing). **Entry:** any inbound or
  outbound contact.
- **Exit gate:** contact recorded in the Growth engine's pipeline with source,
  need in one line and next action; no personal data in the public repository.
- **Artefacts:** pipeline record (Growth engine).
- **Client's view:** a prompt, specific reply.

### L1 Qualify

- **Owner:** Sales. **Entry:** L0 record.
- **Exit gate:**
  - [ ] Buyer, problem, authority, timing, content readiness, budget fit and
        maintenance owner assessed (Growth engine qualification).
  - [ ] Fit with an offer pillar, or a clear decline with a reason.
  - [ ] Founder decision: pursue or decline.
- **Artefacts:** qualification note (Growth engine).
- **Client's view:** a short call; a clear yes, no or "not yet" with a reason.

### L2 Discover & scope

- **Owner:** Sales with Strategy; Design and Engineering assess feasibility.
- **Exit gate:**
  - [ ] Problem statement, decision question and success criteria drafted.
  - [ ] Scope boundary: in, out, assumptions, client inputs and their dates.
  - [ ] Feasibility and capacity confirmed by Design and Engineering leads.
  - [ ] Client confirms the problem and scope summary in writing.
- **Artefacts:** scoping notes and scope summary (Growth engine); confidential
  notes in the vault.
- **Client's view:** a working session; a one-page scope summary to confirm.

### L3 Propose

- **Owner:** Sales (proposals-pitches, pricing-deal-desk).
- **Exit gate:**
  - [ ] Proposal states scope, deliverables, method stages, review rounds per
        stage, timeline, exclusions, change control, acceptance criteria,
        ownership and price (Business engine proposal).
  - [ ] Publication clause offered: anonymised publication permitted or not.
  - [ ] Founder approves before sending; client accepts.
- **Artefacts:** proposal (Business engine; the sent copy lives in the vault).
- **Client's view:** a proposal walkthrough; one round of questions.

### L4 Contract & deposit

- **Owner:** Sales with Operations (finance-legal).
- **Exit gate:**
  - [ ] Contract signed by both parties, filed in `<vault>/<codename>/contracts/`.
  - [ ] Deposit received (Business engine invoicing).
  - [ ] Codename assigned and the client recorded in the vault's `clients.yaml`.
  - [ ] Clearance recorded: **cleared** (anonymised publication permitted) or
        **private**.
- **Artefacts:** contract and invoice (vault); workspace created with
  `bin/3w new <bundle> --cleared` or `--private`.
- **Client's view:** a contract to sign, a deposit invoice and a kickoff date.

### L5 Onboard & kickoff

- **Owner:** Production (producing-pm, client-experience). **Entry:** L4 pass;
  no delivery work starts before it.
- **Exit gate:**
  - [ ] Kickoff held; agenda and outcomes in the decision log.
  - [ ] Plan with milestones, method gates, review dates and client input dates.
  - [ ] RACI agreed; `C1` confirmed as the single feedback consolidator.
  - [ ] Access granted through the vault process; inputs inventoried.
  - [ ] Communication channels, weekly status day and response times agreed.
  - [ ] Anonymised brief written in `projects/<codename>/brief.md` (cleared) or
        the vault (private).
- **Artefacts:** project workspace from the bundle; see
  [project operations](../business/engagement-operations.md#kickoff).
- **Client's view:** one kickoff session, a welcome pack with plan, roles,
  dates and what the studio needs from them.

### L6 Deliver

- **Owner:** the paired Design + Engineering pod; Strategy for research and
  positioning; Media for scoped assets; Production coordinates.
- **Method:** [identity engagement](identity-engagement/README.md) or
  [digital experience](digital-experience/README.md). Each method gate is
  logged in the project gate log.
- **Exit gate:**
  - [ ] Every method gate passed, with approver and version.
  - [ ] Final QA evidence recorded: [final-delivery checklist](quality/final-delivery-checklist.md)
        for identity; [web QA](quality/web-qa-checklist.md) for digital.
  - [ ] Open defects listed with severity, owner and an agreed disposition.
  - [ ] Changes processed through change control; none folded in silently.
- **Artefacts:** method deliverables; weekly status; feedback log; QA log.
- **Client's view:** weekly status, a review at each method gate with a clear
  question, and a limited number of consolidated feedback rounds.

### L7 Launch & handover

- **Owner:** Production with Engineering and Design.
- **Exit gate:**
  - [ ] Launch readiness passed ([launch-readiness checklist](quality/launch-readiness-checklist.md))
        for digital; final-delivery checklist for identity.
  - [ ] Handover pack delivered and walked through
        ([handover and care](handover-and-care.md)).
  - [ ] Client confirms final acceptance and, separately, receipt and access.
  - [ ] Final or milestone invoice issued (Business engine).
- **Artefacts:** handover pack; handover record; acceptance in the decision log.
- **Client's view:** a launch, a walkthrough, a handover pack they can use
  without the studio.

### L8 Care

- **Owner:** Production (handover-retention) with Engineering.
- **Exit gate:**
  - [ ] Warranty period closed; every reported defect fixed or dispositioned.
  - [ ] Care plan agreed, or explicitly declined.
  - [ ] Access no longer needed has been removed and credentials rotated.
- **Artefacts:** care log; handover record updated.
- **Client's view:** a named channel for issues, response times as agreed, and a
  care plan offer.

### L9 Close-out & case study

- **Owner:** Production (retro, learning loop, clearance); Marketing (case
  study, Growth engine); Operations (final invoice, archive, Business engine).
- **Exit gate:**
  - [ ] Retrospective held within two weeks of acceptance; lessons routed
        through the [learning loop](learning-loop.md) with owners.
  - [ ] Publication clearance re-checked: anonymity guard passes, a human has
        reviewed for identifying combinations, and any case study naming the
        client has separate written permission.
  - [ ] Final invoice paid and the vault archived (Business engine).
  - [ ] Project README marked closed; gate log complete.
- **Artefacts:** `retro.md`; method or template change proposals; case study
  (Growth engine) if permitted.
- **Client's view:** a short close-out call or note, a request for feedback and,
  if they wish, a case-study conversation.

## Gate log format

Every project README carries one gate log. Append a row per gate; never edit a
past row; correct it with a new row.

| Gate | Date | Decision | Approver | Evidence | Conditions or notes |
| --- | --- | --- | --- | --- | --- |
| L5 exit: kickoff complete | YYYY-MM-DD | pass with conditions | founder; `C1` | `decisions.md` PD-004 | Brand assets due by the next review |

- **Gate:** lifecycle exit (`L5 exit: …`) or method gate (`DX-04 prototype`).
- **Decision:** `pass`, `pass with conditions`, `hold` or `return to <stage>`.
- **Approver:** roles or codes only.
- **Evidence:** a relative link to a workspace file, or a vault filename.

## Outputs

- One project workspace per engagement, from the
  [template bundles](../templates/bundles/README.md).
- A complete gate log; a decision log; weekly status reports; a retrospective.

## Quality gate

- [ ] No stage starts before the previous exit gate is logged.
- [ ] Every gate names its approver role and evidence.
- [ ] Client approvals are explicit; silence is never logged as approval.
- [ ] Public records pass `bin/3w check` and a human anonymity review.

## Metrics

Track per project in the retrospective, then across projects at quarterly
review. These are proposed measures with no baselines yet.

- Gate pass rate at first review, per stage.
- Feedback rounds used against the agreed limit.
- Change requests raised and accepted.
- Planned against actual duration per stage.
- Defects found after launch during warranty.

## Failure modes

- Starting delivery before contract and deposit (L4) because the client is
  keen.
- Treating a kickoff meeting as onboarding without inputs, access and dates.
- Merging strategy and visual approval into one gate.
- Logging names, fees or URLs in a public gate log.
- Skipping the retrospective when the project went well.

## Related

- [Project operations](../business/engagement-operations.md)
- [Handover and care](handover-and-care.md)
- [Identity engagement method](identity-engagement/README.md) and
  [digital experience method](digital-experience/README.md)
- [Publication rules](../docs/public-private-boundary.md)
- Growth engine (L0–L2) and Business engine (L3–L4, invoicing): see their
  folders once integrated.
