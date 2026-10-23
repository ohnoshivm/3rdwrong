---
title: Digital Experience — proposed flagship offer
type: guide
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Digital Experience

**Proposed flagship #2 for founder review.**
[D-0018](decisions/0018-design-engineering-studio.md) approves digital experience
as the second pillar alongside the core [Identity System](identity-system-offer.md).
This page proposes scope and delivery criteria; it is not an approved rate card,
a record of delivered capability or a promise of an award.

## Intended outcome and fit

Studio-grade websites and interactive/3D experiences grounded in an identity
system: a coherent digital expression of a brand's idea, with clear content,
usable interactions and measured engineering quality. A validated existing
identity or separately agreed identity engagement is an input. Do not hide
identity strategy or a rebrand inside a website build.

**Hypothesis** — Suitable buyers value authored digital expression at a launch,
repositioning or growth moment. Demand in the current ICP remains unvalidated;
qualify the buyer, problem, authority, content readiness, budget and maintenance
owner before proposing work.

## Proposed scope

- Discovery of audience tasks, content, identity rules, constraints and success
  criteria; agreed sitemap, page/template inventory and integration list.
- Digital art direction, UX/UI, responsive behaviour, interaction and motion
  design derived from the identity, with early browser prototypes.
- Website implementation and content integration; CMS and integrations only
  where named in the signed scope. Interactive/3D scenes, shaders, WebGL or
  generative behaviour are optional, purpose-led and explicitly bounded.
- Agreed browser/device testing, accessibility and performance verification,
  deployment, source/documentation handover and operator training.

Define page count, content ownership, languages, revisions, scene/asset count,
source formats, hosting, licences and support terms in the proposal. A studio
site, campaign microsite and interactive experience require different scopes;
none implies unlimited production.

## Exclusions and change handling

Full identity creation, open-ended copy/content production, complex product or
backend platforms, commerce/custom integrations, ongoing hosting/support,
paid-media management, continuous social production and major campaigns are
excluded unless separately agreed. 3D modelling, film, sound and other asset
production need named deliverables, rights and owners; they are not unlimited
inputs. Do not promise standalone advertising management from the organisation
chart. Awards submission and award outcomes are outside client acceptance.

New pages, integrations, scenes, strategy changes or increased asset fidelity
after sign-off require a written scope, fee, schedule and acceptance revision
before implementation. Explain rendering and maintenance costs before selling
complexity. Confirm founder and specialist capacity before committing dates.

## Proposed phases and paired pods

Use [D-0019](decisions/0019-organisation-and-loading-policy.md)'s paired
Design + Engineering model from day one. Design owns what and why; Engineering
owns how. Production coordinates dependencies, Strategy supplies research and
positioning inputs, and Media supplies separately scoped assets. Labs research
is not silently charged as client delivery or treated as production-ready.

| Phase | Design pod | Engineering pod | Review gate |
| --- | --- | --- | --- |
| Frame | Direction + experience-design define audience tasks, identity inputs and creative criteria | Creative-engineering + platform-performance assess feasibility, content/integration constraints and budgets | Founder/client confirm brief, scope and success criteria |
| Prototype | Direction + identity-craft + experience-design test one original concept and key interaction | Creative-engineering prototypes the hardest behaviour in a real browser on target hardware | Joint concept/feasibility review; agree fallback, asset and performance budgets before full build |
| System and build | Experience-design specifies responsive layouts, states, motion and identity rules | Product-frontend + creative-engineering implement agreed pages, content, integrations and scenes | Working slice accepted before scaling; versioned artefacts and changes recorded |
| Verify and refine | Design-qa checks hierarchy, typography, identity coherence, usability and responsive behaviour | Engineering-qa-security + platform-performance check functionality, accessibility, performance and security | Independent review board; fix defects and re-inspect the production build |
| Release and learn | Design documents usage and content constraints | Engineering documents source, deployment, CMS, dependencies, maintenance and fallbacks | Founder/client acceptance, handover, permission review and retrospective |

The handoff contract names identity tokens, content, layouts, component states,
interaction/motion specifications, asset rights/formats, budgets and acceptance
evidence. It defines artefacts, not a wall between the pods. No reviewer reviews
their own department's work alone.

## Proposed acceptance criteria

Confirm exact targets, reference hardware, browsers, network profile and
measurement method before signing. These are proposed engineering criteria,
not claims that a project has passed them.

| Area | Acceptance evidence |
| --- | --- |
| Identity and purpose | Each major visual/interaction decision traces to the approved concept; real content and key tasks remain legible without spectacle |
| Responsive craft | Inspect the production build at agreed desktop, tablet and mobile widths; record screenshots, overflow/wrap defects, fixes and re-inspection |
| Functionality | Exercise navigation, forms, CMS/content flows and agreed integrations; passing relevant automated tests and clean first-party browser console |
| Performance budgets | Approved studio budget ([D-0023](decisions/0023-commercial-and-delivery-defaults.md)): mobile p75 LCP ≤2.0 s, INP ≤200 ms, CLS ≤0.1 where field data exists; ≤2 MB transferred before first interaction with the rest lazy-loaded; 60 fps target on a mid-range phone; a complete prefers-reduced-motion fallback. Projects may set stricter budgets; a looser budget needs a founder-approved exception recorded in the project; pre-launch lab checks use recorded hardware/network settings and cannot establish field INP. Set explicit numerical initial-transfer, JavaScript, image/video/3D, texture, draw-call and frame-time budgets per prototype before full build; measure the built artefact against them and disclose any exception for approval |
| Accessibility | Target WCAG 2.2 AA for the agreed experience; combine automated checks with manual keyboard, focus, contrast, semantics, screen-reader and equivalent-content checks; record scope and unresolved defects |
| Reduced motion and resilience | Honour prefers-reduced-motion with meaningful static or simplified alternatives; no essential task relies on animation, pointer effects, sound or WebGL. Test unavailable WebGL, asset failure and agreed lower-powered devices; provide usable fallback content |
| Engineering and security | Passing production build, appropriate tests, input/integration and dependency review, no exposed secrets, documented deployment and recovery procedure; verify the running built artefact before release |
| Handover | Client can locate source, assets, licences, content instructions and maintenance ownership; record approver, date, accepted version and any agreed exceptions |

If field data is unavailable, label field Core Web Vitals **not verified** and
agree post-launch measurement ownership. Award-level craft does not waive
performance, accessibility or functional acceptance. Do not claim compliance
from an automated score alone.

## Commercial and delivery defaults

Approved defaults ([D-0023](decisions/0023-commercial-and-delivery-defaults.md)), pre-filled in the proposal, SOW and MSA and
editable per project with founder approval:

- **Payment:** 50% to start, 30% on approval of the chosen direction, 20%
  before final files are released.
- **Feedback:** two consolidated rounds per phase (concept, refinement,
  applications); further rounds are change requests.
- **Warranty:** 30 days of free defect fixes after launch; longer support is
  a paid care plan.
- **Portfolio:** named portfolio use after public launch with client-approved
  case-study wording, unless the client opts out as confidential.
- **AI:** AI use in the process is disclosed; AI-generated material in final
  deliverables needs the client's written consent.

## Pricing and commercial hypothesis

**Hypothesis placeholder — to be set by founder.** See the canonical
[pricing hypotheses](pricing.md). No Digital Experience fee, range or delivery
duration is established here; identity pricing is not a proxy for website or
3D costs. Estimate from the agreed prototype, specialist needs, asset costs,
maintenance responsibilities and actual delivery effort before quoting.

## Evidence and revision

**Documented** — Founder instruction, 2026-10-23, recorded in D-0018, establishes
the second pillar. **Unknown** — repeatable demand, delivery cost and viable
pricing have not been established. Review after prototype measurements,
qualified buyer conversations and the first paid engagement; revise this
proposal before treating it as standard operating policy.
