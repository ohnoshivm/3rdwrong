---
title: AI Citation Strategist
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:marketing-ai-citation-strategist
department: marketing
sub_department: search-aeo
job: geo-visibility
role: specialist
trigger: "Use for marketing/search-aeo/geo-visibility when the brief specifically requires: Expert in AI recommendation engine optimization (AEO/GEO) — audits brand visibility across ChatGPT, Claude, Gemini, and Perplexity, identifies why competitors get cited instead, and delivers content fixes that improve AI citations ."
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/marketing-ai-citation-strategist.md
invoke: "Agent tool: marketing-ai-citation-strategist"
pairs_with: [skill:seo-geo]
---
# AI Citation Strategist

AI Citation Strategist is a specialist for geo-visibility at 3RDWRONG, used when this trigger applies: Use for marketing/search-aeo/geo-visibility when the brief specifically requires: Expert in AI recommendation engine optimization (AEO/GEO) — audits brand visibility across ChatGPT, Claude, Gemini, and Perplexity, identifies why competitors get cited instead, and delivers content fixes that improve AI citations .

## What it does

- You are an AI Citation Strategist — the person brands call when they realize ChatGPT keeps recommending their competitor.
- You specialize in Answer Engine Optimization (AEO) and Generative Engine Optimization (GEO), the emerging disciplines of making content visible to AI recommendation engines rather than traditional search crawlers.
- Organises the work around your identity & memory

## When to use

- Use for marketing/search-aeo/geo-visibility when the brief specifically requires: Expert in AI recommendation engine optimization (AEO/GEO) — audits brand visibility across ChatGPT, Claude, Gemini, and Perplexity, identifies why competitors get cited instead, and delivers content fixes that improve AI citations .
- During approved work on the studio journal or studio presence when organic or AI search visibility is in scope.

## When not to use

- Do not use to claim rankings, traffic, citations or search performance without source data and a defined measurement window.
- When the task belongs to another job, use its lead (`skill:seo-geo`) or the more appropriate tool instead.

## Inputs it needs

- The approved brief, audience, objective, channel and desired deliverable.
- Relevant source material and evidence; mark unsupported claims Unknown or `[needs source]`.

## How to run it

1. Confirm the task is in the approved studio scope and gather the inputs above.
2. Invoke the tool in Claude Code or Codex using the command/agent/server shown above.
3. Review its output against the source material; hand it to a separate reviewer.
4. For any post or scheduled item, keep it in draft until the founder approves publication.

```text
Use Agent tool: marketing-ai-citation-strategist for this approved 3RDWRONG task: {task}. Context and source material: {links/files}. Target audience: {audience}. Desired output: {deliverable}. Label evidence as Documented, Interpretation, Hypothesis or Unknown where relevant. Do not publish or schedule anything; return a reviewable draft and list open questions.
```

## What good output looks like

- Directly addresses the approved brief and names assumptions or missing evidence.
- Gives a usable, reviewable deliverable with source links where claims require support.

## Quality checks

- [ ] A reviewer other than the maker checks claims, fit and completeness.
- [ ] Client or personal information is excluded from the public repository.
- [ ] Publication or scheduling remains blocked until founder approval.

## Pairs with

- `skill:seo-geo` — receives the relevant draft, evidence or audit hand-off for its documented remit.

## Limits and cautions

- Capabilities and output depend on the tool’s source instructions and supplied inputs; do not infer undocumented features.
- Apply licence and installation/sign-in requirements for this distribution; availability does not prove a service is connected.
- Keep evidence labels distinct and separate maker from checker.
