---
title: Production department
type: guide
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Production department

Produce scoped client work: plans, timelines, client communication, handover and retention.

Status: proposed registry routing. Source review does not establish live tool performance, licence clearance, runtime connectivity or founder approval.

33 tools; 8 lead, 11 specialist, 11 bench, 3 parked, 0 excluded; 19 active / 14 library.

## Sub-departments → jobs → leads

### producing-pm

| Job | Lead(s) |
| --- | --- |
| `project-planning` | `agency:project-management-studio-producer` |
| `project-tracking` | `openai-templates:artifact-template-project-tracker` |
| `resource-coordination` | `agency:project-management-project-shepherd` |

### client-experience

| Job | Lead(s) |
| --- | --- |
| `client-onboarding` | `creative-production:intake` |
| `client-service` | `agency:customer-service` |
| `meeting-cadence` | `agency:project-management-meeting-notes-specialist` |

### handover-retention

| Job | Lead(s) |
| --- | --- |
| `client-success` | `agency:customer-success-manager` |
| `delivery-handover` | `skill:writing-release-notes` |
| `retention-programmes` | **gap** — No reviewed tool justifies default ownership of this complete job; existing narrow references/specialists do not establish a lead method. |

## Specialists with activation triggers

| Tool | Job | Trigger |
| --- | --- | --- |
| `agency:project-manager-senior` | `producing-pm/project-planning` | Use when the approved work needs this capability: Converts specs to tasks and remembers previous projects. Focused on realistic scope, no background processes, exact spec requirements |
| `agency:sales-account-strategist` | `handover-retention/client-success` | Use for production/handover-retention/client-success when the brief specifically requires: Expert post-sale account strategist specializing in land-and-expand execution, stakeholder mapping, QBR facilitation, and net revenue retention . |
| `figma:generate-project-plan` | `producing-pm/project-planning` | Use when the approved work needs this capability: Generate a FigJam project plan board from a PRD plus codebase context. Interactive flow: research → propose sections → per-section deep research → per-section content + block-shape proposal → create FigJam → skeleton → fill → diagrams → wrap. Each content block (section, nested section, intro callout, table, multi-column text, sticky column, diagram section, metadata strip) has its own subskill reference file. Use when the user asks for 'project plan in FigJam', 'interactive project plan', '/generate-project-plan', or provides a PRD and wants per-section confirmation on content + rendering |
| `mcp:asana` | `producing-pm/project-tracking` | Use when the approved work needs this capability: Configured MCP server: asana. Transport details and credentials are not inventoried |
| `mcp:atlassian` | `producing-pm/project-tracking` | Use when the approved work needs this capability: Configured MCP server: atlassian. Transport details and credentials are not inventoried |
| `mcp:google-calendar` | `client-experience/meeting-cadence` | Use when the approved work needs this capability: Configured MCP server: google calendar. Transport details and credentials are not inventoried |
| `mcp:intercom` | `client-experience/client-service` | Use when the approved work needs this capability: Configured MCP server: intercom. Transport details and credentials are not inventoried |
| `mcp:linear` | `producing-pm/project-tracking` | Use when the approved work needs this capability: Configured MCP server: linear. Transport details and credentials are not inventoried |
| `openai-templates:artifact-template-operating-calendar` | `client-experience/meeting-cadence` | Use when the approved work needs this capability: Create a spreadsheet using the Operating Calendar template and its retained reference file. Use when the user selects or names Operating Calendar. Plan annual and monthly operating milestones, campaigns, launches, deadlines, and recurring events |
| `skill:feature-prioritization` | `producing-pm/project-planning` | When choosing between scoped studio initiatives or client backlog items. |
| `skill:low-effort-high-reward` | `producing-pm/project-planning` | When triaging a concrete studio or client backlog against effort and reward. |

## Bench and parked summary

- **bench: 11.** `agency:healthcare-aging-parent-care-companion`, `agency:healthcare-customer-service`, `agency:hospitality-guest-services`, `agency:language-translator`, `agency:product-manager`, `agency:product-sprint-prioritizer`, `agency:project-management-jira-workflow-steward`, `agency:real-estate-buyer-seller`, `agency:retail-customer-returns`, `agency:study-abroad-advisor`, `engineering:standup`
- **parked: 3.** `notion:notion-meeting-intelligence`, `notion:notion-spec-to-implementation`, `notion:notion-weekly-project-digest`
- **excluded: 0.** None.

Individual reasons and activation requirements are in the [canonical registry](../../toolkit/sources/registry.json). Library means callable by explicit name after review; it is not loaded by default.

## Gaps

- `handover-retention/retention-programmes` — No reviewed tool justifies default ownership of this complete job; existing narrow references/specialists do not establish a lead method.

## Counts by sub-department and role

| Sub-department | Lead | Specialist | Bench | Parked | Excluded | Active | Library | Total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| producing-pm | 3 | 7 | 3 | 2 | 0 | 10 | 5 | 15 |
| client-experience | 3 | 3 | 8 | 1 | 0 | 6 | 9 | 15 |
| handover-retention | 2 | 1 | 0 | 0 | 0 | 3 | 0 | 3 |

## Operating contract

Use the job lead first and a specialist only on its trigger. Maker and checker must be separate people/agent instances; a reviewer never approves its own department alone. Proposed `load: active` is the desired loading policy, while the source inventory records installation presence. No physical activation was performed.

Design and Engineering prototype together early; the handoff names artefacts, constraints, budgets and evidence rather than creating a wall. Human judgement and founder approval remain separate from tool routing.
