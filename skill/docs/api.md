# Skill API

The local agent interface is organized into seven capability groups plus a research-artifact contract for complex queries.

The capability groups are a toolbox. They should guide exploration without forcing a fixed route.

## Library root

The Python API resolves the shared library root from `SUJIANLIN_LIBRARY_ROOT`.
If the variable is unset, it uses the current repo root.

Required runtime directories:

- `graph/`: machine index for nodes, edges, evidence spans, and navigation.
- `Data/Spaces_ac_cn/markdown/`: readable original source layer.
- `Data/Spaces_ac_cn/assets/`: companion asset layer.

Optional runtime directories:

- `wiki/`: human-readable compiled layer for review and browsing. Runtime source lookup and method filtering must not require it.
- `probes/`: quality diagnostics and validation outputs. Missing `probes/` only disables probe-based diagnostics such as failure listing.

## Research artifacts for complex queries

For Level 3 or deeper queries, the calling agent should create research artifacts in the caller's current project, not in this library's `wiki/`:

```text
docs/research/YYYY-MM-DD-<query-slug>/
  materials.md
  search-log.md
  brief-report.md
```

Recommended content:

- `materials.md`: nodes, articles, source summaries, raw markdown spans, methods, concepts, examples, and paths used.
- `search-log.md`: query intent, depth, entry points, exploration trace, concept pool, method pool, source/raw anchors, transfer candidates, failed or weak paths, open threads, and working understanding.
- `brief-report.md`: problem restatement, core findings, methodology abstraction, architecture inspiration, evidence/source levels, uncertainty, and follow-up directions.

Search Logs follow the agent's project or problem. They are not wiki pages, graph nodes, probes, or stable knowledge artifacts.

## Source levels

Complex-query reports should distinguish:

- Direct source support: raw markdown or explicit evidence span.
- Structured support: graph node, graph edge, source index, optional wiki page, or probe result.
- Agent synthesis: conclusion built from multiple library materials.
- Transfer speculation: architecture or research idea proposed beyond the source text.

Stable wiki/graph additions still require the evidence rules defined in `schema.md`.

## Source locator

- `resolve_source(article_id)`
- `resolve_sources_for_node(node_id)`
- `resolve_evidence(evidence_id)`
- `read_source(article_id, section=None, line_range=None, max_lines=120)`
- `list_source_assets(article_id)`
- `source_link(article_id, line_range=None, mode="repo")`

The effective original library contains only `Data/Spaces_ac_cn/markdown/` and `Data/Spaces_ac_cn/assets/`.
`manifest.jsonl`, `raw/`, `reports/`, and `samples/` are auxiliary index, provenance, validation, or debugging material.

Source resolution order is data-side and wiki-independent:

1. `graph/source_index.jsonl`, when present.
2. Article node fields such as `source_markdown`, `markdown_path`, `source_url`, and `source_page`.
3. Evidence span `source_path`.
4. `Data/Spaces_ac_cn/manifest.jsonl` as an auxiliary index.

## Concept / method research navigation

- `search_concept(query)`
- `inspect_concept(node_id, depth=1)`
- `inspect_method(method_id)`
- `suggest_transfer_angles(query)`

These helpers organize results around the concept/method dual core. They return structured context for agent judgment; they do not promote transfer speculation into wiki or graph.

## Research artifact helpers

- `suggest_research_folder(query, date=None)`
- `make_materials_template(query)`
- `make_search_log_template(query, depth="Level 3")`
- `make_brief_report_template(query)`

These helpers produce paths and template text only. The calling agent decides whether and where to write files under the calling project's `docs/research/`.

## Point query

- `search_node(query)`
- `read_node(node_id)`
- `get_sources(node_id)`

## Series query

- `search_series(query)`
- `read_series(series_id)`
- `get_series_order(series_id)`
- `get_series_gaps(series_id)`

## Expansion query

- `expand_node(node_id, depth=2, edge_types=None)`
- `rank_neighbors(node_id)`

## Path query

- `find_path(source, target, constraints=None)`

## Method query

- `search_method(query, include_scaffold=False)`
- `get_examples(method_id)`
- `get_problem_patterns(method_id)`

By default, `search_method` returns stable Method nodes that are answer-ready according to graph-side metadata. Supported markers are `quality_pass: true`, `answer_ready: true`, `quality.answer_ready: true`, or `method_contract.answer_ready: true`. Existing stable methods without an explicit marker remain visible for backward compatibility; set `include_scaffold=True` when exploring draft or explicitly non-ready Method nodes as jump points rather than answer context.

## Transfer query

- `find_shared_pattern(node_id)`
- `find_analogies(method_id)`
- `suggest_transfer(source_problem)`

## Evidence verification

- `verify_with_source(claim)`
- `get_evidence(node_id)`
- `trace_claim(claim)`
