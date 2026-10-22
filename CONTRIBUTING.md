# Contributing

This repository is the reviewed public knowledge base for a small, founder-led studio. The `main` branch holds reviewed material; use short-lived branches for proposed changes. Keep contributions specific, sourced, and safe to publish.

## A small-studio flow

1. Use an issue for research, experiments, proposed methods, skill changes, decisions, or project lessons. Pick the matching issue form and labels.
2. Use a short-lived branch named `type/short-desc`, such as `docs/governance-cadence` or `research/studio-reference`.
3. Open a pull request for substantive changes. Explain what changed, why it matters, its status, and how it was checked.
4. Keep material `proposed`, `hypothesis`, or `experimental` until a named human reviews it. Agents never promote material to `approved`.
5. Run the repository validator before proposing a pull request:

   ```bash
   uv sync --locked
   uv run python scripts/validate.py
   ```

6. For changes to validator or tool code, also run:

   ```bash
   uv run python -m unittest discover -s tests -q
   ```

## Status and evidence

Use the status definitions in [knowledge governance](docs/knowledge-governance.md). A proposed decision that changes strategy needs a decision record and a named founder approval before it becomes approved. Cite primary or credible sources for documented claims. Label reasoning as Documented, Interpretation, Hypothesis, or Unknown.

## Writing and privacy

- Use British English, plain language, one H1, ATX headings, and relative links to files in the repository.
- Keep one canonical home for each fact. Link to it instead of copying policy across pages.
- Do not invent clients, results, approvals, research, quotes, or statistics.
- Everything committed here is public and open source. Do not commit credentials, personal data, third-party contracts or NDA-bound assets. Choose a non-public store before collecting client or interview data. Studio pricing hypotheses and the founding economics are public under D-0017; preserve their status and evidence limits. Read the [publication rules](docs/public-private-boundary.md) before publishing project learning.

## No-code contributions

You can use the GitHub web editor to correct wording, add a source note, or edit a small document. Choose **Propose changes**, leave the status unapproved, then submit the resulting pull request with the source and privacy checks completed. For validator or workflow changes, use a local checkout so the required commands can run.
