---
title: Project study template
type: template
status: proposed
template_for: reference-study
owner: founder
last_reviewed: 2026-10-22
review_every_days: 365
---
# Project study template

Use this as a question set, not a licence to fill gaps. Replace every placeholder before submitting the resulting document.
Set the new document's type to `reference-study`, its status to `reference`, and its review interval to 365 days.
Add real `sources` mappings to the resulting document's frontmatter; retain this template's own metadata when editing the template.

## Source and attribution

**Documented** — {{source_title}} by {{creator}}, for {{client_or_context}}, {{supported_date}}.
Link each claim to an opened source using a named Markdown link or footnote-style link.
Record title, HTTPS URL, access date, and author/publication date when known in `sources`.
For inaccessible URLs record the failure; do not cite a search snippet as if the full source was read.

## Project intelligence card

Use this compact YAML record alongside the prose sections. Evidence labels use the contract's four
categories; never convert an inference into a documented fact. These progress flags do not change
frontmatter approval status. Both start false and change only when the corresponding review or original
application actually occurs.

```yaml
project:
  name: "{{project_name}}"
  studio: "{{verified_studio}}"
  year: "{{supported_year_or_unknown}}"
  original_source: "{{opened_https_source}}"
  evidence_level: "{{Documented_Interpretation_Hypothesis_or_Unknown}}"
challenge:
  business_problem: "{{problem_and_evidence_label}}"
  audience: "{{audience_and_evidence_label}}"
  constraints: "{{constraints_and_evidence_label}}"
strategy:
  insight: "{{insight_and_evidence_label}}"
  creative_thesis: "{{thesis_and_evidence_label}}"
identity:
  invariant_elements: ["{{invariant_and_evidence_label}}"]
  variable_elements: ["{{variable_and_evidence_label}}"]
  typographic_logic: "{{type_logic_and_evidence_label}}"
  composition_logic: "{{composition_logic_and_evidence_label}}"
  motion_logic: "{{motion_logic_or_unknown}}"
evaluation:
  strengths: ["{{reasoned_strength}}"]
  weaknesses: ["{{reasoned_weakness}}"]
  unresolved_questions: ["{{unknown}}"]
transfer:
  reusable_principles: ["{{conditional_principle}}"]
  exercises: ["{{proposed_exercise_and_rejection_condition}}"]
  potential_applications: ["{{hypothetical_application}}"]
status:
  reviewed: false
  applied_to_original_work: false
```

Card structure adapted from Founding Blueprint v1.0, 22 October 2026 ([founding source archive](../../studio/archive/founding-blueprint-v1.0.md)). This is a
proposed capture format, not an approved method.

## Business or creative problem

**Documented** — {{stated_problem_and_source}}.
**Interpretation** — {{our_problem_reframing}}. State what is inferred rather than briefed.

## Research evidence

**Documented** — {{claim}}; {{supporting_source_and_location}}; {{source_kind}}.
Summarise in your own words. Separate client testimony, creator intention, independent observation and measured results.
Do not treat awards, selected mock-ups or a polished film as proof of customer understanding or commercial impact.

## Strategic or conceptual insight

**Interpretation** — {{insight}} follows from {{specific_evidence}} because {{reasoning}}.
**Hypothesis** — {{untested_extension}}; test with {{comparison_and_rejection_condition}}.

## Visual and technical decisions

**Documented** — {{published_rule_or_decision}} with an opened citation.
**Interpretation** — {{observed_relationship}}; identify the exact examples examined.
**Unknown** — {{undocumented_tools_parameters_or_process}}.

## System rules and attribution boundary

- {{invariant}}: what stays recognisable across outputs? Cite the rule if documented.
- {{variable}}: what changes, within what bounds, and in response to what input?
- {{exception}}: what happens with long names, absent imagery, small formats or motion disabled?
- Distinguish the commissioned identity from its launch campaign, implementation partners and later redesigns.
- Record the creator's role, client and supported date; a portfolio appearance alone may not establish sole authorship.

## Why these decisions may work

**Interpretation** — {{mechanism}}, {{alternative_explanation}} and {{trade_off}}.
Keep aesthetic judgment separate from measured perception, memory, preference and purchase behaviour.

## Transferable principles

**Interpretation** — {{principle}} may transfer when {{conditions}}; compare with {{second_study}}.
**Hypothesis** — {{project_test}} could disconfirm the transfer if {{failure_condition}}.

## What not to copy

**Interpretation** — Do not lift {{distinctive_form_copy_asset_or_brand_code}}.
Transfer the decision relationship, then derive an original expression from the new client's situation.
Link originals; do not commit third-party images. Use at most two attributed short quotes, no more than 25 words total per source.

## Evidence classification

### Documented

**Documented** — {{supported_claims_and_source_limits}}.

### Interpretation

**Interpretation** — {{our_analysis_and_alternatives}}.

### Hypothesis

**Hypothesis** — {{testable_claim_outcome_and_failure_condition}}.

### Unknown

**Unknown** — {{missing_evidence}}. State whether absent from reviewed sources or inaccessible; these are different limits.

## Application to 3RDWRONG

**Hypothesis** — {{small_studio_application}}; establish the real client's market, languages, channels, rights and production capacity first.
**Interpretation** — {{non_transferable_context}} prevents assuming museum-scale or global-platform outcomes for a founder-led consumer business.
No identity direction or method becomes approved through this study.

## Exercise

**Hypothesis** — {{original_exercise}} using a new formal grammar and rights-cleared material; define {{outputs}}, {{constraints}}, {{critique_task}} and {{rejection_condition}} before making it.
**Unknown** — {{completion_and_application_evidence}}. Keep applied_to_original_work false until the work and critique are linked; an exercise prompt is not a completed result.

## Open questions

- **Unknown** — {{question_requiring_evidence}}.
- **Hypothesis** — {{next_test_and_decision_it_will_change}}.

## Review log

- 2026-10-22 — Template proposed; resulting study reviewer: {{reviewer}}; last reviewed: {{last_reviewed_date}}; next evidence check: {{review_trigger}}.
