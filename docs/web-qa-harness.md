---
title: Web delivery QA harness
type: guide
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Web delivery QA harness

**Documented** — [D-0023](../studio/decisions/0023-commercial-and-delivery-defaults.md)
sets the delivery budget: mobile p75 LCP ≤ 2.0 s, INP ≤ 200 ms, CLS ≤ 0.1;
≤ 2 MB before first interaction; a 60 fps target on a mid-range phone; a
complete reduced-motion fallback. The [default YAML](../methods/digital-experience/qa-budget.yaml)
applies those values to automated lab gates and keeps field/manual requirements
explicitly unmeasured. It does not approve launch.

## Run against a production build

Prerequisites: Python 3.12+, `uv` (installs the repo's PyYAML dependency),
`lighthouse` on PATH, `playwright-cli` from `@playwright/cli` on PATH, and Google
Chrome installed where those tools can discover it. The harness uses Chrome
through Playwright CLI, without adding a Node dependency to this repository.
Check prerequisites with `lighthouse --version` and `playwright-cli --version`.
The implementation was exercised with Lighthouse 13.5.0 and Playwright CLI 0.1.22.

Serve the project's production build using its own documented preview command,
then run once per key template. Use a new or empty output directory for each
build so evidence from separate builds cannot mix.

```sh
bin/3w qa run http://127.0.0.1:8000 --out /private/tmp/3w-qa/build-001
uv run python scripts/web_qa.py run http://127.0.0.1:8000 --out /private/tmp/3w-qa/build-002
```

Use a private vault directory for real project reports. **Documented** — reports,
Lighthouse request lists, console output and screenshots contain the target URL,
page content and potentially identifying data. They must stay outside the public
repository under [D-0021](../studio/decisions/0021-client-work-public-anonymised.md).
The harness visits the supplied URL and its resources without authentication,
using fresh browser contexts. It rejects credentials embedded in URLs; do not
put secrets in query strings. Localhost HTTP is supported for fixture/build QA.

## Read the report

The output contains `report.md`, `report.json`, `lighthouse-1.json` through
`lighthouse-3.json`, `browser.json`, and six viewport screenshots: 375, 768 and
1440 CSS px in normal and reduced-motion modes, at 900 px high and DPR 1.
Browser evidence includes final URLs, titles, user agent, viewport/overflow
measurements, console errors, uncaught exceptions, animation observations and
the raw frame intervals. Full Lighthouse JSON retains failing audit details,
run warnings, tool version and throttling configuration. Failed collection is
listed in the report; partial runs never become a three-run median.

- `PASS`: this measured line meets its threshold, within the stated lab limits.
- `FAIL`: this measured line breaches its threshold.
- `NOT_MEASURED`: there is no valid observation; this is never a pass.
- `lab_status`: the automated gates alone, `PASS`, `FAIL` or `INCOMPLETE`.
- Overall `status`: `FAIL` for measured breaches, otherwise `INCOMPLETE` because
  field p75 and complete fallback/device validation remain outside this tool.

Exit codes: **1** for measured failures; **2** for incomplete evidence, invalid
input or collection failure. The harness intentionally never exits 0 as a launch
approval. An automated pipeline should retain the artefacts even after a non-zero
exit, inspect `lab_status`, and send incomplete/manual gates to the independent
checker. Do not discard missing evidence by treating every exit 2 as success.

Record build/commit, date, reference device and evidence filenames in the
project's QA log. A checker other than the maker must inspect the screenshots,
triage findings, complete the [web QA checklist](../methods/quality/web-qa-checklist.md)
and [launch-readiness checklist](../methods/quality/launch-readiness-checklist.md),
and seek the existing DX-07/DX-08 approvals. This tool cannot supply those approvals.

## Measurement contract and limits

**Interpretation** — These lab methods are useful warning gates before field
data exists; their limits are repeated in every generated report.

| Measurement | Method | What it cannot establish |
| --- | --- | --- |
| LCP, CLS and TBT | Three independent cold Lighthouse mobile runs; median per metric; default simulated mobile throttling | Mobile p75 field performance; a median of three lab loads is not a population percentile |
| INP | `NOT_MEASURED`; TBT is the lab load-responsiveness proxy | TBT is not an INP measurement or a conversion to INP |
| Total transfer | Median Lighthouse `total-byte-weight`, compressed transfer bytes over the Lighthouse observation window | All future lazy-loaded traffic or traffic on other journeys |
| Transfer before first input | Approximate an input at load: sum full `transferSize` of requests with `rendererStartTime <= observedLoad`, both in milliseconds, from each Lighthouse report; median of three | No real input occurs during Lighthouse; whole requests crossing load may overcount, requests after load are excluded, and a user's actual input time differs |
| Automated accessibility | Maximum count of failed Lighthouse accessibility audit IDs over three runs, including Lighthouse's axe-based checks; errors make it unmeasured | This is not a separate axe-core scan or a count of violating elements; manual audits, keyboard, screen reader and WCAG conformance remain open |
| Reduced motion | Emulate `reduce` before loading at all three widths; fifteen 100 ms polls of running/pending `document.getAnimations()` and playing audio/video at top, midpoint and three-quarter scroll depth; save screenshots with animations allowed | Canvas/WebGL, GIFs, cross-origin frames, JS mutations, later/interaction-triggered motion, or equivalent usable fallback content |
| Scroll fps | Two-second scripted scroll using rAF timestamps at 375 px; report callback rate, p95 interval and raw intervals; no scroll range is unmeasured | A lab estimate on the host, without CPU/GPU throttling; not proof of actual compositor frame delivery or mid-range-phone performance |
| Console | Error-level console messages and uncaught page exceptions during six browser probes | All possible states, later errors, successful form submission, or other journeys |

**Unknown** — mobile p75 LCP/INP/CLS before sufficient field data. Name an owner
for the post-launch RUM/CrUX review. Before launch, add project-specific scripted
click/type journeys and inspect Event Timing for responsiveness; the generic
harness scrolls without clicking arbitrary controls or submitting forms.

**Hypothesis** — TBT ≤ 200 ms is a proposed pre-launch proxy gate, not an approved
D-0023 INP equivalence. Zero automated accessibility failures, console errors
and detected reduced-motion activity are proposed defect gates supporting the
existing checklists. D-0023 supplies the other numeric limits. Decimal MB means
2,000,000 bytes. No timing tolerance or rounding is applied to threshold checks;
a measured 59.9 fps fails the 60 fps lab target and needs investigation on device.

The requested 375/768/1440 screenshots supplement the studio's existing
390/834/1440 matrix. Also inspect 320 px reflow and 1920 px, actual reference
devices and the agreed browser matrix. Static screenshots require human visual
inspection; their existence is not a visual pass. Security, consent, SEO,
functional tests and rollback checks remain separate.

Output paths, including resolved symlinks, must stay outside this checkout.
Omitting `--out` creates a new temporary evidence directory. Explicit private
vault paths such as `~/3rdwrong-vault/<codename>/qa/<build>` are also supported.
All in-repository destinations are refused, including fictional examples;
serve fictional fixtures from the repo but keep collected evidence outside it.

## Project budgets and founder exceptions

Supply `--budget /private/path/project-budget.yaml`. Partial `limits` merge with
the immutable studio defaults; unknown keys, non-numeric, negative and non-finite
values are rejected. For example, a stricter project budget:

```yaml
status: proposed
limits:
  lcp_ms: 1800
  transfer_before_input_bytes: 1000000
```

Any larger maximum or smaller minimum requires an existing, human-authored
founder approval record. The YAML names the covered keys and a record path
relative to the repository root:

```yaml
limits:
  lcp_ms: 2200
exception:
  record: studio/decisions/performance-exception.md
  project: fictional-example
  metrics: [lcp_ms]
```

The record must be a committed, unchanged Markdown decision beneath
`studio/decisions/`; absolute paths, traversal and symlink escapes are rejected.
Caller-authored records beside a budget are never trusted. Its frontmatter must
have `status: approved`, `approved_by: founder`, a non-future `approved_on`, and
`qa_exception: {project: fictional-example, limits: {lcp_ms: 2200}}` matching the
codename and every exact loosened limit. Only the founder creates approvals;
the harness never creates one. Keep identifying detail and the underlying
client approval in the vault; the public decision contains only a cleared
codename and numeric waiver. The report records the canonical path and hash.
This trusts reviewed repository history, not a digital signature or arbitrary
local frontmatter. Editing the distributed budget cannot waive the defaults.

## Tests and local fixture

```sh
uv run python -m unittest discover -s tests -p 'test_web_qa*.py' -v
python3 -m http.server 8000 --bind 127.0.0.1 --directory tests/fixtures/web-qa
# In another terminal, use a fresh output directory:
bin/3w qa run http://127.0.0.1:8000 --out /private/tmp/3w-qa/fixture-001
```

Unit tests need no network or browser. Integration uses Python `http.server` on
an OS-selected localhost port, performs all three Lighthouse runs and browser
probes, and checks a deliberately broken reduced-motion/console fixture. It
skips cleanly when Lighthouse, Playwright CLI or Chrome is missing. Other
collection errors fail the test. If a sandbox blocks localhost binding, rerun
that test outside the sandbox. Set `WEB_QA_INTEGRATION_OUT` to a new private
directory to retain the healthy fixture's full report; otherwise it is temporary.

## Technical sources

- [Lighthouse TBT](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time)
  and [TBT as an INP proxy](https://web.dev/articles/tbt): load responsiveness,
  not a substitute for INP.
- [Lighthouse transfer summary](https://developer.chrome.com/docs/lighthouse/performance/resource-summary):
  request and compressed-transfer reporting.
- [Playwright Page API](https://playwright.dev/docs/api/class-page): viewport,
  screenshots and `emulateMedia` reduced-motion support.
