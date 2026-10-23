---
title: Publication rules
type: policy
status: approved
owner: founder
last_reviewed: 2026-10-23
approved_by: founder
approved_on: 2026-10-23
approval_source: founder instruction, 2026-10-22; revised by founder decision D-0021, 2026-10-23
---

# Publication rules

Everything committed to `ohnoshivm/3rdwrong` is public and open source under the applicable [licences](../LICENSING.md). The founder approved publishing the full knowledge base, including the founding blueprint, pricing hypotheses, project economics, payment structure, launch budget, hours assumption and critical self-review. See [D-0017](../studio/decisions/0017-fully-open-repository.md).

Client work is public **and anonymised**: project records live here under codenames, and everything confidential lives in a private vault outside the repository. See [D-0021](../studio/decisions/0021-client-work-public-anonymised.md).

Prospects and competitors can read and reuse this material under its licence. Publication can be irreversible: deleting a file or rewriting history cannot recall forks, downloads or cached copies. Publication approval does not validate a hypothesis or adopt every recommendation in the blueprint.

## Revision note

**2026-10-23, D-0021.** The founder chose the non-public store that this policy previously left open: a local vault outside any git work tree. This revision adds anonymised project records, project clearance, the vault structure, the anonymity guard and vault backup. The rules on personal data, interviews and publishing checks are unchanged.

## What must never be committed

- Personal data of clients or interviewees, including names, contact details, identifying notes and combinations that could identify a person. Account for India's Digital Personal Data Protection Act, 2023.
- Client identities: real client names, aliases, domains, people, emails and phone numbers. Use the codename.
- Money in client work: fees, quotes, invoices, budgets, payment terms and amounts in any currency. Studio pricing hypotheses follow D-0017 and stay in `studio/`.
- Third-party contracts, proposals sent to clients, confidential briefs and NDA-bound assets or information.
- Credentials, passwords, API tokens, private keys, staging URLs and unnecessary identification numbers (PAN, GSTIN, IFSC, Aadhaar).
- Client working files or unreleased assets that the studio does not own or have permission to publish, and any non-text file inside a project record.

The founder's permission to publish studio knowledge does not grant rights over other people's information or work. Sanitised, non-identifying and rights-cleared learning may enter the knowledge base after review.

## Client project records

| Material | Where it lives |
| --- | --- |
| Anonymised brief, gate log, decisions, status, risks, feedback, QA results, handover record and retrospective of a **cleared** project | `projects/<codename>/` in this repository |
| The whole workspace of a **private** project | `<vault>/<codename>/` |
| Codename-to-client mapping, people, contacts, domains | `<vault>/clients.yaml` |
| Contracts, signed scopes, proposals as sent, NDAs | `<vault>/<codename>/contracts/` |
| Quotes, invoices, payments, rates | `<vault>/<codename>/finance/` (the Business engine documents `rates.yaml` in the vault root) |
| Raw client files, screenshots, proofs, recordings, exports | `<vault>/<codename>/files/` |
| Meeting notes with names, credentials notes, sensitive context | `<vault>/<codename>/private-notes/` |
| Credentials themselves | An approved password manager; the vault records only where they are |

**Cleared** means the signed contract permits anonymised publication of project records. Record the clearance in the project README and the decision log at L4 Contract & deposit. Without it, run `bin/3w new <bundle> --private`; the whole workspace stays in the vault. A client may withdraw clearance: move the workspace to the vault and remove the public folder. Clearance never covers a named case study; that needs separate written permission.

**Codenames** are two neutral lowercase words joined by a hyphen, such as `quiet-harbour`. They must not hint at the client's name, sector, place or product. `bin/3w new` generates one when none is given.

**Anonymise combinations, not just names.** Describe the sector in general terms. Avoid combining city, founding year, niche, launch dates, public events or distinctive facts that would identify the client together. Record approvers by role or code (`C1`, founder). Refer to confidential evidence by vault filename, never by content or URL.

## The vault

The vault is the studio's non-public store. Its path is the `THREEW_VAULT` environment variable, defaulting to `~/3rdwrong-vault`. It must not be inside any git work tree, a public sync folder or this repository; `bin/3w` refuses to use such a path. Create it with `bin/3w vault init`, which sets owner-only permissions and writes an empty `clients.yaml` documenting its structure:

```yaml
clients:
  quiet-harbour:
    name: Registered legal or trading name
    aliases: [Short name, Product brand]
    people:
      - name: Full name
        role: Decision-maker
        email: person@client-domain
        phone: "+91 ..."
    emails: [shared inboxes]
    domains: [client-domain]
    phones: [switchboard numbers]
```

Access is founder-only by default. Share a single project's folder with a collaborator only for the duration of their work, through a client-approved secure location, and record the access and its removal in the project's private notes.

**Retention and deletion.** Keep contracts and finance records for as long as Indian tax and company law requires; take professional advice on the exact periods. Delete raw client files and personal data when the purpose ends or the client asks, unless the law requires retention, and note the deletion date in `private-notes/`.

**Backup.** Back up the vault with Time Machine on an encrypted backup disk, plus an encrypted off-site copy, for example an encrypted disk image or encrypted archive in a cloud store the founder controls. Keep the encryption passphrase in the password manager, not in the vault. Test a restore of one project folder every quarter and record the date in the vault README.

## Anonymity guard

`scripts/oscheck/anonymity.py` enforces this policy mechanically. A guard pass is necessary, not sufficient: a human still reviews every project commit for identifying combinations.

- **In CI** the validator runs generic checks over the operating-record path `projects/`: email addresses (except studio and reserved example domains), phone numbers, currency amounts (₹, Rs, INR, $, €, £ and suffix forms such as lakh or crore), GSTIN, PAN, IFSC, 12-digit Aadhaar-like numbers, and any file that is not `.md`, `.yaml`, `.yml` or `.json`.
- **Locally**, `bin/3w check` adds a deny-list from the vault's `clients.yaml` and blocks every name, alias, person, domain, email and phone it lists, in any tracked or untracked file in the repository. Findings name the vault field, never the term.
- **Before commit**, `bin/3w hooks install` adds a local pre-commit hook that runs the guard on staged files. Hooks are local and never committed; install it on every machine that commits.

## Where excluded material goes

Use the vault for client material and interview data. Do not use this public GitHub repository, its branches, issues, pull requests or attachments as a store. A folder name, opaque identifier or unmerged branch does not make data non-public. Credentials belong in an approved secret manager.

Public references to non-public records use codenames or opaque identifiers only, such as `quiet-harbour` or `interview-042`, without copying identifying content here.

## Interview notes and research evidence

Keep one record per interview in the vault. Name it with an anonymised identifier such as `interview-042.md`, never a person's name or identifying detail. Record whether consent was obtained and what it covers; keep the identity mapping and consent records out of this repository. An anonymised filename alone does not anonymise the contents.

Before anything derived from interviews enters this repository, aggregate findings across interviews, remove identifying combinations, and record the date, sample size and limits. Do not publish raw notes, personal data or attributable quotations. Permission and any NDA or third-party rights must be checked before publishing a derivative; written consent does not remove the repository's prohibition on personal data.

## Before publishing

1. Check that names, images, quotations, assets and results are cleared for the specific public use, and that the project is cleared.
2. Check whether the content, metadata or combined details could identify a person, a client or protected material.
3. Confirm sources, evidence labels and document status; price ranges remain unvalidated hypotheses.
4. Follow the applicable licence and retain third-party notices.
5. Run `bin/3w check` (validator, secret and personal-data scans, anonymity guard with the vault deny-list) and review every finding.

If clearance is uncertain, keep the material in the vault until resolved. A `privacy-review` label requests attention; it does not grant publication permission.
