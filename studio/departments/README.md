---
title: Department index
type: guide
status: proposed
owner: founder
last_reviewed: 2026-10-22
review_every_days: 90
---

# Department index

**Interpretation — proposed operating structure.** Departments organise work,
responsibility and tool selection. They do not expand the studio's approved
[offer scope](../decisions/0002-identity-system-scope.md).

| Department | Current material | Responsibility |
| --- | --- | --- |
| Strategy | Provisional toolkit assignments in the registry | Positioning, consumer/perception research and culture/behaviour. |
| Design | [Operating guide](design.md), [tool registry](design-toolkit.yaml) | Direction, Identity Craft, Living & Digital, independent Critique & QA. |
| Media Production | Provisional toolkit assignments in the registry | Video/motion-graphics production, image generation and audio/voice. |
| Marketing & Content | Provisional toolkit assignments in the registry | Copy/voice, social, launch/PR and search. |
| Engineering | Provisional toolkit assignments in the registry | Frontend implementation, platform/deployment and software tooling. |
| Quality & Security | Provisional toolkit assignments in the registry | General testing, measured performance and security. |
| Business & Sales | Provisional toolkit assignments in the registry | Sales/proposals, pricing/finance and client operations. |
| Operations & Workflow | Provisional toolkit assignments in the registry | Planning, execution discipline and knowledge/docs. |

Each later department should use the same pattern: purpose, accountable owner,
jobs with a small number of leads, specialists with named triggers, an honest
bench, independent review gates, founder sign-off and a complete registry.
These assignments are proposed destinations, not staffed services. Separate
division organisers will refine the seven divisions outside Design.

The [registry schema](design-toolkit.schema.yaml) defines machine-readable
entries. Run the [local scanner](../../scripts/scan_toolkit.py) after installing,
removing or updating tools and before accepting a toolkit review. It checks
this machine; CI cannot reproduce the founder's local installation inventory.
