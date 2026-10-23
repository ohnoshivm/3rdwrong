---
name: 3w-prospect-qualification
description: Qualify a researched account before any outbound contact — ICP fit from public evidence, a sourced trigger, a reachable decision-maker, disqualifiers, compliance basis and suppression check — and decide contact, watch or exclude. Use in outbound prospecting after account research and before writing a sequence; do not use for inbound leads or deal qualification after a conversation.
metadata:
  type: skill
  status: experimental
  owner: founder
  last_reviewed: 2026-10-23
  version: 0.1.0
---
# 3w-prospect-qualification

## Purpose

Spend the 20 hand-written first messages a week (D-0024) only on accounts that fit, have a reason to hear from the studio now, and can lawfully be contacted. Everything else is watched or excluded, with a reason.

## When to use

Use after an account is researched with the [outbound research checklist](../../growth/outbound/README.md#2-research-checklist-2030-minutes-per-account) (`sales:sales-company-research` is the research lead) and before `agency:sales-outreach` writes the message. Re-run when the trigger or contact changes.

## When not to use

Do not use for inbound enquiries or after a conversation has started; L1 qualification uses the [qualification scorecard](../../growth/sales/qualification.md) with `agency:sales-coach`. Do not use to justify bulk sends, bought lists or scraped contacts.

## Inputs

- The account research notes with sources and access dates (vault).
- The [initial ICP](../../studio/initial-icp.md) and current discovery focus.
- The recipient's country and the vault suppression list.

## Dependencies

Read the [outbound system](../../growth/outbound/README.md), [compliance basics](../../growth/outbound/compliance.md), [qualification](../../growth/sales/qualification.md) (scorecard and disqualifiers), [lead sources](../../growth/sales/lead-sources.md) and [D-0024](../../studio/decisions/0024-growth-defaults.md).

## Procedure

1. **Suppression first.** If the person or company is on the suppression list or has opted out before, exclude. Stop.
2. **Trigger.** Is there a visible, sourced trigger (launch, new category, funding, retail expansion, new market, brand or marketing hire)? No trigger → watch, with what to look for.
3. **Pre-score** the scorecard criteria that public evidence can support: genuine problem, buying trigger and timing, offer fit, openness to original thinking (from public behaviour), proof and publication potential. Score 0–3 from evidence only; unknown is 0 and becomes a discovery question. Budget, decision access and conduct stay unscored until a conversation.
4. **Disqualifiers.** Check the qualification disqualifiers that can be seen in advance (wants a copy of another brand, excluded category, conflict with a current client). Any hit → exclude.
5. **Decision-maker.** Name the role (founder, co-founder, brand or marketing lead) and the source; no named role → watch.
6. **Compliance.** Record the recipient's country, whether they are a company or an individual or sole trader, the source of the contact details and the lawful basis. UK or EU sole traders without consent → do not email.
7. **Reason now.** One sentence: why this studio, why now, which proof or method is relevant. If it could be sent to another company, the account is not ready.
8. **Decide** contact, watch (with a check-back date) or exclude, and record it in the vault. The founder approves the monthly list.

## Evidence requirements

Every score and the trigger cite a public source with access date. Assumptions about budget or intent are Hypothesis and do not raise a score.

## Output

```markdown
# Prospect qualification: {{account ref (vault)}}

**Decision:** {{contact | watch until … | exclude}} — {{reason}}
**Trigger:** {{event, source, date}} · **Decision-maker role:** {{role, source}}

| Criterion | Score 0–3 | Evidence |
| --- | --- | --- |

**Disqualifiers:** {{none | which}} · **Suppression checked:** {{date}}
**Compliance:** {{country, recipient type, contact source, basis}}
**Reason now:** {{one sentence}}
```

## Quality checks

- Suppression list checked before anything else.
- Trigger and every score have a source and date.
- Unscorable criteria are left for discovery, not guessed.
- Compliance basis recorded for the recipient's country and type.
- No prospect identity or contact detail in the public repository.

## Failure conditions

Stop when research notes lack sources, when the recipient's country or type is unknown, or when contact details came from a bought list or scraping against platform terms.

## Human review

The founder approves the monthly account list and, until ten consecutive sequences pass without edits, every first message.

## Example

**Fictional example.** Stillsoil Atelier announced a home-fragrance line (fictional source, dated). Pre-score: problem 2, trigger 3, offer fit 3, openness 2, proof 2. No disqualifiers; the founder is named on the company site; the company is a UK limited company, so corporate-subscriber rules apply. Decision: contact.
