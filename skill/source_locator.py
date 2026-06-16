from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from skill.paths import library_root


ROOT = library_root(Path(__file__).resolve().parents[1])
GRAPH_DIR = ROOT / "graph"
DATA_DIR = ROOT / "Data" / "Spaces_ac_cn"


def _load_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _nodes() -> dict[str, dict[str, Any]]:
    return {node["id"]: node for node in _load_jsonl(GRAPH_DIR / "nodes.jsonl")}


def _edges() -> list[dict[str, Any]]:
    return _load_jsonl(GRAPH_DIR / "edges.jsonl")


def _evidence() -> dict[str, dict[str, Any]]:
    return {ev["id"]: ev for ev in _load_jsonl(GRAPH_DIR / "evidence_spans.jsonl")}


def _manifest_records() -> dict[str, dict[str, Any]]:
    path = DATA_DIR / "manifest.jsonl"
    records: dict[str, dict[str, Any]] = {}
    for row in _load_jsonl(path):
        records[str(row["id"])] = row
    return records


def _source_index_records() -> dict[str, dict[str, Any]]:
    records: dict[str, dict[str, Any]] = {}
    for row in _load_jsonl(GRAPH_DIR / "source_index.jsonl"):
        article_id = row.get("article_id") or row.get("id")
        if article_id:
            records[str(article_id)] = row
    return records


def _normalize_data_path(value: str | None) -> str | None:
    if not value:
        return None
    if value.startswith("Data/Spaces_ac_cn/"):
        return value
    if value.startswith("spaces_ac_cn/"):
        return f"Data/Spaces_ac_cn/{value[len('spaces_ac_cn/'):]}"
    return value


def _source_from_parts(
    article_id: str,
    title: str | None,
    source_markdown: str | None,
    source_url: str | None,
    source_page: str | None,
) -> dict[str, Any]:
    normalized_markdown = _normalize_data_path(source_markdown)
    asset_dir = f"Data/Spaces_ac_cn/assets/{article_id}"
    return {
        "article_id": article_id,
        "title": title or "",
        "source_markdown": normalized_markdown or "",
        "asset_dir": asset_dir,
        "source_url": source_url or f"https://spaces.ac.cn/archives/{article_id}",
        "source_page": source_page,
        "exists": {
            "markdown": bool(normalized_markdown and (ROOT / normalized_markdown).exists()),
            "asset_dir": (ROOT / asset_dir).exists(),
        },
    }


def resolve_source(article_id: str) -> dict[str, Any]:
    article_id = str(article_id)

    source_index = _source_index_records()
    if article_id in source_index:
        row = source_index[article_id]
        return _source_from_parts(
            article_id,
            str(row.get("title") or ""),
            str(row.get("source_markdown") or row.get("markdown_path") or ""),
            str(row.get("source_url") or row.get("url") or ""),
            str(row.get("source_page") or "") or None,
        )

    for node in _nodes().values():
        if node.get("id") == f"article::{article_id}" or str(node.get("id", "")).endswith(f"::{article_id}"):
            source_markdown = node.get("source_markdown") or node.get("markdown_path")
            source_url = node.get("source_url") or node.get("url")
            source_page = node.get("source_page")
            if source_markdown:
                return _source_from_parts(
                    article_id,
                    str(node.get("title") or ""),
                    str(source_markdown),
                    str(source_url or ""),
                    str(source_page or "") or None,
                )
            break

    for ev in _evidence().values():
        if str(ev.get("article_id")) == article_id:
            return _source_from_parts(article_id, "", str(ev.get("source_path") or ""), "", None)

    record = _manifest_records().get(article_id)
    if record:
        return _source_from_parts(
            article_id,
            str(record.get("title") or ""),
            str(record.get("markdown_path") or ""),
            str(record.get("url") or ""),
            None,
        )

    raise KeyError(f"Unknown article_id: {article_id}")


def resolve_sources_for_node(node_id: str) -> list[dict[str, Any]]:
    nodes = _nodes()
    if node_id not in nodes:
        raise KeyError(f"Unknown node_id: {node_id}")
    article_ids: list[str] = [str(item) for item in nodes[node_id].get("source_ids") or []]
    evidence_by_id = _evidence()
    for edge in _edges():
        evidence_id = edge.get("evidence_id")
        if edge.get("source") == node_id and evidence_id in evidence_by_id:
            article = evidence_by_id[evidence_id].get("article_id")
            if article:
                article_ids.append(str(article))
    output = []
    seen: set[str] = set()
    for article_id in article_ids:
        if article_id in seen:
            continue
        seen.add(article_id)
        output.append(resolve_source(article_id))
    return output


def resolve_evidence(evidence_id: str) -> dict[str, Any]:
    evidence = _evidence()
    if evidence_id not in evidence:
        raise KeyError(f"Unknown evidence_id: {evidence_id}")
    ev = evidence[evidence_id]
    source = resolve_source(str(ev["article_id"]))
    return {
        "evidence_id": ev["id"],
        "article_id": str(ev["article_id"]),
        "source_markdown": source["source_markdown"] or _normalize_data_path(str(ev.get("source_path") or "")),
        "section": ev.get("section"),
        "span_start": ev.get("span_start"),
        "span_end": ev.get("span_end"),
        "claim": ev.get("claim"),
    }


def _read_lines(repo_path: str) -> list[str]:
    path = ROOT / repo_path
    if not path.exists():
        raise FileNotFoundError(repo_path)
    return path.read_text(encoding="utf-8").splitlines()


def _line_items(lines: list[str], start: int, end: int) -> list[dict[str, Any]]:
    return [{"line": idx, "text": lines[idx - 1]} for idx in range(start, end + 1) if 1 <= idx <= len(lines)]


def _find_section_range(lines: list[str], section: str) -> tuple[int, int]:
    start = None
    start_level = None
    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        if not stripped.startswith("#"):
            continue
        level = len(stripped) - len(stripped.lstrip("#"))
        title = stripped.lstrip("#").strip()
        if start is None and title == section:
            start = idx
            start_level = level
            continue
        if start is not None and level <= int(start_level):
            return start, idx - 1
    if start is None:
        raise KeyError(f"Unknown section: {section}")
    return start, len(lines)


def read_source(
    article_id: str,
    section: str | None = None,
    line_range: tuple[int, int] | None = None,
    max_lines: int = 120,
) -> dict[str, Any]:
    source = resolve_source(article_id)
    lines = _read_lines(source["source_markdown"])
    truncated = False
    if line_range:
        start, end = line_range
    elif section:
        start, end = _find_section_range(lines, section)
    else:
        start, end = 1, min(len(lines), max_lines)
        truncated = len(lines) > max_lines
    if end - start + 1 > max_lines:
        end = start + max_lines - 1
        truncated = True
    return {
        "article_id": str(article_id),
        "source_markdown": source["source_markdown"],
        "section": section,
        "line_range": [start, end],
        "truncated": truncated,
        "lines": _line_items(lines, start, end),
    }


def list_source_assets(article_id: str) -> dict[str, Any]:
    source = resolve_source(article_id)
    asset_dir = source["asset_dir"]
    path = ROOT / asset_dir
    assets = []
    if path.exists():
        for item in sorted(child for child in path.rglob("*") if child.is_file()):
            assets.append({
                "path": str(item.relative_to(ROOT)),
                "size": item.stat().st_size,
            })
    return {
        "article_id": str(article_id),
        "asset_dir": asset_dir,
        "exists": path.exists(),
        "assets": assets,
    }


def source_link(
    article_id: str,
    line_range: tuple[int, int] | None = None,
    mode: str = "repo",
) -> dict[str, Any]:
    source = resolve_source(article_id)
    repo_path = source["source_markdown"]
    if mode == "repo":
        path = repo_path
    elif mode == "absolute":
        path = str((ROOT / repo_path).resolve())
    elif mode == "file_uri":
        path = (ROOT / repo_path).resolve().as_uri()
    else:
        raise ValueError(f"Unknown source link mode: {mode}")
    return {
        "article_id": str(article_id),
        "mode": mode,
        "path": path,
        "line_range": list(line_range) if line_range else None,
    }
