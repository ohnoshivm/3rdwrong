---
title: "Handoff: engineering to QA"
type: checklist
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Handoff: engineering to QA

Engineering hands a feature-complete production build, with motion and scenes, to independent QA. Happens at DX-05/06 → DX-07 ([07 QA](../digital-experience/07-qa.md)). QA is run by people and agents who did not build what they test.

- **From:** Engineering / product-frontend and creative-engineering (makers: `agent:frontend-architect` and the build executors; `agent:motion-director`, `agent:3d-webgl-engineer`).
- **To:** Design / design-qa (`agent:visual-qa-engineer`), accessibility (`agency:testing-accessibility-auditor`), and a fresh `agent:implementer` instance that did not build the feature, using the test-engineering lead `skill:playwright-cli`.
- **Acceptance checker:** `agency:testing-reality-checker` reviews the QA log and closures.

## Artefact checklist (sender)

- [ ] Staging URL of a production build (not a dev server), recorded in the vault; build and test output passing.
- [ ] Build version or commit, and the list of templates and flows in scope.
- [ ] Final content loaded; any missing content listed with an owner.
- [ ] Budget measurements from the latest significant merge against the DX-04 table in `qa/README.md`.
- [ ] Motion and scene notes: triggers, reduced-motion behaviour, no-WebGL fallback, frame-time and memory measurements (DX-06).
- [ ] Code-review record; dependency audit (`skill:supply-chain-risk-auditor`) output.
- [ ] Known defects and limitations, each with severity and owner.
- [ ] Test accounts and CMS roles for QA, issued through the vault process.
- [ ] Current-build automated collection: `bin/3w qa run <url> --out <vault>/<codename>/files/qa/<build>/<template>` per key template after integration. Follow `docs/web-qa-harness.md`; reports and URLs stay private. Preserve `report.md`, `report.json`, three Lighthouse JSON files, `browser.json` and all normal/reduced-motion screenshots. A tool collection failure is listed, never concealed.

## Acceptance checks (receiver, before testing starts)

- [ ] The build is the production build and matches the stated version.
- [ ] Every in-scope template is reachable; console is clean of first-party errors.
- [ ] Budgets were measured on the reference mid-range mobile profile, with tool, device, network and date.
- [ ] Reduced-motion and no-WebGL paths are switchable for testing.

If these fail, return the build before spending QA time on it.

## What QA returns

- [ ] [Web QA checklist](../quality/web-qa-checklist.md) results and the defect list (severity per the [critique protocol](../quality/critique-protocol.md#severity), owner, state) in `qa/README.md`.
- [ ] Screenshots at 1440, 834 and 390 px plus agreed widths, before and after each fix (vault).
- [ ] Accessibility notes: automated output, manual keyboard and focus, screen reader pairings, 200 % zoom, 320 px reflow, reduced motion.
- [ ] Re-inspection record for every closed defect.
- [ ] Harness `status`, `lab_status` and every `NOT_MEASURED` item reviewed under the [mandatory QA gate](../playbooks/digital-experience.md#mandatory-harness-report-and-conditional-gate). The six 375 / 768 / 1440 px captures supplement the agreed matrix; inspect every image, and run separate functional, browser, keyboard and assistive-technology checks.
- [ ] If INCOMPLETE remains, founder's `FIELD-DATA-DEFERRED` and, when needed, `REAL-PHONE-TEST-DEFERRED` decisions name the missing checks, risks, owner, deadline and follow-up evidence. Lab status must be PASS; no other missing evidence is excused.

## Return conditions

Any Blocker (critical) or Major defect returns to its maker. QA does not fix Engineering's code; the maker fixes and QA re-inspects. Gate DX-07 also requires the harness report: PASS, or the explicitly authorised INCOMPLETE route. Exit 2 alone is never a pass; measured FAIL or missing collection evidence holds the gate. Re-run on the fixed build.

## Record

One handoff row in `decisions.md` for the build handed over, and one for the QA result ([format](README.md#handoff-record)).
