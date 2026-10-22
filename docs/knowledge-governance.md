---
title: Knowledge governance
type: guide
status: proposed
owner: founder
last_reviewed: 2026-10-22
---

# Knowledge governance

Status makes the evidence and review state of a document visible. It does not replace judgement or approval.

## Statuses

| Status | Meaning |
| --- | --- |
| `approved` | A named human has approved it. Frontmatter records `approved_by` and `approved_on`. |
| `proposed` | A draft or new practice awaiting human review. |
| `hypothesis` | Plausible but untested; say what evidence would test it. |
| `experimental` | Being evaluated in use; do not treat as established policy. |
| `rejected` | A human reviewed and declined this direction. Record why when useful. |
| `superseded` | Replaced by a newer record; frontmatter links to `superseded_by`. |
| `reference` | A source record or study, not an instruction to adopt its approach. |

Agents may prepare and revise proposed material. They must never promote anything to `approved`. A human approval names the approver and date; substantive strategic approvals belong in the decision record.

## Evidence labels

Use these exact labels when classifying claims:

- **Documented** — stated in a cited primary or credible secondary source.
- **Interpretation** — a reasoned reading of documented material.
- **Hypothesis** — plausible but untested, with a proposed test.
- **Unknown** — not publicly documented; do not fill the gap.

Link documented claims to their sources. Do not present an interpretation or hypothesis as a fact.

## Review cadence and stale reports

The default `review_every_days` interval depends on document type. A document can override it with a positive integer in frontmatter. The defaults and allowed types are stored in [`schemas/metadata.json`](../schemas/metadata.json). Review dates use ISO format (`YYYY-MM-DD`).

Run `uv run python scripts/validate.py --stale` to list overdue reviews. Staleness is a warning and does not fail validation. A warning asks for a human review; it does not mean a document is automatically false or invalid.

Inbox notes use `type: inbox`, `status: proposed`, and an ISO `captured` date. They do not need an owner or review date. The stale report warns when a note has waited more than 30 days; weekly triage should turn it into a study, principle, experiment, decision, or method change, or delete it. Keep personal, client, commercial material, and all pricing hypotheses and price ranges in the private repository. Public hypothesis records may describe the validation question without disclosing the range.

## How knowledge compounds

Record a learning as a sourced study, tested experiment, project lesson, or critique; identify which methods or decisions it affects; then update the canonical document and retain the evidence trail. The working cycle is described in [`methods/learning-loop.md`](../methods/learning-loop.md).

## Outdated or unsupported material

When a claim loses support, record the gap and the source checked. Correct it if the evidence changed; otherwise mark the document `superseded`, set `superseded_by` to the replacement decision ID or file path, and update its index. Do not delete useful history or quietly keep citing a rejected direction as current guidance.

## Metadata rules

[`schemas/metadata.json`](../schemas/metadata.json) is the single source for allowed types and statuses, decision statuses, review defaults, required files, frontmatter-exempt paths, required skill and decision sections, and personal-data allowlists. The validator reads these values. A `version` field is optional and must be a non-empty string when present; other extra frontmatter keys are allowed. Change the schema and its documentation together when a human-approved rule changes.
