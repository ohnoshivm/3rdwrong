---
title: Prospect qualification
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: skill:3w-prospect-qualification
department: outbound
sub_department: prospecting-research
job: prospect-qualification
role: lead
trigger: ""
kind: repo-skill
availability: repo
distribution: repo
source: skills/3w-prospect-qualification/SKILL.md
invoke: "3w-prospect-qualification skill"
pairs_with: [sales:sales-company-research, agency:sales-outreach, skill:3w-reply-triage]
---
# Prospect qualification

The studio's lead tool for prospect qualification: contact, watch or exclude each researched account before outbound. Proposed lead; the registry change is pending.

## What it does

- Checks the suppression list first.
- Requires a sourced trigger and a named decision-maker role.
- Pre-scores only the scorecard criteria public evidence supports; checks visible disqualifiers.
- Records country, recipient type, contact source and lawful basis.

## When to use

- After account research and before writing a sequence; again when the trigger or contact changes.

## When not to use

- Inbound enquiries or post-conversation deal qualification — `agency:sales-coach` with the qualification scorecard.
- Bought lists or scraped contacts.

## Inputs it needs

- Sourced research notes (vault).
- Initial ICP.
- Recipient country and suppression list.

## How to run it

1. Collect the inputs; keep client and prospect details in the vault.
2. Run the skill and return its exact output structure.
3. Have someone other than the maker review the result.
4. File the output where the skill says; act on blockers first.

```text
Use the 3w-prospect-qualification skill for account {{vault ref}}. Research notes: {{vault link}}. Return the qualification record with a contact, watch or exclude decision. Do not put names or contact details in the repository.
```

## What good output looks like

- Every score and the trigger cite a source and date.
- Compliance basis recorded.
- A one-sentence reason now.

## Quality checks

- [ ] Suppression checked first.
- [ ] Unscorable criteria left for discovery.
- [ ] No prospect identity in the public repo.

## Pairs with

- Upstream: `sales:sales-company-research`.
- Downstream: `agency:sales-outreach` (message), `skill:3w-reply-triage` (replies).

## Limits and cautions

- Experimental skill; thresholds come from the qualification method and are a Hypothesis.
- Not legal advice; see compliance basics.
