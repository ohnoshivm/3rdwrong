---
title: Digital experience playbook
type: method
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Digital experience playbook

Who does what, with which tool, checked by whom, in each of the ten [Digital Experience](../digital-experience/README.md) stages. The stages run inside lifecycle L6, with 09 closing L7 and 10 running L8 ([client lifecycle](../lifecycle.md)). The method files hold the steps and quality gates; [web standards](../quality/web-standards.md) holds the thresholds. Field meanings, model routing and maker ≠ checker rules are in the [playbooks index](README.md).

## One pod from day one

Design and Engineering work as one pod from stage 01 ([D-0018](../../studio/decisions/0018-design-engineering-studio.md), [D-0019](../../studio/decisions/0019-organisation-and-loading-policy.md)). Design owns what and why; Engineering owns how. When feasibility is Unknown at concept, Engineering runs a bounded browser spike before recommending the route; it is formative and does not approve direction. The hardest moment is prototyped in the real medium (a browser on target hardware) at stage 04, before the full build, and the prototype sets the budgets. Engineering is in the room for the concept; Design is in the browser for the build.

| Stage | Design half of the pod | Engineering half of the pod | Others |
| --- | --- | --- | --- |
| 01 | `agent:ui-ux-architect` — content, journeys, UX audit | `agent:performance-engineer` — technical audit | Strategy `agent:strategic-architect`; Production inputs |
| 02 | `agent:creative-director` — concept; `agent:ui-ux-architect` — sitemap | `agency:engineering-rapid-prototyper` (or `agent:3d-webgl-engineer` for scenes) — feasibility | Strategy checks fit |
| 03 | `agent:creative-director`, `agent:visual-designer`, `agent:ui-ux-architect` | `agent:frontend-architect` — token format, component feasibility | — |
| 04 | `agent:creative-director` judges in the browser | `agency:engineering-rapid-prototyper`, `agent:3d-webgl-engineer`, `agent:motion-director`; `agent:performance-engineer` measures | — |
| 05 | `agent:ui-ux-architect` specs; browser design review | `agent:frontend-architect`; builds by GPT-6 Luna/Sol or `agent:implementer` / `agent:complex-engineer` | Production content intake |
| 06 | `agent:creative-director` — motion intent | `agent:motion-director`, `agent:3d-webgl-engineer` | Media scoped assets |
| 07 | `agent:visual-qa-engineer` | `agent:implementer` instance that did not build the feature | Production content QA |
| 08 | `agent:creative-auditor` — craft not degraded | `agent:performance-engineer`, security, release | Production go/no-go |
| 09 | Usage and content guidance | `agency:engineering-devops-automator` | Production handover |
| 10 | Iteration design | `agent:performance-engineer`, fixes | Production care |

## Workspace files and source templates

The [digital bundle](../../templates/bundles/project-digital/bundle.yaml) renders `README.md`, `brief.md`, `decisions.md`, `feedback.md`, `risks.md`, `stack-decision.md`, `status/README.md`, `qa/README.md`, `handover.md` and `retro.md` from the same filenames plus `.tmpl` under `templates/bundles/project-digital/workspace/`. Follow [existing-workspace handling](README.md#workspace-and-evidence-discipline), including combined engagements. Store raw client content, URLs, captures, harness reports and code in the agreed private project store; only cleared, anonymised text summaries enter the public workspace.

| Stage | Exact output record / artefact | Source |
| --- | --- | --- |
| 01 | `discovery-synthesis.md`, `content-inventory.md`; `qa/README.md` audit and success criteria | New method records under [DX-01](../digital-experience/01-discovery-and-audit.md); [research intake](../../templates/learning/research-intake.md) for source/method limits; existing [QA log source](../../templates/bundles/project-digital/workspace/qa/README.md.tmpl). |
| 02 | `experience-strategy.md`, `sitemap.md`, `signature-moments.md`; `qa/concept-critique.md` | Open `stack-decision.md` from the [stack record source](../../templates/bundles/project-digital/workspace/stack-decision.md.tmpl); new DX-02 records; [concept route](../../templates/identity-systems/concept-route.md) for each of at least three distinct territories and [design critique](../../templates/critique/design-critique.md). |
| 03 | Private code repository: `docs/ART_DIRECTION.md`, `docs/INTERFACE_ARCHITECTURE.md`, `docs/MOTION_SPEC.md`, `design/tokens.json`; vault template designs | New artefacts to the [pod contract](../handoffs/design-to-engineering.md), not bundle-generated files. Record versions in `decisions.md`. |
| 04 | Runnable prototype in private code repository; `qa/README.md` budget/measurements; `risks.md`; `<vault>/<codename>/finance/estimate.yaml` | Complete and prove `stack-decision.md` before DX-05; DX-04 artefacts; [estimate source](../../templates/bundles/estimate/estimate.yaml.tmpl). |
| 05 | Feature-complete private build, tests and CMS models; `qa/README.md` build/test/review records | DX-05 output contract; test/code filenames follow the chosen project's conventions rather than invented bundle outputs. |
| 06 | Private `docs/MOTION_SPEC.md` updated; scene code; `qa/README.md` measurements | DX-06 output contract and versioned pod contract; captures in `<vault>/<codename>/files/qa/`. |
| 07 | `qa/README.md` defect/checklist log; `<vault>/<codename>/files/qa/<build>/<template>/report.md` and `report.json` plus raw evidence | Existing QA log source; [`scripts/web_qa.py`](../../scripts/web_qa.py) generates harness reports. |
| 08 | `launch-plan.md`; `qa/README.md` performance/security/launch checklist; `decisions.md` go/no-go | New launch-plan record to [DX-08](../digital-experience/08-performance-and-launch-readiness.md); existing bundle logs. |
| 09 | `handover.md`; private code `README.md`, `docs/ARCHITECTURE.md`, `docs/EDITOR_GUIDE.md`; delivery asset index | Existing [handover source](../../templates/bundles/project-digital/workspace/handover.md.tmpl); new code documentation and assets to the [digital pack](../handover-and-care.md#digital-handover-pack). |
| 10 | `handover.md` care log; `qa/README.md` field record; `decisions.md` warranty closure | Existing bundle logs. |

The per-stage pre-client rows map all ten stages in `evals/pilot/stage-matrix.md`. Run both existing cases for each named job before first client use; apply the anchored rubrics to actual pilot output under the protocol. A plan score is not a delivered-site score.

## Stage map

| Stage | Owner agent | Independent reviewer | Gate (client approval in bold) | Duration (Hypothesis) |
| --- | --- | --- | --- | --- |
| [01 Discovery & audit](#01-discovery-and-audit) | `agent:ui-ux-architect` + `agent:performance-engineer` | `agency:research-synthesist`; `agent:frontend-architect` | DX-01 **inputs and success criteria** | 3–5 working days |
| [02 Experience strategy & concept](#02-experience-strategy-and-concept) | `agent:creative-director` | `agency:design-brand-guardian` (Opus); `agent:strategic-architect` | DX-02 **concept and sitemap** | 3–5 working days |
| [03 Art direction & design system](#03-art-direction-and-design-system) | `agent:creative-director` | `agency:design-brand-guardian`; `agent:frontend-architect` | DX-03 **art direction**; tokens frozen | 4–6 working days |
| [04 Prototype](#04-prototype) | `agency:engineering-rapid-prototyper` | `agent:creative-auditor`; `agent:performance-engineer` | DX-04 **prototype**; budgets agreed | 5–10 working days |
| [05 Production build](#05-production-build) | `agent:frontend-architect` | `agency:engineering-code-reviewer`; `agent:visual-qa-engineer` | DX-05 feature-complete | From the DX-04 estimate |
| [06 Motion, 3D & interaction](#06-motion-3d-and-interaction) | `agent:motion-director`; `agent:3d-webgl-engineer` | `agent:performance-engineer`; `agent:creative-auditor` | DX-06 budgets and reduced motion | From the DX-04 estimate |
| [07 QA](#07-qa) | `agent:visual-qa-engineer`; fresh `agent:implementer` QA instance | `agency:testing-reality-checker` | DX-07 no open critical or major defect | From the DX-04 estimate |
| [08 Performance & launch readiness](#08-performance-and-launch-readiness) | `agent:performance-engineer` | Independent `agency:engineering-code-reviewer` running `skill:ceos-production-quality`; `agent:creative-auditor` | DX-08 **launch approved** | From the DX-04 estimate |
| [09 Launch & handover](#09-launch-and-handover) | `agency:engineering-devops-automator`; `agency:project-management-studio-producer` | `agency:testing-evidence-collector` | DX-09 **acceptance; receipt** | 1–2 weeks (L7 range) |
| [10 Care & iteration](#10-care-and-iteration) | `agency:project-management-studio-producer`; `agent:performance-engineer` | `agency:engineering-code-reviewer`; `agent:visual-qa-engineer` | DX-10 warranty closed; care plan | 30-day warranty, then per plan |

**Documented** — no Digital Experience duration is established ([lifecycle](../lifecycle.md#stage-overview)). Ranges for 01–04 are **Hypothesis** planning ranges for one site; 05–08 are estimated from the stage 04 prototype and recorded in the plan, not guessed here.

## Performance budget (D-0023)

The approved award-grade budget ([D-0023](../../studio/decisions/0023-commercial-and-delivery-defaults.md), [web standards](../quality/web-standards.md#core-web-vitals)) applies to every project unless the founder approves a looser exception in writing. Projects may be stricter.

| Budget | Value | Set | Checked | Verified |
| --- | --- | --- | --- | --- |
| LCP, mobile p75 | ≤ 2.0 s | DX-04 | Every significant merge (05), scenes (06) | DX-08 lab; DX-10 field |
| INP, mobile p75 | ≤ 200 ms | DX-04 | 05, 06 (lab proxy: Total Blocking Time and manual interaction tests) | DX-10 field only; not verifiable before launch |
| CLS, mobile p75 | ≤ 0.1 | DX-04 | 05, 06 | DX-08 lab; DX-10 field |
| Transfer before first interaction | ≤ 2 MB; the rest lazy-loaded | DX-04 | 05, 06 | DX-08 |
| Frame rate | 60 fps target on the reference mid-range phone | DX-04 | 06 | DX-08 |
| Reduced motion | Complete `prefers-reduced-motion` fallback | DX-02 (planned per moment) | 04, 06 | DX-07, DX-08 |

Stage 04 also sets the project's own JavaScript, image, video, 3D, texture, draw-call and frame-time budgets in `qa/README.md` ("Budgets agreed at prototype"). Every measurement records tool, version, device, network profile and date. Lab numbers are labelled lab; field numbers are labelled field.

## Accessibility and reduced-motion gates

| Stage | Gate check | Owner → checker |
| --- | --- | --- |
| DX-02 | Every signature moment names its reduced-motion and no-WebGL alternative | `agent:creative-director` → independent `agency:design-brand-guardian` (Opus) |
| DX-03 | Every text and interface colour pair meets [web standards contrast](../quality/web-standards.md#accessibility); component states include focus | `agent:visual-designer` → `design:accessibility-review` instance |
| DX-04 | Reduced-motion and no-WebGL fallbacks built and tested in the slice | Engineering builder → `agent:performance-engineer` |
| DX-05 | Accessible semantics built in, not retrofitted (`skill:building-accessible-interfaces`) | Builder → `agency:engineering-code-reviewer` |
| DX-06 | Reduced motion keeps the same information and order; flashing and long-movement rules; keyboard and browser find survive scroll effects | `agent:motion-director` → `agent:creative-auditor` with `skill:review-animations` |
| DX-07 | Automated checks, then manual keyboard, focus, screen reader (one desktop and one mobile pairing), 200 % zoom, 320 px reflow, reduced motion; target WCAG 2.2 AA | `agency:testing-accessibility-auditor` → `agency:testing-reality-checker` |
| DX-08 | No regression from optimisation; accessibility scope and open defects recorded for launch | `agent:performance-engineer` → founder at go/no-go |

## Checklists by stage

- [Web QA checklist](../quality/web-qa-checklist.md) — run at DX-07 on the production build; copy results into `qa/README.md`.
- [Launch-readiness checklist](../quality/launch-readiness-checklist.md) — run at DX-08 before the go/no-go review.
- [Handover and care: digital handover pack](../handover-and-care.md#digital-handover-pack) — DX-09.
- [Critique protocol](../quality/critique-protocol.md) — severity and verdicts at every review.

## Mandatory harness report and conditional gate

The independent QA executor runs `bin/3w qa run <url> --out <vault>/<codename>/files/qa/<build>/<template>` against the production build, once per key template, using a new empty output directory each time. Read [`docs/web-qa-harness.md`](../../docs/web-qa-harness.md) and [`scripts/web_qa.py`](../../scripts/web_qa.py). Check `lighthouse --version` and `playwright-cli --version` first; missing prerequisites block collection. Read `report.md`, `report.json`, all three `lighthouse-*.json` files, `browser.json` and six screenshots. Reports contain identifying URLs/content and remain vault-only. Record filenames, build, date, profile and reviewer in `qa/README.md`.

The harness uses three cold mobile Lighthouse runs and per-metric medians against D-0023; it captures 375 / 768 / 1440 px with and without reduced motion, checks console/uncaught errors and automated accessibility findings, and records transfer and scroll timing proxies. Those widths supplement the method's 390 / 834 / 1440 matrix plus 320 px reflow and 1920 px. A human inspects all captures and tests agreed journeys, browser/device matrix, keyboard, focus, assistive technology, WebGL/asset failure and equivalent reduced-motion content. Automated checks do not establish WCAG conformance or the real-phone frame rate.

**DX-07 requires a report with verdict PASS, or INCOMPLETE with the following named founder sign-offs.** The current harness deliberately never emits overall PASS: `status` is FAIL or INCOMPLETE; `lab_status` may be PASS. Exit 1 means measured failure; exit 2 includes missing evidence or invalid/failed collection and is never success by itself. Keep its raw verdict unchanged.

| Remaining evidence | Required decision / follow-up |
| --- | --- |
| Mobile field p75 LCP, INP and CLS unavailable before sufficient real-user data | `FIELD-DATA-DEFERRED`: founder records the exact missing metrics, reason, named measurement owner, collection source, review date and breach response. Carry the condition to DX-10; lab medians and TBT never become field p75 or INP. |
| Reference mid-range real-phone test incomplete | `REAL-PHONE-TEST-DEFERRED`: founder names the exact untested device, frame-rate/fallback/journey checks, responsible tester, due date and launch consequence. Before launch at DX-08, supply the real-device evidence or an explicit separate founder decision accepting the remaining risk with `C1` informed. Never claim the phone target was met while deferred. |

Conditional passage is allowed only with `lab_status: PASS`, zero unresolved Blocker/Major defects, complete manual accessibility, functional and equivalent reduced-motion/fallback checks, and an accounted-for list of every `NOT_MEASURED` line. The only deferable absences under this route are field data and the named real-phone checks; missing Lighthouse runs, screenshots, traces or other required checks cause **hold**, not a blanket waiver. Raw harness failure must be fixed and rerun; a looser budget needs a genuine existing founder exception using `--budget` per the harness guide. An agent never authors an approval record.

Production logs `pass with conditions` in the README gate log, references both founder decisions where applicable, and carries all conditions to the DX-08 go/no-go and QA → handover contract. Re-run after fixes or material build changes. DX-08 independently checks the current build's report, launch checklist and outstanding conditions; its founder and `C1` launch decisions remain separate from any lab verdict.

## 01 Discovery and audit

Method: [01 Discovery & audit](../digital-experience/01-discovery-and-audit.md).

| Field | Playbook |
| --- | --- |
| Objective | Establish goals, audiences, tasks, content and constraints, and audit the current site; choose no concept. |
| Owner | Design / experience-design (`agent:ui-ux-architect`: content inventory, journeys, current-site UX audit) paired with Engineering / platform-performance (`agent:performance-engineer`: technical audit). Strategy / research-perception (`agent:strategic-architect`) frames audience tasks. |
| Independent reviewer | `agency:research-synthesist` checks evidence labels; `agent:frontend-architect` checks the technical audit's stack, CMS and integration findings. |
| Lead tools | `skill:designing-user-experience` (interaction-architecture); `skill:reviewing-interface-quality` (ux-audit) for the current site; `design-skills:journey-mapping` (journey-mapping); `skill:ux-research` (primary-research); `skill:ceos-performance-engineering` (web-vitals); `agency:engineering-codebase-onboarding-engineer` (codebase-analysis) when existing code is inherited. |
| Specialists (trigger) | `skill:core-web-vitals` — a focused LCP, INP or CLS diagnosis with field or lab evidence. `mcp:chrome-devtools` — a running page needs traces or network diagnostics. `agency:engineering-wordpress-performance` / `agency:engineering-drupal-performance` — the current site runs on that platform. `skill:technical-seo-checker` (Marketing, technical-seo lead) — SEO basics of the current site. `skill:design-analysis` — extracting visual properties from a reference page for principles only. |
| Inputs | Signed scope; `projects/<codename>/brief.md`; the approved identity system (or the agreed identity engagement output); current site, analytics and CMS access through the vault. |
| Outputs | `discovery-synthesis.md` with evidence labels; content inventory and delivery plan; technical audit and success criteria recorded in `qa/README.md` (checks log) and `decisions.md`; reference notes (principles, never layouts); `risks.md`. |
| Gate | DX-01: founder; **`C1` confirms facts, success criteria and the content plan**. |
| Evidence | Audit measurements with tool, device profile and date; interview notes in the vault; `C1` confirmation in `decisions.md`. |
| Pre-client quality check | Both cases in `evals/cases/strategy/evidence-synthesis/`; both cases in `evals/cases/engineering/web-vitals/`; both cases in `evals/cases/engineering/accessibility-implementation/`. Follow `evals/README.md`; retain independent scores and human spot-check in `qa/README.md`. |
| Failure modes | Designing before content exists; stakeholder preference treated as audience evidence; an integration or language discovered after architecture; reference sites collected as templates. |

## 02 Experience strategy and concept

Method: [02 Experience strategy & concept](../digital-experience/02-experience-strategy-and-concept.md). Open `stack-decision.md` under [D-0025](../../studio/decisions/0025-creative-technology-selection-policy.md): outcome, preferred approach, two alternatives, dependency reasons, risks, mobile/accessibility strategy and prototype plan. This is the candidate architecture; DX-04 proves it. Confirm a dated approved identity strategy first; if it is missing or changed, return to the [strategy gate](identity-system.md#03-strategy). Record any experience-strategy changes for human approval before route exploration; concept and visual decisions never authorise strategy retroactively. Hand-in: [strategy → design](../handoffs/strategy-to-design.md).

| Field | Playbook |
| --- | --- |
| Objective | One original idea, the sitemap and journeys that serve audience tasks, and a few signature moments with costs and fallbacks. |
| Owner | Design / direction (`agent:creative-director`, or `agent:ceo` for flagship and own-studio work) with experience-design (`agent:ui-ux-architect`: sitemap, templates, journeys). Engineering / creative-engineering rates feasibility (`agency:engineering-rapid-prototyper`; `agent:3d-webgl-engineer` for scenes). |
| Independent reviewer | Independent `agency:design-brand-guardian` on Opus (or `agent:ceo` when triggered and not a maker) runs `skill:3w-identity-system-critic` on the concept; `agent:creative-auditor` joins only when rendered evidence exists. `agent:strategic-architect` checks positioning and audience fit. |
| Lead tools | A reference pack from the [`3w-taste-graph`](../../skills/3w-taste-graph/SKILL.md) skill first (registered creative-output prerequisite); `agent:creative-director` and `skill:3w-creative-direction` (concept-direction); `skill:designing-user-experience` (interaction-architecture); `skill:double-diamond` (experience-prototyping); `skill:ceos-motion-direction` (motion-principles) for the intent of each signature moment. |
| Specialists (trigger) | `agent:ceo` — flagship or own-identity concept decision. `skill:ceos-creative-direction` — the studio's own digital touchpoint needs a concept narrative. `skill:ceos-interaction-architecture` — navigation, journeys, states and input behaviour need defining. `skill:find-animation-opportunities` — identifying motion opportunities. `skill:ux-storyboard` — representing journeys or experience narratives. |
| Inputs | DX-01 synthesis, content inventory, success criteria; approved identity strategy and system. |
| Outputs | Candidate `stack-decision.md`; concept statement and route rationale (`decisions.md`); sitemap, template inventory and journey maps; signature-moment list with purpose, reduced-motion and no-WebGL fallback and feasibility rating; `risks.md`. |
| Gate | DX-02: founder selects the concept; **`C1` approves concept and sitemap**. Concept approval does not approve art direction. **Interpretation** — if the SOW treats this as "approval of the chosen direction", the D-0023 30% payment falls here; follow the SOW. |
| Evidence | Critique record with verdict "Strong enough to advance"; Engineering's feasibility note per moment; `C1` approval with version. |
| Pre-client quality check | Both cases in `evals/cases/design/interaction-architecture/`; both cases in `evals/cases/design/concept-direction/`. Follow `evals/README.md`; retain independent scores and human spot-check in `qa/README.md`. |
| Failure modes | Many routes presented to avoid recommending; spectacle no task needs; a concept with no reduced-motion or WebGL-failure plan; a sitemap that silently exceeds scope. |

## 03 Art direction and design system

Method: [03 Art direction & design system](../digital-experience/03-art-direction-and-design-system.md).

| Field | Playbook |
| --- | --- |
| Objective | Tokens first, then two or three key templates at three widths with real content, then the smallest component inventory. |
| Owner | Design / direction (`agent:creative-director`: art direction), identity-craft (`agent:visual-designer`: digital type scale, colour roles, tokens from the human-led W1 system), experience-design (`agent:ui-ux-architect`: components and states). Engineering / product-frontend (`agent:frontend-architect`) sets token format and naming that maps to code. |
| Independent reviewer | `agency:design-brand-guardian` running `skill:3w-identity-system-critic`, formal mode, against concept and identity; rendered templates also go to `agent:creative-auditor`; `agent:frontend-architect` (not a maker of the visuals) confirms tokens and components are buildable. |
| Lead tools | `skill:ceos-art-direction` (art-direction); `frontend-design:frontend-design` (ui-design); [`skill:3w-typography-system`](../../toolkit/cards/design/identity-craft/skill--3w-typography-system.md) (typography); [`skill:3w-colour-system`](../../toolkit/cards/design/identity-craft/skill--3w-colour-system.md) (colour); [`skill:3w-composition-system`](../../toolkit/cards/design/identity-craft/skill--3w-composition-system.md) (composition-layout); `design-skills:design-systems` (design-system-guidelines); `skill:ceos-motion-direction` (motion-principles); `design-skills:ux-writing` (ux-writing). |
| Specialists (trigger) | `agent:visual-designer` — an approved brand system needs digital tokens, a type ramp, measured contrast and grid specification. [`skill:3w-image-production`](../../toolkit/cards/media/image-photo-direction/skill--3w-image-production.md) (image-production-workflow lead) — approved placements need image assets; [`skill:3w-image-qa`](../../toolkit/cards/media/image-photo-direction/skill--3w-image-qa.md) (image-quality-check lead) — independent asset rights/consent and quality check before use. `ui-ux-pro-max:design-system` — a primitive/semantic/component token architecture is needed. `vectorlab-ux-skills:motion` — consistent duration and easing tokens. `design:accessibility-review` — a design artefact needs WCAG review before implementation. `mcp:figma` / `figma:figma-use` — a Figma file exists or is explicitly requested. `design-superpowers:ds-consumer` — the client has an existing design system that must be consumed. |
| Inputs | DX-02 concept, sitemap and signature moments; identity specification and assets with rights. |
| Outputs | Art direction document; design tokens as data (JSON) in the project code repository, version recorded in `decisions.md`; key templates at desktop, tablet and mobile (vault `files/`); component inventory with states; motion language with durations and easings. |
| Gate | DX-03: founder; **`C1` approves art direction on two or three key templates**. Tokens are then frozen for the prototype; later changes go through change control. |
| Evidence | Token file version; templates at three widths; contrast results; critique record; `C1` approval with version. |
| Pre-client quality check | Both cases in `evals/cases/design/typography/`; both cases in `evals/cases/design/colour/`; both cases in `evals/cases/design/composition-layout/`; both cases in `evals/cases/design/motion-principles/`. Follow `evals/README.md`; retain independent scores and human spot-check in `qa/README.md`. |
| Failure modes | Desktop only; components before tokens; gradients, nested cards and default type standing in for decisions; approval from mood boards instead of real templates; the D-0006 look as a default. |

## 04 Prototype

Method: [04 Prototype](../digital-experience/04-prototype.md). Prove and complete the stack record with rejected alternatives, exact versions, prototype/device measurements, independent craft review and the final decision; link DX-04 acceptance from `decisions.md`. This record is required before DX-05. Hand-in: [design → engineering pod contract](../handoffs/design-to-engineering.md).

| Field | Playbook |
| --- | --- |
| Objective | Build the riskiest signature moment and its template in a real browser on target hardware, measure it, and set the budgets the build is held to. |
| Owner | Engineering / creative-engineering (`agency:engineering-rapid-prototyper`; `agent:3d-webgl-engineer` for scenes; `agent:motion-director` for choreography) with `agent:frontend-architect` for the stack decision. Design / experience-design judges feel in the browser (`agent:creative-director`). |
| Independent reviewer | `agent:creative-auditor` reviews the rendered slice against concept and art direction; `agent:performance-engineer` measures (it did not build the slice). |
| Lead tools | `agency:engineering-rapid-prototyper` (creative-prototyping); `skill:ceos-realtime-3d` (realtime-3d); `skill:gsap-core` (motion-implementation); `skill:ceos-shader-engineering` (shader-engineering) only for bespoke shaders; `skill:ceos-performance-engineering` (web-vitals); `skill:playwright-cli` (test-engineering) for screenshots at three widths. |
| Specialists (trigger) | `skill:scaffold-3d-site` — a scoped 3D prototype needs a scaffold after architecture approval. `skill:gsap-scrolltrigger` — scroll-linked pinning or scrubbing is in the concept. `skill:optimize-3d-assets` — 3D assets need web preparation. `vectorlab-ux-skills:reduced-motion` — the motion treatment needs a tested reduced-motion alternative. `playground:playground` — the system needs a self-contained parameter explorer. |
| Inputs | Frozen tokens, key templates, motion language; signature-moment list; reference device and network profile from kickoff. |
| Outputs | Completed `stack-decision.md` with evidence and final architecture decision; prototype on a private preview URL (URL recorded in the vault); measurement record and the budget table in `qa/README.md`; fallback notes; updated risks; updated estimate in `<vault>/<codename>/finance/estimate.yaml`. |
| Gate | DX-04: complete stack decision record with prototype/device evidence and final decision; **founder and `C1` accept the prototype**; Design and Engineering leads jointly agree budgets and fallbacks. Budgets at or under D-0023, or a founder-approved exception recorded in the project. |
| Evidence | Screenshots and a short recording at three widths (vault); measurements on the reference mid-range mobile and a desktop (LCP, CLS, input responsiveness, JS and asset weight, draw calls, texture memory, frame time); fallback tests. |
| Pre-client quality check | Both cases in `evals/cases/engineering/creative-prototyping/`; both cases in `evals/cases/design/interaction-architecture/`; both cases in `evals/cases/engineering/web-vitals/`. Follow `evals/README.md`; retain independent scores and human spot-check in `qa/README.md`. |
| Failure modes | Prototyping the easy part; measuring on a fast laptop; budgets set after the build to match it; prototype shortcuts kept in production code. |

## 05 Production build

Method: [05 Production build](../digital-experience/05-production-build.md). Do not begin without the DX-04-proven `stack-decision.md`; revisit and re-test it when assumptions or dependencies change.

| Field | Playbook |
| --- | --- |
| Objective | Build every page, template, content flow and integration in scope on the architecture the prototype proved, within budget. |
| Owner | Engineering / product-frontend (`agent:frontend-architect`: architecture and code standards). Build execution from an approved spec: GPT-6 Luna (GPT-6.1 Sol for complex multi-file work) through T3 `delegate_task`, or `agent:implementer` / `agent:complex-engineer`. CMS: `agency:engineering-cms-developer`. Design / experience-design (`agent:ui-ux-architect`) supplies specs and responsive behaviour. |
| Independent reviewer | `agency:engineering-code-reviewer` on every consequential change (no self-merging); `agent:visual-qa-engineer` runs the design review in the browser at three widths per completed template. |
| Lead tools | `agent:frontend-architect` (frontend-architecture); `agency:engineering-software-architect` (technical-architecture); `agency:engineering-frontend-developer` (ui-implementation); `agency:engineering-cms-developer` (site-and-cms-build); `skill:building-accessible-interfaces` (accessibility-implementation); `skill:playwright-cli` (test-engineering); `skill:supply-chain-risk-auditor` (dependency-audit); `agency:engineering-devops-automator` (deployment-and-release) for staging. |
| Specialists (trigger) | `skill:ceos-frontend-architecture` — choosing and structuring the frontend for a creative site. `skill:next-best-practices` — the stack is Next.js. `agency:engineering-i18n-engineer` (internationalization lead) — more than one language is in scope. `agency:engineering-backend-architect` (backend-and-api lead) — an API or backend is in scope. `skill:deploy-to-vercel` — hosting is Vercel. `agent:complex-engineer` — the normal executor would struggle. |
| Inputs | Completed DX-04 stack decision record; DX-04 prototype, budgets and fallbacks; templates, tokens and component states; content per the delivery plan. |
| Outputs | Architecture decision in `decisions.md`; feature-complete build on staging; CMS content models with editor previews; tests; design-review log and budget checks per milestone in `qa/README.md`; screenshots in the vault. |
| Gate | DX-05: Engineering and Design leads confirm feature completeness; founder logs it. Scope additions go through change control (`bin/3w new change-order`). |
| Evidence | Build and test output; budget measurements per milestone; code-review record; design-review screenshots. |
| Pre-client quality check | Both cases in `evals/cases/engineering/ui-implementation/`. Follow `evals/README.md`; retain independent scores and human spot-check in `qa/README.md`. |
| Failure modes | Speculative dependencies; hard-coded content the client must later edit; budget overruns found only at 08; "works on my machine" accepted as design review. |

## 06 Motion, 3D and interaction

Method: [06 Motion, 3D & interaction](../digital-experience/06-motion-3d-and-interaction.md). Reference: [Creative Technology selection policy](../creative-technology/selection-policy.md) and the current stack decision record; verify dependency reasons, property/scroll ownership and fallback evidence.

| Field | Playbook |
| --- | --- |
| Objective | Implement motion, scenes and interactions that each carry meaning, stay within budget and have a usable alternative. |
| Owner | Design / experience-design owns intent (`agent:creative-director` with `skill:ceos-motion-direction`: what each moment helps the user understand or do). Engineering / creative-engineering implements (`agent:motion-director`: choreography and GSAP; `agent:3d-webgl-engineer`: scenes). Media produces scoped film, 3D or sound assets under Design's direction. |
| Independent reviewer | `agent:performance-engineer` measures frame time, memory and long tasks; `agent:creative-auditor` with `skill:review-animations` judges purpose, timing and the reduced-motion path. |
| Lead tools | `skill:ceos-motion-direction` (motion-principles); `skill:gsap-core` (motion-implementation); `skill:ceos-realtime-3d` (realtime-3d); `skill:optimize-web-animations` (animation-runtime); `skill:ceos-creative-coding` (generative-creative-coding) only for generative systems. |
| Specialists (trigger) | `skill:gsap-scrolltrigger` — scroll-linked behaviour. `skill:gsap-timeline` — sequenced playback. `skill:gsap-react` — GSAP inside React or Next. `skill:motion` — React gesture, spring or layout interaction. `skill:gsap-performance` — the measured issue is in a GSAP timeline. `skill:scroll-3d-scene` — scroll-driven 3D with one scroll owner. `skill:add-postprocessing` — a restrained post-processing stack is in scope. `skill:ceos-3d-asset-pipeline` — assets need web preparation. |
| Inputs | Motion language and tokens (DX-03); budgets and fallbacks (DX-04); production assets with rights. |
| Outputs | Motion and scene implementation; motion specification (durations, easings, triggers); fallback notes; frame-time and memory measurements in `qa/README.md`; recordings with and without reduced motion in the vault. |
| Gate | DX-06: Design and Engineering leads jointly; founder logs it. One smooth-scroll engine at most; reduced motion complete. |
| Evidence | Recordings in both motion modes; frame time and memory with device and date; no-WebGL and asset-failure fallback tests. |
| Pre-client quality check | Both cases in `evals/cases/design/motion-principles/`; both cases in `evals/cases/engineering/creative-prototyping/`. Follow `evals/README.md`; retain independent scores and human spot-check in `qa/README.md`. |
| Failure modes | Motion for its own sake or one easing everywhere; two scroll engines; scroll-jacking that breaks keyboard, screen readers or browser find; scenes that stall on a mid-range phone. |

## 07 QA

Method: [07 QA](../digital-experience/07-qa.md). Hand-in: [engineering → QA](../handoffs/engineering-to-qa.md).

| Field | Playbook |
| --- | --- |
| Objective | Find and fix visual, accessibility, cross-browser, functional and content defects on the production build before the client and public do. The build also needs the mandatory harness report and independent evidence review. |
| Owner | Design / design-qa (`agent:visual-qa-engineer`: visual and responsive QA at 1440, 834 and 390 px plus agreed widths). Engineering / engineering-qa-security: a fresh `agent:implementer` instance runs functional and cross-browser tests it did not build. Accessibility: `agency:testing-accessibility-auditor`. Production runs content QA with the client's content owners. |
| Independent reviewer | `agency:testing-reality-checker` reviews the QA log, severity and every closure; no department signs its own QA alone. |
| Lead tools | `agent:visual-qa-engineer` (visual-qa-browser); `skill:playwright-cli` (test-engineering); `design-skills:accessibility-audit` (accessibility); `skill:reviewing-interface-quality` (ux-audit); `skill:3w-brand-consistency-qa` (consistency-qa); `skill:audit-reference-originality` (originality-audit); `skill:semgrep` and `claude-security:claude-security` (security-analysis); `skill:content-quality-auditor` (Marketing, editorial-quality) for proofreading. |
| Specialists (trigger) | `skill:break-ui` — verifying layouts, interactions and edge cases across widths. `vectorlab-ux-skills:viewports` — overflow between 375 and 1280 px. `skill:no-ai-design-slop` — an independent review finds generic defaults. `agency:design-ui-finish-gate-reviewer` — scope requires a finish-gate consistency review. `mcp:chrome-devtools` — console or network diagnostics. `skill:stitched-full-page-capture` — full-page evidence capture. |
| Inputs | Feature-complete build with motion and scenes (DX-05, DX-06); final client content. |
| Outputs | Harness report and raw artefacts in the vault; [web QA checklist](../quality/web-qa-checklist.md) results and defect list (severity, owner, state) in `qa/README.md`; screenshots before and after fixes in the vault. |
| Gate | DX-07: founder logs pass or pass with conditions only under the [mandatory harness gate](#mandatory-harness-report-and-conditional-gate), with no open Blocker (critical) or Major and every Minor dispositioned. |
| Evidence | Screenshots at every template and width; automated report outputs; manual accessibility notes; browser and device matrix from [web standards](../quality/web-standards.md#devices-and-browsers). |
| Pre-client quality check | Both cases in `evals/cases/design/consistency-qa/`; both cases in `evals/cases/engineering/accessibility-implementation/`; both cases in `evals/cases/engineering/ui-implementation/`. Follow `evals/README.md`; retain independent scores and human spot-check in `qa/README.md`. |
| Failure modes | QA declared complete from an automated score; a fix not re-inspected; testing only the team's browser; content QA left to launch day. |

## 08 Performance and launch readiness

Method: [08 Performance & launch readiness](../digital-experience/08-performance-and-launch-readiness.md). Reference: [Creative Technology selection policy](../creative-technology/selection-policy.md) and the current stack decision record; verify dependency reasons, property/scroll ownership and fallback evidence.

| Field | Playbook |
| --- | --- |
| Objective | Prove the build meets its budgets and is safe to launch, with a rehearsed go-live and rollback plan. |
| Owner | Engineering / platform-performance (`agent:performance-engineer`: measurements), engineering-qa-security (security review), deployment-and-release (`agency:engineering-devops-automator`: launch and rollback plan). Production (`agency:project-management-studio-producer`) runs the go/no-go. Operations / finance-legal (`agency:data-privacy-officer`) checks consent against the agreed privacy approach. |
| Independent reviewer | Independent `agency:engineering-code-reviewer` running `skill:ceos-production-quality` (release-verification) on the built artefact; `agent:creative-auditor` confirms optimisation did not degrade craft. |
| Lead tools | `skill:ceos-performance-engineering` (web-vitals); `skill:investigating-performance` (runtime-diagnostics); `agency:security-architect` (security-architecture); `skill:semgrep`, `claude-security:claude-security` (security-analysis); `skill:supply-chain-risk-auditor` (dependency-audit); `skill:ceos-production-quality` (release-verification); `skill:technical-seo-checker` (Marketing, technical-seo). |
| Specialists (trigger) | `skill:core-web-vitals` — focused LCP, INP or CLS diagnosis. `skill:vercel-optimize` — deployed on Vercel with measured platform cost or performance issues. `skill:web-quality-audit` — a broad live audit across performance, accessibility, SEO and best practice. `agency:security-senior-secops` — headers, CORS, rate limits or secrets exposure need review. |
| Inputs | DX-07 pass; budgets from DX-04; production hosting and domain access through the vault. |
| Outputs | Performance report (budget against measurement) and security review in `qa/README.md`; launch plan with rollback trigger and owner per step; completed [launch-readiness checklist](../quality/launch-readiness-checklist.md); go/no-go record in `decisions.md`. |
| Gate | DX-08: **founder and `C1` approve launch** at the go/no-go review. |
| Evidence | Measurements with device, network profile and date; dependency audit output; header check; checklist. Field data is **not verified** before launch; name who measures it at stage 10. Reconcile every current-build harness condition; record FIELD-DATA-DEFERRED and any REAL-PHONE-TEST-DEFERRED decision explicitly, never turn INCOMPLETE into a measured pass. |
| Pre-client quality check | Both cases in `evals/cases/engineering/web-vitals/`; both cases in `evals/cases/engineering/accessibility-implementation/`. Follow `evals/README.md`; retain independent scores and human spot-check in `qa/README.md`. |
| Failure modes | Laptop lab scores presented as user experience; launching before a weekend or holiday without cover; no rollback plan; analytics firing before consent. |

## 09 Launch and handover

Method: [09 Launch & handover](../digital-experience/09-launch-and-handover.md). Lifecycle L7. Hand-off: [QA → production and handover](../handoffs/qa-to-handover.md).

| Field | Playbook |
| --- | --- |
| Objective | Release, verify live and transfer everything the client needs to run the site without the studio. |
| Owner | Engineering / deployment-and-release (`agency:engineering-devops-automator`: release, live verification, documentation); Production / handover-retention (`agency:project-management-studio-producer`: pack, walkthrough, records); Design: usage and content guidance. |
| Independent reviewer | `agency:testing-evidence-collector` runs live smoke tests at three widths independently of whoever deployed. |
| Lead tools | `agency:engineering-devops-automator` (deployment-and-release); `skill:writing-release-notes` (delivery-handover) for the client-facing release; `design:design-handoff` (handover-specs); `skill:ceos-production-quality` (release-verification). |
| Specialists (trigger) | `skill:deploy-to-vercel` / `vercel:deployments-cicd` — hosting is Vercel. `agency:engineering-technical-writer` — handover documentation needs specialist writing. `agency:engineering-sre` — monitoring or error budgets are in scope. |
| Inputs | DX-08 launch approval and plan. |
| Outputs | Live site; [digital handover pack](../handover-and-care.md#digital-handover-pack); `handover.md`; editor training record; account, domain and repository transfer locations in the vault; acceptance and receipt in `decisions.md`; final invoice per D-0023 (`bin/3w new invoice`, vault only). |
| Gate | DX-09: **`C1` confirms final acceptance and, separately, receipt and access**. Record the 30-day warranty dates from launch; receipt is a separate event. |
| Evidence | Live screenshots (vault); smoke-test notes; handover checklist; training record; acceptance record with version. |
| Pre-client quality check | Both cases in `evals/cases/engineering/ui-implementation/`; both cases in `evals/cases/design/consistency-qa/`. Follow `evals/README.md`; retain independent scores and human spot-check in `qa/README.md`. |
| Failure modes | Deployment treated as handover; editors trained on dummy content; studio-owned accounts left as the only owner of client infrastructure. |

## 10 Care and iteration

Method: [10 Care & iteration](../digital-experience/10-care-and-iteration.md). Lifecycle L8.

| Field | Playbook |
| --- | --- |
| Objective | Fix warranty defects, monitor the live site and improve it through measured iterations under an agreed care plan. |
| Owner | Production / handover-retention (`agency:project-management-studio-producer` triages: warranty defect, change request or care work); Engineering / platform-performance (`agent:performance-engineer`: monitoring and field Core Web Vitals; fixes by `agent:implementer` or GPT-6 Luna); Design for iteration craft. |
| Independent reviewer | `agency:engineering-code-reviewer` on every fix; `agent:visual-qa-engineer` re-inspects affected templates. |
| Lead tools | `agency:customer-success-manager` (client-success) when a care retainer exists; `skill:investigating-performance` (runtime-diagnostics); `skill:ceos-performance-engineering` (web-vitals); `skill:supply-chain-risk-auditor` (dependency-audit). [`skill:3w-care-retention`](../../toolkit/cards/production/handover-retention/skill--3w-care-retention.md) (retention-programmes) leads warranty closure, evidence-based care and access removal. |
| Specialists (trigger) | `agency:engineering-incident-response-commander` — a production incident. `agency:engineering-sre` — SLOs or observability are in the care plan. `skill:core-web-vitals` — field data shows a budget breach. |
| Inputs | Live site; handover record; warranty terms; care plan if any. |
| Outputs | Care log in `handover.md`; field measurement record in `qa/README.md`; iteration proposals; warranty closure in `decisions.md`; access removed and credentials rotated. |
| Gate | DX-10: founder and `C1` close the 30-day warranty and agree or decline a care plan. Resolve deferred device tests; review the field-data condition on its due date. If traffic is insufficient, keep field p75 Unknown with owner and next review, rather than closing it as passed. |
| Evidence | Care log entries; field measurements with dates against the D-0023 budget; closure record. |
| Pre-client quality check | Both cases in `evals/cases/engineering/web-vitals/`; both cases in `evals/cases/strategy/evidence-synthesis/`. Follow `evals/README.md`; retain independent scores and human spot-check in `qa/README.md`. |
| Failure modes | Unlimited "small changes" absorbed as warranty; no monitoring; dependencies unpatched with no owner. |

## Gaps recorded by this playbook

- W1 supplies the typography, colour and composition leads at stage 03; W2 supplies retention-programmes at stage 10. Their source paths remain integration dependencies, listed in the [playbooks index](README.md#how-to-read-a-playbook-entry).
- **Interpretation:** no new registry job gap is created for functional QA: `skill:playwright-cli` already leads test-engineering. Assign a fresh `agent:implementer` instance to execute the agreed test plan; `agency:engineering-code-reviewer` checks coverage and `agency:testing-reality-checker` checks evidence. No invented QA persona is needed. Content QA borrows Marketing's `skill:content-quality-auditor`.

## Related

- [Playbooks index](README.md) · [Identity system playbook](identity-system.md) · [Client lifecycle playbook](client-lifecycle.md)
- [Handoffs](../handoffs/README.md) · [Department heads and RACI](../../studio/departments/heads.md)
- [Digital Experience offer](../../studio/digital-experience-offer.md) acceptance criteria
