---
id: D-0008
title: Public and private repository architecture
type: decision
status: superseded
superseded_by: D-0017
date: 2026-10-22
owner: founder
last_reviewed: 2026-10-22
approved_by: founder
approved_on: 2026-10-22
approval_source: founding brief, 2026-10-22
---
# D-0008: Public and private repository architecture

## Decision

Historical decision (superseded): maintain a public repository for reusable methods, templates, skills and approved public-safe studio knowledge, and a separate private repository for client work and confidential material. Client files, personal data, secrets, internal margins and contracts do not belong in the public repository.

## Status

Superseded by [D-0017](0017-fully-open-repository.md), approved by the founder on 2026-10-22. The text below records the previous two-repo architecture as history and must not be followed as current policy.

## Rationale

The founding brief mandates a public GitHub repository and prohibits confidential and client material in it. A separate private home gives client work an explicit boundary.

## Alternatives considered

Store client projects alongside public methods; publish anonymised material without checking re-identification risk; rely on folder names inside one public repository.

## Evidence

Documented: founding brief, 2026-10-22; shared contract, 2026-10-22. See [publication rules](../../docs/public-private-boundary.md).

## Consequences

Historical consequence (superseded): create the private client-work repository when the first client signs. The current rule instead requires choosing a non-public store before any client or interview data exists. Apply file-sharing hygiene and permission checks before public case-study use.

## Revision triggers

Review if repository access, data protection needs or the publication model changes. Any exception requires an explicit founder decision and a safety review.
