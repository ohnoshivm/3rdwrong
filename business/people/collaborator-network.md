---
title: Collaborator network
type: method
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Collaborator network

**Proposed.** How the studio finds, tests, onboards, briefs, reviews, pays
and offboards freelance collaborators. Names, contacts, rates and
assessments live in the vault; the method lives here.

## Purpose

A small bench of trusted specialists who deliver at the studio's standard,
are paid fairly and on time, and never put client confidentiality at risk.

## When it applies

Whenever a project needs a skill or capacity the founder will not supply, and
at the quarterly bench review.

## Roles

Operations — people-partners runs sourcing, onboarding, payment and
offboarding. The relevant craft lead (Design, Engineering, Strategy, Media)
sets and judges the test task. The **founder** approves every new
collaborator, rate and access grant.

## Inputs

The role needed, project timeline, budget per role from the approved
estimate (vault), the [collaborator agreement](../legal/collaborator-agreement.md),
the mutual NDA if discussing a live project before the agreement.

## Steps

### 1. Sourcing

- Start with referrals from trusted collaborators and peers, then work you
  admire (award sites, studio credits, open-source contributions), then
  communities. Look for shipped work, not polished profiles.
- Keep a vault bench list: role, strengths, availability, rate, last
  project, notes.

### 2. Vetting with a paid test task

1. Review three pieces of shipped work; ask what exactly they did on each.
2. A 30-minute conversation: process, communication, how they handle
   feedback and deadlines.
3. **Paid test task:** a bounded, realistic brief from a fictional client
   (use Stillsoil Atelier), capped at a few hours, paid at their normal rate.
   Never use live client work as a test.
4. Judge against the brief's criteria: craft, thinking, communication,
   timeliness. Craft lead recommends; founder decides.

### 3. Onboarding checklist

- [ ] Collaborator agreement signed (and NDA if any earlier disclosure).
- [ ] Tax details collected in the vault (PAN, GSTIN if registered); TDS
      treatment confirmed with the CA.
- [ ] Rate and payment terms recorded in the vault.
- [ ] Working agreements shared and acknowledged.
- [ ] Accounts created with least privilege: project tools, the specific
      vault folders for their codenames only — never `rates.yaml`,
      `clients.yaml` or other clients' folders.
- [ ] Two-factor authentication on every studio account.
- [ ] Codename rule explained: client names never appear in public channels,
      commits, file names or AI tools that may retain them.
- [ ] Access register updated: who has access to what, granted when, by whom.

### 4. Briefing standard

Every piece of work starts with a written brief (Work Order) containing:
objective and the decision it supports; context and links; deliverables with
formats; acceptance criteria; constraints (identity rules, performance
budgets, accessibility); deadline and review points; hours or fee cap; who
answers questions and how fast. If a collaborator cannot restate the brief in
their own words, it is not ready.

### 5. Review standards

- Review against the brief's criteria, not taste alone; name what works,
  what fails, and why.
- Internal review before anything reaches the client. Collaborators do not
  send work to clients directly unless the brief says so.
- Use the studio's critique protocol and QA checklists for the craft.
- Record quality notes in the vault after each Work Order.

### 6. Payment process

1. Collaborator invoices against an accepted Work Order.
2. Operations checks it against the Work Order and the founder approves.
3. Pay within the agreement's term, regardless of client payment unless the
   agreement says otherwise; deduct TDS where required and issue the
   certificate.

### 7. Offboarding and access removal

On the last Work Order or on ending the agreement, the same week:

- [ ] Remove access to every tool, shared folder, repository and vault folder.
- [ ] Rotate any shared secret they could see.
- [ ] Receive written confirmation that client and studio material was
      returned or deleted.
- [ ] Settle final invoices.
- [ ] Update the access register and the bench notes.

## Outputs

Vault: bench list, signed agreements, access register, quality notes,
payment records.

## Quality gate

- [ ] No access before a signed agreement.
- [ ] Test tasks paid and fictional.
- [ ] Every Work Order has a written brief meeting the standard.
- [ ] Access register matches reality at the quarterly review.
- [ ] Offboarding completed within a week of the last Work Order.

## Metrics

Collaborator invoices paid on time; rework rate per collaborator; days from
need to signed collaborator; access-register discrepancies (target: none).

## Failure modes

- Hiring from a portfolio without a test and discovering the gap mid-project.
- Unpaid "test" work on a live brief.
- Access left open after a project ends.
- Vague briefs, then blaming the collaborator for misses.

## Related

[People and roles](README.md) · [Working agreements](working-agreements.md) ·
[Collaborator agreement](../legal/collaborator-agreement.md) ·
[IP and licensing guide](../legal/ip-and-licensing.md)
