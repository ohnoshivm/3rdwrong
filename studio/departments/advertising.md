---
title: Advertising department
type: guide
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Advertising department

Support studio paid demand and explicitly scoped client launch campaigns with paid media, creative and measurement.

Status: proposed registry routing. Source review does not establish live tool performance, licence clearance, runtime connectivity or founder approval.

63 tools; 12 lead, 19 specialist, 32 bench, 0 parked, 0 excluded; 31 active / 32 library.

## Sub-departments → jobs → leads

### paid-social

| Job | Lead(s) |
| --- | --- |
| `paid-social-planning` | `agency:paid-media-paid-social-strategist` |
| `audience-targeting` | `skill:audience-segment-builder` |
| `budget-bidding` | `skill:budget-optimizer` |

### search-programmatic

| Job | Lead(s) |
| --- | --- |
| `paid-search-planning` | `agency:paid-media-ppc-strategist` |
| `query-optimization` | `agency:paid-media-search-query-analyst` |
| `programmatic-buying` | `agency:paid-media-programmatic-buyer` |
| `shopping-feeds` | `skill:product-feed-optimizer` |

### ad-creative-measurement

| Job | Lead(s) |
| --- | --- |
| `ad-creative` | `agency:paid-media-creative-strategist` |
| `creative-testing` | `skill:ad-test-designer` |
| `conversion-tracking` | `agency:paid-media-tracking-specialist` |
| `attribution-reporting` | `skill:attribution-reconciler` |
| `account-audit` | `agency:paid-media-auditor` |

## Specialists with activation triggers

| Tool | Job | Trigger |
| --- | --- | --- |
| `agency-mcp:seo-audit` | `ad-creative-measurement/account-audit` | Use for the named audit, measurement, compliance, or reporting task when its evidence and data source are available. |
| `agency:marketing-growth-hacker` | `ad-creative-measurement/ad-creative` | Use for the named audit, measurement, compliance, or reporting task when its evidence and data source are available. |
| `agency:marketing-livestream-commerce-coach` | `ad-creative-measurement/ad-creative` | Use only when the studio’s own presence or a specifically approved campaign targets this platform, market, or commerce channel. |
| `skill:ab-testing` | `ad-creative-measurement/ad-creative` | Use for the named audit, measurement, compliance, or reporting task when its evidence and data source are available. |
| `skill:ad-account-auditor` | `ad-creative-measurement/account-audit` | Use for advertising/ad-creative-measurement/account-audit when the brief specifically requires: Use when auditing a paid ad account for incremental contribution, wasted spend, or measurement integrity before scaling; runs a typed 20-item ROAS profile with verified vetoes and a SHIP/FIX/BLOCK/UNDECIDED gate on own exported data . |
| `skill:ad-creative` | `ad-creative-measurement/ad-creative` | Use for advertising/ad-creative-measurement/ad-creative when the brief specifically requires: When the user wants to generate, iterate, or scale ad creative — headlines, descriptions, primary text, or full ad variations — for any paid advertising platform . |
| `skill:ad-creative-builder` | `ad-creative-measurement/ad-creative` | Use for advertising/ad-creative-measurement/ad-creative when the brief specifically requires: Use when the user asks to "write ad copy", "generate RSA headlines", or "build ad creative at volume"; produces ad units — RSA headlines/descriptions, hooks, and an angle matrix — message-matched to the destination landing page . |
| `skill:ads` | `ad-creative-measurement/ad-creative` | Use for advertising/ad-creative-measurement/ad-creative when the brief specifically requires: When the user wants help with paid advertising campaigns on Google Ads, Meta (Facebook/Instagram), LinkedIn, Twitter/X, or other ad platforms . |
| `skill:analytics` | `ad-creative-measurement/ad-creative` | Use for the named audit, measurement, compliance, or reporting task when its evidence and data source are available. |
| `skill:bid-strategy-planner` | `ad-creative-measurement/ad-creative` | Use for advertising/ad-creative-measurement/ad-creative when the brief specifically requires: Use when the user asks to "pick a bid strategy", "set a tCPA/tROAS target", or "plan the learning-phase entry"; produces a bid-strategy choice (tCPA / tROAS / max-conversions / manual CPC), the starting target math, a portfolio grouping map, and a learning-phase entry plan . |
| `skill:budget-pacing-monitor` | `ad-creative-measurement/ad-creative` | Use for advertising/ad-creative-measurement/ad-creative when the brief specifically requires: Use when the user asks to "check pacing", "am I over/under-spending", "is this campaign on track to hit budget", or "why did spend spike/stall mid-flight"; returns a spend-vs-target-curve read, learning-phase status, an over/under-delivery call, and a reallocation trigger . |
| `skill:campaign-planner` | `ad-creative-measurement/ad-creative` | Use for advertising/ad-creative-measurement/ad-creative when the brief specifically requires: Use when the user asks to "plan an influencer campaign", "build a campaign blueprint", "track or close a creator campaign", or "record a late campaign correction"; produces the plan and, when requested, a non-canonical evidence tracker with scoped identity, publication, reconciliation, close, and reopen receipts . |
| `skill:chatcut-ugc-ad-guide` | `ad-creative-measurement/ad-creative` | Use only when the studio explicitly accepts physical product ad-video work. |
| `skill:co-marketing` | `ad-creative-measurement/ad-creative` | Use only when the named content, channel, lifecycle, or campaign task is explicitly in the approved marketing scope. |
| `skill:conversion-signal-qa` | `ad-creative-measurement/ad-creative` | Use for advertising/ad-creative-measurement/ad-creative when the brief specifically requires: Use when the user asks to "QA my conversion tracking before launch", "check my UTMs / pixel / event firing", "set up a tracking pre-flight", or "set the dedup rule so Meta and Google stop double-counting"; builds and fixes the measurement plumbing — conversion-event firing, UTM hygiene, cross-platform dedup rules, attribution-window alignment, and offline/iOS-ATT modeled-gap flags — as a pre-flight checklist plus a UTM/event-spec builder . |
| `skill:conversion-value-mapper` | `ad-creative-measurement/ad-creative` | Use for advertising/ad-creative-measurement/ad-creative when the brief specifically requires: Use when the user asks to "set up conversion values so tROAS optimizes profit not orders", "map margin onto my purchase value", "build value rules for lead / phone / signup conversions", or "stop bidding to revenue when I care about profit"; defines and QAs the conversion VALUE model — per-conversion values, margin/net-value adjustment, static-vs-dynamic value rules, proxy values for non-revenue actions, and a value-vs-count sanity check — as a value-model spec plus a pre-launch value QA sheet . |
| `skill:paid-measurement-loop` | `ad-creative-measurement/attribution-reporting` | Use for advertising/ad-creative-measurement/attribution-reporting when the brief specifically requires: Use when the user asks to "read back" a paid campaign change, "did this ad change work", or "compare ROAS/CPA before and after"; reads ROAS/CPA against a control over a fixed readback window and returns a Promote / Keep-testing / Rollback / Unproven readback decision with the math delegated to roi-calculator . |
| `skill:placement-exclusion-manager` | `ad-creative-measurement/ad-creative` | Use for advertising/ad-creative-measurement/ad-creative when the brief specifically requires: Use when the user asks to "build my brand-safety exclusion lists", "set placement / topic / content exclusions before launch", "add network and audience exclusions", or "prep the A1 brand-safety evidence for the auditor"; produces a placement/network exclusion list, a content-suitability & sensitive-topic block list, an audience/negative-audience exclusion set, and a packaged A1 brand/placement-safety evidence file for the gate . |
| `skill:platform-norm-profiler` | `ad-creative-measurement/ad-creative` | Use for the named audit, measurement, compliance, or reporting task when its evidence and data source are available. |

## Bench and parked summary

- **bench: 32.** `agency-mcp:client-audit`, `agency-mcp:client-report`, `agency-mcp:google-ads-manager`, `agency-mcp:meta-ads-manager`, `agency-mcp:weekly-review`, `agency:healthcare-marketing-compliance`, `anthropic-skills:marketing-studio-director`, `juicylucy-ads:ad-naming`, `juicylucy-ads:ad-platform`, `juicylucy-ads:captions-overlay`, `juicylucy-ads:cut-the-curve`, `juicylucy-ads:juicy-cli`, `juicylucy-ads:juicylucy`, `juicylucy-ads:juicylucy-setup`, `juicylucy-ads:motion-doctrine`, `juicylucy-ads:oversized-cursor`, `juicylucy-ads:seam-craft`, `juicylucy-ads:static-ad-production`, `juicylucy-ads:static-copywriting`, `juicylucy-ads:static-formats`, `juicylucy-ads:static-image-craft`, `juicylucy-ads:static-localization`, `juicylucy-ads:static-winner-analysis`, `juicylucy-ads:video-ad-production`, `skill:ai-ugc-marketing`, `skill:attribution`, `skill:campaign-architect`, `skill:content-amplifier`, `skill:fatigue-frequency-manager`, `skill:landing-experience-checker`, `skill:roi-calculator`, `skill:short-video-scripter`
- **parked: 0.** None.
- **excluded: 0.** None.

Individual reasons and activation requirements are in the [canonical registry](../../toolkit/sources/registry.json). Library means callable by explicit name after review; it is not loaded by default.

## Gaps

No lead coverage gaps.

## Counts by sub-department and role

| Sub-department | Lead | Specialist | Bench | Parked | Excluded | Active | Library | Total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| paid-social | 3 | 0 | 2 | 0 | 0 | 3 | 2 | 5 |
| search-programmatic | 4 | 0 | 2 | 0 | 0 | 4 | 2 | 6 |
| ad-creative-measurement | 5 | 19 | 28 | 0 | 0 | 24 | 28 | 52 |

## Operating contract

Use the job lead first and a specialist only on its trigger. Maker and checker must be separate people/agent instances; a reviewer never approves its own department alone. Proposed `load: active` is the desired loading policy, while the source inventory records installation presence. No physical activation was performed.

Design and Engineering prototype together early; the handoff names artefacts, constraints, budgets and evidence rather than creating a wall. Human judgement and founder approval remain separate from tool routing.
