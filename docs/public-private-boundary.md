---
title: Public and private boundary
type: guide
status: proposed
owner: founder
last_reviewed: 2026-10-22
---

# Public and private boundary

This repository is public. If material cannot be clearly cleared for public release, keep it out of Git and ask the founder before publishing a derivative.

## Classification

| Classification | Examples | Handling |
| --- | --- | --- |
| Public | General methods, approved public strategy, cited public research, sanitised lessons. | Store in this repository with evidence, status, and privacy review. |
| Private | Client names, proposals, contracts, budgets, pricing hypotheses and price ranges, working files, unreleased assets, confidential research, identifying project notes. | Keep in the private repository with access limited to people who need it. |
| Never stored in Git | Passwords, API tokens, private keys, personal identification numbers, unnecessary personal data, credentials embedded in files or history. | Use an approved secret manager or secure transfer channel; do not add it to public or private Git history. |

The following material from the founder's source report stays private and must not be copied or paraphrased into the public repository:

- Project economics, costs, contribution, and founder-hour figures.
- Payment percentages and contract specifics.
- Pricing hypotheses and price ranges, including unvalidated test ranges.
- The internal 90-day budget allowance and weekly-hours assumption.
- The founder's critical review text.
- The current trademark-clearance status; public documents may state only that clearance is a required step.

The original source is Founding Blueprint v1.0, 22 October 2026 (private archive). In this workspace its local staging folder is `../3rdwrongs-private/`, a sibling of this repository and never a directory inside it, until the private GitHub repository exists.

## Before publishing

Ask:

1. Is every name, image, quotation, and result cleared for this public use in writing?
2. Can a person or client be identified from the material, metadata, or combination of details?
3. Does the claim have a source, and is its evidence label accurate?
4. Does publication reveal a contract, price, margin, proposal, unreleased asset, or private research?
5. Would a generalised explanation preserve the learning without exposing the source material?

If an answer is uncertain, do not add the material. A `privacy-review` label requests extra attention; it is not permission to publish.

## Future private repository

A separate private repository called `3rdwrongs-private` holds material that is not cleared for public release. Create folders only when first needed. Its structure is:

```text
clients/
contracts/
finance/
proposals/
research-confidential/
assets-unreleased/
pricing/
archive/
```

Sensitive files do not become safe merely because a repository is private.

## References from public documents

Public documents may refer to private material by an opaque identifier only, such as `project-042`. Never copy private content, quotes, assets, client names, or identifying detail into the public repository. Do not publish client names or assets without written permission that covers the specific publication.
