---
title: Webassembly Engineer Agent
type: tool-card
status: proposed
owner: founder
last_reviewed: 2026-10-23
tool_id: agency:engineering-webassembly-engineer
department: engineering
sub_department: creative-engineering
job: creative-prototyping
role: specialist
trigger: "Use for engineering/creative-engineering/creative-prototyping when the brief specifically requires: Expert WebAssembly engineer — compiling Rust/C++/Go to Wasm, JS interop and the boundary marshalling cost, WASI and server-side runtimes (Wasmtime/Wasmer), the component model, and near-native performance tuning ."
kind: upstream-agent
availability: repo
distribution: vendor
source: .claude/agents/engineering-webassembly-engineer.md
invoke: "Agent tool: engineering-webassembly-engineer"
pairs_with: [agency:engineering-rapid-prototyper, playground:playground]
---
# Webassembly Engineer Agent

Webassembly Engineer Agent is the specialist when Use for engineering/creative-engineering/creative-prototyping when the brief specifically requires: Expert WebAssembly engineer — compiling Rust/C++/Go to Wasm, JS interop and the boundary marshalling cost, WASI and server-side runtimes (Wasmtime/Wasmer), the component model, and near-native performance tuning . at 3RDWRONG.

## What it does

- Expert WebAssembly engineer — compiling Rust/C++/Go to Wasm, JS interop and the boundary marshalling cost, WASI and server-side runtimes (Wasmtime/Wasmer), the component model, and near-native performance tuning
- Organises the method around 🧠 your identity & memory
- Role: WebAssembly and Wasm-runtime specialist across browser (Emscripten/wasm-bindgen) and server-side (WASI, Wasmtime/Wasmer, the component model)
- Personality: Boundary-obsessed, benchmark-driven, allergic to premature Wasm, precise about what the sandbox does and doesn't give you
- Memory: You remember which workloads paid off in Wasm and which lost to marshalling overhead, the memory-growth cliff that fragmented a heap, and the toolchain flag that halved a binary

## When to use

- Use for engineering/creative-engineering/creative-prototyping when the brief specifically requires: Expert WebAssembly engineer — compiling Rust/C++/Go to Wasm, JS interop and the boundary marshalling cost, WASI and server-side runtimes (Wasmtime/Wasmer), the component model, and near-native performance tuning .

## When not to use

- When the approved brief does not call for creative prototyping; use the smallest relevant implementation method.
- To independently approve its own work; use a separate reviewer and the relevant QA tool.
- When required inputs or platform prerequisites are missing; clarify them before implementation.

## Inputs it needs

- Approved brief, intended audience, success criteria and project status.
- Relevant design, code, platform, device and integration context named by the source.
- Constraints and reference artefacts; mark unsupported assumptions Unknown.

## How to run it

1. Check that the brief matches the registry trigger and the source's documented scope.
2. Provide the inputs and constraints above; load or invoke `agency:engineering-webassembly-engineer`.
3. Review the output against the quality checks and pass it to an independent checker.

```text
Use agency:engineering-webassembly-engineer for {project}. Approved brief and success criteria: {link}. Relevant artefacts and platform: {links and versions}. Constraints: {performance, accessibility, delivery}. Work only within the source's documented scope. Label evidence Documented, Interpretation, Hypothesis or Unknown; return findings, assumptions, limitations and a concrete next action.
```

## What good output looks like

- Addresses the registry job and trigger with a concrete artefact, recommendation or implementation handoff.
- Makes assumptions and undocumented capabilities explicit; links findings to provided evidence.
- States constraints, unresolved risks and a next action suitable for independent review.

## Quality checks

- [ ] A reviewer other than the maker checks each source-specific requirement against the brief.
- [ ] Claims are supported by the source or supplied evidence; unknowns are labelled.
- [ ] Platform, responsive behaviour, accessibility and performance constraints are checked where applicable.
- [ ] No client data or secrets are committed to a public repository.

## Pairs with

- `agency:engineering-rapid-prototyper`: coordinate inputs and hand off the reviewed result.
- `playground:playground`: coordinate inputs and hand off the reviewed result.

## Limits and cautions

- Do not use beyond the documented scope; if a capability or outcome is absent from the source, treat it as Not documented.
- Keep client data out of the public repository (D-0021); apply maker ≠ checker and label evidence as Documented, Interpretation, Hypothesis or Unknown.
