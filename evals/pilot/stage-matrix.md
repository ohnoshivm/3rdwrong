---
title: Pilot stage and rubric crosswalk
type: guide
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Pilot stage and rubric crosswalk

**Documented:** stage names follow the current [Identity engagement](../../methods/identity-engagement/README.md)
and [Digital Experience](../../methods/digital-experience/README.md) methods.
The 19 names and gate requirements were checked read-only against the release
playbooks on 2026-10-23; `scorecard.yaml` records each exact playbook section,
its gate requirement and lifecycle mapping. Names match all 19 sections.
**Hypothesis:** the proposed stage weights below express relative delivery
risk. They sum to 100%; Identity System and Digital Experience each hold 50%.

The exact two-case paths for every listed job are in [scorecard.yaml](scorecard.yaml).
Use both cases for tool bake-offs. For the pilot, apply these anchored rubrics
to each stage's actual output and write a stage-specific brief using the
[run log template](run-log-template.md); keep the criterion IDs/anchors/weights
fixed, record the case hash and explain the application. Where task context
differs, create a new proposed case with the stage's actual inputs and validate
it before running. Do not present a plan-only case pass as a delivery pass.

| Stage | Index weight | Relevant job rubrics | Required stage evidence and gate |
| --- | --- | --- | --- |
| I01 Discovery | 5% | `evidence-synthesis` | Source inventory, fictional evidence boundary and research questions; No separate client gate; the factual summary goes to C1 with phase 02. Founder approves the factual summary and participant handling. |
| I02 Diagnosis | 5% | `evidence-synthesis`, `positioning-canvas` | Problem frame, category-source coverage, tensions and missing evidence; Discovery and diagnosis gate: C1 confirms factual accuracy and the work question; founder logs it. This does not approve an interpretation or concept. |
| I03 Strategy | 7% | `positioning-canvas` | Versioned strategy, perception-to-identity map and separate human strategy gate; Founder approves the strategy for presentation. C1 signs a dated strategy version before phase 04 starts. Present without visual references. A later material change returns here and is recorded before concept work resumes. |
| I04 Concept | 7% | `concept-direction`, `concept-critique` | Three different ideas, comparative critique and human route selection; Founder chooses the route to recommend. C1 selects a route for development (concept decision, not visual sign-off). Under D-0023 the 30% payment falls on approval of the chosen direction: Operations raises it with bin/3w new invoice (vault only). |
| I05 Identity | 10% | `verbal-identity`, `typography`, `colour`, `mark-logo`, `composition-layout` | Original editable identity elements, human craft review, specimens, rights and production limits; No client visual gate here. Founder signs the craft; C1 confirms product language and required scripts. Component review does not approve the system. |
| I06 System | 7% | `composition-layout`, `consistency-qa` | Versioned rules across label, line sheet and mobile; separate visual-system gate; Founder approves the system for presentation. C1 gives visual sign-off, separate from the strategy sign-off. A strategy change returns to 03; a production defect returns to its rule. |
| I07 Validation | 5% | `concept-critique`, `consistency-qa`, `accessibility-implementation` | System matrix at actual dimensions, defects and independent retest evidence; Founder (as design lead) signs the validation record. C1 accepts known limits and residual exceptions in writing (decisions.md). |
| I08 Delivery | 3% | `consistency-qa` | Opened exports, asset/rights index, guidelines, access and separate receipt rehearsal; Founder approves release. C1 confirms receipt and access, recorded separately from creative approval; receipt is not a new creative approval. |
| I09 Learning | 1% | `evidence-synthesis` | Source-linked retrospective, tool defects, method changes and next evaluation; Founder approves retro actions and publication. C1 gives or withholds case-study permission (separate written permission to name the client). |
| DX01 Discovery and audit | 3% | `evidence-synthesis`, `web-vitals`, `accessibility-implementation` | Fictional digital scope extension, content/task inventory and confirmed success criteria; DX-01: founder; C1 confirms facts, success criteria and the content plan. |
| DX02 Experience strategy and concept | 5% | `interaction-architecture`, `concept-direction` | Original experience idea, sitemap, journeys and concept gate; DX-02: founder selects the concept; C1 approves concept and sitemap. Concept approval does not approve art direction. Interpretation — if the SOW treats this as "approval of the chosen direction", the D-0023 30% payment falls here; follow the SOW. |
| DX03 Art direction and design system | 6% | `typography`, `colour`, `composition-layout`, `motion-principles` | Named tokens, type/colour/layout rules, states, motion and art-direction gate; DX-03: founder; C1 approves art direction on two or three key templates. Tokens are then frozen for the prototype; later changes go through change control. |
| DX04 Prototype | 7% | `creative-prototyping`, `interaction-architecture`, `web-vitals` | Hardest browser slice on target hardware, static comparison, budget/fallback acceptance; DX-04: complete stack decision record with prototype/device evidence and final decision; founder and C1 accept the prototype; Design and Engineering leads jointly agree budgets and fallbacks. Budgets at or under D-0023, or a founder-approved exception recorded in the project. |
| DX05 Production build | 8% | `ui-implementation` | Passing production build, meaningful tests, content/states and integration boundaries; DX-05: Engineering and Design leads confirm feature completeness; founder logs it. Scope additions go through change control (bin/3w new change-order). |
| DX06 Motion, 3D and interaction | 5% | `motion-principles`, `creative-prototyping` | Purposeful scenes, frame traces, one scroll engine, complete reduced-motion/static path; DX-06: Design and Engineering leads jointly; founder logs it. One smooth-scroll engine at most; reduced motion complete. |
| DX07 QA | 6% | `consistency-qa`, `accessibility-implementation`, `ui-implementation` | Desktop/tablet/mobile evidence, browser/keyboard/AT checks, no unresolved Blocker or Major; DX-07: founder logs pass or pass with conditions only under the mandatory harness gate, with no open Blocker (critical) or Major and every Minor dispositioned. |
| DX08 Performance and launch readiness | 5% | `web-vitals`, `accessibility-implementation` | D-0023 measurements, security/rights/SEO/analytics checklist, rollback and human launch rehearsal gate; DX-08: founder and C1 approve launch at the go/no-go review. |
| DX09 Launch and handover | 3% | `ui-implementation`, `consistency-qa` | Sandbox release verification, restoration, opened handover pack, acceptance and receipt recorded separately; DX-09: C1 confirms final acceptance and, separately, receipt and access. Record the 30-day warranty dates from launch; receipt is a separate event. |
| DX10 Care and iteration | 2% | `web-vitals`, `evidence-synthesis` | Simulated warranty defect, monitoring/field owner, care choice and access-removal rehearsal; DX-10: founder and C1 close the 30-day warranty and agree or decline a care plan. Resolve deferred device tests; review the field-data condition on its due date. If traffic is insufficient, keep field p75 Unknown with owner and next review, rather than closing it as passed. |

Every row is initially **not-run**. A stage score is the arithmetic mean of
its applicable job scores, each itself a weighted criterion mean. Record every
job score separately; do not omit a weak job. Scope exclusions need a human
record before execution; replace an irrelevant 3D task with a documented
purpose/static prototype evaluation, preserving DX04/DX06 and their weights.

The final-delivery and launch checklists are hard gates alongside scores.
They cover duties such as rights, acceptance, security, rollback and account
transfer that a craft rubric alone does not certify. See
[readiness scorecard](readiness-scorecard.md).

## Lifecycle and conditional gates

The delivery stages sit inside L6 Deliver. I08/DX09 close into L7 Launch and
handover, DX10 into L8 Care and I09 into L9 Close-out and case study. Before
I01/DX01, rehearse L0–L5: lead, qualification, scope confirmation, proposal,
contract/deposit/clearance and kickoff. Scorecard lifecycle requirements retain
those gates without inventing ten additional delivery-stage scores.

DX04 also requires the complete stack decision record and joint budget/fallback
acceptance. DX07 requires the current-build harness report; INCOMPLETE cannot
become a measured pass. Any allowed field/real-phone deferral needs a named
owner, due date and founder decision under the integrated playbook; this pilot
still requires no open Blocker or Major. DX08 reconciles every condition before
the launch rehearsal. DX10 resolves deferred device tests and reviews field
conditions; insufficient traffic remains Unknown with an owner and next review.

All rehearsal approvals are fictional role-coded decisions. Demo case scores
support rehearsal learning only; they never become studio leaderboard evidence.
