---
title: Digital experience method
type: method
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Digital experience method

How the studio delivers the second pillar, Digital Experience ([D-0018](../../studio/decisions/0018-design-engineering-studio.md)):
award-level websites, WebGL/3D, motion and creative engineering grounded in an
identity system. It runs inside lifecycle stage L6 Deliver, with stages 09 and
10 carrying into L7 and L8. Scope, exclusions and acceptance criteria come from
the Digital Experience offer page in `studio/`; this method says how the work
is done.

## Purpose

Turn an approved identity and a signed scope into a measured, accessible,
maintainable digital experience, with original craft and real rendered
evidence at every gate.

## When it applies

Any engagement whose signed scope includes a website, campaign site or
interactive experience. If no validated identity exists, run or agree an
identity engagement first; do not hide a rebrand inside a website build.

## Roles

The paired pod from [D-0019](../../studio/decisions/0019-organisation-and-loading-policy.md) works together from day one. **Design** owns what
and why: concept, art direction, UX/UI, interaction and motion design, design
QA. **Engineering** owns how: implementation, 3D/WebGL, CMS, deployment,
performance, code QA and security. **Production** coordinates, **Strategy**
supplies research and positioning inputs, **Media** produces scoped assets
under Design's direction, and **Labs** research is never silently billed as
delivery. The founder approves every gate; the client decision-maker `C1`
approves the gates marked as client gates. No reviewer reviews their own
department's work alone.

## Stages and gates

| Stage | Purpose | Lead pod roles | Gate (client approval in bold) |
| --- | --- | --- | --- |
| [01 Discovery & audit](01-discovery-and-audit.md) | Understand audiences, content, identity, constraints and the current site | Strategy, experience-design, platform-performance | DX-01: **confirmed inputs and success criteria** |
| [02 Experience strategy & concept](02-experience-strategy-and-concept.md) | One original idea, information architecture and key journeys | direction, experience-design, creative-engineering | DX-02: **concept and sitemap approved** |
| [03 Art direction & design system](03-art-direction-and-design-system.md) | Tokens, type, colour, layout, components and motion language | direction, identity-craft, experience-design | DX-03: **art direction approved**; tokens frozen for the prototype |
| [04 Prototype](04-prototype.md) | The critical slice in a real browser on target hardware | creative-engineering, experience-design | DX-04: **prototype accepted**; budgets and fallbacks agreed |
| [05 Production build](05-production-build.md) | Pages, content, CMS and integrations on the agreed architecture | product-frontend, platform-performance | DX-05: working build feature-complete |
| [06 Motion, 3D & interaction](06-motion-3d-and-interaction.md) | Purposeful motion and scenes within budget | creative-engineering, experience-design | DX-06: motion and scenes pass budgets and reduced-motion review |
| [07 QA](07-qa.md) | Visual, accessibility, cross-browser and content QA | design-qa, engineering-qa-security | DX-07: no open critical or major defects |
| [08 Performance & launch readiness](08-performance-and-launch-readiness.md) | Measured budgets, security, SEO, analytics and go-live plan | platform-performance, engineering-qa-security | DX-08: **launch approved** |
| [09 Launch & handover](09-launch-and-handover.md) | Release, verify live, transfer ownership | deployment-and-release, Production | DX-09: **final acceptance and receipt** |
| [10 Care & iteration](10-care-and-iteration.md) | Warranty, monitoring, measured iteration | Production, platform-performance | DX-10: warranty closed; care plan agreed or declined |

## Studio standards that apply to every stage

- **References are inspiration only.** Study principles; never copy layouts,
  assets, copy or identity. Record what was learned, not what was taken.
- **Tokens before components.** Spacing, type, colour, radii, motion durations
  and easings exist as named tokens before any component is built.
- **Prototype before the full build.** The hardest part runs in a real browser
  on target hardware before scaling to every page.
- **One smooth-scroll engine.** Never stack two scroll libraries or competing
  scroll-jacking systems.
- **Motion only with purpose,** supporting hierarchy, narrative or feedback,
  and always honouring `prefers-reduced-motion`.
- **Real rendered evidence.** Nothing is done until inspected in a real browser
  at desktop, tablet and mobile widths, with screenshots kept in the vault.
- **Measured, not assumed.** Performance and accessibility claims cite a
  measurement, its device, network profile and date.

Full thresholds are in [web standards](../quality/web-standards.md).

## Gate discipline

Strategy, concept, art direction and launch are separate approvals; one never
implies another. A change to an approved concept or art direction returns to
that stage and goes through change control
([project operations](../../business/engagement-operations.md#change-control)).
Log every gate in the project README's gate log ([lifecycle](../lifecycle.md#gate-log-format)).

## Metrics

Proposed, with no baselines yet: budget exceptions approved per project;
defects found in stage 07 versus after launch; rounds used per client gate;
p75 Core Web Vitals 28 days after launch where field data exists.

## Related

- [Client lifecycle](../lifecycle.md)
- [Web standards](../quality/web-standards.md),
  [web QA checklist](../quality/web-qa-checklist.md),
  [launch-readiness checklist](../quality/launch-readiness-checklist.md)
- [Automated QA harness](../../docs/web-qa-harness.md) and [machine-readable budget](qa-budget.yaml)
- [Critique protocol](../quality/critique-protocol.md)
- [Handover and care](../handover-and-care.md)
- [Living identities](../living-identities.md) for motion, generative and
  interactive extensions of an identity
- Project workspace: [bin/3w new project-digital](../../bin/3w) ([template bundles](../../templates/bundles/README.md))
