---
title: Design department
type: guide
status: proposed
owner: founder
last_reviewed: 2026-10-23
review_every_days: 90
---

# Design department

## Purpose and standards

Build distinctive, deployable identity systems through meaningful ideas, human craft and independent evidence. Brand identity is the core; Digital Experience is the second pillar under [D-0018](../decisions/0018-design-engineering-studio.md), which supersedes D-0002. Department routing remains proposed; it is not capability certification.

The founder leads taste, concept, typography, optical judgement, colour, composition and final craft decisions. Start reference work in [taste/](../../taste/README.md); extract principles and keep a never-copy list. Strategy supplies signed, sourced discovery and cultural research. Design owns WHAT and WHY; Engineering owns implementation, general testing, performance and security. Media owns film, motion-graphics assets, image production and sound.

Design and Engineering prototype together early. Motion must communicate or provide feedback, honour reduced motion, preserve keyboard/touch operation and use one scroll engine. Agree scope before complex 3D, campaign production or delivery commitments.

Decide concept, identity and experience intent; own WHAT and WHY with independent craft and visual critique.

Status: proposed registry routing. Source review does not establish live tool performance, licence clearance, runtime connectivity or founder approval.

251 tools; 26 lead, 153 specialist, 71 bench, 1 parked, 0 excluded; 179 active / 72 library.

## Sub-departments → jobs → leads

### direction

| Job | Lead(s) |
| --- | --- |
| `inspiration-taste` | `skill:taste-skill` |
| `category-audit` | `skill:3w-category-code-audit` |
| `concept-direction` | `agent:creative-director`, `skill:3w-creative-direction` |
| `art-direction` | `skill:ceos-art-direction` |
| `verbal-identity` | `anthropic-skills:world-class-copywriter` |

### identity-craft

| Job | Lead(s) |
| --- | --- |
| `typography` | `skill:3w-typography-system` |
| `colour` | `skill:3w-colour-system` |
| `mark-logo` | `skill:3w-mark-exploration` |
| `composition-layout` | `skill:3w-composition-system` |
| `image-generation-direction` | `anthropic-skills:gpt-image-2-director` |
| `design-system-guidelines` | `design-skills:design-systems` |
| `handover-specs` | `design:design-handoff` |
| `presentation` | `anthropic-skills:pptx` |

### experience-design

| Job | Lead(s) |
| --- | --- |
| `interaction-architecture` | `skill:designing-user-experience` |
| `ui-design` | `frontend-design:frontend-design` |
| `motion-principles` | `skill:ceos-motion-direction` |
| `ux-writing` | `design-skills:ux-writing` |
| `experience-prototyping` | `skill:double-diamond` |

### design-qa

| Job | Lead(s) |
| --- | --- |
| `concept-critique` | `agent:creative-auditor`, `skill:3w-identity-system-critic` |
| `ux-audit` | `skill:reviewing-interface-quality` |
| `accessibility` | `design-skills:accessibility-audit` |
| `originality-audit` | `skill:audit-reference-originality` |
| `visual-qa-browser` | `agent:visual-qa-engineer` |
| `consistency-qa` | `skill:3w-brand-consistency-qa` |

## Specialists with activation triggers

| Tool | Job | Trigger |
| --- | --- | --- |
| `agency:design-brand-guardian` | `identity-craft/design-system-guidelines` | When the approved scope specifically requires design system guidelines expertise. |
| `agency:design-image-prompt-engineer` | `identity-craft/image-generation-direction` | When the approved scope specifically requires image generation direction expertise. |
| `agency:design-inclusive-visuals-specialist` | `identity-craft/image-generation-direction` | When the approved scope specifically requires image generation direction expertise. |
| `agency:design-persona-walkthrough` | `design-qa/ux-audit` | When the approved scope specifically requires ux audit expertise. |
| `agency:design-ui-designer` | `experience-design/ui-design` | When the approved scope specifically requires composition layout expertise. |
| `agency:design-ui-finish-gate-reviewer` | `design-qa/consistency-qa` | When the approved scope specifically requires consistency qa expertise. |
| `agency:design-ux-architect` | `experience-design/interaction-architecture` | When the approved scope specifically requires interaction architecture expertise. |
| `agency:design-visual-storyteller` | `identity-craft/presentation` | When the approved scope specifically requires presentation expertise. |
| `agency:engineering-section-508-specialist` | `design-qa/accessibility` | When the approved scope specifically requires accessibility expertise. |
| `agency:engineering-technical-writer` | `identity-craft/handover-specs` | When the approved scope specifically requires handover specs expertise. |
| `agency:product-behavioral-nudge-engine` | `experience-design/interaction-architecture` | When the approved scope specifically requires interaction architecture expertise. |
| `agency:sales-proposal-strategist` | `identity-craft/presentation` | When the approved scope specifically requires presentation expertise. |
| `agency:specialized-document-generator` | `identity-craft/presentation` | An approved guidelines or presentation package needs programmatically generated office documents. |
| `agency:testing-accessibility-auditor` | `design-qa/accessibility` | When the approved scope specifically requires accessibility expertise. |
| `agency:testing-evidence-collector` | `design-qa/visual-qa-browser` | When the approved scope specifically requires visual qa browser expertise. |
| `agency:testing-reality-checker` | `design-qa/consistency-qa` | When the approved scope specifically requires consistency qa expertise. |
| `agency:xr-cockpit-interaction-specialist` | `experience-design/interaction-architecture` | When the approved scope specifically requires interaction architecture expertise. |
| `agency:xr-interface-architect` | `experience-design/interaction-architecture` | When the approved scope specifically requires interaction architecture expertise. |
| `agent:ceo` | `direction/concept-direction` | A flagship assignment or the studio own identity needs a consequential concept or critique decision; use Opus/max. |
| `agent:creative-writer` | `direction/verbal-identity` | When writing studio brand voice, headlines, scripts or identity copy. |
| `agent:ui-ux-architect` | `experience-design/interaction-architecture` | When structuring studio-owned interfaces, flows, states and responsive rules. |
| `agent:ui-ux-pro-max:design-review` | `design-qa/ux-audit` | When the approved scope specifically requires use after front-end changes or when auditing a screen for visual quality, responsiveness, and WCAG 2.1 AA; it drives browser checks and ranks evidence-based findings. |
| `creative-production:produce` | `identity-craft/image-generation-direction` | when creating, adapting, or reviewing brand and visual creative assets |
| `design-skills:design-critique` | `design-qa/ux-audit` | A supplied interaction flow needs a heuristic evaluation with explicit findings. |
| `design-skills:design-elevation` | `identity-craft/composition-layout` | The concept is already approved and a bounded artefact needs formal hierarchy and craft refinement. |
| `design-skills:interaction-design` | `experience-design/interaction-architecture` | A digital application has a named gesture, state-machine or error-prevention problem. |
| `design-steward:align` | `identity-craft/design-system-guidelines` | The founder has made a design decision and existing tokens or design documents must be aligned to it. |
| `design-steward:audit` | `design-qa/ux-audit` | An existing project has conflicting design decisions and needs a cited source/provenance audit. |
| `design-steward:brief` | `identity-craft/handover-specs` | An existing Critic Layer capture needs an implementation brief with stable issue IDs. |
| `design-steward:canon-check` | `design-qa/consistency-qa` | When the approved scope specifically requires existing design decisions conflict or their provenance needs a cited audit. |
| `design-steward:canon-update` | `identity-craft/design-system-guidelines` | The founder has decided a design change and durable system documentation must be aligned. |
| `design-steward:critic-layer` | `design-qa/visual-qa-browser` | An independent reviewer needs an in-browser annotated critique capture. |
| `design-steward:review` | `design-qa/visual-qa-browser` | An independent reviewer needs an annotated browser capture to communicate concrete UI defects. |
| `design-steward:verify` | `design-qa/visual-qa-browser` | When the approved scope specifically requires implemented changes must be checked against an existing Critic Layer issue list and acceptance criteria. |
| `design-superpowers:creative` | `direction/art-direction` | An approved strategy needs rough digital visual-direction alternatives before implementation. |
| `design-superpowers:design` | `experience-design/ui-design` | An existing design system must be used to design a new scoped screen or flow. |
| `design-superpowers:design-review` | `design-qa/consistency-qa` | An enterprise design-system implementation needs a focused compliance review. |
| `design-superpowers:ds-consumer` | `identity-craft/design-system-guidelines` | A digital application must consume an existing enterprise design system without inventing parallel components. |
| `design-superpowers:ds-make` | `identity-craft/design-system-guidelines` | A specified enterprise token, component or pattern needs creation or a versioned change. |
| `design-superpowers:ds-manage` | `identity-craft/design-system-guidelines` | An adopted enterprise design system needs a publishing cascade or adoption/drift review. |
| `design-superpowers:ds-producer` | `identity-craft/design-system-guidelines` | A design-system component or icon needs a producer-side specification and documented lifecycle. |
| `design-superpowers:figma-setup` | `identity-craft/design-system-guidelines` | A design-superpowers Figma workflow explicitly needs PluginOS installation or verification. |
| `design-superpowers:map-design` | `identity-craft/design-system-guidelines` | A supplied screenshot, URL, Figma file or codebase needs its existing design language extracted. |
| `design:accessibility-review` | `design-qa/accessibility` | A supplied design artefact needs a WCAG 2.1 AA review before implementation. |
| `design:design-critique` | `design-qa/ux-audit` | A supplied UI screenshot or Figma design needs a bounded usability/hierarchy critique, separate from the maker. |
| `design:design-system` | `identity-craft/design-system-guidelines` | An existing component system needs a focused naming, state or documentation audit. |
| `design:ux-copy` | `experience-design/ux-writing` | An approved digital touchpoint needs labels, errors, empty states or recovery copy. |
| `figma:figma-create-new-file` | `identity-craft/composition-layout` | A Figma file/workspace exists or is explicitly requested, and the task requires create new file. Load this prerequisite only for its corresponding Figma operation. |
| `figma:figma-generate-design` | `experience-design/ui-design` | A Figma file/workspace exists or is explicitly requested, and the task requires generate design. Load this prerequisite only for its corresponding Figma operation. |
| `figma:figma-generate-diagram` | `identity-craft/presentation` | A Figma file/workspace exists or is explicitly requested, and the task requires generate diagram. Load this prerequisite only for its corresponding Figma operation. |
| `figma:figma-generate-library` | `identity-craft/design-system-guidelines` | A Figma file/workspace exists or is explicitly requested, and the task requires generate library. Load this prerequisite only for its corresponding Figma operation. |
| `figma:figma-spec` | `identity-craft/handover-specs` | A Figma file/workspace exists or is explicitly requested, and the task requires spec. Load this prerequisite only for its corresponding Figma operation. |
| `figma:figma-use` | `identity-craft/composition-layout` | A Figma file/workspace exists or is explicitly requested, and the task requires use. Load this prerequisite only for its corresponding Figma operation. |
| `figma:figma-use-figjam` | `direction/concept-direction` | A Figma file/workspace exists or is explicitly requested, and the task requires use figjam. Load this prerequisite only for its corresponding Figma operation. |
| `figma:figma-use-motion` | `experience-design/motion-principles` | A Figma file/workspace exists or is explicitly requested, and the task requires use motion. Load this prerequisite only for its corresponding Figma operation. |
| `figma:figma-use-slides` | `identity-craft/presentation` | A Figma file/workspace exists or is explicitly requested, and the task requires use slides. Load this prerequisite only for its corresponding Figma operation. |
| `figma:video-interaction-mapper` | `experience-design/interaction-architecture` | A Figma file/workspace exists or is explicitly requested, and the task requires video interaction mapper. Load this prerequisite only for its corresponding Figma operation. |
| `mcp:claude-docs` | `identity-craft/handover-specs` | Approved guidelines or handover specifications must be authored or exchanged through the Claude Docs connector. |
| `mcp:figma` | `identity-craft/design-system-guidelines` | A supplied Figma file or explicitly requested Figma workspace needs inspection, asset access or implementation handoff. |
| `mcp:mobbin` | `direction/inspiration-taste` | A digital interaction question needs source-backed interface reference research; record it under taste/. |
| `mcp:stitch` | `identity-craft/composition-layout` | When the approved scope specifically requires generate or inspect interface prototypes when the server is connected. |
| `open-design:open-design-mode` | `design-qa/visual-qa-browser` | when inspecting an existing interface and making evidence-based design changes |
| `product-design:audit` | `design-qa/ux-audit` | when auditing product flows or interface usability |
| `product-design:design-qa` | `design-qa/consistency-qa` | when checking product UI against a design system or interaction requirements |
| `skill:accessibility` | `design-qa/accessibility` | When the approved scope specifically requires auditing or building accessible digital experiences. |
| `skill:ai-governors` | `design-qa/ux-audit` | When the approved scope specifically requires designing or reviewing human oversight, transparency, consent, and trust signals in AI experiences. |
| `skill:ai-identifiers` | `direction/verbal-identity` | When the approved scope specifically requires defining the brand-level visual, verbal, and behavioral identity of an AI. |
| `skill:ai-inputs` | `experience-design/interaction-architecture` | When the approved scope specifically requires designing AI inputs, controls, onboarding, or discoverability in an AI product. |
| `skill:ai-trust-builders` | `design-qa/ux-audit` | When the approved scope specifically requires designing or reviewing human oversight, transparency, consent, and trust signals in AI experiences. |
| `skill:ai-tuners` | `experience-design/interaction-architecture` | When the approved scope specifically requires designing AI inputs, controls, onboarding, or discoverability in an AI product. |
| `skill:ai-wayfinders` | `experience-design/interaction-architecture` | When the approved scope specifically requires designing AI inputs, controls, onboarding, or discoverability in an AI product. |
| `skill:alina-head-of-website-department` | `direction/concept-direction` | When the approved scope specifically requires starting a studio site, identity touchpoint, or coordinated creative web project. |
| `skill:animate` | `experience-design/motion-principles` | When defining motion purpose, timing, easing, choreography, and reduced-motion behavior. |
| `skill:animation-vocabulary` | `experience-design/motion-principles` | When defining motion purpose, timing, easing, choreography, and reduced-motion behavior. |
| `skill:apple-design` | `experience-design/motion-principles` | When defining motion purpose, timing, easing, choreography, and reduced-motion behavior. |
| `skill:applying-themes` | `identity-craft/design-system-guidelines` | When the approved scope specifically requires applying or authoring a coherent visual theme and design system. |
| `skill:brand-language-codifier` | `direction/verbal-identity` | When defining verbal identity, voice, naming rules, or brand language. |
| `skill:break-ui` | `design-qa/consistency-qa` | When verifying a web touchpoint across responsive layouts, interactions, accessibility, and edge cases. |
| `skill:brutalist-skill` | `direction/inspiration-taste` | When the approved scope specifically requires exploring or applying the aesthetic system described by this skill. |
| `skill:built-in-browser` | `design-qa/visual-qa-browser` | When the studio needs the documented visual qa browser task. |
| `skill:ceos-creative-direction` | `direction/concept-direction` | The studio own digital touchpoint needs a concept narrative; the 3w creative-direction method remains the identity gate. |
| `skill:ceos-interaction-architecture` | `experience-design/interaction-architecture` | When the approved scope specifically requires defining navigation, user journeys, states, and input behavior for a website. |
| `skill:ceos-visual-audit` | `design-qa/visual-qa-browser` | An independent Codex reviewer has real rendered screenshots and needs a prioritised visual defect report. |
| `skill:cognitive-load-conversion` | `design-qa/ux-audit` | When the approved scope specifically requires evaluating cognitive load or persuasion in a conversion flow. |
| `skill:craft` | `design-qa/consistency-qa` | When the approved scope specifically requires designing or improving a distinctive frontend visual composition. |
| `skill:daily-ui-inspiration-capture` | `direction/inspiration-taste` | When the approved scope specifically requires packaging a dated set of interface inspiration references. |
| `skill:dataviz` | `identity-craft/composition-layout` | An approved guidelines or identity application needs charts with supplied, verified data. |
| `skill:design-analysis` | `direction/inspiration-taste` | When the approved scope specifically requires extracting visual properties from a screenshot or live page. |
| `skill:design-first-ui-prompting` | `identity-craft/handover-specs` | When the approved scope specifically requires writing a design-first prompt for a UI generation workflow. |
| `skill:designing-frontend-interfaces` | `experience-design/ui-design` | When the approved scope specifically requires designing or restyling web interfaces with distinctive visual direction. |
| `skill:dieter-rams-principles` | `direction/concept-direction` | When the approved scope specifically requires evaluating or refining a design through Dieter Rams’ principles. |
| `skill:find-animation-opportunities` | `experience-design/motion-principles` | When identifying motion opportunities, auditing existing motion, or extracting interaction patterns from a supplied reference. |
| `skill:general-design-review` | `design-qa/ux-audit` | When the approved scope specifically requires reviewing an existing interface or user flow for usability and quality. |
| `skill:generate-reference-inspired-brand-worlds` | `direction/concept-direction` | When exploring original visual territories from references or comparing several distinct directions. |
| `skill:gpt-tasteskill` | `direction/inspiration-taste` | When the approved scope specifically requires exploring or applying the aesthetic system described by this skill. |
| `skill:gstack-design-review` | `design-qa/concept-critique` | When reviewing a visual artifact for hierarchy, generic patterns, consistency, or actionable design defects. |
| `skill:gstack-design-shotgun` | `direction/concept-direction` | When exploring original visual territories from references or comparing several distinct directions. |
| `skill:gstack-ios-design-review` | `design-qa/visual-qa-browser` | When reviewing a studio-owned iOS interface on a connected device. |
| `skill:gstack-plan-design-review` | `design-qa/concept-critique` | When a design plan needs scored critique before implementation. |
| `skill:html-to-interaction-prompts` | `experience-design/motion-principles` | When identifying motion opportunities, auditing existing motion, or extracting interaction patterns from a supplied reference. |
| `skill:imagegen-frontend-mobile` | `identity-craft/image-generation-direction` | When the approved scope specifically requires generating website or mobile screen design references. |
| `skill:imagegen-frontend-web` | `identity-craft/image-generation-direction` | When the approved scope specifically requires generating website or mobile screen design references. |
| `skill:improve-animations` | `experience-design/motion-principles` | When identifying motion opportunities, auditing existing motion, or extracting interaction patterns from a supplied reference. |
| `skill:interface-design` | `experience-design/interaction-architecture` | When shaping multi-state product UI or defining resilient interaction patterns for a studio-owned app or site. |
| `skill:minimalist-skill` | `direction/inspiration-taste` | When the approved scope specifically requires exploring or applying the aesthetic system described by this skill. |
| `skill:no-ai-design-slop` | `design-qa/consistency-qa` | An independent review identifies generic defaults or established UI defects that require a removal-first check. |
| `skill:onboarding` | `experience-design/interaction-architecture` | Use only when the named content, channel, lifecycle, or campaign task is explicitly in the approved marketing scope. |
| `skill:persuasive-ux` | `design-qa/ux-audit` | When the approved scope specifically requires evaluating cognitive load or persuasion in a conversion flow. |
| `skill:reveal-hover-effect` | `experience-design/interaction-architecture` | The approved concept specifically calls for this effect: reveal-hover-effect. |
| `skill:review-animations` | `design-qa/consistency-qa` | When the approved scope specifically requires use when the task specifically needs reviews animation and motion code against a high craft bar derived from emil kowalski's design engineering philosophy. |
| `skill:scroll-world-storytelling` | `experience-design/motion-principles` | The approved concept specifically calls for this effect: scroll-world-storytelling. |
| `skill:site-structure-optimizer` | `experience-design/interaction-architecture` | Use only when the named content, channel, lifecycle, or campaign task is explicitly in the approved marketing scope. |
| `skill:skeuomorphic-ui` | `identity-craft/design-system-guidelines` | When the approved scope specifically requires use when the task specifically needs create skeuomorphic web ui surfaces with layered gradients, stacked inner and outer shadows, reflective gradient borders, micro texture, and embossed text or icon details. |
| `skill:soft-skill` | `direction/inspiration-taste` | When the approved scope specifically requires exploring or applying the aesthetic system described by this skill. |
| `skill:solar-duotone-bold` | `identity-craft/image-generation-direction` | When the approved scope specifically requires use when the task specifically needs use iconify solar duotone bold icon style. |
| `skill:split-layout-technical` | `identity-craft/composition-layout` | When the approved scope specifically requires use when the task specifically needs create a technical split-screen design system with dual panels, fine frame lines, mono metadata, quiet editorial typography, and premium inset surfaces. |
| `skill:stitch-skill` | `identity-craft/design-system-guidelines` | When the approved scope specifically requires applying or authoring a coherent visual theme and design system. |
| `skill:stitched-full-page-capture` | `design-qa/visual-qa-browser` | When the approved scope specifically requires verifying rendered web touchpoints, interactions, responsive states, or screenshots. |
| `skill:technical-wireframe-info-layout` | `identity-craft/composition-layout` | When the approved scope specifically requires use when the task specifically needs create a monochrome technical wireframe design system with exploded 3d structure, connector annotations, sparse information labels, and precise dark diagnostic framing. |
| `skill:ux-heuristics-review` | `design-qa/ux-audit` | When the approved scope specifically requires reviewing an existing interface or user flow for usability and quality. |
| `skill:ux-storyboard` | `experience-design/experience-prototyping` | When the approved scope specifically requires representing user needs, journeys, or experience narratives. |
| `skill:video-to-superprompt` | `direction/inspiration-taste` | When the approved scope specifically requires analyzing a reference video for its design and interaction principles. |
| `stitch-design:extract-design-md` | `identity-craft/design-system-guidelines` | An existing frontend must be translated into a semantic DESIGN.md before Stitch work. |
| `stitch-design:manage-design-system` | `identity-craft/design-system-guidelines` | An existing Stitch project needs design-system assets or token changes applied through Stitch MCP. |
| `stitch-utilities:design-md` | `identity-craft/design-system-guidelines` | An existing Stitch project needs its design language documented in DESIGN.md. |
| `stitch-utilities:site-md` | `experience-design/interaction-architecture` | Use when the approved work needs this capability: Analyze a project description or site requirements and synthesize a project constitution into SITE.md for the Stitch Build Loop |
| `stitch-utilities:taste-design` | `identity-craft/composition-layout` | An approved Stitch project needs a restrained semantic design-system prompt; its preset aesthetics remain subordinate to the concept. |
| `ui-ux-pro-max:banner-design` | `identity-craft/composition-layout` | An explicitly agreed identity application needs a banner composition at specified dimensions. |
| `ui-ux-pro-max:brand` | `identity-craft/composition-layout` | A supplied brand guideline or asset library needs a bounded voice/identity consistency operation. |
| `ui-ux-pro-max:design-system` | `identity-craft/design-system-guidelines` | A digital design system needs a primitive/semantic/component token architecture. |
| `ui-ux-pro-max:ui-ux-pro-max` | `direction/art-direction` | A constrained digital interface needs searchable platform, type, palette or component guidance. |
| `vectorlab-ux-skills:anti-slop` | `design-qa/visual-qa-browser` | A supplied generated interface exhibits a specific decorative cliche that needs removal. |
| `vectorlab-ux-skills:colour-palette` | `identity-craft/colour` | A digital palette needs role/distribution checks after the human colour direction is approved. |
| `vectorlab-ux-skills:defaults` | `experience-design/interaction-architecture` | A defined form or preferences flow needs useful defaults or draft persistence. |
| `vectorlab-ux-skills:empty-states` | `experience-design/interaction-architecture` | A defined empty or filtered-zero state needs a next action. |
| `vectorlab-ux-skills:errors` | `experience-design/ux-writing` | A defined failure state needs blame-free recovery copy. |
| `vectorlab-ux-skills:forms` | `experience-design/interaction-architecture` | An approved form needs field reduction or blur-validation behaviour. |
| `vectorlab-ux-skills:icon-buttons` | `experience-design/interaction-architecture` | A supplied toolbar needs icon-only controls with labels, tooltips and shortcuts. |
| `vectorlab-ux-skills:keyboard` | `design-qa/accessibility` | A specified modal, shortcut or interactive control needs focus containment and restoration. |
| `vectorlab-ux-skills:labels` | `experience-design/ux-writing` | A supplied form is missing persistent visible labels. |
| `vectorlab-ux-skills:loaders` | `experience-design/interaction-architecture` | A measured asynchronous wait needs the correct feedback pattern for its duration. |
| `vectorlab-ux-skills:motion` | `experience-design/motion-principles` | An approved digital interaction needs consistent duration/easing tokens. |
| `vectorlab-ux-skills:page-patterns` | `experience-design/ui-design` | A digital screen lacks a named structural pattern and the adopted product system needs one. |
| `vectorlab-ux-skills:reduced-motion` | `design-qa/accessibility` | A supplied motion treatment needs a tested prefers-reduced-motion alternative. |
| `vectorlab-ux-skills:setup-ui-ux-skills` | `experience-design/ui-design` | A digital project explicitly adopts VectorLab and needs its one-time reference and access-target setup. |
| `vectorlab-ux-skills:spacing` | `identity-craft/composition-layout` | A supplied layout has a measured alignment, spatial-rhythm or line-length defect. |
| `vectorlab-ux-skills:surfaces` | `experience-design/interaction-architecture` | A specified edit flow needs a decision between inline editing, a drawer or a dedicated page. |
| `vectorlab-ux-skills:typography` | `identity-craft/typography` | A supplied digital type hierarchy has a scale, weight or line-height defect. |
| `vectorlab-ux-skills:ux-audit` | `design-qa/ux-audit` | A supplied digital interface explicitly adopts the VectorLab rules and needs its independent preflight. |
| `vectorlab-ux-skills:verbs` | `experience-design/ux-writing` | An approved interface needs verb-first action labels. |
| `vectorlab-ux-skills:viewports` | `design-qa/visual-qa-browser` | A supplied layout overflows or loses usability between 375px and 1280px. |
| `agent:visual-designer` | `identity-craft/typography` | An approved brand type and colour system must be converted into digital tokens, a type ramp, measured contrast table and grid specification for a build. |
| `skill:3w-taste-graph` | `direction/inspiration-taste` | Before any creative-output task, load a Taste Graph reference pack for the brief (AGENTS.md; D-0020). |

## Bench and parked summary

- **bench: 71.** `agency:design-whimsy-injector`, `frontend-design-premium:frontend-design-premium`, `product-design:ideate`, `product-design:index`, `skill:agency-grid-layout-minimal`, `skill:audit-ai-design-slop`, `skill:aura-asset-images`, `skill:beautiful-shadows`, `skill:blue-cloudy-clean-modern`, `skill:blue-laser-clean-glass-layout`, `skill:book-serif-index`, `skill:bright-green-tech-system-webgl`, `skill:build-daily-inspiration-sites`, `skill:chrome-browser`, `skill:clean-minimal-beige-light-mode`, `skill:company-logos`, `skill:container-lines`, `skill:corner-diagonals`, `skill:corner-lasers`, `skill:cro`, `skill:css-alpha-masking`, `skill:dark-blue-contrasting-clean`, `skill:dark-glass-clean-layout`, `skill:dither-laser-dark-mode`, `skill:documentary-brutalist-agency`, `skill:editorial-portfolio-chapters`, `skill:editorial-service-booking`, `skill:editorial-tech`, `skill:emil-design-eng`, `skill:framed-grid-layout`, `skill:framed-tech-dark-border-gradient`, `skill:funky-purple-container-tech`, `skill:glass-dark-mode-clock`, `skill:glass-dark-ui`, `skill:gstack-browse`, `skill:gstack-design-consultation`, `skill:gstack-diagram`, `skill:high-contrast-skeuomorphic-clean`, `skill:image-first-grid-layout`, `skill:impeccable`, `skill:landing-optimizer`, `skill:landing-page`, `skill:light-mode-paper-technical`, `skill:like-wish-what-if`, `skill:master-of-visual-design`, `skill:mesh-gradient-dark-blue-clean`, `skill:nested-container-clean-agency`, `skill:nested-container-frames`, `skill:number-details`, `skill:operational-enterprise-ai`, `skill:orange-clean-paper-saas`, `skill:paywalls`, `skill:popups`, `skill:product-proof-saas`, `skill:redesign-skill`, `skill:signup`, `skill:site-architecture`, `skill:tech-green-dark-mode-modern`, `skill:unsplash-asset-images`, `skill:web-design-guidelines`, `stitch-design:code-to-design`, `stitch-design:generate-design`, `stitch-design:upload-to-stitch`, `stitch-utilities:enhance-prompt`, `superdesign:superdesign`, `ui-ux-pro-max:design`, `ui-ux-pro-max:slides`, `ui-ux-pro-max:ui-styling`, `visualize:visualize`, `watch:watch`, `wix:wix-design-system`
- **parked: 1.** `skill:prototype`
- **excluded: 0.** None.

Individual reasons and activation requirements are in the [canonical registry](../../toolkit/sources/registry.json). Library means callable by explicit name after review; it is not loaded by default.

## Gaps

Experimental craft leads now cover colour, mark-logo and composition-layout.
Human approval remains mandatory; [delivery subjob gaps](registry-summary.md#designengineering-lead-gaps) cover export/archive coordination, physical proofing and fluent native-language verification.

## Counts by sub-department and role

| Sub-department | Lead | Specialist | Bench | Parked | Excluded | Active | Library | Total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| direction | 6 | 21 | 5 | 0 | 0 | 27 | 5 | 32 |
| identity-craft | 8 | 49 | 34 | 0 | 0 | 57 | 34 | 91 |
| experience-design | 5 | 42 | 28 | 1 | 0 | 47 | 29 | 76 |
| design-qa | 7 | 41 | 4 | 0 | 0 | 48 | 4 | 52 |

## Operating contract

Use the job lead first and a specialist only on its trigger. Maker and checker must be separate people/agent instances; a reviewer never approves its own department alone. Proposed `load: active` is the desired loading policy, while the source inventory records installation presence. No physical activation was performed.

Design and Engineering prototype together early; the handoff names artefacts, constraints, budgets and evidence rather than creating a wall. Human judgement and founder approval remain separate from tool routing.

Cultural intelligence lives in Strategy/culture-behaviour. Design QA may call `agency:specialized-cultural-intelligence-strategist` as an independent reviewer without duplicating its home.

## Quality rules and gates

1. **Strategy first.** Verify the approved strategy, criteria, constraints,
   approver, date and version before concept development. Draft-strategy
   critique remains formative and cannot authorise production.
2. **At least three distinct routes at each concept stage.** Each route must
   have a different organising idea, describable without visual adjectives.
   Changes of colour, typeface or texture alone are variations, not routes.
3. **Kill, do not polish.** Nothing advances below the exact verdict
   “Strong enough to advance”. Revise or reject the idea before spending on
   finish. A technically competent but conceptually weak route still fails.
4. **Maker ≠ checker; two independent passes.** First review concept,
   strategy fit and audience assumptions. Then review formal craft and
   implementation against actual artefacts. Separate reviewers, evidence and
   verdicts from the maker; record who made and who checked each version.
5. **Originality before anything leaves the studio.** Run
   `audit-reference-originality` against the actual sources in `taste/` and
   the category audit. Flag templates, distinctive copying, the generic
   awards-site look and [D-0006's rejected vocabulary](../decisions/0006-rejected-own-identity-direction.md):
   black backgrounds combined with heavy grotesk type and neon accents.
   Check form, copy, imagery and motion, not only logo similarity. This is
   evidence-based creative review, not legal clearance.
6. **Real evidence; mockups are not evidence.** Inspect actual vector/raster
   exports from a 16px favicon to large format, monochrome and reverse;
   measure contrast and test real scripts, text and print proofs. Digital
   work needs real screenshots at desktop/tablet/mobile widths, exercised
   interactions, keyboard/focus checks, reduced-motion evidence, clean console
   and measured Core Web Vitals. Label lab measurements and field data
   separately. Print needs physical/vendor proofs with stock, inks, process
   and size recorded. Record unrun checks as Unknown or not verified.
7. **Typography and craft are human-led.** AI may extend exploration and
   prepare variations/exports; a designer makes optical, cultural, language,
   rights, material and production judgements. Persona expertise claims and
   generated imagery do not prove audience response or production quality.
8. **Best model at every gate.** Use Opus for direction and critique; use
   `ceo` for flagship and own-identity decisions. Use the strongest available
   suitable model for craft and evidence review. Cheaper models handle only
   already-directed variations, mechanical preparation and exports. Never
   lower the gate because a preferred model is unavailable; record the gap.
9. **Founder sign-off ends each sub-department.** The reviewer recommends;
   the founder records a decision against a named artefact version. This
   guide and tool output never promote material to approved automatically.

Use **Documented**, **Interpretation**, **Hypothesis** and **Unknown** exactly.
Audience meaning, memory and preference remain hypotheses without observed
research. Follow the [critique protocol](../../methods/quality/critique-protocol.md)
and [identity testing matrix](../../methods/quality/identity-system-testing.md).

## Handoffs

| Stage | Required handoff and independent check | Human gate |
| --- | --- | --- |
| Strategy approved → Direction | Signed strategy; sourced discovery/category audit; three idea routes; concept and audience-assumption critique. | Founder selects a route for development. |
| Direction → Identity Craft | Idea sentence, never-copy list, rationale, reference sources and approved constraints; independent concept verdict. | Founder signs direction. |
| Identity Craft → Experience Design | Versioned marks, type/colour/composition rules, image direction, real-scale evidence and application scope; independent formal/consistency check. | Founder signs craft. |
| Experience Design → delivery | Motion/interaction rules, real exports, three-width browser evidence where relevant, reduced motion, performance and print proofs; independent implementation check. | Founder signs living applications. |
| Design QA at every handoff → release | Separate concept and formal/implementation passes, originality report, unresolved findings, rights and acceptance record. | Founder signs QA and authorises release. |

Every handoff includes maker, checker, artefact version, evidence links,
verdict, unknowns, next owner and founder decision. Return a failed gate to
its responsible maker. Do not hide a failed idea inside presentation polish.

## Choose a tool

Choose the job, then its lead first. Use a specialist only when its named
trigger applies. Use one primary tool for the job; never chain overlapping
routers or critiques in pursuit of an averaged answer. Required tool-specific
prerequisites may accompany that tool, but do not become competing leads.

Bench means installed but not routed, with a stated reason. Reconsider a
benched tool only with a bounded comparison and founder decision. Availability
means the instructions or declaration were found for that provider; it does
not establish authentication, connectivity, licence or output quality.

`repo` tools travel with this checkout. Local tools do not. A broken MCP stays
on the bench until its connection and a meaningful operation are verified.
Tool count is coverage evidence, not a quality score.
