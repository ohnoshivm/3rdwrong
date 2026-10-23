---
name: hands-free
description: Plan a multi-step outcome as a resumable, evidence-backed plan. Use for hands-free planning; use execute to run and resume to continue interrupted work.
---

# Hands Free planning

Turn the requested outcome into a bounded plan with observable acceptance criteria.

1. Read current project guidance, existing plans, and user decisions. For a small
   task, do the requested work directly instead of adding orchestration overhead.
2. Ask only material unanswered questions, grouped together. State reasonable
   implementation assumptions; missing authorization is never an assumption.
3. Discover available tools and agents. Use a single agent by default. Parallel
   agents are optional when supported and authorized, with distinct ownership.
   Never assume special agent roles or model-routing controls exist.
4. Write `.hands-free/<run-id>/plan.json` using `../../references/execution.md`.
   Include outcome, constraints, capabilities, dependency-ordered steps, relevant
   issue IDs and acceptance criteria. Include existing authorization and any new
   decision needed. Budget estimates are advisory unless enforced by the host.
5. If asked to plan, deliver the plan. If asked to implement/run, continue through
   the execute skill without an extra permission round for authorized work.

No automatic permission elevation, invented agents, or default headless execution.
Resume uses the saved ledger and evidence rather than restarting the whole plan.
