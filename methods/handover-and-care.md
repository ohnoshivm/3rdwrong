---
title: Handover and care
type: method
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Handover and care

How the studio transfers finished work so the client can own it, supports it
through a warranty period, offers ongoing care, and closes access cleanly.
Covers lifecycle stages L7 Launch & handover and L8 Care.

## Purpose

The client can find, use, edit and maintain everything they paid for without
the studio, and every access the studio held is either justified by a care
plan or removed.

## When it applies

Every engagement at L7, for both pillars. Internal projects use the pack as a
checklist only.

## Roles

- **Production** (handover-retention): owns the pack, the walkthrough, the
  records and offboarding.
- **Design:** guidelines, usage rules, source files.
- **Engineering:** source code, deployment, CMS, documentation (digital).
- **Operations** (finance-legal): licences, ownership transfer terms.
- **Sign-off:** `C1` confirms final acceptance and, separately, receipt and
  access. The founder approves the release and the care scope.

## Inputs

- Approved final work with version references; signed scope and acceptance
  criteria; licence records; the project's `handover.md`.

## Steps

1. Assemble the pack for the offer (below); check it against the
   [final-delivery checklist](quality/final-delivery-checklist.md) (identity)
   or [launch-readiness checklist](quality/launch-readiness-checklist.md)
   (digital).
2. Deliver through a client-approved secure location; record the location in
   the vault, never in the public record.
3. Walk the client through the pack live; train editors on their own content.
4. Record final acceptance and receipt separately in `decisions.md`; update
   `handover.md`. Receipt is not a new creative approval.
5. Start the warranty period; publish the care channel and response times.
6. At warranty end, close it, agree or decline a care plan, and run
   offboarding.

### Identity handover pack

- Guidelines: strategy summary, concept, rules, accessibility notes,
  production notes, examples and exceptions.
- Asset library in agreed formats with an index: name, purpose, variant,
  format, dimensions, colour space and version.
- Editable source files where agreed.
- Font licence notes and the acquisition path; no restricted font files.
- Rights register for third-party images, illustrations and software.
- Handover record: location, version, recipients, permissions, open items.

### Digital handover pack

- Source repository transferred to, or mirrored in, a client-owned account,
  with a README covering set-up, build, deploy and rollback.
- Architecture note: stack, hosting, integrations, environment variables (names
  only), third-party services and their owners.
- CMS editor guide, content models and image guidance; training record.
- Design tokens, component inventory and motion specification.
- Budgets and the final measurement record; known limitations and accepted
  exceptions.
- Accounts and ownership: domain, DNS, hosting, CMS, analytics, search
  console, error monitoring, each with the client as owner.
- Dependency list with licences and an update policy.
- Asset library and rights register, as for identity.

## Warranty period

A fixed period after launch (or final acceptance where there is no launch)
during which the studio fixes, at no extra charge, defects where the
delivered work does not meet the agreed acceptance criteria. The studio
default is **30 days** ([D-0023](../studio/decisions/0023-commercial-and-delivery-defaults.md)); a contract may differ only with founder
approval. Longer support is a paid care plan.

- **Covered:** defects against acceptance criteria on the agreed matrix.
- **Not covered:** new features, content changes, changes requested after
  acceptance, third-party service changes, browser releases after launch, and
  issues caused by edits outside the studio. These go to change control or a
  care plan.
- Response and fix times are set in the contract and recorded in
  `handover.md`.

## Care-plan structure

A care plan is optional, scoped and time-bound; prices are set by the Business
engine and never recorded here or in a project record. Each plan states:

| Element | What to define |
| --- | --- |
| Term | Start, length, renewal and notice |
| Monitoring | Uptime, errors, field Core Web Vitals, security advisories |
| Maintenance | Dependency and platform updates, backups, certificate and domain renewals |
| Support | Channel, hours, response and fix times by severity |
| Iteration | A fixed allowance of design and engineering time, planned monthly or quarterly |
| Reporting | A periodic report: incidents, measurements, updates, recommendations |
| Exclusions | New pages, new features or redesigns go to a new scope |
| Access | Which studio accounts remain, why, and when they are reviewed |

Identity care, where offered, covers guideline updates, new application
templates and brand-consistency reviews, using the same structure.

## Offboarding and access removal

At warranty end without a care plan, or when a care plan ends:

- [ ] Studio accounts removed from the client's hosting, CMS, analytics, DNS,
      repositories and shared drives, or downgraded as agreed.
- [ ] Shared credentials rotated by the client; the studio confirms it holds
      none.
- [ ] Studio-held API keys and deploy tokens revoked.
- [ ] Vault folder for the codename archived; raw files and personal data
      deleted when no longer needed, with the date noted in `private-notes/`.
- [ ] `handover.md` and the gate log updated; L8 exit logged.

## Outputs

Handover pack; acceptance and receipt records; warranty closure; care plan or
recorded decline; offboarding record.

## Quality gate

- [ ] Every pack item delivered and opened by the client.
- [ ] Acceptance and receipt recorded separately with version.
- [ ] Warranty terms and response times written down before launch.
- [ ] Access removal verified, not assumed.

## Metrics

Proposed: warranty defects per project; time to fix by severity; care-plan
uptake; access-removal completion at L8 exit.

## Failure modes

- A handover that depends on studio accounts.
- Warranty used as an unlimited change budget.
- Credentials sent by email or chat instead of the client's password manager.
- Forgotten studio access years later.

## Related

[Client lifecycle](lifecycle.md) ·
[Project operations](../business/engagement-operations.md) ·
[09 Launch & handover](digital-experience/09-launch-and-handover.md) ·
[10 Care & iteration](digital-experience/10-care-and-iteration.md) ·
[Identity 08 Delivery](identity-engagement/08-delivery.md)
