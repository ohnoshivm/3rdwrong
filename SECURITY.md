# Security and privacy reporting

## Scope

This policy covers the public `3rdwrong` repository, its validation tools, and information accidentally committed here. Report leaked credentials, personal data, confidential client information, or a vulnerability in the repository tooling.

## Report privately

Use [GitHub private vulnerability reporting](https://github.com/ohnoshivm/3rdwrong/security/advisories/new). Do not open a public issue for a live credential, personal-data exposure, or confidential client material. Do not send sensitive material through public discussions.

## Response

1. Restrict access to the exposed system and rotate or revoke affected credentials first. Deleting a file does not revoke a credential.
2. Preserve only the minimum incident details needed to assess scope. Notify affected clients through the agreed private channel where client material is involved.
3. Remove the exposed material from Git history with `git filter-repo`, then force-push the cleaned history and coordinate the update with collaborators.
4. Contact GitHub Support to request removal of cached views that still expose the material. A normal commit that deletes the file does not remove earlier history or cached copies.
5. Review logs and access, record corrective actions without copying the secret or personal data, and close the incident only after the affected credential and history have been addressed.

Everything committed here is public under the [publication rules](docs/public-private-boundary.md). Choose a non-public store before any client or interview data exists; personal data, third-party contracts, credentials and NDA-bound assets must never be committed. Secret and personal-data scans include the upstream agents.

The repository secret scanner is a guardrail, not a substitute for private handling or incident response. Use `secret-scan: allow` only for a reviewed false positive on that line, and explain the reason in the pull request. Unmodified upstream security examples use narrowly scoped, file-and-line-hash-bound exceptions in `schemas/metadata.json`; see [knowledge governance](docs/knowledge-governance.md#upstream-agents-and-scanner-exceptions). Never exclude the vendor directory from scanning.
