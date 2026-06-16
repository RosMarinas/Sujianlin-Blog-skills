# 认知型知识网络技能

This README describes packaging and installing the skill and its shared library data.

## Package Shape

Use two packages, connected by one root directory setting.

### Skill discovery package

Install this into a Codex skill discovery directory so Codex can discover `SKILL.md`.
For a user-level install, Codex scans:

```text
$HOME/.agents/skills/<skill-name>/SKILL.md
```

For a repository-level install, Codex scans `.agents/skills` from the current working directory up to the repository root.

```text
cognitive-knowledge-network/
  SKILL.md
  skill/
    README.md
    docs/
      api.md
      examples.md
    paths.py
    tools.py
    source_locator.py
    research_navigation.py
    research_artifacts.py
    validate.py
    __init__.py
```

The installed skill tells agents how to use the library and provides reusable Python helpers.

### Shared library root

Keep one shared library root for all agents and projects:

```text
<library-root>/
  graph/                             # required
  Data/Spaces_ac_cn/markdown/        # required
  Data/Spaces_ac_cn/assets/          # required
  wiki/                              # optional human-readable compiled layer
  probes/                            # optional
```

`graph/` is required for the current API because concept/method navigation, evidence lookup, and source resolution depend on node, edge, and evidence JSONL files.

`wiki/` is optional for the installed skill runtime. It can be packaged with the shared library for human reading and review, but runtime helpers must resolve source paths and method readiness from `graph/`, `graph/source_index.jsonl`, evidence spans, or the manifest instead of parsing wiki pages.

`probes/` is optional. It supports validation and diagnostics such as `list_failures()`, but the core library remains usable without it.

`Data/Spaces_ac_cn/raw/`, `manifest.jsonl`, `reports/`, and `samples/` are auxiliary provenance, index, validation, or debugging material. They are not default research objects.

## Configure Root

Set `SUJIANLIN_LIBRARY_ROOT` for every agent or project that should use the shared library:

```bash
export SUJIANLIN_LIBRARY_ROOT="/Users/polaris/Documents/Graduate/AI/Document/notes/Blog"
export PYTHONPATH="$SUJIANLIN_LIBRARY_ROOT:$PYTHONPATH"
```

If `SUJIANLIN_LIBRARY_ROOT` is unset, the Python API falls back to the repo root containing this `skill/` package.

## Install

### Via Makefile

```bash
make install
```

Installs the skill wrapper to `$HOME/.agents/skills/cognitive-knowledge-network/`.

Override the install target:

```bash
make install INSTALL_DIR=/path/to/.agents/skills/cognitive-knowledge-network
```

This copy-style install keeps the shared library data at the source `SUJIANLIN_LIBRARY_ROOT`.
Use the symlink install below when the installed skill directory should also be the data root.

### Symlink install with bundled data

When this package already contains `graph/`, `wiki/`, and `Data/Spaces_ac_cn/`, keep the package root as the data root and symlink the whole package into the user skill directory:

```bash
PACK="/Users/polaris/Documents/Utils/skills/cognitive-knowledge-network"
INSTALL_DIR="$HOME/.agents/skills/cognitive-knowledge-network"

cd "$PACK"
cp skill/SKILL.md SKILL.md

mkdir -p "$(dirname "$INSTALL_DIR")"
ln -sfn "$PACK" "$INSTALL_DIR"

export SUJIANLIN_LIBRARY_ROOT="$PACK"
export PYTHONPATH="$PACK:$PYTHONPATH"
```

Codex supports symlinked skill folders. This layout makes `SKILL.md`, Python helpers, `graph/`, optional `wiki/`, and source data all resolve from the same package root.

### Manual install

```bash
INSTALL_DIR="$HOME/.agents/skills/cognitive-knowledge-network"
mkdir -p "$INSTALL_DIR/skill/docs"

cp skill/SKILL.md "$INSTALL_DIR"/
cp skill/README.md "$INSTALL_DIR/skill"/
cp -r skill/docs/*.md "$INSTALL_DIR/skill/docs/"
cp skill/*.py "$INSTALL_DIR/skill"/
```

### Development install (editable)

```bash
make install-dev
```

Or equivalently:

```bash
uv pip install -e .
```

### Uninstall

```bash
make uninstall
```

For a repo-local development install, keep using this repository directly and set:

```bash
export SUJIANLIN_LIBRARY_ROOT="$(pwd)"
export PYTHONPATH="$(pwd):$PYTHONPATH"
```

## Data Validation

Run integrity checks on the graph data before installing to a shared location:

```bash
make validate
```

Or directly:

```bash
uv run python -m skill.validate
```

Checks performed:

- All graph JSONL files exist and are non-empty
- Every edge source/target references a known node
- Every `evidence_id` on edges exists in `evidence_spans.jsonl`
- Every `wiki_path` in node data points to an existing file, only when the optional `wiki/` layer is present
- Every alias target node exists in `nodes.jsonl`
- Every evidence `source_path` points to an existing markdown file

## Platform Support

The skill package is agent-platform agnostic. Configure as follows per platform:

| Platform    | Discovery                        | Python import                              |
|-------------|----------------------------------|--------------------------------------------|
| Codex CLI   | `SKILL.md` in skill directory    | `PYTHONPATH` + `SUJIANLIN_LIBRARY_ROOT`    |
| Claude Code | `Skill` tool loads skill content | `PYTHONPATH` + `SUJIANLIN_LIBRARY_ROOT`    |
| Gemini CLI  | `activate_skill` via `GEMINI.md` | Same env vars                              |

All platforms share the same Python API (`skill.tools.*`). Platform-specific adaptations only affect agent skill discovery, not the Python module.

## Smoke Test

### Via Makefile

```bash
make smoke
```

### Full test suite

```bash
make test
```

Or manually:

```bash
export SUJIANLIN_LIBRARY_ROOT="$(pwd)"
export PYTHONPATH="$(pwd):$PYTHONPATH"

uv run --with pytest pytest \
  tests/test_source_locator.py \
  tests/test_research_navigation.py \
  tests/test_research_artifacts.py \
  tests/test_methodological_skill_smoke.py \
  tests/test_library_root_config.py \
  tests/test_skill_packaging_docs.py \
  tests/test_skill_validate.py \
  tests/test_installed_skill.py \
  -q
```

### Minimal API smoke test

```bash
uv run python - <<'PY'
from skill.tools import resolve_source, search_concept

print(resolve_source("11767")["source_markdown"])
print([ref.node_id for ref in search_concept("奇异值熵")[:3]])
PY
```

### CI entry point

```bash
make check
```

Runs validation followed by the full test suite.

Expected behavior:

- `resolve_source("11767")` returns a path under `Data/Spaces_ac_cn/markdown/`.
- Concept search returns `concept::奇异值熵`.
- No normal source lookup exposes `Data/Spaces_ac_cn/raw/` as the source object.
- Complex-query Search Logs and reports are created by the calling project under `docs/research/`, not inside this library's `wiki/`.
