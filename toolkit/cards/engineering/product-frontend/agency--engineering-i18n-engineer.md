---
title: Internationalization Engineer
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:engineering-i18n-engineer
department: engineering
sub_department: product-frontend
job: internationalization
role: lead
trigger: ""
kind: upstream-agent
availability: claude-managed
distribution: vendor
source: .claude/agents/engineering-i18n-engineer.md
invoke: "Claude Code agent: Internationalization Engineer Agent"
pairs_with: [agency:engineering-frontend-developer, skill:building-accessible-interfaces]
---
# Internationalization Engineer

Internationalization Engineer is the studio's lead for `internationalization`.

## What it does

- Externalises strings with ICU MessageFormat and CLDR plurals
- Uses locale APIs for date, number, currency, list and relative-time formatting
- Builds RTL-safe layouts and pseudo-localisation checks

## When to use

- Before string/catalog and layout choices lock for multilingual work
- During implementation of locale, RTL or extraction pipelines

## When not to use

- For translation/cultural validation pair with language reviewers
- For general frontend use `agency:engineering-frontend-developer`
- Do not use to approve its own work; assign a separate checker.

## Inputs it needs

- Target locales, scripts and fallback policy
- Message catalog and extraction workflow
- RTL, long-string and formatting examples

## How to run it

1. Confirm the task matches the job and, for a specialist, the registry trigger.
2. Invoke `Claude Code agent: Internationalization Engineer Agent` and provide the approved brief, artefacts, constraints and source context.
3. Ask for the documented deliverable; inspect assumptions and verification before handoff.

```text
Use `agency:engineering-i18n-engineer` for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform/version: {links and versions}. Constraints: {accessibility, performance, delivery}. Work within the documented scope and registry trigger. Label evidence Documented, Interpretation, Hypothesis or Unknown; return the requested artefact, assumptions, limitations, verification actually performed and a concrete next action.
```

## What good output looks like

- Locale-ready strings and formatting plan
- RTL and pseudo-locale checks with translator context

## Quality checks

- [ ] Work matches the approved brief and the maker is not its checker.
- [ ] Claims are supported by source or supplied evidence; label uncertainty explicitly.
- [ ] Responsive behaviour, accessibility and performance are checked where they apply.
- [ ] Verification lists only commands, tests or browser checks actually run.

## Pairs with

- `agency:engineering-frontend-developer` — coordinate the artefacts and handoff at the relevant stage.
- `skill:building-accessible-interfaces` — coordinate the artefacts and handoff at the relevant stage.

## Limits and cautions

- Do not concatenate translated fragments or hand-roll formats
- source covers web, mobile and backend, use platform-specific guidance
- Keep client data and credentials out of the public repository (D-0021); check licence and distribution prerequisites, including installation or sign-in when required.
