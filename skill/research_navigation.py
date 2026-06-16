from __future__ import annotations

import json
from collections import deque
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from skill.paths import library_root
from skill.source_locator import resolve_sources_for_node


ROOT = library_root(Path(__file__).resolve().parents[1])
GRAPH_DIR = ROOT / "graph"


@dataclass(frozen=True)
class NodeRef:
    node_id: str
    node_type: str
    title: str


def _load_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _nodes() -> dict[str, dict[str, Any]]:
    return {node["id"]: node for node in _load_jsonl(GRAPH_DIR / "nodes.jsonl")}


def _edges() -> list[dict[str, Any]]:
    return _load_jsonl(GRAPH_DIR / "edges.jsonl")


def _aliases() -> dict[str, list[str]]:
    path = GRAPH_DIR / "aliases.json"
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def _node_ref(node: dict[str, Any]) -> NodeRef:
    return NodeRef(node_id=node["id"], node_type=node["type"], title=node["title"])


def _dedupe_refs(refs: list[NodeRef]) -> list[NodeRef]:
    output: list[NodeRef] = []
    seen: set[str] = set()
    for ref in refs:
        if ref.node_id in seen:
            continue
        seen.add(ref.node_id)
        output.append(ref)
    return output


def lookup_node(node_id: str) -> dict[str, Any]:
    nodes = _nodes()
    if node_id not in nodes:
        raise KeyError(f"Unknown node_id: {node_id}")
    return nodes[node_id]


def search_node(query: str) -> list[NodeRef]:
    query_lower = query.lower()
    nodes = _nodes()
    results: list[NodeRef] = []
    for alias, node_ids in _aliases().items():
        if query_lower in alias.lower():
            for node_id in node_ids:
                if node_id in nodes:
                    results.append(_node_ref(nodes[node_id]))
    for node in nodes.values():
        haystack = " ".join([node["id"], node["title"], *(node.get("aliases") or [])]).lower()
        if query_lower in haystack:
            results.append(_node_ref(node))
    return _dedupe_refs(results)


def expand_node(
    node_id: str,
    edge_types: list[str] | None = None,
    depth: int = 1,
) -> list[dict[str, Any]]:
    allowed = set(edge_types) if edge_types else None
    seen_nodes = {node_id}
    seen_edges: set[tuple[str, str, str]] = set()
    output: list[dict[str, Any]] = []
    queue: deque[tuple[str, int]] = deque([(node_id, 0)])
    all_edges = _edges()
    while queue:
        current, current_depth = queue.popleft()
        if current_depth >= depth:
            continue
        for edge in all_edges:
            if edge["source"] != current:
                continue
            if allowed is not None and edge["edge_type"] not in allowed:
                continue
            edge_key = (edge["source"], edge["edge_type"], edge["target"])
            if edge_key not in seen_edges:
                output.append(edge)
                seen_edges.add(edge_key)
            if edge["target"] not in seen_nodes:
                seen_nodes.add(edge["target"])
                queue.append((edge["target"], current_depth + 1))
    return output


def rank_neighbors(node_id: str) -> list[NodeRef]:
    nodes = _nodes()
    refs: list[NodeRef] = []
    for edge in expand_node(node_id, depth=1):
        target = edge["target"]
        if target in nodes:
            refs.append(_node_ref(nodes[target]))
    return _dedupe_refs(refs)


def get_examples(method_id: str) -> list[NodeRef]:
    nodes = _nodes()
    refs: list[NodeRef] = []
    for edge in _edges():
        if edge["source"].startswith("example::") and edge["target"] == method_id and edge["source"] in nodes:
            refs.append(_node_ref(nodes[edge["source"]]))
    return _dedupe_refs(refs)


def get_problem_patterns(method_id: str) -> list[NodeRef]:
    nodes = _nodes()
    refs: list[NodeRef] = []
    for edge in _edges():
        if edge["source"] == method_id and edge["target"].startswith("problem_pattern::") and edge["target"] in nodes:
            refs.append(_node_ref(nodes[edge["target"]]))
        if (
            edge["target"] == method_id
            and edge["source"].startswith("problem_pattern::")
            and edge["edge_type"] == "motivates"
            and edge["source"] in nodes
        ):
            refs.append(_node_ref(nodes[edge["source"]]))
    return _dedupe_refs(refs)


def search_concept(query: str) -> list[NodeRef]:
    return [ref for ref in search_node(query) if ref.node_type == "concept"]


def inspect_concept(node_id: str, depth: int = 1) -> dict[str, Any]:
    node = lookup_node(node_id)
    if node["type"] != "concept":
        raise ValueError(f"Expected concept node, got {node['type']}: {node_id}")
    edges = expand_node(node_id, depth=depth)
    neighbors = rank_neighbors(node_id)
    related_methods = [ref for ref in neighbors if ref.node_type == "method"]
    return {
        "node": node,
        "sources": resolve_sources_for_node(node_id),
        "neighbor_edges": edges,
        "neighbors": [ref.__dict__ for ref in neighbors],
        "related_methods": [ref.__dict__ for ref in related_methods],
        "source_level": "structured support",
    }


def inspect_method(method_id: str) -> dict[str, Any]:
    node = lookup_node(method_id)
    if node["type"] != "method":
        raise ValueError(f"Expected method node, got {node['type']}: {method_id}")
    examples = get_examples(method_id)
    patterns = get_problem_patterns(method_id)
    return {
        "node": node,
        "sources": resolve_sources_for_node(method_id),
        "examples": [ref.__dict__ for ref in examples],
        "problem_patterns": [ref.__dict__ for ref in patterns],
        "neighbor_edges": expand_node(method_id, depth=1),
        "source_level": "structured support",
    }


def suggest_transfer_angles(query: str) -> dict[str, Any]:
    matches = search_node(query)
    angles: list[dict[str, Any]] = []
    for ref in matches[:5]:
        if ref.node_type == "method":
            label = "method transfer"
            prompt = (
                f"Inspect {ref.node_id} as a generative operation and compare "
                "its problem structure to the target research problem."
            )
        elif ref.node_type == "concept":
            label = "concept anchor"
            prompt = f"Use {ref.node_id} as a semantic anchor before proposing method transfer."
        else:
            label = "library context"
            prompt = f"Use {ref.node_id} as supporting context, then pivot to linked concepts or methods."
        angles.append({
            "node_id": ref.node_id,
            "node_type": ref.node_type,
            "title": ref.title,
            "angle": label,
            "prompt": prompt,
            "source_level": "structured support",
        })
    return {"query": query, "angles": angles}
