---
name: 3w-awards-submission
description: Decide on and prepare a 3RDWRONG award entry using the studio's awards strategy — fit check against the award's own published criteria, client permission, free-submissions-only rule (D-0024), submission checklist, entry text and results log. Use after a launch or close-out when work might be entered; do not use to design for juries, enter paid awards or claim results before they are official.
metadata:
  type: skill
  status: experimental
  owner: founder
  last_reviewed: 2026-10-23
  version: 0.1.0
---
# 3w-awards-submission

## Purpose

Enter only work that fits an award's lens and that the studio has permission to show, describe it truthfully, and learn from every result. This skill applies [awards strategy](../../growth/proof/awards.md); it does not replace it.

## When to use

After L7 launch of a digital-experience project, at L9 for identity work, and for strong self-initiated work, when someone proposes an entry or the monthly growth review checks the awards calendar.

## When not to use

Do not use to enter paid awards while the paid awards budget is zero (D-0024). Do not use to change a client's work for a jury. Do not use for press relations; that is `skill:press-media-relations`.

## Inputs

- The live work or case study, its launch date and credits.
- Client permission to enter and credit, or a self-initiated label.
- The award's current official criteria, categories, deadline and fee, read on its official site with the access date.
- Engineering's performance and accessibility notes for digital entries.

## Dependencies

Read [awards strategy](../../growth/proof/awards.md), [D-0024](../../studio/decisions/0024-growth-defaults.md), [D-0021](../../studio/decisions/0021-client-work-public-anonymised.md), [award site teardowns](../../taste/award-site-teardowns.md) and [growth metrics](../../growth/metrics.md). `agency:marketing-pr-communications-manager` may help with wider communications; its business-award template (results-led, quantified outcomes) does not apply to design-jury awards.

## Procedure

1. **Read the award.** Record what it judges from its official page, with date. If criteria cannot be verified, mark Unknown and do not enter until checked.
2. **Fit check.** Is the work strong against those criteria, and does recognition there reach people the studio wants to reach? If either answer is no, skip and record why.
3. **Permission.** Client work needs written agreement to be entered and credited; check D-0021 clearance. Self-initiated work is labelled as such.
4. **Cost.** Confirm the submission is free. Any fee stops the entry until the founder changes D-0024; record the decision in the vault.
5. **Prepare** with the submission checklist in the awards strategy: stable live URL, performance and accessibility checked, images at the platform's current specifications, short description of the idea and the decision, credits as permitted, deliberate category.
6. **Write the entry text.** State the problem, the idea and the craft decisions in plain words. No results the studio cannot document; no adjectives doing the work of evidence.
7. **Founder sign-off**, then submit and log the entry and date.
8. **Log results** in the platform's own wording, whatever the outcome, with one learning. Add badges or mentions only after official publication.

## Evidence requirements

Criteria and fees cite the official page and access date. Any performance or outcome statement in the entry cites a measurement or the client's permission. Award results are quoted, never paraphrased upwards.

## Output

```markdown
# Award entry: {{award}} — {{work}}

**Criteria (source, date):** {{…}} · **Fee:** {{free | paid → blocked}}
**Fit:** {{enter | skip}} — {{reason}} · **Permission:** {{record ref | self-initiated}}

## Checklist
- [ ] Live URL stable · [ ] Performance and accessibility notes · [ ] Images to spec
- [ ] Description · [ ] Credits · [ ] Category · [ ] Founder sign-off

## Entry text
## Result log: {{date, platform wording, learning}}
```

## Quality checks

- Criteria come from the official source with a date.
- Fit and permission were settled before any preparation work.
- No fee is committed while D-0024 holds.
- The entry text makes no undocumented claims.
- No award claim before the official result; no "award-winning studio" inflation.

## Failure conditions

Stop when permission is missing, the fee is not zero, the live work is unstable, or the criteria cannot be verified.

## Human review

The founder decides enter or skip and signs off each submission. The client approves credits for their work.

## Example

**Fictional example.** A fictional self-initiated type-specimen site launches. The fit check against the CSS Design Awards page (read that day) is positive and submission is free; the work is labelled self-initiated. Engineering's notes confirm the budget. The founder signs off; the entry and later result are logged.
