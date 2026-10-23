---
title: Contracts and legal
type: guide
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 180
---

# Contracts and legal

**Template, not legal advice — have a qualified lawyer in India review before use.**

**Proposed.** Which agreement to use when, how to sign and file it, and the
Indian legal context the templates assume. Party names and signed copies live
in the vault under `<codename>/contracts/`; this repository holds unsigned
templates only.

## Purpose

Give every engagement and collaboration a written basis before work starts,
so that scope, payment, ownership and confidentiality are settled when
relationships are good rather than argued when they are not.

## When it applies

| Situation | Document | Lifecycle |
| --- | --- | --- |
| Sharing confidential information before a deal | [Mutual NDA](mutual-nda.md) | L1–L2 |
| A client engagement | [Master services agreement](master-services-agreement.md) + SOW ([bundle](../../templates/bundles/sow/)) | L4 |
| A scope change | Change order ([bundle](../../templates/bundles/change-order/)) | L6–L8 |
| Any collaborator doing client or studio work | [Collaborator agreement](collaborator-agreement.md) + brief | Before access to any client material |
| Ownership, licences, fonts, stock, AI, open source, portfolio | [IP and licensing guide](ip-and-licensing.md) | L3 onwards |

## Roles

Operations — finance-legal prepares documents and keeps the register of
signed agreements in the vault. Sales — proposals-pitches sends client
documents with the SOW. Operations — people-partners sends collaborator
documents. The **founder** signs every agreement; nobody else commits the
studio. A qualified lawyer in India reviews each template once before first
use and again when the law or the studio's model changes.

## Inputs

The accepted proposal option, the client's or collaborator's legal details
(vault), any client paper they ask the studio to sign instead.

## Steps

1. Choose the document from the table above. If the client sends its own
   paper, compare it with the MSA clause by clause and flag differences on
   payment, IP transfer timing, liability, portfolio rights and termination
   to the founder before signing.
2. Fill the `{{placeholders}}` in a vault copy, never in the repository.
3. Sign electronically where both parties agree. The Information Technology
   Act, 2000 recognises electronic records and electronic signatures, with
   listed exceptions ([India Code](https://www.indiacode.nic.in/)).
4. Pay stamp duty where the state stamp law requires it (e-stamping is
   available in many states); an insufficiently stamped agreement may not be
   admissible in evidence until duty and penalty are paid. Ask the lawyer
   which instruments and which state apply.
5. File the signed PDF in `<codename>/contracts/` and add it to the vault
   register: document, version, parties (vault only), date, term, renewal or
   expiry date.
6. Diary every expiry, renewal and notice date in the operating rhythm.

## Indian legal context

The templates are drafted against these laws. Read the current text on
[India Code](https://www.indiacode.nic.in/) and confirm with a lawyer.

- **Indian Contract Act, 1872** — a valid contract needs free consent,
  lawful consideration and object (section 10). Agreements in restraint of
  a lawful trade are void except as the Act allows (section 27), so
  post-termination non-compete clauses are generally unenforceable in India;
  the templates use narrow non-solicitation during the term instead. Agreed
  damages for breach are capped at reasonable compensation up to the named
  amount (section 74).
- **Copyright Act, 1957** — the author is the first owner unless an
  exception applies, such as work made under a contract of employment
  (section 17). A commissioned independent contractor, including a
  collaborator, keeps copyright unless it is assigned. An assignment must be
  in writing signed by the assignor and identify the work, rights, duration
  and territory (section 19); if duration is not stated it is deemed five
  years, and if territory is not stated it is presumed to be India. State
  "worldwide" and "for the full term of copyright" expressly. Authors' moral
  rights (section 57) survive assignment. See the
  [Copyright Office](https://copyright.gov.in/).
- **Arbitration and Conciliation Act, 1996** — governs domestic and
  international arbitration seated in India. Choose a seat (a city), the
  number of arbitrators, the language and, optionally, an institution such as
  the Mumbai Centre for International Arbitration or the India International
  Arbitration Centre.
- **Commercial Courts Act, 2015** — commercial disputes above the specified
  value require pre-institution mediation unless urgent interim relief is
  sought (section 12A). Check whether the studio's disputes would reach the
  specified value.
- **Micro, Small and Medium Enterprises Development Act, 2006** — if the
  studio is registered as a micro or small enterprise (Udyam), buyers in
  India must pay within the agreed period, which may not exceed the
  statutory maximum, or owe compound interest at the statutory rate
  (sections 15–16). Confirm registration and its effect with the chartered
  accountant; see [Udyam registration](https://udyamregistration.gov.in/).
- **Digital Personal Data Protection Act, 2023** — when the studio processes
  personal data for a client it usually acts as a data processor under the
  client's instructions. The MSA includes a data clause; check the current
  status of the Act's rules before relying on it.
- **Trade Marks Act, 1999** — copyright in a logo is not trade-mark
  protection. Clearance and registration are the client's responsibility
  unless separately scoped; see the
  [Trade Marks Registry](https://ipindia.gov.in/).

## Cross-border clients

- **Governing law and forum.** Prefer Indian law with arbitration seated in
  India. If a client insists on its own law, keep arbitration rather than
  foreign courts: India is party to the New York Convention, so foreign
  awards from reciprocating countries are generally enforceable, whereas a
  foreign court judgment is directly executable in India only if it comes
  from a reciprocating territory notified under section 44A of the Code of
  Civil Procedure, 1908.
- **Currency and payment.** Invoice in the agreed currency; receive through
  banking channels so the bank can issue an inward-remittance advice. See
  [Indian tax basics](../finance/india-tax-basics.md) for export of services,
  LUT and remittance documents.
- **Withholding abroad.** Some countries withhold tax on service payments.
  Ask the chartered accountant whether a tax treaty (DTAA) relief or a tax
  residency certificate reduces it before signing.
- **Data.** Clients in the EU or UK may require a data processing agreement
  under their law. Agree it before receiving personal data.
- **IP assignment.** Keep the written, signed assignment language even under
  foreign law; it satisfies section 19 and most other systems.

## Outputs

Signed agreements and the register in the vault; nothing client-specific in
the repository.

## Quality gate

- [ ] The right document for the situation, current template version.
- [ ] Lawyer review of the template recorded (date, reviewer, version) in the vault.
- [ ] Placeholders filled in the vault copy only.
- [ ] Stamp duty checked; signatures complete; filed and registered in the vault.
- [ ] Expiry and notice dates in the calendar.

## Metrics

Share of engagements with a signed MSA and SOW before kickoff (target: all);
share of collaborators with a signed agreement before access (target: all).

## Failure modes

- Starting on an email "go ahead"; no assignment, no payment terms.
- Signing client paper that transfers IP before payment or bans portfolio use without noticing.
- An assignment silent on duration and territory, defaulting to five years and India.
- Collaborators never assigning their copyright, so the studio cannot assign it onwards.

## Related

[Proposals](../proposals.md) · [Invoicing and collections](../finance/invoicing-and-collections.md) ·
[Collaborator network](../people/collaborator-network.md) ·
[Publication rules](../../docs/public-private-boundary.md)
