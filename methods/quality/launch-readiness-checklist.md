---
title: Launch-readiness checklist
type: checklist
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Launch-readiness checklist

Run at [stage 08](../digital-experience/08-performance-and-launch-readiness.md)
before the go/no-go review. Every item needs a result and an owner role.
Production URLs, credentials and account details are recorded in the vault,
not in the project record.

## Performance

- [ ] Budgets from DX-04 measured on the production build: LCP, CLS, Total
      Blocking Time, JavaScript and transfer weight, scene frame time and
      memory — no looser than the studio budget in [D-0023](../../studio/decisions/0023-commercial-and-delivery-defaults.md) without an
      approved exception.
- [ ] Tool, version, device, network profile and date recorded.
- [ ] Exceptions approved by the founder and accepted by `C1`.
- [ ] Owner named for field Core Web Vitals review after launch.

## Security

- [ ] Security headers set and verified ([web standards](web-standards.md#security-headers)).
- [ ] Dependency audit run; no high-severity finding open.
- [ ] No secrets in the repository or client bundle; environment variables in
      the host's secret store.
- [ ] Admin and CMS accounts use strong authentication and least privilege.
- [ ] Backups and a restore path exist for CMS content and media.

## Search and sharing

- [ ] Redirect map from retired URLs implemented and tested.
- [ ] `sitemap.xml` and `robots.txt` correct for production (staging blocks
      removed).
- [ ] Canonical URLs, titles, descriptions and social cards verified.
- [ ] Search console ownership arranged for the client.

## Privacy and analytics

- [ ] Analytics records the agreed events and respects consent.
- [ ] Privacy notice and cookie information approved by the client.
- [ ] Third-party embeds listed; none load before consent where consent is
      required.

## Operations

- [ ] Domain, DNS, certificate and hosting ownership as contracted.
- [ ] Launch plan with timing, steps, owners and smoke tests.
- [ ] Rollback trigger and procedure verified.
- [ ] Error monitoring and uptime alerts route to a named owner.
- [ ] Support cover for the first days after launch; no launch before a
      holiday without cover.
- [ ] Client communications ready: launch notice, editor access, care channel.

## Decision

- [ ] Web QA checklist passed with no open critical or major defect.
- [ ] Go/no-go held; decision, approvers (roles) and conditions logged in the
      gate log as DX-08.
