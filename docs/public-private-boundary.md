---
title: Publication rules
type: policy
status: approved
owner: founder
last_reviewed: 2026-10-22
approved_by: founder
approved_on: 2026-10-22
approval_source: founder instruction, 2026-10-22
---

# Publication rules

Everything committed to `ohnoshivm/3rdwrong` is public and open source under the applicable [licences](../LICENSING.md). The founder approved publishing the full knowledge base, including the founding blueprint, pricing hypotheses, project economics, payment structure, launch budget, hours assumption and critical self-review. See [D-0017](../studio/decisions/0017-fully-open-repository.md).

Prospects and competitors can read and reuse this material under its licence. Publication can be irreversible: deleting a file or rewriting history cannot recall forks, downloads or cached copies. Publication approval does not validate a hypothesis or adopt every recommendation in the blueprint.

## What must never be committed

- Personal data of clients or interviewees, including names, contact details, identifying notes and combinations that could identify a person. Account for India's Digital Personal Data Protection Act, 2023.
- Third-party contracts, confidential proposals and NDA-bound assets or information.
- Credentials, passwords, API tokens, private keys and unnecessary identification numbers.
- Client working files or unreleased assets that the studio does not own or have permission to publish.

The founder's permission to publish studio knowledge does not grant rights over other people's information or work. Sanitised, non-identifying and rights-cleared learning may enter the knowledge base after review.

## Where excluded material goes

Before the first client or interview data exists, the founder must choose a non-public store with appropriate access, retention, consent and deletion controls. Do not use this public GitHub repository, its branches, issues, pull requests or attachments as that store. A folder name, opaque identifier or unmerged branch does not make data non-public. Credentials belong in an approved secret manager.

No particular store has been chosen yet. Record the choice and access rules before collecting data. Public references to non-public records use opaque identifiers only, such as `project-042`, without copying identifying content here.

## Interview notes and research evidence

Keep one record per interview in the chosen non-public store. Name it with an anonymised identifier such as `interview-042.md`, never a person's name or identifying detail. Record whether consent was obtained and what it covers; keep the identity mapping and consent records out of this repository. An anonymised filename alone does not anonymise the contents.

Before anything derived from interviews enters this repository, aggregate findings across interviews, remove identifying combinations, and record the date, sample size and limits. Do not publish raw notes, personal data or attributable quotations. Permission and any NDA or third-party rights must be checked before publishing a derivative; written consent does not remove the repository's prohibition on personal data.

## Before publishing

1. Check that names, images, quotations, assets and results are cleared for the specific public use.
2. Check whether the content, metadata or combined details could identify a person or reveal protected material.
3. Confirm sources, evidence labels and document status; price ranges remain unvalidated hypotheses.
4. Follow the applicable licence and retain third-party notices.
5. Run the validator's secret and personal-data scans, and review their findings.

If clearance is uncertain, keep the material in the chosen non-public store until resolved. A `privacy-review` label requests attention; it does not grant publication permission.
