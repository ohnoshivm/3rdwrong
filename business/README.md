---
title: Business engine
type: guide
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Business engine

How 3RDWRONG prices, proposes, contracts, invoices, stays tax-compliant, runs
its week, measures itself and works with collaborators. **Proposed** for
founder review; nothing here is approved policy until the founder approves it
through the [review queue](review-queue.md).

## The rule: public method, private numbers

Under [D-0021](../studio/decisions/0021-client-work-public-anonymised.md) (founder decision, 2026-10-23), client work in this repository is
public and anonymised. Methods, templates and calculators live here. Every
client name, person, contact, client file and every amount of money — rates,
prices, deal values, invoices, cash, targets in currency — lives in the
private **vault**: the folder named by the `THREEW_VAULT` environment variable,
default `~/3rdwrong-vault`, created by the [Delivery engine](../methods/lifecycle.md)'s [`3w vault init`](../bin/3w).

```text
$THREEW_VAULT/
  clients.yaml                  codename -> client identity (private)
  rates.yaml                    studio rates, overheads, margins, tax set-aside
  finance/reviews/YYYY-MM.md    monthly finance reviews
  reviews/weekly/YYYY-Www.md    Friday weekly reviews
  <codename>/
    contracts/                  signed MSA, SOW, NDA, change orders
    finance/                    estimate.yaml, investment sheet, invoices/
    files/                      client working files
    private-notes/              anything identifying
```

Public files refer to clients by codename only. Examples use the fictional
client Stillsoil Atelier and clearly fictional numbers without currency
symbols. The validator rejects rupee amounts outside reviewed `studio/`
hypotheses; treat that as a floor, not the boundary: no currency amount of
any kind enters the repository. See the [publication rules](../docs/public-private-boundary.md).

## Lifecycle coverage

The canonical client lifecycle is shared across the three engines.

| Stage | Owner engine | Business-engine material |
| --- | --- | --- |
| L0 Lead, L1 Qualify, L2 Discover & scope | Growth (client acquisition) | [Estimation guide](pricing/estimation-guide.md) starts in L2 |
| **L3 Propose** | Business | [Pricing method](pricing/README.md), [proposals](proposals.md), proposal bundle |
| **L4 Contract & deposit** | Business | [Legal templates](legal/README.md), SOW bundle, [deposit invoice](finance/invoicing-and-collections.md) |
| L5 Onboard & kickoff | Delivery | Collaborator onboarding in the [collaborator network](people/collaborator-network.md) |
| L6 Deliver (offer method) | Delivery | Milestone invoices, [change pricing](pricing/commercial-rules.md#change-pricing), change-order bundle |
| L7 Launch & handover | Delivery | Final invoice before final file release |
| L8 Care | Delivery | Care-plan pricing and recurring invoices |
| L9 Close-out & case study | Delivery | Project margin review in the [scorecard](scorecard.md); anonymised publication clause in [IP and licensing](legal/ip-and-licensing.md) |

Growth's L0–L2 detail lives in [client acquisition](client-acquisition.md) and
the [Growth engine](../growth/README.md); Delivery's backbone and L5–L8 detail live in
[engagement operations](engagement-operations.md) and the [Delivery engine](../methods/lifecycle.md).

## Map

| Area | Documents | Owning department ([D-0019](../studio/decisions/0019-organisation-and-loading-policy.md)) |
| --- | --- | --- |
| Pricing | [method](pricing/README.md), [estimation guide](pricing/estimation-guide.md), [commercial rules](pricing/commercial-rules.md), [rates and estimates format](pricing/rates-and-estimates.md), [scripts/pricing.py](../scripts/pricing.py) | Sales — pricing-deal-desk |
| Proposals | [proposals](proposals.md); bundles [proposal](../templates/bundles/proposal/), [sow](../templates/bundles/sow/), [change-order](../templates/bundles/change-order/) | Sales — proposals-pitches |
| Legal | [legal index](legal/README.md): MSA, mutual NDA, collaborator agreement, IP and licensing | Operations — finance-legal |
| Finance | [finance](finance/README.md), [invoicing and collections](finance/invoicing-and-collections.md), [Indian tax basics](finance/india-tax-basics.md); bundles [invoice](../templates/bundles/invoice/), [finance-review](../templates/bundles/finance-review/), [rates](../templates/bundles/rates/), [estimate](../templates/bundles/estimate/) | Operations — finance-legal |
| Rhythm and measurement | [operating rhythm](operating-rhythm.md), [scorecard](scorecard.md), [weekly-review](../templates/bundles/weekly-review/) bundle | Operations — planning-workflow |
| Governance | [review queue](review-queue.md), [scripts/review_queue.py](../scripts/review_queue.py) | Operations — knowledge-systems |
| People | [roles](people/README.md), [collaborator network](people/collaborator-network.md), [working agreements](people/working-agreements.md) | Operations — people-partners |
| Tools | [tooling](tooling.md) | Operations — planning-workflow |

The founder signs off every price, proposal, contract, change order and
payment decision. Departments are accountability structures, not headcount.

## Template bundles

Each bundle is a folder under `templates/bundles/<bundle>/` with a
`bundle.yaml` (`kind`, `description`, `template`, `target`, `variables` with
an `example` each) and one `.tmpl` file using `{{variable}}` placeholders.
Targets starting `{vault}/` render into the vault; all others render into the
repository and must stay anonymised. The [Delivery engine](../methods/lifecycle.md)'s [`3w new <bundle>`](../bin/3w)
renders them; [tests/test_bundles.py](../tests/test_bundles.py) checks that every bundle renders
cleanly with its examples.

## Related

- [Pricing hypotheses](../studio/pricing.md) — published ranges; owned by the studio release, not this engine.
- [Identity System offer](../studio/identity-system-offer.md) and [Brand Direction Sprint](../studio/brand-direction-sprint.md); the [Digital Experience offer](../studio/digital-experience-offer.md).
- [Founding blueprint commercial operating rules](../studio/archive/founding-blueprint-v1.0.md#commercial-operating-rules).
