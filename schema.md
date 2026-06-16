# Schema

This file defines the stable page, graph, and quality-loop contracts for the compiled knowledge network.

## Wiki page types

- `article_summary`
- `series`
- `topic`
- `concept`
- `formula`
- `proposition`
- `method`
- `problem_pattern`
- `example`
- `reading_path`
- `synthesis`

All wiki pages use YAML frontmatter with this minimum shape:

```yaml
---
type:
title:
aliases:
sources:
  - Data/Spaces_ac_cn/markdown/...
source_ids:
  - "11767"
status: draft | stable | candidate | deprecated
updated:
---
```

## Wiki file naming conventions

| Page type | Directory | Naming pattern | Example |
|-----------|-----------|----------------|----------|
| article_summary | wiki/sources/ | spaces-{id}-{slug}.md | spaces-11767-矩阵参数的奇异值熵越高越好吗.md |
| series | wiki/series/ | {series-name}.md | 基于流式幂迭代的Muon实现.md |
| topic | wiki/topics/ | {topic-name}.md | 矩阵优化.md |
| concept | wiki/concepts/ | {concept-name}.md | 奇异值熵.md |
| formula | wiki/formulas/ | {formula-name}.md | 香农熵.md |
| proposition | wiki/propositions/ | {proposition-slug}.md | 奇异值熵不必最大化.md |
| method | wiki/methods/ | {method-description}.md | 从几何图景转化概率问题.md |
| problem_pattern | wiki/problem_patterns/ | {pattern-description}.md | 将经验判断转化为可计算命题.md |
| example | wiki/examples/ | spaces-{id}-{example-slug}.md | spaces-11767-奇异值熵密度推导.md |
| reading_path | wiki/reading_paths/ | {path-name}.md | Muon与矩阵优化阅读路径.md |
| synthesis | wiki/topics/ | {synthesis-name}.md | (shares directory with topics) |

## Page-type specific frontmatter

Common rules:

- `type`, `title`, `sources`, `source_ids`, `status`, and `updated` are required for every page type.
- `aliases` is optional for every page type and should be an empty list when no alias is known.
- `sources` must use repo-relative `Data/Spaces_ac_cn/...` paths, not `spaces_ac_cn/...`.
- `source_ids` must be strings, not numbers.
- `status` must be one of `draft`, `stable`, `candidate`, or `deprecated`.
- `updated` must be an ISO date in `YYYY-MM-DD` form.
- Stable claims require at least one `evidence_spans` entry or a directly cited source section.
- Draft pages without `evidence_spans` must include `null_evidence_reason` explaining why evidence is absent or deferred.
- `type` values must be bare YAML strings (e.g., `type: method`), never JSON-quoted (e.g., `type: "method"`).

### article_summary

```yaml
---
type: article_summary
title: # required
article_id: # required, e.g. "11767"
source_url: # required, e.g. https://spaces.ac.cn/archives/11767
date: # required, original publication date
category: # required, Mathematics | Big-Data
source_markdown: # required, path relative to repo root
source_html: # optional, path relative to repo root
series: # optional, list of series page wikilinks
topics: # optional, list of topic wikilinks
concepts: # optional, list of concept wikilinks
methods: # optional, list of method wikilinks
problem_patterns: # optional, list of problem_pattern wikilinks
evidence_spans: # optional, list of evidence_span ids
sources:
  - Data/Spaces_ac_cn/markdown/...
source_ids:
  - "11767"
status: draft | stable | candidate | deprecated
updated: # ISO 8601 date
---
```

### series

```yaml
---
type: series
title: # required
aliases: # optional, alternate names
article_ids: # required, ordered list of article ids in this series
sources: # required, list of source markdown paths
source_ids: # required, same ids as article_ids unless the page cites additional sources
series_goal: # required, one-sentence problem solved by the series
entry_roles: # required, map of article id -> role in the series
key_concepts: # required, list of concept wikilinks
key_methods: # required, list of method wikilinks
reading_paths: # optional, list of reading_path wikilinks
status: draft | stable | candidate | deprecated
updated: # ISO 8601 date
---
```

### topic

```yaml
---
type: topic
title: # required
aliases: # optional
scope: # required, what belongs in this topic
sources: # required
source_ids: # required
series: # optional, list of series wikilinks
concepts: # required, list of concept wikilinks
formulas: # optional, list of formula wikilinks
propositions: # optional, list of proposition wikilinks
methods: # optional, list of method wikilinks
problem_patterns: # optional, list of problem_pattern wikilinks
reading_paths: # optional, list of reading_path wikilinks
open_questions: # optional, list of known gaps
status: draft | stable | candidate | deprecated
updated: # ISO 8601 date
---
```

### concept

```yaml
---
type: concept
title: # required
aliases: # optional
definition: # required, concise working definition
standard_notation: # optional, canonical symbols used by this wiki for this concept
sources: # required
source_ids: # required
prerequisites: # optional, list of concept/formula wikilinks
equivalent_forms: # optional, list of formula/proposition wikilinks
direct_consequences: # optional, list of proposition wikilinks
related_formulas: # optional, list of formula wikilinks
related_methods: # optional, list of method wikilinks
series: # optional, list of series wikilinks
evidence_spans: # required for stable concepts
status: draft | stable | candidate | deprecated
updated: # ISO 8601 date
---
```

### formula

```yaml
---
type: formula
title: # required
aliases: # optional
latex: # required, canonical formula body
symbol_meanings: # required, map/list explaining symbols
standard_notation: # required, canonical symbol choices used by this wiki
conditions: # required, assumptions under which the formula holds
sources: # required
source_ids: # required
derived_from: # optional, list of formula/proposition wikilinks
implies: # optional, list of proposition wikilinks
appears_in: # required, list of article_summary wikilinks
evidence_spans: # required for stable formulas
status: draft | stable | candidate | deprecated
updated: # ISO 8601 date
---
```

### proposition

```yaml
---
type: proposition
title: # required
aliases: # optional
statement: # required
assumptions: # required, list of prerequisites/conditions
sources: # required
source_ids: # required
requires: # optional, list of concept/formula/proposition wikilinks
proof_route: # required, concise proof or derivation outline
methods: # optional, list of method wikilinks
limits: # optional, applicability limits or counterexamples
examples: # optional, list of example wikilinks
evidence_spans: # required
status: draft | stable | candidate | deprecated
updated: # ISO 8601 date
---
```

### method

```yaml
---
type: method
title: # required, description of the method
aliases: # optional
operation_types: # required, from the 9-type taxonomy in the workflow doc Phase 9
  primary: # required, e.g. decompose / reduce dimension
  secondary: # optional, list of additional types
sources: # required, articles where this method appears
source_ids: # required
method_summary: # required, what generative move the method performs
typical_structure: # required, step list or structured outline
applicability: # required, when to activate this method
tools: # optional, mathematical tools commonly used
examples: # required, list of example/article wikilinks
problem_patterns: # optional, list of problem_pattern wikilinks
related_methods: # optional, list of method wikilinks
evidence_spans: # required for stable methods
status: draft | stable | candidate | deprecated
updated: # ISO 8601 date
---
```

Method hierarchy (high-level transferable generative moves vs. low-level domain implementations) is expressed through `generalizes` / `specializes` graph edges, not through a `method_level` field. Both levels use `type: method`.

### problem_pattern

```yaml
---
type: problem_pattern
title: # required
aliases: # optional
pattern_summary: # required, reusable problem shape
trigger_questions: # required, questions that identify this pattern
sources: # required
source_ids: # required
activates_methods: # required, list of method wikilinks
typical_prerequisites: # optional, concept/formula wikilinks
examples: # required, list of example/article wikilinks
failure_modes: # optional, common wrong paths or overgeneralizations
evidence_spans: # required for stable patterns
status: draft | stable | candidate | deprecated
updated: # ISO 8601 date
---
```

### example

```yaml
---
type: example
title: # required
aliases: # optional
article_id: # required
article: # required, article_summary wikilink
section: # required, source section title
claim: # required, what this example demonstrates
notation_mapping: # required, map from wiki standard notation to source-local notation
steps: # required, ordered derivation/proof/application steps
used_concepts: # required, list of concept wikilinks
used_formulas: # optional, list of formula wikilinks
used_methods: # optional, list of method wikilinks
problem_pattern: # optional, problem_pattern wikilink
source_span: # required, evidence_span id
sources: # required
source_ids: # required
status: draft | stable | candidate | deprecated
updated: # ISO 8601 date
---
```

### reading_path

```yaml
---
type: reading_path
title: # required
aliases: # optional
goal: # required, what the path helps a reader learn
audience: # required, intended reader state
ordered_nodes: # required, ordered list of article/topic/concept/series wikilinks
source_ids: # required, ids touched by the path
sources: # required
prerequisites: # optional
checkpoints: # required, questions the reader should answer along the path
next_paths: # optional
status: draft | stable | candidate | deprecated
updated: # ISO 8601 date
---
```

### synthesis

```yaml
---
type: synthesis
title: # required
aliases: # optional
synthesis_question: # required, cross-topic question being answered
scope: # required, included and excluded areas
sources: # required
source_ids: # required
topics: # required, list of topic wikilinks
claims: # required, source-backed claims
open_questions: # optional
evidence_spans: # required for stable synthesis pages
status: draft | stable | candidate | deprecated
updated: # ISO 8601 date
---
```

## Graph node types

- `article`
- `series`
- `topic`
- `concept`
- `formula`
- `proposition`
- `method`
- `problem_pattern`
- `example`
- `reading_path`
- `evidence_span`

## Preferred edge types

- `defines`
- `uses`
- `requires`
- `derives`
- `equivalent_to`
- `generalizes`
- `specializes`
- `motivates`
- `solves`
- `belongs_to`
- `contains`
- `precedes`
- `continues`
- `is_example_of`
- `expresses_method`
- `shares_pattern_with`
- `appears_in`
- `verified_by`
- `contrasts_with`
- `tentative_link`
- `updates`
- `corrects`
- `alternative_view_of`
- `refines`
- `mentions`

## Edge type semantics

| Edge type | Direction | Meaning |
|-----------|-----------|----------|
| requires | A requires B | A depends on B as a prerequisite |
| derives | A derives B | A logically produces or proves B |
| equivalent_to | A equivalent_to B | A and B are equivalent formulations (symmetric) |
| belongs_to | A belongs_to B | A is a member of series/topic/path B |
| contains | A contains B | Series/topic/path A includes node B |
| precedes | A precedes B | A comes before B in a series or derivation |
| is_example_of | A is_example_of B | A is a concrete instance of method/pattern B |
| expresses_method | A expresses_method B | A demonstrates or embodies method B |
| shares_pattern_with | A shares_pattern_with B | A and B share a reasoning pattern (symmetric) |
| verified_by | A verified_by B | Claim A is supported by evidence span B |
| updates | A updates B | A is a later revision or correction of B |
| corrects | A corrects B | A explicitly fixes an error or limitation in B |
| alternative_view_of | A alternative_view_of B | A gives another source-backed framing of B |
| refines | A refines B | A narrows, strengthens, or clarifies B |
| mentions | A mentions B | A weakly mentions B; excluded from default retrieval expansion |

## Graph JSONL schemas

### nodes.jsonl

One JSON object per line. Fields:

```json
{"id": "concept::奇异值熵", "type": "concept", "title": "奇异值熵", "wiki_path": "wiki/concepts/奇异值熵.md", "aliases": ["singular value entropy"], "source_ids": ["11767"], "status": "draft"}
```

Node ID convention: `{type}::{title}` (e.g. `concept::奇异值熵`, `article::11767`, `series::基于流式幂迭代的Muon实现`)

The separator is exactly two colons `::`. No other separator is valid.

**Anti-patterns (rejected):**

| Invalid | Reason | Correct |
|---------|--------|----------|
| `concept-2d-rope` | Hyphen separator, no type prefix in some cases | `concept::2d-rope` |
| `concept:partial-rope` | Single colon | `concept::partial-rope` |
| `base-beta-encoding` | Missing type prefix | `concept::base-beta-encoding` |
| `method:key-normalization` | Single colon | `method::key-normalization` |
| `concept__rope` | Double underscore | `concept::rope` |

Any edge or probe that references a node by a non-compliant ID is invalid and must be fixed before merge.

Required fields:

| Field | Required | Notes |
|-------|----------|-------|
| `id` | yes | Unique node id. Use `article::{id}` for source articles. |
| `type` | yes | One of the graph node types above. |
| `title` | yes | Human-readable title. |
| `wiki_path` | yes for page-backed nodes | Repo-relative wiki path, or `null` for internal-only nodes. |
| `aliases` | yes | Empty list when no aliases are known. |
| `source_ids` | yes | List of string article IDs. |
| `status` | yes | `draft`, `stable`, `candidate`, or `deprecated`. |
| `summary` | optional | One-sentence description for query display. |

### edges.jsonl

One JSON object per line. Fields:

```json
{"source": "concept::奇异值熵", "edge_type": "belongs_to", "target": "topic::矩阵优化", "evidence_id": null, "confidence": "stable", "strength": "strong", "notes": ""}
```

Confidence values: `stable` | `candidate` | `tentative`

Edge strength values: `strong` | `weak`

Required fields:

| Field | Required | Notes |
|-------|----------|-------|
| `source` | yes | Existing node id from `nodes.jsonl`. |
| `edge_type` | yes | One of the preferred edge types above. |
| `target` | yes | Existing node id from `nodes.jsonl`. |
| `evidence_id` | yes | Evidence span id or `null`. Required for `stable` proposition-supporting edges. |
| `confidence` | yes | `stable`, `candidate`, or `tentative`. |
| `strength` | yes | `strong` for reasoning-critical links, `weak` for mentions or loose context. |
| `notes` | yes | Empty string when no note is needed. |

Symmetric relations such as `equivalent_to` and `shares_pattern_with` should be written in both directions unless a query tool explicitly treats them as symmetric.

Default graph queries must ignore `mentions` and other `strength: weak` edges unless the caller explicitly asks for weak context.

### evidence_spans.jsonl

One JSON object per line. Fields:

```json
{"id": "ev::11767::平均场", "article_id": "11767", "source_path": "Data/Spaces_ac_cn/markdown/Mathematics/2026-05-29-矩阵参数的奇异值熵越高越好吗.md", "section": "平均场", "claim": "奇异值熵不必最大化", "span_start": null, "span_end": null}
```

Required fields:

| Field | Required | Notes |
|-------|----------|-------|
| `id` | yes | `ev::{article_id}::{section-or-claim-slug}`. |
| `article_id` | yes | String source article ID. |
| `source_path` | yes | Repo-relative `Data/Spaces_ac_cn/...` path. |
| `section` | yes | Source Markdown heading or section label. |
| `claim` | yes | Claim supported by this span. |
| `span_start` | yes | Line number when known, otherwise `null`. |
| `span_end` | yes | Line number when known, otherwise `null`. |
| `quote` | optional | Short excerpt only; avoid copying long source passages. |

**JSON escaping rule**: The `claim`, `quote`, and `section` fields must use valid JSON string escaping. Double-quote characters (`"`) inside these fields must be escaped as `\"`. Every append to `evidence_spans.jsonl` must be followed by a JSONL-parse check before the batch is considered complete.

### aliases.json

`aliases.json` is a single JSON object:

```json
{
  "奇异值熵": ["concept::奇异值熵"],
  "singular value entropy": ["concept::奇异值熵"],
  "Muon": ["topic::矩阵优化", "series::基于流式幂迭代的Muon实现"]
}
```

Keys are lookup strings. Values are ordered node-id lists. Keep ambiguous aliases ordered by MVP relevance.

### probes JSONL

`probes/questions.jsonl` fields:

```json
{"id": "probe::mvp::singular_entropy_limit", "type": "evidence", "question": "为什么奇异值熵不应被简单最大化？", "required_nodes": ["concept::奇异值熵", "proposition::奇异值熵不必最大化", "article::11767"], "status": "active"}
```

`probes/results.jsonl` fields:

```json
{"probe_id": "probe::mvp::singular_entropy_limit", "answered": true, "used_nodes": ["concept::奇异值熵"], "used_sources": ["11767"], "notes": "", "run_at": "2026-06-09"}
```

`probes/failures.jsonl` fields:

```json
{"probe_id": "probe::mvp::singular_entropy_limit", "failure_type": "missing_evidence", "missing_node_or_edge": "proposition::奇异值熵不必最大化 verified_by ev::11767::完整分析", "next_fix": "Add evidence span and verified_by edge", "created": "2026-06-09"}
```

## Quality-loop outputs

- `graph/nodes.jsonl`
- `graph/edges.jsonl`
- `graph/evidence_spans.jsonl`
- `graph/aliases.json`
- `graph/communities.json`
- `probes/questions.jsonl`
- `probes/results.jsonl`
- `probes/failures.jsonl`

## Method taxonomy rule

Methods use a closed seed registry with a **match-first, create-last** policy. Workers must search existing method pages and the operation-type taxonomy before proposing new methods. The search key is operation type (what mathematical object is transformed into what, by what generative move), not name or topic. A method from a different series that performs the same type of mathematical transformation is a match, not a coincidence. New proposals go to `wiki/methods/_candidates.md`, not directly to stable pages. The goal is that the method taxonomy grows increasingly general and reusable, with fewer new methods needed per series as compilation progresses.

Design rationale and the full operation-type taxonomy: see the top-level design doc (§13, §17.5) and workflow doc (Phase 9 Bridge Pass B).

## Mathematical notation rule

Formula pages must define `standard_notation`. Example pages must define `notation_mapping` when source symbols differ from the wiki standard. Never silently rewrite source formulas to match wiki notation.

Design rationale and the two-layer symbol strategy: see the top-level design doc (§7.4).

## Granularity rule

"Process stays in blocks, reusable results become nodes." Promote intermediate results to `formula` or `proposition` nodes only when they are reused across multiple pages or act as key lemmas.

Design rationale: see the top-level design doc (§8.9).

## Agent graph retrieval rule

Agent-facing graph APIs must return bounded subgraphs. Required signature:

```text
get_subgraph(center_node, max_radius=2, edge_types=None, limit=10, sort_by="relevance")
```

Defaults: `max_radius ≤ 2`, `limit ≤ 10`, weak edges and `mentions` excluded by default.

Design rationale and the full agent skill interface: see the top-level design doc (§14).

## Manifest path mapping

Paths in `manifest.jsonl` use the prefix `spaces_ac_cn/` (e.g. `spaces_ac_cn/markdown/...`).
Actual file paths in this repo use `Data/Spaces_ac_cn/` (e.g. `Data/Spaces_ac_cn/markdown/...`).

When referencing sources in wiki frontmatter, always use the repo-relative path with `Data/Spaces_ac_cn/` prefix.
