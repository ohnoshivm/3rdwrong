---
title: Shopify
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: shopify:shopify
department: engineering
sub_department: product-frontend
job: site-and-cms-build
role: specialist
trigger: "Use for tasks involving Build anything on Shopify."
kind: skill
availability: both
distribution: vendor
source: toolkit/vendor/plugin-openai-curated-remote-shopify-4.1.2/skills/shopify
invoke: "shopify skill"
pairs_with: [agency:engineering-cms-developer, agency:engineering-frontend-developer]
---
# Shopify

Shopify is the studio's specialist for `site-and-cms-build`; use it when the registry trigger below applies.

## What it does

- Routes work across Shopify CLI, Admin/Storefront APIs, ShopifyQL and platform features
- Requires selecting a topic and reading that topic reference
- Searches docs and validates code using topic-specific instructions

## When to use

- Use for tasks involving Build anything on Shopify.
- For an explicitly Shopify store, app or platform integration

## When not to use

- For another CMS use `agency:engineering-cms-developer`
- For generic UI use `agency:engineering-frontend-developer`
- Do not use to approve its own work; assign a separate checker.

## Inputs it needs

- Shopify topic/surface and project version
- Store/app context and existing code
- Secure credential access

## How to run it

1. Confirm the task matches the job and, for a specialist, the registry trigger.
2. Invoke `shopify skill` and provide the approved brief, artefacts, constraints and source context.
3. Ask for the documented deliverable; inspect assumptions and verification before handoff.

```text
Use `shopify:shopify` for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform/version: {links and versions}. Constraints: {accessibility, performance, delivery}. Work within the documented scope and registry trigger. Label evidence Documented, Interpretation, Hypothesis or Unknown; return the requested artefact, assumptions, limitations, verification actually performed and a concrete next action.
```

## What good output looks like

- Scoped implementation using selected topic guide
- Generated code validated by topic method

## Quality checks

- [ ] Work matches the approved brief and the maker is not its checker.
- [ ] Claims are supported by source or supplied evidence; label uncertainty explicitly.
- [ ] Responsive behaviour, accessibility and performance are checked where they apply.
- [ ] Verification lists only commands, tests or browser checks actually run.

## Pairs with

- `agency:engineering-cms-developer` — coordinate the artefacts and handoff at the relevant stage.
- `agency:engineering-frontend-developer` — coordinate the artefacts and handoff at the relevant stage.

## Limits and cautions

- Node.js required
- do not leak credentials
- follow version-specific search and validation flags
- Keep client data and credentials out of the public repository (D-0021); check licence and distribution prerequisites, including installation or sign-in when required.
