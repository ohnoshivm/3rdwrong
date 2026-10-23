---
title: Department heads, reviewers and RACI
type: guide
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Department heads, reviewers and RACI

Who coordinates each of the eleven departments ([D-0019](../decisions/0019-organisation-and-loading-policy.md)), who owns each sub-department's jobs, who reviews whose work, where problems escalate and what quality bar each department holds. Heads coordinate; independent reviewers check evidence; the founder signs decisions. Every assignment here is **proposed** until the founder approves it. Agents are named by registry `id` ([registry](../../toolkit/sources/registry.json)); job leads are in the [registry summary](registry-summary.md). How these roles run a project is in the [delivery playbooks](../../methods/playbooks/README.md).

**Interpretation** — in a founder-led studio, "head" is an accountability role an agent coordinates under the founder, not headcount. All escalation paths end with the founder. `agent:ceo` is loaded only for flagship/own-identity work; it cannot independently check a direction it made. Choose a fresh Opus reviewer from the pool instead.

## Department heads

### Design

- **Head agent:** `agent:creative-director` (Opus). Flagship and own-identity work escalates to `agent:ceo`.
- **Sub-department job owners:** direction — `agent:creative-director` with `skill:3w-creative-direction`; identity-craft — the founder (human-led type, mark, colour, composition), executed with `agent:visual-designer`; typography — [`skill:3w-typography-system`](../../toolkit/cards/design/identity-craft/skill--3w-typography-system.md); colour — [`skill:3w-colour-system`](../../toolkit/cards/design/identity-craft/skill--3w-colour-system.md); mark-logo — [`skill:3w-mark-exploration`](../../toolkit/cards/design/identity-craft/skill--3w-mark-exploration.md); composition-layout — [`skill:3w-composition-system`](../../toolkit/cards/design/identity-craft/skill--3w-composition-system.md); `agent:visual-designer` is the triggered digital executor, not the brand typography lead; experience-design — `agent:ui-ux-architect`; design-qa — independent `agent:ceo` or `agency:design-brand-guardian` (concept and formal critique through `skill:3w-identity-system-critic`) and `agent:visual-qa-engineer` (browser).
- **Reviewer pool:** `agent:creative-auditor`, `agent:visual-qa-engineer`, `skill:3w-identity-system-critic`, `skill:3w-brand-consistency-qa`, `skill:audit-reference-originality`, `agency:design-ui-finish-gate-reviewer`, `agency:testing-accessibility-auditor`.
- **Escalation:** maker → `agent:creative-director` → `agent:ceo` (flagship or own identity) → founder.
- **Quality bar:** the nine [Design quality rules](design.md#quality-rules-and-gates): strategy first, three distinct routes, nothing advances below "Strong enough to advance", two independent passes, originality before release, real evidence, human-led craft, best model at every gate, founder sign-off.

### Engineering

- **Policy ownership:** Engineering / creative-engineering maintains the [Creative Technology selection policy](../../methods/creative-technology/selection-policy.md) under [D-0025](../decisions/0025-creative-technology-selection-policy.md), including stack records and prototype evidence.

- **Head agent:** `agent:frontend-architect`. Hard architecture or diagnosis escalates to `agent:strategic-architect` (Opus).
- **Sub-department job owners:** creative-engineering — `agency:engineering-rapid-prototyper` (prototypes), `agent:3d-webgl-engineer` (scenes), `agent:motion-director` (motion); product-frontend — `agent:frontend-architect`; platform-performance — `agent:performance-engineer`; engineering-qa-security — `agency:engineering-code-reviewer` (code) and `agency:security-architect` (security); a fresh `agent:implementer` runs the test-engineering lead `skill:playwright-cli` against work it did not build.
- **Reviewer pool:** `agency:engineering-code-reviewer`, `agent:performance-engineer`, `skill:ceos-production-quality`, `skill:semgrep`, `claude-security:claude-security`, `skill:supply-chain-risk-auditor`, `skill:playwright-cli` run by a non-building instance.
- **Escalation:** builder → `agent:frontend-architect` → `agent:strategic-architect` → founder.
- **Quality bar:** the [D-0023](../decisions/0023-commercial-and-delivery-defaults.md) budget (mobile p75 LCP ≤ 2.0 s, INP ≤ 200 ms, CLS ≤ 0.1, ≤ 2 MB before first interaction, 60 fps target, complete reduced-motion fallback); current-build `bin/3w qa run <url>` report following the [Web QA harness guide](../../docs/web-qa-harness.md) and the [conditional QA gate](../../methods/playbooks/digital-experience.md#mandatory-harness-report-and-conditional-gate); WCAG 2.2 AA target; passing production build; no self-merging of consequential changes; measured claims with device, profile and date ([web standards](../../methods/quality/web-standards.md)).

### Labs

- **Repertoire ownership:** Labs maintains the [Creative Technology starter repertoire](../../experiments/creative-technology-repertoire.md); Engineering independently checks kits before project reuse.

- **Head agent:** `agent:frontend-architect` as proposed technical coordinator, under the founder; `agent:creative-director` supplies a study's creative question. This is a coordination assignment, not a registry rehome or proof of research capacity.
- **Sub-department job owners:** experiments — `skill:master-of-games` (playable-prototypes); [`skill:3w-effect-study`](../../toolkit/cards/labs/experiments/skill--3w-effect-study.md) (effect-studies), [`skill:3w-labs-benchmark`](../../toolkit/cards/labs/experiments/skill--3w-labs-benchmark.md) (research-benchmarks); house-engine — `skill:web-technique-to-skill` (reusable-kits), `skill:build-vesperfall-review-assets` (asset-pipelines); [`skill:3w-engine-validation`](../../toolkit/cards/labs/house-engine/skill--3w-engine-validation.md) (engine-validation); open-source-showcase — `agency:specialized-developer-advocate` (contributor-community), `skill:publish-project-to-github` (project-packaging); [`skill:3w-demo-publishing`](../../toolkit/cards/labs/open-source-showcase/skill--3w-demo-publishing.md) (demo-publishing).
- **Reviewer pool:** Engineering's reviewers for anything reused in client work, plus `skill:audit-reference-originality`.
- **Escalation:** owner → founder.
- **Quality bar:** non-client work only; reuse in an engagement needs a concept-specific choice, independent originality review, reduced-motion behaviour and performance evidence ([Labs](labs.md)); never silently billed as delivery.

### Strategy

- **Head agent:** `agent:strategic-architect` (Opus). Flagship or own-identity strategy escalates to `agent:ceo`.
- **Sub-department job owners:** positioning — `agent:strategic-architect` with `skill:positioning-mapper` and `skill:positioning-truth-tracer`; research-perception — `skill:3w-brand-discovery` run by `agent:strategic-architect`, `agency:research-synthesist` (evidence-synthesis), `agent:researcher` for criteria-led lookups; culture-behaviour — `agency:specialized-cultural-intelligence-strategist`, `agency:academic-historian`; [`skill:3w-behavioural-lens`](../../toolkit/cards/strategy/culture-behaviour/skill--3w-behavioural-lens.md) (behavioural-theory), [`skill:3w-narrative-analysis`](../../toolkit/cards/strategy/culture-behaviour/skill--3w-narrative-analysis.md) (narrative-analysis).
- **Reviewer pool:** `agency:research-synthesist`, `agency:specialized-strategy-duel-agent`, `agency:academic-statistician` (before quantitative claims).
- **Escalation:** maker → `agent:strategic-architect` → `agent:ceo` (flagship) → founder.
- **Quality bar:** every claim labelled Documented, Interpretation, Hypothesis or Unknown; no audience claim from founder preference; strategy signed by `C1` before concept work; strategy and visual approval kept separate.

### Production

- **Head agent:** `agency:project-management-studio-producer`.
- **Sub-department job owners:** producing-pm — `agency:project-management-studio-producer` (planning), `openai-templates:artifact-template-project-tracker` (tracking), `agency:project-management-project-shepherd` (resource coordination); client-experience — `creative-production:intake` (onboarding), `agency:project-management-meeting-notes-specialist` (cadence); handover-retention — `skill:writing-release-notes` (delivery handover), `agency:customer-success-manager` (care retainers only); [`skill:3w-care-retention`](../../toolkit/cards/production/handover-retention/skill--3w-care-retention.md) (retention-programmes).
- **Reviewer pool:** `agency:project-management-project-shepherd` (plans), `agency:testing-evidence-collector` (handover packs).
- **Escalation:** producer → founder. On a founder-led project the founder may also be producer; record that in the RACI so checks still happen ([project operations](../../business/engagement-operations.md#roles)).
- **Quality bar:** no stage starts before its gate is logged; silence is never approval; two consolidated rounds per phase, then change orders; a completed `evals/pilot/README.md` rehearsal and founder readiness decision before first-client delivery; public records pass `bin/3w check` and a human anonymity review.

### Media

- **Head agent:** `agency:project-management-studio-producer` as proposed production coordinator for scope, schedule and rights. Design's `agent:creative-director` retains image/motion intent; Media's lead tools execute their bounded jobs. This shared coordination does not create a new media-director capability.
- **Sub-department job owners:** film-motion-graphics — `anthropic-skills:motionmaxxing` (brand-film), `remotion:remotion-best-practices` (programmatic-video), `chatcut-desktop:chatcut-plugin-basics` (video-editing); image-photo-direction — `skill:imagegen` (brand-image-assets); [`skill:3w-image-production`](../../toolkit/cards/media/image-photo-direction/skill--3w-image-production.md) (image-production-workflow), [`skill:3w-image-qa`](../../toolkit/cards/media/image-photo-direction/skill--3w-image-qa.md) (image-quality-check, independent checker only); sound-voice — `chatcut-desktop:voice`, `chatcut-desktop:transcription`, `agency:specialized-focus-music-architect`.
- **Reviewer pool:** `chatcut-desktop:verification` (media-quality-check); Design's `agency:design-brand-guardian` for asset intent and `agent:creative-auditor` for rendered digital contexts; `agency:design-inclusive-visuals-specialist` for imagery.
- **Escalation:** maker → `agent:creative-director` → founder.
- **Quality bar:** produced only from approved direction; rights and AI-consent status recorded for every asset (D-0023), with independent [`skill:3w-image-qa`](../../toolkit/cards/media/image-photo-direction/skill--3w-image-qa.md) release checks; production formats within the project's weight budget.

### Marketing

- **Head agent:** `agent:creative-writer` (Opus) for voice; drafts and revises, never publishes.
- **Sub-department job owners:** studio-brand-voice — `skill:voice-dossier-builder`, `skill:message-system-architect`, `skill:content-quality-auditor`, `skill:marketing-plan`; content-social — `skill:content-writer`, `skill:social-calendar-builder` and the other content-social leads; pr-awards — `skill:press-media-relations`, launch leads; [`skill:3w-awards-submission`](../../toolkit/cards/marketing/pr-awards/skill--3w-awards-submission.md) (awards-submissions); search-aeo — `skill:seo-plan`, `skill:technical-seo-checker` and related leads.
- **Reviewer pool:** `skill:content-quality-auditor`, `skill:social-quality-auditor`; Design and Engineering leads for craft accuracy of anything public.
- **Escalation:** writer → `agent:creative-writer` → founder.
- **Quality bar:** no invented results; client work only within permission (D-0021, D-0023); D-0024 channels and free award submissions until revisited by founder decision; founder signs everything published under the studio name.

### Advertising

- **Head agent:** `agency:paid-media-paid-social-strategist`. Dormant until the paid-advertising trigger is decided ([advertising](../../growth/advertising.md); still open under D-0024).
- **Sub-department job owners:** paid-social, search-programmatic and ad-creative-measurement leads as listed in [Advertising](advertising.md).
- **Reviewer pool:** `agency:paid-media-auditor` (account-audit), `skill:attribution-reconciler`.
- **Escalation:** strategist → founder.
- **Quality bar:** no spend without a founder-approved budget and a measurement plan.

### Outbound

- **Head agent:** `agency:sales-outbound-strategist`.
- **Sub-department job owners:** prospecting-research — `skill:prospecting`, `sales:sales-company-research`; [`skill:3w-prospect-qualification`](../../toolkit/cards/outbound/prospecting-research/skill--3w-prospect-qualification.md) (prospect-qualification); outreach-sequences — `agency:sales-outbound-strategist`, `agency:sales-outreach`; [`skill:3w-reply-triage`](../../toolkit/cards/outbound/outreach-sequences/skill--3w-reply-triage.md) (reply-triage); partnerships-referrals — `skill:influencer-marketing`, `skill:referrals`, `skill:outreach-manager`.
- **Reviewer pool:** the founder (every first message); the [outbound compliance rules](../../growth/outbound/compliance.md).
- **Escalation:** strategist → founder.
- **Quality bar:** D-0024: 20 researched, hand-written first messages a week, never automated; no personal data in the repository.

### Sales

- **Head agent:** `agency:sales-deal-strategist`.
- **Sub-department job owners:** discovery-qualification — `sales:prepare-for-meeting`, `agency:sales-discovery-coach`, `agency:sales-coach`; proposals-pitches — `sales:sales-presentations`, `sales:build-business-case`, `skill:sales-enablement`; pricing-deal-desk — `agency:specialized-pricing-analyst`, `skill:offers`, `agency:sales-deal-strategist`; pipeline-forecasting — `agency:sales-pipeline-analyst`, `skill:revops`, `agency:data-consolidation-agent`.
- **Reviewer pool:** `agent:strategic-architect` (scope and fit), Design and Engineering leads (feasibility), `agency:sales-pipeline-analyst` (forecast).
- **Escalation:** deal strategist → founder.
- **Quality bar:** founder approves every proposal before sending; D-0023 defaults in every proposal; prices and names only in the vault.

### Operations

- **Head agent:** `agency:project-management-studio-operations`.
- **Sub-department job owners:** planning-workflow — `superpowers:writing-plans` (only within the project's approved orchestration policy), `agency:agents-orchestrator` (only when selected as the one coordinator), `superpowers:verification-before-completion`, `agency:operations-manager`; knowledge-systems — `agency:zk-steward`, `skill-creator:skill-creator`, `skill:gstack-document-generate`; finance-legal — `agency:chief-financial-officer`, `agency:legal-document-review`, `agency:data-privacy-officer`; people-partners — `agency:recruitment-specialist`, `agency:organizational-psychologist`, `agency:supply-chain-strategist`. Mechanical work goes to `agent:bulk-executor` (workflow-orchestration specialist).
- **Reviewer pool:** `superpowers:verification-before-completion` (evidence gate), `agency:legal-document-review`, `agency:data-privacy-officer`.
- **Escalation:** owner → founder; legal and tax questions go to a lawyer or chartered accountant, not an agent.
- **Quality bar:** no money in the repository; contract templates carry their lawyer-review note; vault access least-privilege.

## Sub-department job ownership

**Hypothesis** — the coordinating agent below owns briefing, completeness and routing for every listed job, using each job's exact lead in its linked charter and the integrated W1/W2 leads above. This is accountability, not a claim that the coordinator personally performs every craft. The founder remains the human type/mark/colour/composition owner; Operations routes contract and privacy work to their named legal/privacy leads. Media coordinators schedule production through its job tools, never replace Design's direction or independent image QA.

Use the linked W1/W2 cards and their [source skills](../../skills/README.md) for execution. All four craft leads and twelve gap-closing leads remain experimental. No registry placement changes are implied by cross-department coordination. The table enumerates every charter job without creating competing tool placements; use the live registry, approved integration patches and tool cards for execution instructions and specialist triggers.

| Department / sub-department | Coordinating agent | Bounded jobs (lead tools remain in charter) |
| --- | --- | --- |
| [design](design.md) / `direction` | `agent:creative-director` | `inspiration-taste`, `category-audit`, `concept-direction`, `art-direction`, `verbal-identity` |
| [design](design.md) / `identity-craft` | `agent:visual-designer` | `typography`, `colour`, `mark-logo`, `composition-layout`, `image-generation-direction`, `design-system-guidelines`, `handover-specs`, `presentation` |
| [design](design.md) / `experience-design` | `agent:ui-ux-architect` | `interaction-architecture`, `ui-design`, `motion-principles`, `ux-writing`, `experience-prototyping` |
| [design](design.md) / `design-qa` | `agent:visual-qa-engineer` | `concept-critique`, `ux-audit`, `accessibility`, `originality-audit`, `visual-qa-browser`, `consistency-qa` |
| [engineering](engineering.md) / `creative-engineering` | `agent:frontend-architect` | `realtime-3d`, `shader-engineering`, `motion-implementation`, `generative-creative-coding`, `immersive-implementation`, `creative-prototyping` |
| [engineering](engineering.md) / `product-frontend` | `agent:frontend-architect` | `frontend-architecture`, `ui-implementation`, `site-and-cms-build`, `accessibility-implementation`, `internationalization`, `code-modernization`, `application-integrations` |
| [engineering](engineering.md) / `platform-performance` | `agent:performance-engineer` | `backend-and-api`, `data-and-storage`, `deployment-and-release`, `cloud-platform-guidance`, `web-vitals`, `runtime-diagnostics`, `animation-runtime` |
| [engineering](engineering.md) / `engineering-qa-security` | `agency:engineering-code-reviewer` | `technical-architecture`, `code-review`, `codebase-analysis`, `test-engineering`, `security-architecture`, `security-analysis`, `dependency-audit`, `release-verification` |
| [labs](labs.md) / `experiments` | `agent:frontend-architect` | `effect-studies`, `playable-prototypes`, `research-benchmarks` |
| [labs](labs.md) / `house-engine` | `agent:frontend-architect` | `reusable-kits`, `asset-pipelines`, `engine-validation` |
| [labs](labs.md) / `open-source-showcase` | `agency:specialized-developer-advocate` | `demo-publishing`, `contributor-community`, `project-packaging` |
| [strategy](strategy.md) / `positioning` | `agent:strategic-architect` | `positioning-canvas`, `positioning-proof`, `category-narratives` |
| [strategy](strategy.md) / `research-perception` | `agent:strategic-architect` | `brand-discovery`, `research-design`, `primary-research`, `evidence-synthesis`, `source-collection`, `audience-modelling`, `journey-mapping`, `market-signals` |
| [strategy](strategy.md) / `culture-behaviour` | `agent:strategic-architect` | `cultural-systems`, `historical-context`, `behavioural-theory`, `narrative-analysis` |
| [production](production.md) / `producing-pm` | `agency:project-management-studio-producer` | `project-planning`, `project-tracking`, `resource-coordination` |
| [production](production.md) / `client-experience` | `agency:customer-service` | `client-onboarding`, `client-service`, `meeting-cadence` |
| [production](production.md) / `handover-retention` | `agency:project-management-studio-producer` | `client-success`, `delivery-handover`, `retention-programmes` |
| [media](media.md) / `film-motion-graphics` | `agency:project-management-studio-producer` | `brand-film`, `programmatic-video`, `video-editing`, `video-effects`, `media-quality-check`, `media-tool-access`, `short-form-editing`, `asset-research` |
| [media](media.md) / `image-photo-direction` | `agency:project-management-studio-producer` | `brand-image-assets`, `image-production-workflow`, `image-quality-check` |
| [media](media.md) / `sound-voice` | `agency:project-management-studio-producer` | `voice-and-sound`, `transcription-captions`, `music-composition` |
| [marketing](marketing.md) / `studio-brand-voice` | `agent:creative-writer` | `brand-voice`, `message-architecture`, `editorial-quality`, `marketing-planning` |
| [marketing](marketing.md) / `content-social` | `agent:creative-writer` | `content-writing`, `content-planning`, `social-copy`, `community-engagement`, `social-measurement`, `social-listening`, `social-quality`, `lifecycle-copy` |
| [marketing](marketing.md) / `pr-awards` | `agent:creative-writer` | `earned-media`, `awards-submissions`, `launch-planning`, `launch-assets`, `launch-gate`, `launch-measurement` |
| [marketing](marketing.md) / `search-aeo` | `agent:creative-writer` | `keyword-research`, `technical-seo`, `seo-content`, `geo-visibility`, `search-measurement`, `seo-strategy` |
| [advertising](advertising.md) / `paid-social` | `agency:paid-media-paid-social-strategist` | `paid-social-planning`, `audience-targeting`, `budget-bidding` |
| [advertising](advertising.md) / `search-programmatic` | `agency:paid-media-ppc-strategist` | `paid-search-planning`, `query-optimization`, `programmatic-buying`, `shopping-feeds` |
| [advertising](advertising.md) / `ad-creative-measurement` | `agency:paid-media-creative-strategist` | `ad-creative`, `creative-testing`, `conversion-tracking`, `attribution-reporting`, `account-audit` |
| [outbound](outbound.md) / `prospecting-research` | `agency:sales-outbound-strategist` | `prospect-discovery`, `account-research`, `prospect-qualification` |
| [outbound](outbound.md) / `outreach-sequences` | `agency:sales-outbound-strategist` | `sequence-design`, `outreach-copy`, `reply-triage` |
| [outbound](outbound.md) / `partnerships-referrals` | `agency:sales-outbound-strategist` | `creator-partnerships`, `referral-programmes`, `partner-outreach` |
| [sales](sales.md) / `discovery-qualification` | `agency:sales-discovery-coach` | `meeting-prep`, `discovery-calls`, `deal-qualification` |
| [sales](sales.md) / `proposals-pitches` | `agency:sales-proposal-strategist` | `proposal-decks`, `business-cases`, `seller-enablement` |
| [sales](sales.md) / `pricing-deal-desk` | `agency:sales-deal-strategist` | `pricing-models`, `offer-packaging`, `deal-strategy` |
| [sales](sales.md) / `pipeline-forecasting` | `agency:sales-pipeline-analyst` | `pipeline-forecast`, `revenue-operations`, `sales-reporting` |
| [operations](operations.md) / `planning-workflow` | `agency:project-management-studio-operations` | `project-planning`, `workflow-orchestration`, `delivery-discipline`, `process-improvement`, `automation-operations`, `studio-operations` |
| [operations](operations.md) / `knowledge-systems` | `agency:zk-steward` | `documentation`, `knowledge-management`, `skill-authoring`, `document-production`, `tool-integration` |
| [operations](operations.md) / `finance-legal` | `agency:chief-financial-officer` | `financial-operations`, `legal-contracts`, `privacy-compliance` |
| [operations](operations.md) / `people-partners` | `agency:recruitment-specialist` | `recruitment-onboarding`, `team-development`, `vendor-partners` |

Choose independent reviewer instances from the pools above; a listed QA coordinator cannot check an artefact they made or fixed. Read-only heads return decisions; `agent:implementer` persists the records as described in the [role-boundary rule](../../methods/playbooks/README.md#model-routing). Local agent files in `~/.claude/agents/` are workstation prerequisites, not portable repository assets; Agency Agents live in `.claude/agents/`. Installation and availability must be checked at kickoff.

Quality Lab's `evals/README.md` and job cases are the pre-client check for covered jobs, with a different judge model and human spot-check. Jobs without cases remain Unknown; Operations proposes missing cases. Production owns `evals/pilot/README.md` and the 19-stage rehearsal; the founder alone decides first-client readiness. A tool's presence, evaluation score or departmental title cannot supply approval.

## Who reviews whose work

No department approves its own work alone. Same-department reviewers check craft; the cross-department reviewer checks fit.

| Maker department | Same-department check | Cross-department check |
| --- | --- | --- |
| Strategy | `agency:research-synthesist` | Design (`agent:creative-director`) checks that criteria can judge routes |
| Design | Independent `agent:ceo` or `agency:design-brand-guardian` for identity; `agent:creative-auditor`, `agent:visual-qa-engineer` for rendered digital work | Strategy (`agent:strategic-architect`) for strategy fit; Engineering (`agent:frontend-architect`) for buildability |
| Engineering | `agency:engineering-code-reviewer`, `agent:performance-engineer` | Design (`agent:visual-qa-engineer`, `agent:creative-auditor`) in the browser |
| Media | `chatcut-desktop:verification`; independent [`skill:3w-image-qa`](../../toolkit/cards/media/image-photo-direction/skill--3w-image-qa.md) for images | Design (`agency:design-brand-guardian` for imagery; `agent:creative-auditor` for rendered digital contexts) for intent |
| Production | `agency:project-management-project-shepherd` | `agency:testing-evidence-collector` for handover packs |
| Marketing | `skill:content-quality-auditor` | Design and Engineering for craft accuracy; founder for anonymity |
| Sales | `agency:sales-pipeline-analyst` | Strategy for scope; Design and Engineering for feasibility |
| Advertising | Independent `agency:paid-media-auditor` | Marketing for truthful claims; founder for spend and scope |
| Outbound | — | Founder for every first message |
| Operations | `superpowers:verification-before-completion` | Founder; lawyer or chartered accountant where required |
| Labs | — | Engineering reviewers and an originality audit before any reuse |

## RACI by lifecycle stage

R = responsible, A = accountable for the studio stage, C = consulted, I = informed, — = no default involvement. Each row has one studio A, the founder. The separate `C1` column states client decision rights rather than a second internal A. This extends the [project RACI](../../business/engagement-operations.md#raci). The producer must name real instances and a distinct checker at kickoff, including where the founder is also producer or craft maker.

| Stage | Founder | Outbound | Sales | Strategy | Design | Engineering | Production | Media | Marketing | Advertising | Labs | Operations | `C1` decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L0 Lead | A | R | C | — | — | — | — | — | R | — | — | I | — |
| L1 Qualify | A | C | R | C | — | — | — | — | I | — | — | I | — |
| L2 Discovery and scope | A | — | R | R | C | C | C | — | — | — | — | I | Confirms scope |
| L3 Proposal | A | — | R | C | C | C | C | — | — | — | — | C | Accepts or negotiates |
| L4 Contract and deposit | A | — | R | — | — | — | I | — | — | — | — | R | Signs, pays, sets clearance |
| L5 Kickoff | A | — | I | C | C | C | R | I | — | — | — | C | Confirms plan and inputs |
| L6 Identity 01–03 | A | — | — | R | C | C | R | — | — | — | — | I | Facts, then strategy |
| L6 Identity 04–07 | A | — | — | C | R | C | R | C | — | — | — | I | Route, then visual system |
| L6 Digital 01–08 | A | — | — | C | R | R | R | C | — | — | — | I | Separate concept, art direction, prototype and launch decisions |
| L7 Launch and handover | A | — | — | — | C | R | R | C | I | — | — | C | Acceptance and receipt separately |
| L8 Care | A | — | I | — | C | R | R | — | — | — | — | I | Reports defects, agrees or declines plan |
| L9 Case study and close-out | A | C | R (win/loss) | C | C | C | R | C | R | — | — | R | Permission and wording, separately from acceptance |

Advertising becomes C/R only for a separately approved launch extension with founder-approved budget and measurement plan; no spend is inferred. Labs can be C when a validated kit is considered, and remains outside client delivery. Media's C becomes R only for an explicitly scoped asset pack. Any activation updates the project's RACI and scope first.

## Related

- [Department index](README.md) · [Registry summary](registry-summary.md)
- [Delivery playbooks](../../methods/playbooks/README.md) · [Handoffs](../../methods/handoffs/README.md)
