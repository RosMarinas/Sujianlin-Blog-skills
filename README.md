# cognitive-knowledge-network

[中文说明](README_zh.md)

`cognitive-knowledge-network` is an agent-compatible skill and local cognitive library for both human readers and AI agents. This repository organizes Su Jianlin's blog corpus into a concept-and-method-oriented cognitive knowledge network, then exposes it both as a human-readable visual wiki and as an agent-friendly skill interface.

This public repository distributes the skill, schema, documentation, and
derived knowledge layers without bundling the original `Data/` corpus. The omitted `Data/` directory is the original evidence layer: a locally collected and organized archive of Su Jianlin blog materials, including source markdown converted from original pages and related assets.

## What is the Cognitive Knowledge Network?

The Cognitive Knowledge Network is a methodology-oriented local cognitive library. Built on top of the crawled blog corpus of Su Jianlin, creator of Scientific Spaces (`kexue.fm` / `spaces.ac.cn`), it acts as a knowledge
compilation layer that converts unstructured articles into a structured,
machine-traversable, and evidence-backed network of mathematical concepts and transferable methods.

Unlike traditional wikis, which focus on static descriptions, or basic RAG
systems, which retrieve raw text chunks, this network compiles mathematical ideas into logical structures designed for AI agents and human researchers.

## What problems does it solve?

- `Shallow retrieval vs. logical derivation`: keyword search can find an
  article, but it usually cannot recover how a formula was derived, why an
  optimizer works, or how an idea transfers across topics. This repository
  models typed logical relations such as `requires`, `derives`,
  `expresses_method`, `shares_pattern_with`, and `verified_by`.
- `Mathematical and symbolic inconsistency`: notation changes across years,
  topics, and article series. The network addresses this through a dual-layer
  strategy: standard notation on `concept` and `formula` pages, plus
  source-local notation mapping on `example` pages.
- `Concept inflation and method explosion`: instead of letting agents invent
  ad hoc abstractions, the network follows a strict match-first, create-last
  policy for concepts and methods.
- `Knowledge evolution and correction`: mathematical views evolve over time.
  The network records temporal and logical updates through explicit edges such
  as `updates`, `corrects`, `refines`, and `alternative_view_of`.

## What can it do?

The architecture is organized into five cohesive layers:

1. `Source Evidence Layer`: preserves immutable source materials for
   ground-truth audits. In the public GitHub version, this layer is referenced
   but not bundled.
2. `Compiled Wiki Layer`: organizes content into page types such as `concept`,
   `method`, `formula`, `proposition`, `series`, `problem_pattern`, `example`,
   and `reading_path`.
3. `Cognitive Graph Layer`: translates compiled pages into machine-traversable
   nodes and typed edges for graph exploration, path search, and neighborhood
   analysis.
4. `Quality Loop Layer`: uses lints and query-based probes to detect
   structural problems such as orphans, unsupported claims, and missing
   notation mappings.
5. `Agent Interface Layer`: exposes APIs and skill interfaces for bounded
   subgraph queries, source resolution, reading-path recovery, and structured
   research artifacts.

## What can it do for GitHub users and developers?

### Deep mathematical insight for model design

Instead of only copying formulas, you can traverse the network to understand
the generative logic behind advanced deep learning designs, including Muon,
MuP, RoPE, SSM, MoE, and diffusion-related topics.

Example questions:

- Why are embedding or LM-head matrices not suitable for Muon optimization?
- What is the derivation chain for singular value entropy density?
- How does RoPE's geometric representation translate complex-valued reasoning
  into relative position encoding?

### Structured learning and reading paths

The repository compiles article series into structured reading paths, so users
can learn a topic chronologically with target goals, checkpoints, and concept
dependencies instead of reading isolated posts.

### Local mathematical tooling for AI agents

Agents can use the local APIs to query source-backed mathematical knowledge,
locate supporting passages, inspect assumptions, and generate code or notes
with lower hallucination risk.

### A blueprint for knowledge engineering

If you are building agent workflows, local RAG systems, or knowledge graphs,
this repository is also a reference implementation for JSONL graph schemas,
typed evidence links, validation loops, and self-diagnostic probes.

## Visualization

The skill also ships with a visualization interface for browsing the graph and
inspecting node-level detail.

![Global graph view](figures/Screenshot%202026-06-16%20at%2013.49.49.png)

_Global graph view with node-type filters and layout controls._

![Focused node detail view](figures/Screenshot%202026-06-16%20at%2013.50.27.png)

_Focused graph inspection with a side panel for method-level summaries and
step structure._

## Repository layout

- `SKILL.md`: skill entrypoint
- `skill/`: Python helpers and skill-local docs
- `schema.md`: page and graph contracts
- `wiki/`: derived knowledge pages
- `graph/`: structured derived graph content
- `purpose.md`: repository purpose and boundaries, if present
- `docs/`: design and workflow documentation, if present
- `probes/`: validation and diagnostic artifacts, if present

`Data/` is intentionally excluded from the public GitHub package.

## Licensing

This is a mixed-license repository.

### MIT-licensed layer

Unless a file says otherwise, the MIT License applies to the software and
engineering layer, including:

- `SKILL.md`
- `skill/`
- `visualize.py`
- `visualize.html`
- `schema.md`
- `README.md`
- `README_zh.md`
- `.gitignore`
- build, test, and packaging files
- `purpose.md` if added later
- `docs/` if added later

See [LICENSE](LICENSE).

### CC BY-NC-SA 4.0 content layer

Unless a file says otherwise, the following derived knowledge directories are
licensed under CC BY-NC-SA 4.0:

- `figures/`
- `wiki/`
- `graph/`
- `probes/` if added later

These directories are not released under MIT.

See [LICENSE-content.md](LICENSE-content.md).

## Upstream provenance

This repository is built around content derived from the blog corpus of Su
Jianlin.

- Original author: Su Jianlin
- Original sites: `https://spaces.ac.cn/` and `https://kexue.fm/`

The `wiki/` and `graph/` directories are curated and structured by this
repository's maintainers. They contain maintainer-authored organization,
selection, and structured representation. However, they are still derived from
the upstream blog corpus and are therefore distributed under CC BY-NC-SA 4.0
rather than MIT.

Where upstream attribution is preserved in file metadata or page frontmatter,
that attribution should remain intact in downstream reuse.
