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

| Group | Department | Responsibility |
| --- | --- | --- |
| Craft | [Design](design.md) | Concept, identity, experience intent and independent visual critique. |
| Craft | [Engineering](engineering.md) | Creative engineering, implementation, platform, performance and security. |
| Craft | [Labs](labs.md) | Experiments, reusable house engines and open-source showcases. |
| Delivery | [Strategy](strategy.md) | Positioning, research, perception, culture and behaviour. |
| Delivery | [Production](production.md) | Producing, project management, client experience and handover. |
| Delivery | [Media](media.md) | Film, motion graphics, image/photo direction and sound. |
| Growth | [Marketing](marketing.md) | Studio voice, content, social, PR, awards and search. |
| Growth | [Advertising](advertising.md) | Paid social, search, creative measurement and attribution. |
| Growth | [Outbound](outbound.md) | Prospecting, sequences, partnerships and referrals. |
| Growth | [Sales](sales.md) | Qualification, pitches, pricing/deal desk and forecasting. |
| Studio | [Operations](operations.md) | Workflow, knowledge systems, finance/legal and people/partners. |

## Loading policy

Choose the job lead first. Leads and specialists are active; load a specialist only when its recorded trigger applies. Bench and parked tools remain in the library, callable by explicit name after review. Use one primary route rather than stacking overlapping routers. Department heads coordinate; independent reviewers check evidence; the founder signs decisions. Design and Engineering prototype together early.

The [canonical registry](../../toolkit/sources/registry.json) records 1,364 source tools, 808 active and 556 library entries. The [registry summary](registry-summary.md) records all jobs/leads, counts, gaps, source corrections and boundary overrides. The [toolkit coverage](../../toolkit/coverage.json), [pinned fetch plan](../../toolkit/fetch.yaml) and [manual checklist](../../toolkit/manual.md) explain distribution and availability.

## Lead gaps

Gaps are deliberate rather than filled by an unreviewed tool. Design needs human ownership for mark/logo, colour and cross-format composition. Labs lacks leads for effect studies, research benchmarks, engine validation and demo publishing. Strategy lacks behavioural-theory and narrative-analysis leads; Production lacks retention-programmes; Media lacks image-production-workflow and image-quality-check; Marketing lacks awards-submissions. Consult each department's Gaps section and the registry summary for the complete current list.

## Legacy scanner compatibility

The v1 [Design registry](design-toolkit.yaml) and [schema](design-toolkit.schema.yaml) are retained only because [scan_toolkit.py](../../scripts/scan_toolkit.py) validates the v1 schema and local installation inventory. They are superseded for routing by the canonical v2 JSON. The scanner cannot consume v2's department taxonomy and reduced portable fields; migrating its local discovery contract needs a separate tested change. Do not use its v1 placements as current department policy or CI evidence.
