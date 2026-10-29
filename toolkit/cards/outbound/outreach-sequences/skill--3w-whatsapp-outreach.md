---
title: WhatsApp outreach
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-29
tool_id: skill:3w-whatsapp-outreach
department: outbound
sub_department: outreach-sequences
job: whatsapp-outreach
role: lead
trigger: ""
kind: repo-skill
availability: repo
distribution: repo
source: skills/3w-whatsapp-outreach/SKILL.md
invoke: "3w-whatsapp-outreach skill"
pairs_with: [skill:3w-prospect-qualification, skill:3w-reply-triage, agency:sales-outreach]
---
# WhatsApp outreach

The studio's lead tool for small, founder-approved WhatsApp opener batches sent one to one through WhatsApp Web. Registered job lead; the skill remains experimental.

## What it does

- Excludes suppressed, previously contacted and duplicate numbers.
- Selects a small batch of business lines that each have a source.
- Drafts a short, three-paragraph human opener with an opt-out line.
- Sends only the approved batch, checks paragraph spacing before each send and logs delivery status.

## When to use

- When the founder wants WhatsApp openers sent to a sourced contact list and will approve each batch.

## When not to use

- Bulk broadcasts, sender automation, number probing or contact uploads.
- Follow-ups without separate approval.
- Replies: `skill:3w-reply-triage`.

## Inputs it needs

- Contact file with provenance, suppression list and contact history.
- Approved offer and sender identity.
- Signed-in WhatsApp Web session.

## How to run it

1. Collect the inputs; keep contacts and send logs in the vault.
2. Run the skill and return its exact output structure.
3. Have someone other than the maker review the result.
4. File the output where the skill says; act on blockers first.

```text
Use the 3w-whatsapp-outreach skill on {{vault contact file}}. Exclude history and suppression matches, draft a five-recipient batch for my approval, and send only after I approve the exact recipients and text.
```

## What good output looks like

- Every recipient has a source row, an approved message and an observed status.
- Every message shows three spaced paragraphs in the chat.

## Quality checks

- [ ] Founder approved recipients, text and account before any send.
- [ ] No suppressed or repeat recipients.
- [ ] No names or numbers in the public repo.

## Pairs with

- Upstream: `skill:3w-prospect-qualification`, `agency:sales-outreach`.
- Downstream: `skill:3w-reply-triage` and the pipeline (L0 lead).

## Limits and cautions

- Experimental skill. Cold WhatsApp messages can get the sending account restricted, so keep batches small and paced.
- An internet-sourced number does not establish consent or WhatsApp registration.
