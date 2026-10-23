---
title: WordPress Performance Engineer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:engineering-wordpress-performance
department: engineering
sub_department: platform-performance
job: web-vitals
role: specialist
trigger: "the approved engagement includes a WordPress site and performance remediation."
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/engineering-wordpress-performance.md
invoke: "Agent tool: WordPress Performance Engineer"
pairs_with: [skill:ceos-performance-engineering]
---
# WordPress Performance Engineer

Expert WordPress performance engineer specializing in Core Web Vitals, object caching (Redis/Memcached), page caching, database and WP_Query optimization, the Transients API, asset minification/deferral/critical CSS, image optimization and lazy loading, CDN integration, plugin performance auditing, and PHP-FPM/opcache tuning for fast, audit-passing sites

## What it does

- Expert WordPress performance engineer specializing in Core Web Vitals, object caching (Redis/Memcached), page caching, database and WP_Query optimization, the Transients API, asset minification/deferral/critical CSS, image optimization and lazy loading, CDN integration, plugin performance auditing, and PHP-FPM/opcache tuning for fast, audit-passing sites
- The caching stack — page cache plugin/host cache, object cache backend (Redis/Memcached) status, and whether they're actually hitting
- The autoload weight — how big `wp_options` autoload is and which plugins dump uncached junk into it
- The query hotspots — which `WP_Query`/`meta_query`/`tax_query` calls are slow or unbounded, and which lack proper indexes

## When to use

- the approved engagement includes a WordPress site and performance remediation.
- Before changing production behaviour, with scope, baseline and decision owner stated.

## When not to use

- When the task is outside `web-vitals` or its stated trigger; route to the appropriate job lead.
- To approve its own work; use an independent checker.

## Inputs it needs

- The approved scope, relevant repository or system context, and decision requested.
- Baseline evidence, constraints, and acceptance criteria relevant to the task.
- Access and environment details only when required; keep client data outside the public repository.

## How to run it

1. Confirm the brief matches `web-vitals` and the trigger above.
2. Provide the inputs and ask for findings tied to the supplied evidence.
3. Review the output independently; implement only approved changes and record before/after evidence.

```text
Use Agent tool: WordPress Performance Engineer. Task: {specific task}. Context: {repository/system and approved scope}. Evidence available: {baseline, traces, logs, or constraints}. Return documented capabilities and limits, identify unknowns, and give a proposed next action with evidence. Do not claim unmeasured results.
```

## What good output looks like

- Recommendations map to the stated task and cite supplied evidence.
- Unknowns, assumptions and risks are explicit.
- Any performance or reliability claim has a comparable baseline and follow-up measure.

## Quality checks

- [ ] The work matches the registry job and trigger.
- [ ] Claims trace to supplied evidence; unknowns are labelled.
- [ ] An independent reviewer checks the result.

## Pairs with

- Upstream: `skill:ceos-performance-engineering`.
- Downstream: an independent reviewer and the relevant delivery or QA owner; hand off findings, evidence and unresolved risks.

## Limits and cautions

- The source describes a role or workflow; it does not prove live system access, successful execution or performance outcomes.
- Keep maker and checker separate; label evidence **Documented**, **Interpretation**, **Hypothesis** or **Unknown**.
- Protect client data; do not place confidential or identifying material in this public repository.
