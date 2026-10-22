---
id: D-0017
title: Fully open repository
type: decision
status: approved
date: 2026-10-22
owner: founder
last_reviewed: 2026-10-22
approved_by: founder
approved_on: 2026-10-22
approval_source: founder instruction, 2026-10-22
---

# D-0017: Fully open repository

## Decision

Everything in the 3RDWRONG knowledge base is public and open source under the applicable licences. Publish the full founding blueprint, pricing hypotheses, economics, payment structure, launch budget, founder-hours assumption and critical founder's review. Retire `3rdwrongs-private` and merge its knowledge into this repository. This decision supersedes [D-0008](0008-public-private-repository-boundary.md).

## Status

Approved by the founder on 2026-10-22 after being told what the content includes and that publication can be irreversible. This approves publication; hypotheses remain hypotheses and the blueprint remains a reference superseded wherever later decisions differ.

## Rationale

The founder chose a fully open knowledge base so the studio's thinking, assumptions and learning can be inspected and reused. One canonical repository removes the two-repo staging boundary.

## Alternatives considered

- **Two-repo boundary:** retain public methods and a separate restricted archive. This limits exposure but fragments retrieval and maintenance; the founder rejected it.
- **Open safe parts plus a private vault:** publish selected derivatives while keeping commercial assumptions and self-review non-public. This preserves discretion but leaves an incomplete public account and an ongoing classification burden; the founder rejected it.
- **Fully open knowledge base:** prices, project economics, payment structure, budget, hours assumptions and self-review are visible to prospects and competitors. They may be misunderstood, influence negotiations or be copied. Once public, forks, downloads and caches may persist even after deletion. The founder was told these trade-offs and explicitly chose publication.

## Evidence

**Documented** — Founder instruction, 2026-10-22: merge all four source files' knowledge, publish the full blueprint and pricing hypotheses, retire the restricted archive, and record approval after disclosure of content and irreversibility. This is an approval record, not evidence that pricing or market assumptions have been validated. The [founding blueprint](../archive/founding-blueprint-v1.0.md) is partly AI-researched.

## Consequences

Follow the [publication rules](../../docs/public-private-boundary.md). Personal data of clients and interviewees (including obligations under India's Digital Personal Data Protection Act, 2023), third-party contracts, credentials and NDA-bound assets must never be committed. The founder cannot open-source other people's rights or confidentiality obligations.

Before the first client or interview data exists, choose a non-public store with suitable access, consent, retention and deletion controls. It must not be this public GitHub repository, its branches, issues or attachments. Use anonymised interview identifiers and publish only non-identifying, aggregated, rights-cleared findings. Keep secret and personal-data scanning enabled across the repository, including upstream agents.

The previous two-repo architecture survives only as superseded history. Licensing distinguishes original writing, code, upstream agents and rights excluded from the studio's grant.

## Revision triggers

Review if legal obligations, third-party rights, re-identification risk or operating needs change, or if the founder requests a different publication model. Review before collecting the first client or interview data. A future restriction cannot recall already-public copies; record any revision explicitly rather than promising reversibility.
