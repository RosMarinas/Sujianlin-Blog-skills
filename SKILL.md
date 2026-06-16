---
name: cognitive-knowledge-network
description: Use when an agent needs to explore the compiled Su Jianlin blog library for concepts, methods, transferable problem patterns, source evidence, raw markdown, or architecture-design inspiration.
---

# 认知型知识网络技能

Use this skill when an agent needs to explore the compiled Su Jianlin blog library for concepts, methods, transferable problem patterns, source evidence, or architecture-design inspiration.

This skill is a research navigation layer, not a workflow controller. It should guide the agent through the library, expose structure, keep sources traceable, and help produce reusable research materials. It must not replace the agent's own judgment about search depth, abstraction, transfer, or final conclusions.

---

## Before your first query

Read these to understand the library's model and boundaries:

1. `purpose.md` — what this library is for (and what it isn't)
2. `schema.md` — how data is organized: page types, graph structure, evidence rules
3. `docs/superpowers/specs/2026-06-09-认知型知识网络-顶层设计文档.md` — architectural context

## Quick start

The library uses two core node types:

- **concept** — semantic anchors: definitions, roles, formulas, proposition contexts
- **method** — transfer hubs: generative moves that turn a problem structure into a transformed representation and a result

Start with:

- `search_concept(query)` / `search_method(query)` — find nodes by keyword or alias
- `lookup_node(node_id)` — read a single node's data
- `expand_node(node_id, depth=1)` — explore connected nodes via edges
- `resolve_source(article_id)` — get the readable source path for an article
- `read_source(article_id, section=..., line_range=...)` — read source content

For deeper queries, use `inspect_concept()`, `inspect_method()`, or `find_reading_path()`.

## Repo boundaries

- Resolve the shared library root from `SUJIANLIN_LIBRARY_ROOT`; if unset, use the current repo root.
- Read from the shared library root, especially `graph/`, `Data/Spaces_ac_cn/markdown/`, and `Data/Spaces_ac_cn/assets/`.
- Treat `wiki/` as an optional human-readable compiled layer. Do not rely on it for runtime source lookup or method filtering.
- Write only to derived layers owned by the current task, such as `graph/`, `probes/`, `skill/`, or `wiki/` when explicitly compiling wiki pages.
- Treat unsupported summaries and edges as tentative until evidence-backed
- Do not write agent Search Logs or research summaries into `wiki/`. Complex-query logs follow the calling project or problem and belong under that project's `docs/research/`.

## Agent contract

- Judge query depth before searching. Simple confirmation should stay shallow; research-oriented architecture questions should not stop at a single lookup.
- Use routes freely. The agent may start from articles, concepts, methods, examples, formulas, propositions, source summaries, or raw markdown.
- Prefer concept/method organization when summarizing what was learned.
- Distinguish source levels in final writing: direct source support, graph/structured support, optional wiki support, agent synthesis, and transfer speculation.
- Raw markdown is normal library material, not a fallback. Use it when details, context, or re-abstraction require the original text, and record why it was read.

## Query depth guide

- Level 1 — quick confirmation: check whether an concept, article, formula, or method exists.
- Level 2 — local understanding: read a concept/method/source and nearby context.
- Level 3 — chain reconstruction: recover a derivation, method-use path, or series progression; create a Search Log and brief report.
- Level 4 — system exploration: compare methods or extract transferable structures across articles; create full research artifacts.
- Level 5 — deep dive: build a theme-level methodology map; Search Log is a primary artifact.

## When you need a specific function

→ `skill/docs/api.md` — full API reference by capability group

Covers: source locator, research navigation, research artifacts, point/series/expansion/path/method/transfer queries, evidence verification.

## When exploring search strategies

→ `skill/docs/examples.md` — concrete query examples by scenario

Shows point queries, series queries, expansion, path finding, method lookup, transfer analysis, and evidence verification with real topic examples.

## Runtime requirements

- `graph/`: required machine index for node, edge, evidence, and concept/method navigation APIs.
- `Data/Spaces_ac_cn/markdown/`: required original readable source layer.
- `Data/Spaces_ac_cn/assets/`: required companion asset layer for article images.
- `wiki/`: optional human-readable compiled layer.
- `probes/`: optional validation and quality-diagnostic layer.

Source access must prefer `Data/Spaces_ac_cn/markdown/` and `Data/Spaces_ac_cn/assets/`. `raw/`, `manifest.jsonl`, `reports/`, and `samples/` are auxiliary index, provenance, validation, or debugging material — not default research objects.

For Level 3+ work, create research artifacts in the calling project's `docs/research/YYYY-MM-DD-<query-slug>/`. Do not write these artifacts into this library's `wiki/`.
