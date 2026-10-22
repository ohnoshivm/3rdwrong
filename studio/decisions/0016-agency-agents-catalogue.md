---
id: D-0016
title: Agency Agents catalogue
type: decision
status: approved
date: 2026-10-22
owner: founder
last_reviewed: 2026-10-22
review_every_days: 90
approved_by: founder
approved_on: 2026-10-22
approval_source: founder instruction, 2026-10-22
---

# D-0016: Agency Agents catalogue

## Decision

Install the [Agency Agents catalogue](https://github.com/msitarzewski/agency-agents) minus 53 excluded agents (229 included), at repository level only in `.claude/agents/`, pinned to commit `4e3ac3ca6604c75113f52c695dbddcc7af928b46`. Use upstream's Claude Code installer with an explicit destination and preserve its identity-format output without hand edits. Record every file's SHA-256 in [the lock](../../agents/agency-agents.lock.json); apply the founder's [exclusions](../../agents/exclusions.txt) and update through [`scripts/sync_agents.sh`](../../scripts/sync_agents.sh).

## Status

Approved by the founder on 2026-10-22. Installing a persona does not approve its advice, establish an achieved capability or change the status of studio knowledge.

## Rationale

The founder first chose all 282 agents, then explicitly removed the GIS (13), Healthcare (3), Finance (5), Game Development (21) and Support (6) divisions, plus `academic-geographer` and four testing agents (`testing-api-tester`, `testing-test-automation-engineer`, `testing-test-results-analyzer`, `testing-workflow-optimizer`). This excludes 53 agents and retains 229 for breadth available on demand.

Academic (5) and Testing (5: `testing-accessibility-auditor`, `testing-reality-checker`, `testing-evidence-collector`, `testing-tool-evaluator`, `testing-performance-benchmarker`) remain because they serve the perception-led method in [D-0001](0001-strategic-positioning.md) and the evidence principle in [D-0003](0003-operating-philosophy.md). Studio skills and narrow routing remain the first choice; specialist personas are available when a task benefits from them. The catalogue is local to this repository, with no global installation.

This choice is in tension with [D-0003](0003-operating-philosophy.md): “Exceptional execution matters more than the number of tools installed.” It also departs from the [founding blueprint's advice against large agent collections](../archive/founding-blueprint-v1.0.md#what-we-should-not-install-immediately). The founder accepts this exception for availability; it does not make catalogue size evidence of execution quality.

## Alternatives considered

- **Curated 8–12 agents:** lower discovery and routing overhead, less maintenance and closer alignment with the blueprint, but fewer specialists immediately available. Not the founder's choice.
- **Whole divisions:** a middle ground with thematic coverage and reduced listing cost, but arbitrary division boundaries can exclude useful cross-disciplinary help. Not the founder's choice.
- **All 282 agents:** maximum breadth with higher discovery, routing and maintenance costs. Initially chosen, then narrowed by the founder.
- **Catalogue minus explicit exclusions:** retain 229 agents and document 53 exclusions with reasons. Chosen by the founder after removing irrelevant divisions, duplicated roles and unsuitable legal/financial specialisms; use a chartered accountant for real accounting and tax matters.

## Evidence

**Documented** — Founder instructions, 2026-10-22: initially install all agents at repo level, then apply the explicit exclusion list. Upstream HEAD resolved to the pinned SHA above; upstream `tools.json` declares Claude Code's `identity` format and `scripts/install.sh --tool claude-code --no-interactive --path <destination>` copies the original agent Markdown. The upstream installer renders 282 files with no filename collisions; the installed selection contains 229 files and excludes 53. The lock records the exclusions digest, full source-to-division inventory, included/excluded counts and included file hashes. Upstream code and agent material are MIT; see [third-party notices](../../THIRD_PARTY_NOTICES.md).

**Documented (estimate, 2026-10-23)** — The 229 agent names and descriptions total 61,667 characters, roughly 15,400 tokens if the full discovery list is loaded into a session (characters ÷ 4; not a live token count). Persona bodies load only when an agent is used.

## Consequences

The agent discovery list may add per-session context cost even when only one persona is used. Estimated listing overhead: about 15,400 tokens per session (see Evidence). Broader routing increases the risk of selecting an irrelevant or overlapping persona; use [AGENTS.md](../../AGENTS.md) and studio skills first, then open only the selected specialist.

3RDWRONG status rules, evidence labels, the ban on invented results and the [publication rules](../../docs/public-private-boundary.md) override every persona instruction and example success metric. Keep vendor files unmodified; their upstream examples are not studio results. Pin and hash the catalogue and exclusion list, review upstream changes before upgrades, preserve the MIT notice, and retain secret scanning. Upstream files are excluded from local frontmatter, link, index and Markdown style checks.

## Revision triggers

Review after 90 days (2027-01-20), or sooner if measured token overhead is too high, routing repeatedly selects the wrong agents, agents remain unused after 90 days, upstream licence or installer contracts change, or maintenance outweighs useful work. Review Marketing, Specialized and Engineering for irrelevant agents. Any change to the founder-chosen selection requires a recorded founder decision.
