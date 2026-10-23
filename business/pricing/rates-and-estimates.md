---
title: Rates and estimates format
type: guide
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 180
---

# Rates and estimates format

**Proposed.** The file formats read by [scripts/pricing.py](../../scripts/pricing.py). Both files live
in the vault and never in this repository. Render starting points from the
[rates](../../templates/bundles/rates/) and [estimate](../../templates/bundles/estimate/)
bundles.

## Purpose

Keep the studio's numbers in one private, versionable place so that every
estimate is priced against the same rates and assumptions.

## When it applies

Rates: set once, reviewed quarterly in the strategy and offer review. Estimate:
one per opportunity, change order or care plan.

## Roles

Operations — finance-legal maintains `rates.yaml`; the **founder** approves
every change. The pricing lead (Sales) owns each estimate.

## Inputs

Collaborator fees, the founder's target pay, studio overheads, the target and
floor margins, the tax set-aside agreed with the chartered accountant.

## Steps

1. Render the rates bundle to `$THREEW_VAULT/rates.yaml` and replace every
   zero.
2. Render one estimate per opportunity to
   `$THREEW_VAULT/<codename>/finance/estimate.yaml`.
3. Run [`uv run python scripts/pricing.py <estimate>`](../../scripts/pricing.py); add `--rates PATH` to
   test alternative rates. The script prints to standard output only and
   warns if either file sits inside the repository.

### `rates.yaml`

| Key | Meaning |
| --- | --- |
| `currency_label` | Text printed with amounts. |
| `roles.<role>.cost_per_hour` | What an hour costs the studio: collaborator fee or founder target pay. |
| `roles.<role>.rate_per_hour` | Standard sell rate, used as the rate-card cross-check. |
| `roles.<role>.external` | `true` if paid in cash to a collaborator (drives the cash check). |
| `overhead_rate` | Overheads (tools, space, insurance, accounting) as a share of labour cost. |
| `expense_markup` | Handling markup on pass-through expenses. |
| `target_margin` | Gross margin for a GO. |
| `floor_margin` | Below this, NO-GO; between floor and target, REVIEW. |
| `tax_set_aside` | Share of each receipt moved to the tax account. |
| `rounding` | Derived prices round up to this step. |
| `payment_schedule` | Default milestones as `{milestone, share}`; shares sum to 1. |

### `estimate.yaml`

| Key | Meaning |
| --- | --- |
| `codename`, `offer` | Identification; codename only. |
| `risk_buffer` | Share of hours added for uncertainty ([estimation guide](estimation-guide.md)). |
| `stages` | Mapping of stage to `{role: hours}`. |
| `expenses` | List of `{item, cost, only?}`; `only` limits an item to named options. |
| `options` | List of `{name, label, include, price?}`; `include` lists stages; `price` sets a founder value price. Omit it to derive the price. |
| `payment_schedule` | Optional override of the rates default. |

### Calculations

- Hours = Σ stage hours × (1 + risk buffer), per role.
- Cost = labour (hours × cost per hour) + overhead (labour × overhead rate) + expenses.
- Floor price = cost ÷ (1 − target margin).
- Rate-card price = hours × rate per hour + expenses × (1 + expense markup).
- Derived price = the higher of floor and rate-card price, rounded up. A value price, when given, replaces it.
- Gross margin = (price − cost) ÷ price.
- Effective hourly rate = (price − expenses) ÷ hours.
- Cash check: first payment ≥ expenses + first-stage hours of external roles × their cost.

## Outputs

A private markdown report per option: cost, floor price, rate-card price,
price, margin, effective hourly rate, payment schedule with tax set-aside and
a GO / REVIEW / NO-GO verdict.

## Quality gate

- [ ] Both files are in the vault; `git status` in the repository shows neither.
- [ ] No zero left in `rates.yaml`.
- [ ] Payment-schedule shares sum to 1 (the script enforces it).

## Metrics

Rates last reviewed date; share of estimates priced with the current rates.

## Failure modes

- Copying the calculator output into a proposal file, issue or commit message.
- Leaving founder cost at zero, which makes every project look profitable.
- Editing rates mid-proposal without founder approval.

## Related

[Pricing method](README.md) · [Estimation guide](estimation-guide.md) ·
[Finance](../finance/README.md)
