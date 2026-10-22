---
title: Repository maintenance
type: guide
status: proposed
owner: founder
last_reviewed: 2026-10-22
---

# Repository maintenance

Keep the repository small and current. Review the checks alongside the knowledge they protect.

## Weekly

- Triage `inbox/`: promote useful notes into the right canonical document or delete them. Keep private material out of the public repo.
- After document or frontmatter changes, run `uv run python scripts/build_index.py`; check it with `uv run python scripts/build_index.py --check`.
- The index check is also part of `uv run python scripts/validate.py`; stale knowledge review dates remain warnings.

## Monthly

- Run `uv run python scripts/validate.py --stale` and assign overdue documents for review.
- Resolve broken links, check new source links, and review `privacy-review` changes before publication.
- Review Dependabot pull requests. For GitHub Actions SHA updates, read the upstream release notes, verify the target tag and full commit SHA, inspect changed inputs and runtime requirements, then merge after CI passes.
- Run `uv run python scripts/sync_labels.py --dry-run` when labels change. Review the printed commands before running `uv run python scripts/sync_labels.py` with GitHub CLI access.

## Quarterly

- Revisit the review intervals in `schemas/metadata.json` and update the governance guide if they change.
- Check that proposed material is still useful, hypotheses have a test plan, and superseded records point to a current replacement.
- Review publication rules and access to the non-public store; choose that store before client or interview data exists.

## Python dependencies

Keep runtime dependencies to the standard library and PyYAML. When dependency metadata changes, regenerate the lockfile with `uv lock`, then verify with `uv sync --locked`, the validator, and unit tests.

## Secret or personal-data incident

Follow [`SECURITY.md`](../SECURITY.md) immediately. Rotate or revoke the credential first. Removing a file from the latest commit does not remove it from history; use the documented history cleanup and cached-view steps.
