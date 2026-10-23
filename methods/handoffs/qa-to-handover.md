---
title: "Handoff: QA to production and handover"
type: checklist
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Handoff: QA to production and handover

Validated work moves to Production to be packaged, released and handed to the client. Happens at identity 07 → 08 and Digital Experience DX-07/08 → DX-09 (lifecycle L7). Production owns the pack and the records; Design and Engineering own the contents ([handover and care](../handover-and-care.md)).

- **From:** Design / design-qa and Engineering (validation or QA and launch-readiness owners).
- **To:** Production / handover-retention (`agency:project-management-studio-producer`).
- **Acceptance checker:** `agency:testing-evidence-collector` opens every item against the checklist; Operations / finance-legal (`agency:legal-document-review`) checks licence and ownership wording.

## Artefact checklist: identity

- [ ] Strategy and visual sign-offs with versions (`decisions.md`).
- [ ] Completed [identity system testing](../quality/identity-system-testing.md) matrix and defect log with retests; accepted exceptions signed by `C1`.
- [ ] Final `identity-system-spec.md` and guidelines source.
- [ ] Export list: formats, sizes, colour profiles and naming scheme, for `agent:bulk-executor` to run and Design to check.
- [ ] Font licence notes and acquisition path (no restricted font files); image and illustration rights register; AI-consent record for any AI-generated final (D-0023).
- [ ] Recipients and the client-approved delivery location (vault only).

## Artefact checklist: digital

- [ ] DX-07 QA log with no open critical or major defect; minors dispositioned.
- [ ] Current-build `bin/3w qa run <url>` reports for key templates following the [Web QA harness guide](../../docs/web-qa-harness.md) with raw evidence retained privately, lab status PASS and no unaccounted missing evidence. Overall PASS or INCOMPLETE follows the [mandatory harness rule](../playbooks/digital-experience.md#mandatory-harness-report-and-conditional-gate); the current harness intentionally leaves field/manual gates INCOMPLETE.
- [ ] `FIELD-DATA-DEFERRED` founder record names mobile p75 LCP/INP/CLS collection, owner, date and breach response. Any `REAL-PHONE-TEST-DEFERRED` condition from DX-07 has real-device closure evidence or an explicit DX-08 founder risk decision, with `C1` informed. Carry these in `handover.md`; do not rewrite the report verdict.
- [ ] DX-08 performance report against budgets, security review, completed [launch-readiness checklist](../quality/launch-readiness-checklist.md), launch plan with rollback, go/no-go record.
- [ ] Every item of the [digital handover pack](../handover-and-care.md#digital-handover-pack): repository, architecture note, CMS editor guide, tokens and motion specification, budgets and final measurements, accounts with the client as owner, dependency list with licences, asset and rights register.
- [ ] Training plan for the client's editors using their own content.
- [ ] Monitoring owner named for the 30-day warranty and who measures field Core Web Vitals.

## Acceptance checks (Production)

- [ ] The [final-delivery checklist](../quality/final-delivery-checklist.md) (identity) or launch-readiness checklist (digital) is complete, or each exception is recorded.
- [ ] Every delivered file opens; versions match the sign-offs.
- [ ] No client-owned infrastructure is left with the studio as its only owner.
- [ ] Operations confirms the final 20% payment before release of final files (D-0023); invoice and payment evidence stay in the vault. An unpaid final invoice is not release authority without a written founder variation.
- [ ] All image finals passed independent [`skill:3w-image-qa`](../../toolkit/cards/media/image-photo-direction/skill--3w-image-qa.md); unknown rights or AI-final consent block release. This is separate from layout/brand consistency QA.

## Return conditions

Return to the maker when a file fails to open, a version does not match its sign-off, a licence is unclear, a harness FAIL remains, or a checklist item is unmet without a permitted recorded exception. An unknown licence or missing written AI-final consent cannot be carried as an ordinary minor exception.

## Exit

`C1` confirms final acceptance and, separately, receipt and access; both are recorded in `decisions.md` and `handover.md`. Receipt is not a new creative approval. Record the 30-day warranty start at launch, or final acceptance when there is no launch, and the end date. [`skill:3w-care-retention`](../../toolkit/cards/production/handover-retention/skill--3w-care-retention.md) routes the care conversation, issue channel and eventual access removal.

## Record

One handoff row in `decisions.md` ([format](README.md#handoff-record)).
