---
id: D-0019
title: Organisation and loading policy
type: decision
status: approved
date: 2026-10-23
owner: founder
last_reviewed: 2026-10-23
approved_by: founder
approved_on: 2026-10-23
approval_source: founder instruction, 2026-10-23
---

# D-0019: Organisation and loading policy

## Decision

Organise 3RDWRONGS into 11 full departments across four groups, supporting
[D-0018](0018-design-engineering-studio.md). Design and Engineering are the two
flagship departments. A department is an accountability structure, not a claim
of staffing, proven capacity or a separately saleable service.

| Group | Department | Sub-departments | Flagship |
| --- | --- | --- | --- |
| Craft | Design | direction; identity-craft; experience-design; design-qa | Yes |
| Craft | Engineering | creative-engineering; product-frontend; platform-performance; engineering-qa-security | Yes |
| Craft | Labs (R&D) | experiments; house-engine; open-source-showcase | No |
| Delivery | Strategy | positioning; research-perception; culture-behaviour | No |
| Delivery | Production | producing-pm; client-experience; handover-retention | No |
| Delivery | Media | film-motion-graphics; image-photo-direction; sound-voice | No |
| Growth | Marketing | studio-brand-voice; content-social; pr-awards; search-aeo | No |
| Growth | Advertising | paid-social; search-programmatic; ad-creative-measurement | No |
| Growth | Outbound | prospecting-research; outreach-sequences; partnerships-referrals | No |
| Growth | Sales | discovery-qualification; proposals-pitches; pricing-deal-desk; pipeline-forecasting | No |
| Studio | Operations | planning-workflow; knowledge-systems; finance-legal; people-partners | No |

### Ownership and boundaries

Each department has a department-head accountable for standards, job leads and
review. Job-owners own bounded outputs; specialists contribute when triggered;
a producer coordinates project dependencies. An independent review board
reviews consequential work: no reviewer reviews their own department's work
alone. The founder retains strategic, creative and release approval.

Design owns what and why: concept, identity, UX/UI, interaction and motion
design, art direction and design QA. Engineering owns how: implementation,
3D, WebGL/WebGPU, shaders, frontend, CMS, deployment, performance, code QA and
security. Work as a paired pod from day one and prototype in the real medium
early; the handoff contract defines artefacts rather than a departmental wall.

Strategy owns client strategy and research. Production owns project management,
client communication, timelines and handover. Media produces film, motion
graphics, images and sound as assets; their direction stays with Design.
Marketing owns the studio's brand, content, PR, awards and search. Advertising
owns paid media, including agreed client launch extensions; standalone ads
management needs a further founder decision. Outbound opens conversations;
Sales owns qualification through signing. Operations owns workflow, knowledge
and agent infrastructure, finance/legal and collaborators. Labs owns non-client
R&D, the house engine and open-source/showcase experiments; ordinary delivery
engineering stays in Engineering.

### Loading and registry policy

Apply the same roles and loading rules to **skills and Agency Agents**:

- **Lead:** at most two per job; installed and loaded in active directories.
- **Specialist:** installed and loaded, with a named use trigger; being loaded
  does not mean it runs on every job.
- **Bench:** installed in the repository library, callable by name, with a
  recorded reason; not loaded in active discovery directories.
- **Parked:** installed in the repository library, callable by name, with a
  recorded activation trigger; not loaded in active discovery directories.
- **Excluded:** do not install or activate; retain the reason in the registry.

The department/tool registry is the single source of truth for documentation,
routing and installation/loading views. Record stable identities, department,
sub-department, job, role, triggers or reasons and source/provenance there;
derive those views from it rather than maintaining competing lists. Active
skills are linked into active skill directories; active Agency Agents live in
`.claude/agents`. A library entry alone must not make a bench/parked tool active.

## Status

Approved by the founder on 2026-10-23. This records the target operating policy,
not a claim that registry migration, installation changes or department guides
have already been completed.

## Rationale

**Interpretation** — Separate full departments make ownership visible across
craft, delivery, growth and studio operations. Paired Design + Engineering
pods support the new positioning. Explicit loading roles preserve access to
the library while keeping active discovery intentional. One registry reduces
drift between what documentation recommends and what tools are loaded.

## Alternatives considered

- Retain the earlier eight-department/division taxonomy: rejected in favour of
  the founder's 11-department, four-group model.
- Load every installed skill and agent: rejected because installation is not
  the same as active routing.
- Load only leads: rejected; the founder chose leads plus triggered specialists.
- Maintain documentation, routing and install lists separately: rejected in
  favour of registry-derived views.

## Evidence

**Documented** — Founder instruction, 2026-10-23, and the supplied
DEPARTMENTS-SPEC-v2 specification establish this taxonomy, boundary model,
roles and loading policy. The table and rules above preserve those decisions
in the repository. [D-0016](0016-agency-agents-catalogue.md) records the previous
catalogue installation; this decision governs the active loading distinction,
while upstream provenance and founder exclusions remain applicable.

**Unknown** — The model's effect on quality, context use and founder workload
has not been measured. Department names do not establish staffed capability.

## Consequences

Migrate department guides and the registry from the previous taxonomy, then
generate consistent documentation, routing and loading/install views. Preserve
provenance, exclusion and publication checks. Do not claim completion from this
record alone: verify role assignments and active-directory contents against
the registry. Existing department material is transitional wherever it conflicts
with this decision. Methods and routes also need the corresponding revision.

Use department heads and an independent review board without multiplying
competing orchestrators. Record owners, review findings and founder approvals;
review-board checks do not replace human acceptance.

## Revision triggers

Review after the first paired-pod delivery, registry/install drift, repeated
ownership conflicts, missing specialist capacity, excessive active context or
review bottlenecks. Change taxonomy or loading policy through a new founder
decision; individual assignments must retain their registry reason or trigger.
