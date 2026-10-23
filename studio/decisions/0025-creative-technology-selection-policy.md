---
id: D-0025
title: Creative Technology selection policy
type: decision
status: approved
date: 2026-10-23
owner: founder
last_reviewed: 2026-10-23
approved_by: founder
approved_on: 2026-10-23
approval_source: founder reply "yes" to "approve D-0025", 3RDWRONG build session, 2026-10-23
---

# D-0025: Creative Technology selection policy

## Decision

Adopt the [Creative Technology selection policy](../../methods/creative-technology/selection-policy.md),
the [three access levels](../../methods/creative-technology/README.md#three-access-levels),
the native-first and recorded-reason rules, and the required
[stack decision record](../../templates/bundles/project-digital/workspace/stack-decision.md.tmpl)
as studio policy for all agents and humans choosing digital technology.
[D-0023](0023-commercial-and-delivery-defaults.md) stays the binding performance
budget; this decision does not loosen any threshold or grant an exception.

Select the simplest approach that faithfully delivers the creative outcome.
Start with HTML/CSS/SVG and native scrolling. Add Lenis, physics,
post-processing, WebGPU or another specialist dependency only for an explicit,
recorded reason proved in a bounded prototype. GSAP and Motion must not animate
the same property on the same element; use one scroll engine.

Core, Creative specialists and Advanced specialists are access levels, not
registry roles or automatic dependencies. [D-0019](0019-organisation-and-loading-policy.md)
still governs loading and activation. Every digital project must prepare its
stack record before the prototype and complete its prototype/device evidence
and final decision at DX-04 before production build.

## Status

Approved by the founder on 2026-10-23 through the reply “yes” to “approve
D-0025” in the 3RDWRONG build session. This adopts the rules above. Supporting
method documents, matrix, learning library, template and Labs backlog retain
`status: proposed` for continuing review; their metadata does not override the
adopted requirements. No other document is promoted to approved by an agent.

## Rationale

**Interpretation** — Technology should follow an original concept and usable
content. A small, explicit stack reduces speculative dependencies and makes
performance, maintenance and interaction ownership easier to test. Early proof
of the riskiest interaction connects creative ambition to actual device cost.
Access levels keep specialist techniques available without making every tool
part of every project.

## Alternatives considered

- **One immersive stack for all projects:** convenient scaffolding, but forces
  3D, React, smooth scrolling and effects onto briefs that may need none of them.
- **Unrecorded case-by-case choice:** flexible, but loses rejected alternatives,
  compatibility evidence and the reasoning future maintainers need.
- **Treat the supplied handbook as verified policy verbatim:** preserves its
  breadth, but would turn AI-assisted recommendations and changing version
  claims into unsupported rules. Archive it and maintain a dated evidence ledger.

## Evidence

**Documented** — Founder-supplied [handbook](../archive/creative-technology-handbook-2026-10.md),
received 2026-10-23, and founder approval of D-0025 reported in this build session.
[Official-source checks](../../methods/creative-technology/verification.md)
record current renderer, animation-runtime and Core Web Vitals claims.
[D-0018](0018-design-engineering-studio.md) establishes the studio's two-pillar
practice; D-0019 owns organisation/loading; D-0023 sets performance.

**Hypothesis** — Recorded alternatives and prototypes will improve creative
fidelity and reduce dependency/maintenance cost. Test through the Labs studies
and first delivery; this is not a measured improvement yet.

**Unknown** — Team fluency, actual project device costs and support effort for
all candidate technologies. A tool inventory is not delivery evidence.

## Consequences

- Engineering's creative-engineering sub-department owns policy maintenance;
  Design owns intent and art-direction critique; Labs owns the
  [starter repertoire](../../experiments/creative-technology-repertoire.md).
- Use the [matrix](../../methods/creative-technology/selection-matrix.md) to
  compare tasks and actual studio coverage. Gaps remain gaps; no tool is invented
  or automatically activated. Registry changes remain separately reviewed.
- Open the stack record at DX-02, prove it at DX-04 and require it for DX-05.
  Record changed assumptions, rejected alternatives and re-test triggers.
- Budget exceptions still need founder approval under D-0023. Lab results do
  not establish field p75 Core Web Vitals.
- Follow [D-0021](0021-client-work-public-anonymised.md): only cleared,
  anonymised decisions may enter this public repo; identifying URLs, captures,
  client files and confidential detail remain in the vault.
- Source recipes may assume heavy dependencies. Card-level technology notes
  subordinate those defaults to this policy without editing vendored files.
- Studying a reference is internal. Publication requires original work,
  independent critique, rights checks and founder release approval.
  [D-0006](0006-rejected-own-identity-direction.md) stays rejected.

## Revision triggers

Review after the five starter studies, first Digital Experience delivery,
repeated budget or maintenance failures, registry gaps blocking a brief,
renderer/framework breaking releases, or evidence that a simpler approach
cannot preserve the intended result. Recheck official version claims before
implementation; revise adopted policy through a founder decision.
