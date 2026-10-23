# Changelog

Changes to the 3RDWRONG Creative Operating System are recorded here.

## [Unreleased]

### Added

- Web delivery QA harness (`bin/3w qa run`): three mobile Lighthouse runs, explicit lab/field limits, project budget checks with founder exception records, Playwright responsive/reduced-motion evidence, console and scroll cadence probes, Markdown/JSON reports and local integration coverage.

- Creative Technology system from the founder-supplied October 2026 handbook:
  archived source, selection policy, tool/effect matrices, official-source
  verification, learning library and five proposed Labs starter studies.
- Founder-approved D-0025 adopts native-first selection, three access levels,
  recorded reasons for specialist dependencies and a stack decision record for
  every digital project; D-0023 remains the binding performance budget.
- Digital project bundle creates the stack record; stages 02/04/05 require it
  before production, with motion and launch checks linked to the policy.
- Four experimental identity-craft skills that fill the design department's craft gaps: `3w-mark-exploration` (mark-logo), `3w-colour-system` (colour), `3w-composition-system` (composition-layout) and `3w-typography-system` (typography), each with a `.claude/skills` link and a tool card under `toolkit/cards/design/identity-craft/`.
- Standard-library `scripts/colour_check.py` for WCAG 2.2 contrast, CIEDE2000 palette matrices, and Machado colour-vision simulations, with published-reference tests.
- Fictional Stillsoil Atelier test runs and skill evaluations for all four skills; the runs led to version 0.1.1 of each (formative-run rules, declared colour-vision thresholds, mandatory-text and fixed-content inputs, below-minimum mark decision, specimen strings).
- Twelve experimental studio skills that close the remaining department lead gaps outside identity craft: `3w-effect-study`, `3w-labs-benchmark`, `3w-engine-validation`, `3w-demo-publishing` (Labs); `3w-behavioural-lens`, `3w-narrative-analysis` (Strategy); `3w-care-retention` (Production); `3w-image-production`, `3w-image-qa` (Media); `3w-awards-submission` (Marketing); `3w-prospect-qualification`, `3w-reply-triage` (Outbound). Each links to the studio method it applies, has a `.claude/skills` symlink and a proposed tool card under `toolkit/cards/`; registry placement and materials are integrated.
- Proposed delivery playbooks (`methods/playbooks/`): how a project runs through the eleven departments, model routing, maker ≠ checker and founder gates; per-phase identity playbook, per-stage Digital Experience pod playbook with the D-0023 budget, accessibility and reduced-motion gates; client lifecycle playbook from lead to case study with D-0021, D-0023 and D-0024 defaults.
- Proposed department handoff contracts (`methods/handoffs/`): strategy → design, design → engineering pod contract, engineering → QA, QA → production and handover, delivery → marketing, each with artefact checklists and a handoff record.
- Proposed department heads, reviewer pools, escalation paths, quality bars and a lifecycle RACI (`studio/departments/heads.md`).
- W1/W2 experimental leads routed by registry id, exact bundle/output provenance, read-only agent boundaries and existing-workspace handling; canonical registry patches applied during integration.
- Quality Lab paired-case checks and the 19-stage pre-client pilot wired into delivery gates; Web QA harness reports required at DX-07/08 with explicit founder field-data and real-phone deferrals, vault-only raw evidence and independent review. No pilot execution or client-readiness result is claimed.

### Changed

- Integrated Web QA after independent round-2 clearance; wired its source, guide and budget links into delivery handoffs, heads and Creative Technology. Labs studies require a harness verdict PASS or the named founder-authorised INCOMPLETE route; Quality Lab remains under review.

- Integrated 17 registry entries and materials (16 job leads plus the existing Taste Graph prerequisite), updated department counts/leads and expanded coverage to 825 tool cards, and regenerated toolkit, handbook and routing outputs.
- Wired delivery playbooks to the integrated skills/cards, D-0025 stack records, living-identity selection and Engineering/Labs ownership; retained Quality Lab and Web QA as phase-2 dependencies.
- Aligned the demo-publishing skill/card with the already-approved D-0009 licensing model.
- APCA is not shipped; it may be checked manually with the official tool, subject to its licence. WCAG 2.2 contrast determines pass/fail; CIEDE2000 and CVD checks are retained.
- Agent routing, Engineering/Labs ownership and living-identity guidance link
  the system. Six source cards qualify Lenis, full scaffolds, post-processing
  and WebGPU defaults; vendored sources remain unchanged.
- Applied registry changes: the four skills become leads of their jobs and `agent:visual-designer` becomes a typography specialist for digital tokens and type ramps.

## [0.5.0] - 2026-10-23

### Added

- 808 proposed tool cards documenting inputs, invocation, passing output, quality checks and limits for every current registry lead and specialist across eleven departments.
- Deterministic human tool handbook and agent routing index, generated by `scripts/build_handbook.py` with per-department coverage, specialist triggers, bench/parked reasons and stale-output checks.
- Tool-card standard, registry-aware metadata and routing validation, staged strict department coverage, and card/generator regression tests.

### Changed

- Added handbook entry points to README, AGENTS, CLAUDE and department guides: humans browse by department and job; agents filter the routing index, load the lead first and open only the selected card.
- Aligned handbook guidance with D-0022's studio name and D-0023/D-0024 defaults; final AI-generated deliverables require written client consent and the studio performance budget applies to mobile p75 measurements.

## [0.4.0] - 2026-10-23

### Added

- Approved D-0022 (studio name 3RDWRONG), D-0023 (commercial and delivery defaults) and D-0024 (growth defaults), recorded from the founder decisions session of 2026-10-23.
- Taste Graph (D-0020): local PostgreSQL reference library, public seeds, capture/search/curation CLI and the experimental `3w-taste-graph` reference-pack skill.
- Delivery engine: lifecycle, Digital Experience method, web quality and launch gates, handover/care, `bin/3w`, project bundles and anonymity guard.
- Approved D-0021: contract-cleared client records are public and anonymised; confidential identities, client files and all money stay in a private vault.
- Business engine: pricing/estimation, proposals/SOWs, legal/IP and finance guidance, collaborator methods, operating rhythm, founder review queue and eight operating-record bundles.
- Growth engine: qualification/discovery, pipeline, content, outbound/compliance, proof, partnerships, advertising and metrics; five bundles for case studies, content briefs and private discovery/outreach/win-loss records.
- Real CLI integration coverage for all 15 shipped bundles, including cleared and private project workspaces.

### Changed

- Renamed the studio from 3RDWRONGS to 3RDWRONG across first-party files and generated toolkit manifests (D-0022); the founding archive stays verbatim with a note.
- Applied D-0023 defaults to the MSA (portfolio, AI and arbitration options resolved; `{{arbitration_seat}}` placeholder), commercial rules, invoicing, engagement operations, handover warranty, web standards and QA budgets, both offer pages and the proposal, SOW and digital QA bundles.
- Applied D-0024 defaults to content channels, outbound volume and the awards budget.
- Integrated context routing and documentation for creative references, delivery, business and growth work; pricing reads vault inputs and prints only.
- Normalised all bundle variables to one documented list format; made `bin/3w` honour `--set codename` and validate a cleared workspace’s vault before any public or private write.
- Refreshed the core toolkit plugin, lock and coverage for `3w-taste-graph`; kept toolkit and anonymity checks together.
- Replaced the old client-acquisition guide with a route into `growth/` and wired cross-engine references.
- Made zero-filled pricing templates report an actionable input error instead of dividing by zero.

## [0.3.0] - 2026-10-23

### Added

- Eleven department guides in four groups, recut registry summary and v2 portable routing; Design retains its human craft standards and evidence gates.
- Third-party toolkit with VENDOR snapshots, pinned FETCH plan, MANUAL enablement, licensing notices, 12-plugin Claude Code marketplace and non-overwriting one-command installer for Claude/Codex.

- Founder-approved D-0018: design-engineering studio direction, with brand identity at the core, digital experience as the second pillar and an explicitly labelled 6–12-month ambition.
- Founder-approved D-0019: 11 departments in four groups, flagship Design and Engineering, department-head/independent-review-board model, and registry-led loading policy for skills and Agency Agents.
- Proposed positioning v0.2 and Digital Experience flagship offer for founder review, including paired-pod delivery, performance/accessibility criteria and pricing to be set by founder.
- Proposed 12-month roadmap milestones for OS v0.3, own identity and website proof, two self-initiated projects, Labs house-engine v1, first paid Digital Experience project and top-job evaluations.

### Changed

- Superseded D-0001 and D-0002 with D-0018 while retaining their historical text and approvals.
- Aligned README and the two authorised AGENTS entry lines with the approved direction/status; updated studio navigation, identity-offer guidance and pricing hypotheses without rewriting founder positioning or ICP.
- Flagged ICP and remaining method migration for review, updated the decision register and regenerated INDEX.md.

Founder approvals: approved_by: founder; approved_on: 2026-10-23; approval_source: founder instruction, 2026-10-23. Related proposals and hypotheses retain their statuses.

## [0.2.0] - 2026-10-22

### Added

- Full founding source archive, public pricing hypotheses and founder-approved D-0017 retiring `3rdwrongs-private`; publication includes economics, payment structure, budget, hours and critical self-review.
- Agency Agents catalogue at repository level (229 included, 53 founder exclusions from 282 upstream agents), pinned to `4e3ac3ca6604c75113f52c695dbddcc7af928b46`, with MIT notices, reproducible upstream installation, per-file hashes, an integrity validator and founder-approved D-0016.
- Founder's three-tier master website swipe file with verified entries, existing-study links and source access notes.
- Standing inspiration discovery guide for project references, with verified source descriptions and use limits.
- Primary taste resource for Award Site Teardowns (rickcreates.com), with evidence-graded use guidance and links to original-site benchmarks.

### Changed

- Renamed the repository and local home to `ohnoshivm/3rdwrong` and `~/3rdwrong`, including clone instructions and Python package metadata.
- Replaced the two-repo boundary with publication rules, superseded D-0008, restored unvalidated studio price ranges and retained secret/personal-data scans, including upstream agents.
- Prefixed all five studio skills with `3w-`, recreated relative Claude Code symlinks, and updated references and required paths.
- Excluded upstream agent Markdown from local knowledge metadata, links, index generation and Markdown style checks; added regression tests and regenerated `INDEX.md`.

Founder approvals: approved_by: founder; approved_on: 2026-10-22; approval_source: founder instruction, 2026-10-22.

## [0.1.0] - 2026-10-22

### Added

- Public repository foundation for studio knowledge, methods, research, templates, and experimental skills.
- Metadata governance, validation tools, contribution guidance, and AI entry points.
- Studio knowledge: founder positioning thesis and initial ICP, Identity System offer, Brand Direction Sprint, creative philosophy, strategic rationale, portfolio strategy, roadmap, and decision records D-0001 to D-0015.
- Methods: nine-phase identity engagement, perception-to-identity map, creative guardrails, taste practice, critique protocol, system testing, and final-delivery checklist.
- Intelligence: seven research templates, five sourced reference studies, psychology notes, proposed principles, research queue, and resources.
- Five experimental skills (`3w-brand-discovery`, `3w-category-code-audit`, `3w-creative-direction`, `3w-identity-system-critic`, `3w-brand-consistency-qa`) with two test runs on a fictional example.
- `taste/` reference websites, `inbox/` quick capture, and generated `INDEX.md`.
- Validator (metadata, decisions, skills, links, required files, secrets and privacy, index freshness), unit tests, and CI with SHA-pinned actions.
