from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from skill.paths import library_root

ROOT = library_root(Path(__file__).resolve().parents[1])
GRAPH_DIR = ROOT / "graph"


def _load_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def check_graph_dirs() -> list[str]:
    errors: list[str] = []
    required = ["nodes.jsonl", "edges.jsonl", "evidence_spans.jsonl"]
    for name in required:
        path = GRAPH_DIR / name
        if not path.exists():
            errors.append(f"Missing graph file: {path}")
        elif path.stat().st_size == 0:
            errors.append(f"Empty graph file: {path}")
    return errors


def check_node_references() -> list[str]:
    errors: list[str] = []
    nodes = _load_jsonl(GRAPH_DIR / "nodes.jsonl")
    edges = _load_jsonl(GRAPH_DIR / "edges.jsonl")
    node_ids: set[str] = {n["id"] for n in nodes}

    for i, edge in enumerate(edges):
        src = edge.get("source")
        tgt = edge.get("target")
        if src and src not in node_ids:
            errors.append(f"edges.jsonl[{i}]: source '{src}' not in nodes")
        if tgt and tgt not in node_ids:
            errors.append(f"edges.jsonl[{i}]: target '{tgt}' not in nodes")
    return errors


def check_evidence_references() -> list[str]:
    errors: list[str] = []
    edges = _load_jsonl(GRAPH_DIR / "edges.jsonl")
    evidence = {ev["id"] for ev in _load_jsonl(GRAPH_DIR / "evidence_spans.jsonl")}

    for i, edge in enumerate(edges):
        ev_id = edge.get("evidence_id")
        if ev_id and ev_id not in evidence:
            errors.append(f"edges.jsonl[{i}]: evidence_id '{ev_id}' not in evidence_spans.jsonl")
    return errors


def check_wiki_paths() -> list[str]:
    errors: list[str] = []
    nodes = _load_jsonl(GRAPH_DIR / "nodes.jsonl")

    for node in nodes:
        wiki_path = node.get("wiki_path")
        if not isinstance(wiki_path, str) or not wiki_path.strip():
            continue
        full_path = ROOT / wiki_path
        if not full_path.exists():
            errors.append(f"Node '{node['id']}': wiki_path '{wiki_path}' not found")
    return errors


def check_aliases() -> list[str]:
    errors: list[str] = []
    alias_path = GRAPH_DIR / "aliases.json"
    nodes = {n["id"] for n in _load_jsonl(GRAPH_DIR / "nodes.jsonl")}

    if not alias_path.exists():
        errors.append("Missing aliases.json")
        return errors

    try:
        aliases = json.loads(alias_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        errors.append(f"aliases.json: invalid JSON: {e}")
        return errors

    for alias, node_ids in aliases.items():
        if not isinstance(node_ids, list):
            errors.append(f"aliases.json['{alias}']: expected list, got {type(node_ids).__name__}")
            continue
        for nid in node_ids:
            if nid not in nodes:
                errors.append(f"aliases.json['{alias}']: '{nid}' not in nodes")
    return errors


def check_markdown_source_maps() -> list[str]:
    errors: list[str] = []
    evidence = _load_jsonl(GRAPH_DIR / "evidence_spans.jsonl")

    for ev in evidence:
        source_path = ev.get("source_path")
        if source_path:
            full = ROOT / source_path
            if not full.exists():
                errors.append(f"evidence '{ev['id']}': source_path '{source_path}' not found")
    return errors


def run_all(include_wiki: bool | None = None) -> dict[str, list[str]]:
    if include_wiki is None:
        include_wiki = (ROOT / "wiki").exists()
    steps = {
        "graph_dirs": check_graph_dirs,
        "node_references": check_node_references,
        "evidence_references": check_evidence_references,
        "aliases": check_aliases,
        "markdown_source_maps": check_markdown_source_maps,
    }
    if include_wiki:
        steps["wiki_paths"] = check_wiki_paths
    results: dict[str, list[str]] = {}
    for name, fn in steps.items():
        try:
            results[name] = fn()
        except Exception as e:
            results[name] = [f"check '{name}' raised: {e}"]
    return results


def main() -> int:
    results = run_all()
    total_failures = 0
    for name, errors in results.items():
        if errors:
            print(f"[FAIL] {name}:")
            for err in errors:
                print(f"       {err}")
            total_failures += len(errors)
        else:
            print(f"[PASS] {name}")
    if total_failures:
        print(f"\n{total_failures} validation error(s) found.")
    else:
        print("\nAll validation checks passed.")
    return 1 if total_failures else 0


if __name__ == "__main__":
    sys.exit(main())
