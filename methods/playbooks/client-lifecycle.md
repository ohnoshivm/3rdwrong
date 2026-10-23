---
title: Client lifecycle playbook
type: method
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Client lifecycle playbook

Which department, agent and tool carries a client from first contact to case study. The [client lifecycle](../lifecycle.md) owns the stages, entry conditions and exit gates; the [Growth engine](../../growth/README.md) owns L0–L2 and the growth parts of L9; the [Business engine](../../business/README.md) owns L3–L4 and invoicing; the Delivery methods own L5–L8. This page routes the work; it does not restate those gates. Field meanings and model routing are in the [playbooks index](README.md).

## Rules that apply at every stage

- **[D-0021](../../studio/decisions/0021-client-work-public-anonymised.md) anonymity.** The repository holds codenames and roles (`C1`, `C2`) only. Names, contacts, domains, money, contracts, interview notes and client files live in the vault (`THREEW_VAULT` or `~/3rdwrong-vault`). Uncleared projects live wholly in the vault (`--private`). Run `bin/3w check` before every commit that touches `projects/`, and a human reviews for identifying combinations.
- **[D-0023](../../studio/decisions/0023-commercial-and-delivery-defaults.md) delivery defaults.** Payment 50 / 30 / 20 (start, approval of the chosen direction, before final files); two consolidated feedback rounds per phase; named portfolio use only after public launch, with client-approved wording and a contract opt-out; arbitration seat `{{arbitration_seat}}`; AI use disclosed and AI-generated finals only with written consent; 30-day warranty; the Digital Experience performance budget. Varying a default needs the founder's written approval, recorded in the project (money in the vault).
- **[D-0024](../../studio/decisions/0024-growth-defaults.md) growth defaults.** Four content channels; 20 researched, hand-written first messages a week, never automated or batch-sent; free award submissions only until the studio site or a flagship project is ready. Paid advertising waits for its trigger (still a founder decision; see [advertising](../../growth/advertising.md)).
- **Money never enters the repository.** `scripts/pricing.py` reads vault inputs and only prints; never paste its output into a public file.

## Stage map

| Stage | Departments | Owner agent | Independent reviewer | Bundle sources / commands (respect existing targets) | Founder gate | Client gate | Duration (Hypothesis, from the lifecycle) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [L0 Lead](#l0-lead) | Outbound, Marketing | `agency:sales-outbound-strategist` | Founder (every first message) | `outreach-sequence` (vault) | — | — | Continuous |
| [L1 Qualify](#l1-qualify) | Sales | `agency:sales-coach` | `agent:strategic-architect` | — (vault pipeline) | Pursue or decline | — | 1–5 working days |
| [L2 Discover & scope](#l2-discover-and-scope) | Sales, Strategy; Design and Engineering feasibility | `agency:sales-discovery-coach` | `agent:creative-director` + `agent:frontend-architect` (feasibility) | `discovery-notes`, `estimate` (vault) | Scope is deliverable | Confirms scope summary | 1–3 weeks |
| [L3 Propose](#l3-propose) | Sales | `agency:sales-deal-strategist` | `agent:strategic-architect` | `proposal` (vault) | Approves before sending | Accepts or negotiates | 3–10 working days |
| [L4 Contract & deposit](#l4-contract-and-deposit) | Sales, Operations | `agency:legal-document-review` (contract), `agency:chief-financial-officer` (deposit) | Founder; lawyer where the template note requires | `sow`, `invoice` (vault) | Signs | Signs, pays deposit, sets clearance | 1–10 working days |
| [L5 Onboard & kickoff](#l5-onboard-and-kickoff) | Production | `agency:project-management-studio-producer` | `agency:project-management-project-shepherd` | `project-identity` or `project-digital` | Plan and team | Confirms plan, roles, access, inputs | 3–5 working days |
| [L6 Deliver](#l6-deliver) | Design + Engineering pod; Strategy, Media as scoped; Production | Per [identity](identity-system.md) or [digital](digital-experience.md) playbook | Per playbook | `change-order` as needed; `weekly-review` (vault) | Every method gate | Every client method gate | Identity 4–6 weeks proposed; digital from the DX-04 estimate |
| [L7 Launch & handover](#l7-launch-and-handover) | Production, Engineering, Design | `agency:project-management-studio-producer` | `agency:testing-evidence-collector` | `invoice` (vault) | Release | Final acceptance; receipt and access | 1–2 weeks |
| [L8 Care](#l8-care) | Production, Engineering | `agency:project-management-studio-producer` | `agency:engineering-code-reviewer` | — | Care scope | Reports issues; approves care work | 30-day warranty, then per plan |
| [L9 Close-out & case study](#l9-close-out-and-case-study) | Production, Marketing, Operations, Sales, Media | Producer (retro); `agent:creative-writer` (case study) | `skill:content-quality-auditor`; founder anonymity review | `case-study`, `win-loss` (vault), `invoice` (vault) | Retro actions; publication | Final invoice; case-study permission | 1–3 weeks after acceptance |

## L0 Lead

| Field | Playbook |
| --- | --- |
| Work | Find and open conversations with fitting prospects; answer inbound within one working day; record every lead. Guides: [lead sources](../../growth/sales/lead-sources.md), [outbound](../../growth/outbound/README.md), [compliance](../../growth/outbound/compliance.md), [inbound](../../growth/content/inbound.md). |
| Owner | Outbound / outreach-sequences (`agency:sales-outbound-strategist` designs the sequence); Marketing / content-social for inbound. |
| Reviewer | The founder reads and approves every first message; D-0024 requires each to be researched and written by hand. |
| Lead tools | `skill:prospecting` (prospect-discovery); `sales:sales-company-research` (account-research); `agency:sales-outbound-strategist` (sequence-design); `agency:sales-outreach` (outreach-copy) for follow-up drafts, not first messages; `skill:engagement-inbox-manager` (community-engagement) for inbound. [`skill:3w-prospect-qualification`](../../toolkit/cards/outbound/prospecting-research/skill--3w-prospect-qualification.md) (prospect-qualification) screens sourced accounts before contact; [`skill:3w-reply-triage`](../../toolkit/cards/outbound/outreach-sequences/skill--3w-reply-triage.md) (reply-triage) stops the sequence at a reply, records same-day suppression for opt-outs, and routes positive replies into L0. These tools draft/record; they never auto-send. |
| Specialists (trigger) | `agent:researcher` — exact fields and inclusion criteria are supplied for enrichment. `sales:enrich-company-and-contact-data` — prospect or contact enrichment is explicitly needed. |
| Files | Vault pipeline record (codename, source, one-line need, next action); `outreach-sequence` bundle in the vault. Nothing personal in the repository. |
| Failure modes | Automated or batch first messages (breaks D-0024); contact data in a public file; enrichment by a cheap model treated as qualification. |

## L1 Qualify

| Field | Playbook |
| --- | --- |
| Work | Score fit against the ICP, check disqualifiers and red flags, and decide pursue, not yet or decline. Guide: [qualification](../../growth/sales/qualification.md). |
| Owner | Sales / discovery-qualification. `agency:sales-coach` (deal-qualification lead) prepares the scorecard. |
| Reviewer | `agent:strategic-architect` challenges the fit and the offer pillar; the founder decides. |
| Lead tools | `agency:sales-coach` (deal-qualification); `sales:prepare-for-meeting` (meeting-prep). |
| Specialists (trigger) | `sales:follow-up-after-call` — a draft follow-up after a qualified call is requested. |
| Files | Qualification note in the vault pipeline. |
| Gate | Founder: pursue or decline, with a reason. |
| Failure modes | Pursuing a poor fit because the pipeline is thin; declining without recording why. |

## L2 Discover and scope

| Field | Playbook |
| --- | --- |
| Work | Understand the problem well enough to scope it; confirm feasibility and capacity. Guide: [discovery call](../../growth/sales/discovery-call.md); estimation: [estimation guide](../../business/pricing/estimation-guide.md). |
| Owner | Sales (`agency:sales-discovery-coach`, discovery-calls lead) with Strategy (`agent:strategic-architect` frames the problem and decision question). |
| Reviewer | Feasibility is checked by people who will deliver: `agent:creative-director` (Design) and `agent:frontend-architect` (Engineering). For Digital Experience scopes, Engineering names the riskiest moment that stage 04 will prototype. |
| Lead tools | `agency:sales-discovery-coach` (discovery-calls); `skill:3w-brand-discovery` (brand-discovery) for a light evidence frame only; `sales:build-business-case` (business-cases) when the client needs one. |
| Files | `bin/3w new discovery-notes --codename <codename>` (vault private notes and hand-off pack); `bin/3w new estimate --codename <codename>` (vault). One-page scope summary sent to `C1`. |
| Gate | Founder: scope is deliverable. `C1` confirms the problem and scope summary in writing. |
| Hand-off | To L3 through the discovery-notes hand-off pack. |
| Failure modes | Scoping a website when no validated identity exists (run or agree an identity engagement first); feasibility assumed rather than checked; discovery notes written into the repository. |

## L3 Propose

| Field | Playbook |
| --- | --- |
| Work | A scoped, priced plan with method stages, review rounds, exclusions, change control, acceptance criteria and ownership. Guides: [proposals](../../business/proposals.md), [commercial rules](../../business/pricing/commercial-rules.md). |
| Owner | Sales / pricing-deal-desk and proposals-pitches. `agency:sales-deal-strategist` (deal-strategy lead) owns the deal; `agent:creative-writer` drafts proposal prose; prices come from `scripts/pricing.py` (vault inputs, printed only). |
| Reviewer | `agent:strategic-architect` checks scope, criteria and method stages agree; Design and Engineering leads confirm deliverables and budgets are achievable. |
| Lead tools | `agency:sales-deal-strategist` (deal-strategy); `agency:specialized-pricing-analyst` (pricing-models); `skill:offers` (offer-packaging); `sales:sales-presentations` (proposal-decks). |
| Specialists (trigger) | `agency:sales-proposal-strategist` — scope requires presentation expertise for the proposal deck. `sales:plan-deal-strategy` — an active opportunity with a defined buyer and decision process. |
| Files | `bin/3w new proposal --private --codename <codename>` → `<vault>/<codename>/proposal.md` from [proposal source](../../templates/bundles/proposal/proposal.md.tmpl). Keep the sent copy with names and prices in the vault. Before contract clearance is known, never use `--cleared`. A later public summary is anonymised and contract-cleared; it is not the sent proposal. |
| Defaults in the proposal | D-0023 payment split, two rounds per phase, 30-day warranty, AI disclosure and consent, portfolio clause with opt-out; for Digital Experience, the performance budget as an acceptance criterion; publication clause (anonymised publication permitted or not). |
| Gate | Founder approves before sending; client accepts. |
| Failure modes | Price or client name in the public proposal; acceptance criteria that cannot be tested; a looser performance budget without a founder exception. |

## L4 Contract and deposit

| Field | Playbook |
| --- | --- |
| Work | Make the commitment binding; record codename and clearance. Guides: [MSA](../../business/legal/master-services-agreement.md), [IP and licensing](../../business/legal/ip-and-licensing.md), [invoicing](../../business/finance/invoicing-and-collections.md). |
| Owner | Operations / finance-legal: `agency:legal-document-review` compares the contract with the template and flags risk clauses; `agency:chief-financial-officer` (financial-operations lead) handles the deposit invoice. Sales holds the relationship. |
| Reviewer | The founder reads every flagged clause; the lawyer-review note on each template still applies. Agents never sign or approve. |
| Lead tools | `agency:legal-document-review` (legal-contracts); `agency:chief-financial-officer` (financial-operations); `agency:data-privacy-officer` (privacy-compliance) when personal data will be processed. |
| Files | `bin/3w new sow --private --codename <codename>` → `<vault>/<codename>/sow.md` from [scope source](../../templates/bundles/sow/sow.md.tmpl); signed contract in `<vault>/<codename>/contracts/`; deposit via `bin/3w new invoice` (vault); the client recorded under the codename in the vault's `clients.yaml`. |
| Gate | Founder signs. Client signs, pays the deposit (50%) and sets clearance: **cleared** or **private**. |
| Failure modes | Starting delivery before contract and deposit because the client is keen; clearance left unrecorded. |

## L5 Onboard and kickoff

| Field | Playbook |
| --- | --- |
| Work | Set up the workspace and align everyone. Guide: [project operations: kickoff](../../business/engagement-operations.md#kickoff). |
| Owner | Production / producing-pm. `agency:project-management-studio-producer` (project-planning lead) runs kickoff and the plan. |
| Reviewer | `agency:project-management-project-shepherd` checks dependencies, client input dates and gate placement; the founder approves plan and team. |
| Lead tools | `agency:project-management-studio-producer` (project-planning); `openai-templates:artifact-template-project-tracker` (project-tracking); `creative-production:intake` (client-onboarding); `agency:project-management-meeting-notes-specialist` (meeting-cadence). |
| Specialists (trigger) | `agency:project-manager-senior` — a spec needs converting to tasks. `mcp:linear` / `mcp:asana` — the project uses that tracker and the connection is verified. |
| Files | Populate from [identity](../../templates/bundles/project-identity/bundle.yaml) or [digital](../../templates/bundles/project-digital/bundle.yaml) bundle using [existing-workspace handling](README.md#workspace-and-evidence-discipline); only a genuinely new target uses `bin/3w new project-*`. Files: README gate log, `brief.md`, `decisions.md`, `risks.md`, `status/`, `feedback.md`, `qa/`, `handover.md`, `retro.md`. |
| Gate | Founder: plan and team. `C1`: plan, roles, access and inputs; `C1` confirmed as the single feedback consolidator. |
| Failure modes | A kickoff meeting without inputs, access or dates; RACI missing the founder-as-producer note on a founder-led project. |

## L6 Deliver

Run the offer playbook: [identity system](identity-system.md) or [digital experience](digital-experience.md). Production coordinates throughout: weekly status (Friday, [operating rhythm](../../business/operating-rhythm.md)), the feedback log, two consolidated rounds per phase, and change orders (`bin/3w new change-order`) for anything beyond them. Every method gate is logged in the README gate log. Hand-offs between departments use the [handoff contracts](../handoffs/README.md).

## L7 Launch and handover

| Field | Playbook |
| --- | --- |
| Work | Release (digital), deliver the handover pack, walk the client through it. Identity: [phase 08](identity-system.md#08-delivery). Digital: [DX-08 and DX-09](digital-experience.md#09-launch-and-handover). Guide: [handover and care](../handover-and-care.md). |
| Owner | Production / handover-retention with Engineering and Design. |
| Reviewer | `agency:testing-evidence-collector` verifies the pack and the live site independently of the makers. |
| Files | `handover.md`; acceptance and receipt in `decisions.md`; final 20% invoice before final files (vault). |
| Marketing | Announce only what the contract permits. Client launches are the client's; `skill:launch-window-planner` and `skill:launch-asset-packager` apply to studio announcements after permission. |
| Gate | Founder: release. `C1`: final acceptance and, separately, receipt and access. |

## L8 Care

| Field | Playbook |
| --- | --- |
| Work | 30-day warranty (D-0023), then an optional paid care plan. Digital: [DX-10](digital-experience.md#10-care-and-iteration). |
| Owner | Production / handover-retention (`agency:project-management-studio-producer` triages); Engineering fixes. `agency:customer-success-manager` only when a care retainer exists (its registry trigger). |
| Reviewer | `agency:engineering-code-reviewer` on each fix; the founder approves care scope. |
| Lead tools | [`skill:3w-care-retention`](../../toolkit/cards/production/handover-retention/skill--3w-care-retention.md) (retention-programmes); evidence-based recommendations, once-only testimonial/referral asks, and access removal. |
| Gate | Warranty closed; care plan agreed or declined; access removed and credentials rotated. |

## L9 Close-out and case study

| Field | Playbook |
| --- | --- |
| Work | Retrospective, permission check, case study if cleared, testimonial and referral asks, award decision, final invoice and archive. Guides: [case studies](../../growth/proof/case-studies.md), [testimonials](../../growth/proof/testimonials.md), [awards](../../growth/proof/awards.md), [partnerships and referrals](../../growth/partnerships-and-referrals.md), [win/loss](../../growth/sales/win-loss.md). |
| Owner | Production runs the retro (identity [phase 09](identity-system.md#09-learning)) and the clearance check; Marketing writes the case study (`agent:creative-writer` with `skill:content-writer`); Media supplies case-study visuals under Design's direction; Operations closes finance and archive; Sales files win/loss; Outbound makes the referral ask. |
| Reviewer | `skill:content-quality-auditor` (editorial-quality) run by an instance that did not write the piece; Design and Engineering check craft accuracy of anything public; the founder runs the anonymity review. |
| Lead tools | `skill:content-writer` (content-writing); `skill:content-quality-auditor` (editorial-quality); `skill:press-media-relations` (earned-media) only with permission; `skill:referrals` (referral-programmes); specialist `sales:find-customer-quotes` only when gathering approved, verbatim client proof. [`skill:3w-awards-submission`](../../toolkit/cards/marketing/pr-awards/skill--3w-awards-submission.md) leads awards-submissions: verify official criteria and zero fee, permissions and credits before preparing an entry; D-0024 limits submissions to free ones for now. |
| Files | `projects/<codename>/retro.md`; `bin/3w new case-study --cleared --codename <codename>` → `projects/<codename>/case-study.md` (anonymised, only if the contract permits publication); `bin/3w new win-loss` (vault); final invoice (vault); hand-off record per [delivery → marketing](../handoffs/delivery-to-marketing.md). |
| Portfolio versus repository | D-0023 allows named portfolio use after the client's public launch with client-approved wording; D-0021 still keeps the repository record codenamed. Naming the client anywhere needs separate written permission, stored in the vault. |
| Gate | Founder: retro actions and publication. `C1`: case-study permission. Project README marked closed; gate log complete. |
| Failure modes | Skipping the retro because the project went well; a case study claiming results without permission or evidence; identifying combinations (sector + city + launch date) left in a public file. |

## Related

- [Playbooks index](README.md) · [Handoffs](../handoffs/README.md) · [Department heads and RACI](../../studio/departments/heads.md)
- [Client lifecycle method](../lifecycle.md) · [Project operations](../../business/engagement-operations.md) · [Publication rules](../../docs/public-private-boundary.md)
