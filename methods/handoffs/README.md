---
title: Department handoffs
type: guide
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Department handoffs

A handoff is the moment work changes owner between departments. Each contract below lists the artefacts the sending department must supply, the checks the receiving department runs before accepting, and when the work goes back. A handoff is a contract about artefacts, not a wall: the sending owner stays available, and Design and Engineering work as one pod throughout ([D-0019](../../studio/decisions/0019-organisation-and-loading-policy.md)).

| Contract | From → to | Where it happens |
| --- | --- | --- |
| [Strategy → design](strategy-to-design.md) | Strategy → Design | Identity 03 → 04; DX-01 → DX-02 |
| [Design → engineering (pod contract)](design-to-engineering.md) | Design ⇄ Engineering | Identity 06 for digital applications; DX-03 → DX-04, kept live to DX-06 |
| [Engineering → QA](engineering-to-qa.md) | Engineering → Design QA and independent Engineering QA | DX-05/06 → DX-07 |
| [QA → production and handover](qa-to-handover.md) | Design QA / Engineering → Production | Identity 07 → 08; DX-07/08 → DX-09 |
| [Delivery → marketing](delivery-to-marketing.md) | Production → Marketing (with Media) | L9 case study and proof |

Design's internal handoffs (direction → identity-craft → experience-design → release) stay in the [Design department guide](../../studio/departments/design.md#handoffs). Commercial handoffs (L2 → L3) use the `discovery-notes` hand-off pack in the [Growth engine](../../growth/README.md).

## Rules for every handoff

1. **No gate, no handoff.** The previous gate is logged in the project README gate log with approver and evidence ([format](../lifecycle.md#gate-log-format)).
2. **Versioned artefacts only.** Every item names a file and version; "latest" is not a version.
3. **Maker ≠ checker.** The receiving department's acceptance check is run by an agent instance that did not make the artefact, named in the record.
4. **Evidence over description.** Provide inspectable screenshots, measurements and exports; public logs retain only anonymised summaries and vault filenames. Unrun checks are recorded as **Unknown** or "not verified". Include relevant `evals/cases/` results, model separation and human spot-check; a score never replaces acceptance.
5. **Return, do not patch.** A failed acceptance check returns the work to its maker with the finding; the receiver does not quietly fix another department's artefact.
6. **Public or vault.** Client-identifying artefacts stay in the vault ([D-0021](../../studio/decisions/0021-client-work-public-anonymised.md)); the handoff record in the repository links by vault filename only.

## Handoff record

Append one row per handoff to `projects/<codename>/decisions.md` (or the vault copy for private projects). Never edit a past row; correct it with a new one.

| Field | Content |
| --- | --- |
| Handoff | Contract name, e.g. `strategy → design` |
| Date | YYYY-MM-DD |
| Artefacts | Files and versions handed over |
| Maker | Department and agent or role that made them |
| Checker | Receiving department and agent instance that ran the acceptance check |
| Verdict | `accepted`, `accepted with conditions` or `returned` |
| Evidence | Relative links or vault filenames |
| Unknowns | Open questions carried forward, each with an owner |
| Next owner | Who now holds the work |
| Founder decision | The gate decision this handoff relies on |

Use `accepted with conditions` only where the governing gate permits it. Name each missing item, risk, owner, due date and founder decision; the receiver acknowledges the condition explicitly. Never carry an unresolved Blocker, unknown rights or missing AI-final consent as routine acceptance. Use the [DX harness rule](../playbooks/digital-experience.md#mandatory-harness-report-and-conditional-gate) for field-data and real-phone deferrals. The handoff verdict is separate from the lifecycle gate values `pass`, `pass with conditions`, `hold` and `return to <stage>`, and from the written critique verdict.

## Related

- [Playbooks index](../playbooks/README.md) · [Department heads and RACI](../../studio/departments/heads.md)
- [Critique protocol](../quality/critique-protocol.md) for severity and verdicts
