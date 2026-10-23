---
title: Account-managed tool descriptions
type: guide
status: proposed
owner: founder
last_reviewed: 2026-10-23
---

# Account-managed tools with no local source file (descriptions captured from the founder's Claude session, 2026-10-23)

Use these as the "tool's own file" for cards. Mark capabilities not listed here as "Not documented".

## skill:dataviz (claude-managed skill)

Use whenever creating ANY chart, graph, plot, dashboard or data visualisation in any medium (HTML/React artifact, inline SVG, matplotlib/plotly/d3/Recharts code, PNG). Read BEFORE the first line of chart code, choosing chart colours, building a stat tile / meter / KPI row, or laying out a dashboard. Produces visualisations that read as one system — elegant, accessible, consistent in light and dark — using a brand-neutral placeholder palette you swap for your own. Teaches a design-system-agnostic method: a form heuristic, a colour formula with a runnable validator, mark specs and interaction rules. A validated default palette is documented in references/palette.md (swap its values for the brand's). When the destination is a first-party document connector that renders live charts, hand it the rows rather than a rendered image. Triggers: chart, graph, plot, data viz, dashboard, analytics, categorical/sequential/diverging palette, stat tile, sparkline, heatmap, legend, axis, tooltip, chart colours.
Studio use: charts and data displays inside brand guidelines, case studies, client reports and digital products — align the palette with the client identity system.

## mcp:claude-docs (claude.ai connector "Claude Docs")

Living documents created and edited in the founder's claude.ai account. Tools: batch (create a doc or apply several operations atomically), guide (topic guides: index, editing, tabs, comments, charts, chart-definition, diagram, uploads, sharing, skill), update (edit a tab's contents, rename a doc/tab, change a stored value), plus read/query/export/create/delete. Usage rules from the connector: make a doc only when the user asks for one; create its skeleton first (title, byline, a pending block per section) then fill sections; findings go in the doc, not chat; doc comments are answered with doc comments. Requires the founder's claude.ai sign-in; not available to collaborators without their own access.
Studio use: shareable living documents (briefs, critiques, reports) when a document outside the repo is requested; repo remains the source of truth.

## mcp:hyperframes and mcp:heygen ("HyperFrames by HeyGen" claude.ai connector)

HyperFrames is HeyGen's framework for creating, editing and rendering programmable HTML-based video projects; projects render to MP4, WebM or MOV at any frame rate. Connector tools: compose (author a new project or edit an existing one via project_id; runs in the background, typically minutes; optional design_source style presets: claude, blockframe, monochrome, mat, signal), list_projects, get_project (metadata + player widget), get_project_status, get_render_status, render_video, submit_feedback. From CLI/IDE agents (Claude Code, Codex) `compose` and `render_video` are DISABLED — local authoring uses the HyperFrames skills instead (`npx skills add heygen-com/hyperframes`, giving /hyperframes, /hyperframes-cli, /hyperframes-media), which produce standalone HTML/GSAP compositions on disk. Route: "local editable composition" → local skills; "hosted HeyGen project / cloud render / shareable" → the connector. Requires the founder's HeyGen account (OAuth).
Studio use: motion-graphics and launch films for identity and digital-experience projects; brand-consistent video assets.

## mcp:chatcut_desktop (local ChatCut desktop app MCP)

Configured but currently failing to connect (the ChatCut app's MCP binary is not installed at the configured path). The ChatCut skills (chatcut-*: motion graphics, video/image generation, transcription, voice, music, multicam sync, UGC/talking-head guides) are installed separately for Codex (GPL-3.0 plugin, FETCH). Card: describe it as the connector to the ChatCut desktop editor; capabilities beyond the skills: Not documented; status: install the ChatCut desktop app to enable.

## mcp:creative_production_mcp

Configured in local MCP config; no capability documentation found on disk. Card only if its role is lead/specialist: mark capabilities "Not documented" and its status "verify before use"; otherwise recommend benching in the correction pass.
