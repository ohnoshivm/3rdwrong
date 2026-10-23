---
title: Department index
type: guide
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Department index

[D-0019](../decisions/0019-organisation-and-loading-policy.md) approves eleven departments in four groups, with Design and Engineering as the flagships. These guides propose job routing under that organisation; tool presence does not prove runtime quality or connectivity.

| Group | Department | Handbook | Responsibility |
| --- | --- | --- | --- |
| Craft | [Design](design.md) | [Tool handbook](../../handbook/design.md) | Concept, identity, experience intent and independent visual critique. |
| Craft | [Engineering](engineering.md) | [Tool handbook](../../handbook/engineering.md) | Creative engineering, implementation, platform, performance and security. |
| Craft | [Labs](labs.md) | [Tool handbook](../../handbook/labs.md) | Experiments, reusable house engines and open-source showcases. |
| Delivery | [Strategy](strategy.md) | [Tool handbook](../../handbook/strategy.md) | Positioning, research, perception, culture and behaviour. |
| Delivery | [Production](production.md) | [Tool handbook](../../handbook/production.md) | Producing, project management, client experience and handover. |
| Delivery | [Media](media.md) | [Tool handbook](../../handbook/media.md) | Film, motion graphics, image/photo direction and sound. |
| Growth | [Marketing](marketing.md) | [Tool handbook](../../handbook/marketing.md) | Studio voice, content, social, PR, awards and search. |
| Growth | [Advertising](advertising.md) | [Tool handbook](../../handbook/advertising.md) | Paid social, search, creative measurement and attribution. |
| Growth | [Outbound](outbound.md) | [Tool handbook](../../handbook/outbound.md) | Prospecting, sequences, partnerships and referrals. |
| Growth | [Sales](sales.md) | [Tool handbook](../../handbook/sales.md) | Qualification, pitches, pricing/deal desk and forecasting. |
| Studio | [Operations](operations.md) | [Tool handbook](../../handbook/operations.md) | Workflow, knowledge systems, finance/legal and people/partners. |

## Loading policy

Choose the job lead first. Leads and specialists are active; load a specialist only when its recorded trigger applies. Bench and parked tools remain in the library, callable by explicit name after review. Use one primary route rather than stacking overlapping routers. Department heads coordinate; independent reviewers check evidence; the founder signs decisions. Design and Engineering prototype together early.

The [canonical registry](../../toolkit/sources/registry.json) records 1,364 source tools, 808 active and 556 library entries. The [registry summary](registry-summary.md) records all jobs/leads, counts, gaps, source corrections and boundary overrides. The [toolkit coverage](../../toolkit/coverage.json), [pinned fetch plan](../../toolkit/fetch.yaml) and [manual checklist](../../toolkit/manual.md) explain distribution and availability.

## Heads and playbooks

[Department heads](heads.md) proposes a head agent, job owners, reviewer pool, escalation path and quality bar for each department, with a RACI per lifecycle stage. The [delivery playbooks](../../methods/playbooks/README.md) show how the departments run one project together, and the [handoff contracts](../../methods/handoffs/README.md) define what passes between them.

## Lead gaps

The current registry/charters retain the pre-v0.6 gaps; do not treat them as proof that a newer skill is installed. The [heads guide](heads.md) and [playbooks](../../methods/playbooks/README.md) route the four W1 craft leads and twelve W2 gap-closing leads by their proposed registry ids. Their `skills/3w-*/SKILL.md` files and scratch registry patches are integration dependencies. The registry owner applies them and regenerates charter views; this workstream does not edit the canonical registry. Type, mark, colour and composition decisions remain human-led.

Remaining delivery limits are explicit in the [identity playbook](../../methods/playbooks/identity-system.md#gaps-recorded-by-this-playbook): no complete identity export/manifest lead, physical production proofing needs a vendor, and script verification needs fluent human reviewers. Assign these people at kickoff. Tool presence and source review never replace the pre-client `evals/` checks or founder review of the complete `evals/pilot/README.md` rehearsal.

## Legacy scanner compatibility

The v1 [Design registry](design-toolkit.yaml) and [schema](design-toolkit.schema.yaml) are retained only because [scan_toolkit.py](../../scripts/scan_toolkit.py) validates the v1 schema and local installation inventory. They are superseded for routing by the canonical v2 JSON. The scanner cannot consume v2's department taxonomy and reduced portable fields; migrating its local discovery contract needs a separate tested change. Do not use its v1 placements as current department policy or CI evidence.
