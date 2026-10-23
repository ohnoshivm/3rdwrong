---
title: Tooling principles and proposed stack
type: guide
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---
# Tooling principles and proposed stack

**Status: proposed.** This is a set of candidate roles, not a current software
inventory, procurement commitment or product comparison. Product plans,
licences, compatibility and pricing are intentionally not stated; verify them
with official sources before relying on a tool.

## Candidate stack

| Tool or capability | Proposed role | Adoption stance |
| --- | --- | --- |
| Affinity | Core graphic design work | Adopt now if current licence and file workflow meet the work. |
| Figma | Shared interface or collaborative layout work | Use an entry plan only if needed; check current plan and licence first. |
| Obsidian / Markdown | Working notes and reusable knowledge | Adopt now; this repository is the canonical public method library. |
| Are.na | Selective reference collection | Use selectively; preserve source, context and permission boundaries. |
| Existing Claude / GPT access | Research and drafting assistance | Reuse existing access; human judgement owns strategy and approval. |
| GitHub | Versioned methods, skills and code | Reuse the current repository and its publication rules. |
| p5.js | Small creative-coding studies | High-leverage candidate when a concept needs a generative prototype. |
| Motion Canvas | Motion-system experiments | Experiment only for a defined motion question. |
| Blender | Specialist 3D | Later, when a real project need and competence justify it. |
| Style Dictionary | Token transformation | Later, when repeated delivery needs demonstrate the value of automation. |
| Playwright and axe-core | Digital-work checks | Use when delivering digital work and when project scope requires them. |

The names above are candidate tools from the blueprint, not claims that each
is installed, licensed, current, suitable or necessary. Check official
documentation, product terms and file compatibility before use. See
*Founding Blueprint v1.0, 22 October 2026 ([founding source archive](../studio/archive/founding-blueprint-v1.0.md))* for the source
list; this document intentionally omits current prices and plan details.

## Business engine capabilities

The [business engine](README.md) needs capabilities, not particular
products. None is chosen yet; apply the adoption test below and record the
choice in the vault, not here.

| Capability | Role in the engine | Requirement |
| --- | --- | --- |
| Private vault | Clients, contracts, rates, estimates, invoices, reviews ([D-0021](../studio/decisions/0021-client-work-public-anonymised.md)) | Outside this repository; encrypted at rest and backed up; created by the [Delivery engine](../methods/lifecycle.md)'s [`3w vault init`](../bin/3w) |
| [scripts/pricing.py](../scripts/pricing.py) | Prices vault estimates against vault rates | In this repository; prints only, never writes files |
| [scripts/review_queue.py](../scripts/review_queue.py) | Ranked founder review queue | In this repository; reads frontmatter only |
| Accounting and invoicing tool | Formal GST invoices, books, receivables | Supports the invoice must-haves in [Indian tax basics](finance/india-tax-basics.md); export for the chartered accountant |
| Separate bank accounts | Operating, tax and reserve | See [finance](finance/README.md) |
| Electronic signature | MSA, SOW, NDA, collaborator agreements | Audit trail; valid under the Information Technology Act, 2000 for the document type |
| Password manager | Shared credentials, collaborator access | Per-person accounts; supports revocation at offboarding |
| Time records | Hours by project, stage and role | Feeds margin, utilisation and estimate accuracy in the [scorecard](scorecard.md) |
| Calendar | Operating rhythm, invoice and tax dates | Shared with collaborators only for their projects |

Keep money, client identities and credentials out of every public tool,
including this repository's issues and pull requests.

## Do not install immediately

- Proprietary generative platforms before a repeat client problem requires
  their capabilities.
- A new AI-routing or model-management system while existing access is enough.
- Complex motion, 3D or rendering dependencies before a concept needs them.
- Token or documentation tooling before the same manual transformation
  recurs and creates measurable error or effort.
- Multiple overlapping note, asset-library or project-management systems.

## Adoption test

Buy or add a capability only after identifying a real bottleneck. Record the
task, repeated failure or delay, current workaround, licence and data risks,
expected improvement, owner and review date. Prefer the smallest reversible
experiment; remove tools that add overhead without improving a client-facing
decision or reducing repeated work.
