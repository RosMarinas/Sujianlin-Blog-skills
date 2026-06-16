from __future__ import annotations

import json
from collections import deque
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from skill.paths import library_root


ROOT = library_root(Path(__file__).resolve().parents[1])
GRAPH_DIR = ROOT / "graph"
PROBES_DIR = ROOT / "probes"


@dataclass(frozen=True)
class NodeRef:
    node_id: str
    node_type: str
    title: str


@dataclass(frozen=True)
class EdgeRef:
    source: str
    edge_type: str
    target: str


@dataclass(frozen=True)
class EvidenceRef:
    evidence_id: str
    source_path: str
    article_id: str | None = None
    section: str | None = None


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


def _aliases() -> dict[str, list[str]]:
    path = GRAPH_DIR / "aliases.json"
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def _node_ref(node: dict[str, Any]) -> NodeRef:
    return NodeRef(node_id=node["id"], node_type=node["type"], title=node["title"])


def _method_answer_ready(node: dict[str, Any]) -> bool:
    if node.get("type") != "method" or node.get("status") != "stable":
        return False
    if "quality_pass" in node:
        return node.get("quality_pass") is True
    if "answer_ready" in node:
        return node.get("answer_ready") is True
    quality = node.get("quality")
    if isinstance(quality, dict) and "answer_ready" in quality:
        return quality.get("answer_ready") is True
    contract = node.get("method_contract")
    if isinstance(contract, dict) and "answer_ready" in contract:
        return contract.get("answer_ready") is True
    return True


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
        ref = _node_ref(node)
        if query_lower in haystack and ref not in results:
            results.append(ref)
    return results


def read_node(node_id: str) -> dict[str, Any]:
    return lookup_node(node_id)


def get_sources(node_id: str) -> list[EvidenceRef]:
    return get_evidence(node_id)


def search_series(query: str) -> list[NodeRef]:
    return [ref for ref in search_node(query) if ref.node_type == "series"]


def read_series(series_id: str) -> dict[str, Any]:
    return lookup_node(series_id)


def get_series_order(series_id: str) -> list[NodeRef]:
    nodes = _nodes()
    contains = [edge for edge in _edges() if edge["source"] == series_id and edge["edge_type"] == "contains"]
    return [_node_ref(nodes[edge["target"]]) for edge in contains if edge["target"] in nodes]


def get_series_gaps(series_id: str) -> list[str]:
    expected = ["article::11654", "article::11673", "article::11697", "article::11710", "article::11719"]
    actual = [ref.node_id for ref in get_series_order(series_id)]
    return [node_id for node_id in expected if node_id not in actual]


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
    return refs


def find_path(source: str, target: str, constraints: dict[str, Any] | None = None) -> list[EdgeRef]:
    max_depth = int((constraints or {}).get("max_depth", 4))
    queue: deque[tuple[str, list[dict[str, Any]]]] = deque([(source, [])])
    visited = {source}
    while queue:
        current, path = queue.popleft()
        if len(path) >= max_depth:
            continue
        for edge in _edges():
            if edge["source"] != current:
                continue
            next_path = [*path, edge]
            if edge["target"] == target:
                return [EdgeRef(e["source"], e["edge_type"], e["target"]) for e in next_path]
            if edge["target"] not in visited:
                visited.add(edge["target"])
                queue.append((edge["target"], next_path))
    return []


def find_reading_path(topic_or_series: str) -> dict[str, Any]:
    query_lower = topic_or_series.lower()
    path_refs = [ref for ref in search_node(topic_or_series) if ref.node_type == "reading_path"]
    if path_refs:
        path_node = lookup_node(path_refs[0].node_id)
    else:
        path_node = next(
            (
                node for node in _nodes().values()
                if node["type"] == "reading_path"
                and (
                    query_lower in node["title"].lower()
                    or any(query_lower in alias.lower() for alias in node.get("aliases") or [])
                )
            ),
            None,
        )
        if path_node is None:
            raise KeyError(f"Unknown reading path query: {topic_or_series}")
    contains = expand_node(path_node["id"], edge_types=["contains"], depth=1)
    for edge in list(contains):
        target = lookup_node(edge["target"])
        if target["type"] == "series":
            contains.extend(expand_node(target["id"], edge_types=["contains"], depth=1))
    return {"query": topic_or_series, "path": path_node, "ordered_edges": contains}


def search_method(query: str, include_scaffold: bool = False) -> list[NodeRef]:
    nodes = _nodes()
    refs = [ref for ref in search_node(query) if ref.node_type == "method"]
    if include_scaffold:
        return refs
    return [ref for ref in refs if _method_answer_ready(nodes[ref.node_id])]


def get_examples(method_id: str) -> list[NodeRef]:
    nodes = _nodes()
    refs: list[NodeRef] = []
    for edge in _edges():
        if edge["source"].startswith("example::") and edge["target"] == method_id and edge["source"] in nodes:
            refs.append(_node_ref(nodes[edge["source"]]))
    return refs


def get_problem_patterns(method_id: str) -> list[NodeRef]:
    nodes = _nodes()
    refs: list[NodeRef] = []
    seen: set[str] = set()
    for edge in _edges():
        if edge["source"] == method_id and edge["target"].startswith("problem_pattern::") and edge["target"] in nodes:
            seen.add(edge["target"])
            refs.append(_node_ref(nodes[edge["target"]]))
        if (
            edge["target"] == method_id
            and edge["source"].startswith("problem_pattern::")
            and edge["edge_type"] == "motivates"
            and edge["source"] in nodes
            and edge["source"] not in seen
        ):
            seen.add(edge["source"])
            refs.append(_node_ref(nodes[edge["source"]]))
    return refs


def find_shared_pattern(node_id: str) -> list[NodeRef]:
    nodes = _nodes()
    pattern_ids = {
        edge["target"] for edge in _edges()
        if edge["source"] == node_id and edge["edge_type"] in {"is_example_of", "shares_pattern_with"}
    }
    return [_node_ref(nodes[target_id]) for target_id in pattern_ids if target_id in nodes]


def find_analogies(method_id: str) -> list[NodeRef]:
    return get_examples(method_id)


def suggest_transfer(source_problem: str) -> list[str]:
    matches = search_node(source_problem)
    return [f"Inspect {match.node_id} and expand by method/problem_pattern edges." for match in matches[:3]]


def verify_claim(proposition_id: str) -> dict[str, Any]:
    proposition = lookup_node(proposition_id)
    evidence_records = []
    evidence_by_id = _evidence()
    for edge in _edges():
        if edge["source"] == proposition_id and edge["edge_type"] == "verified_by":
            evidence_id = edge.get("evidence_id")
            if evidence_id in evidence_by_id:
                evidence_records.append(evidence_by_id[evidence_id])
    return {"proposition": proposition, "evidence": evidence_records}


def verify_with_source(claim: str) -> dict[str, Any]:
    matches = [
        node for node in _nodes().values()
        if node["type"] == "proposition" and claim.lower() in node["title"].lower()
    ]
    if not matches:
        return {"claim": claim, "verified": False, "evidence": []}
    verification = verify_claim(matches[0]["id"])
    return {"claim": claim, "verified": bool(verification["evidence"]), **verification}


def get_evidence(node_id: str) -> list[EvidenceRef]:
    evidence_by_id = _evidence()
    refs: list[EvidenceRef] = []
    for edge in _edges():
        if edge["source"] != node_id or not edge.get("evidence_id"):
            continue
        ev = evidence_by_id.get(edge["evidence_id"])
        if ev:
            refs.append(EvidenceRef(
                evidence_id=ev["id"],
                source_path=ev["source_path"],
                article_id=ev.get("article_id"),
                section=ev.get("section"),
            ))
    return refs


def trace_claim(claim: str) -> list[EvidenceRef]:
    result = verify_with_source(claim)
    return [
        EvidenceRef(
            evidence_id=ev["id"],
            source_path=ev["source_path"],
            article_id=ev.get("article_id"),
            section=ev.get("section"),
        )
        for ev in result.get("evidence", [])
    ]


def list_failures() -> list[dict[str, Any]]:
    return _load_jsonl(PROBES_DIR / "failures.jsonl")


def resolve_source(article_id: str) -> dict[str, Any]:
    from skill.source_locator import resolve_source as _resolve_source

    return _resolve_source(article_id)


def resolve_sources_for_node(node_id: str) -> list[dict[str, Any]]:
    from skill.source_locator import resolve_sources_for_node as _resolve_sources_for_node

    return _resolve_sources_for_node(node_id)


def resolve_evidence(evidence_id: str) -> dict[str, Any]:
    from skill.source_locator import resolve_evidence as _resolve_evidence

    return _resolve_evidence(evidence_id)


def read_source(
    article_id: str,
    section: str | None = None,
    line_range: tuple[int, int] | None = None,
    max_lines: int = 120,
) -> dict[str, Any]:
    from skill.source_locator import read_source as _read_source

    return _read_source(article_id, section=section, line_range=line_range, max_lines=max_lines)


def list_source_assets(article_id: str) -> dict[str, Any]:
    from skill.source_locator import list_source_assets as _list_source_assets

    return _list_source_assets(article_id)


def source_link(
    article_id: str,
    line_range: tuple[int, int] | None = None,
    mode: str = "repo",
) -> dict[str, Any]:
    from skill.source_locator import source_link as _source_link

    return _source_link(article_id, line_range=line_range, mode=mode)


def search_concept(query: str) -> list[Any]:
    from skill.research_navigation import search_concept as _search_concept

    return _search_concept(query)


def inspect_concept(node_id: str, depth: int = 1) -> dict[str, Any]:
    from skill.research_navigation import inspect_concept as _inspect_concept

    return _inspect_concept(node_id, depth=depth)


def inspect_method(method_id: str) -> dict[str, Any]:
    from skill.research_navigation import inspect_method as _inspect_method

    return _inspect_method(method_id)


def suggest_transfer_angles(query: str) -> dict[str, Any]:
    from skill.research_navigation import suggest_transfer_angles as _suggest_transfer_angles

    return _suggest_transfer_angles(query)


def suggest_research_folder(query: str, date: str | None = None) -> str:
    from skill.research_artifacts import suggest_research_folder as _suggest_research_folder

    return _suggest_research_folder(query, date=date)


def make_materials_template(query: str) -> str:
    from skill.research_artifacts import make_materials_template as _make_materials_template

    return _make_materials_template(query)


def make_search_log_template(query: str, depth: str = "Level 3") -> str:
    from skill.research_artifacts import make_search_log_template as _make_search_log_template

    return _make_search_log_template(query, depth=depth)


def make_brief_report_template(query: str) -> str:
    from skill.research_artifacts import make_brief_report_template as _make_brief_report_template

    return _make_brief_report_template(query)


def get_subgraph(
    center_node: str,
    max_radius: int = 2,
    edge_types: list[str] | None = None,
    limit: int = 10,
    sort_by: str = "relevance",
) -> dict[str, Any]:
    # Cap max_radius and limit to default bounds
    radius = min(max_radius, 2)
    lim = min(limit, 10)

    nodes_dict = _nodes()
    if center_node not in nodes_dict:
        return {"nodes": [], "edges": []}

    # Build adjacency list
    adj = {}
    all_edges = _edges()
    for edge in all_edges:
        etype = edge.get("edge_type")
        if edge_types is not None:
            if etype not in edge_types:
                continue
        else:
            if etype == "mentions":
                continue
        if edge.get("strength") == "weak":
            continue

        src = edge["source"]
        tgt = edge["target"]
        adj.setdefault(src, []).append((tgt, edge))
        adj.setdefault(tgt, []).append((src, edge))

    # BFS
    queue = deque([(center_node, 0)])
    visited_nodes = {center_node}
    node_distances = {center_node: 0}
    collected_edges = []
    seen_edges = set()

    while queue:
        curr, dist = queue.popleft()
        if dist >= radius:
            continue
        for neighbor, edge in adj.get(curr, []):
            edge_key = (edge["source"], edge["edge_type"], edge["target"])
            if edge_key not in seen_edges:
                collected_edges.append(edge)
                seen_edges.add(edge_key)

            if neighbor not in visited_nodes:
                visited_nodes.add(neighbor)
                node_distances[neighbor] = dist + 1
                queue.append((neighbor, dist + 1))

    # Sort by relevance (distance from center)
    sorted_nodes = sorted(visited_nodes, key=lambda x: node_distances[x])
    limited_nodes_set = set(sorted_nodes[:lim])

    result_nodes = []
    for nid in sorted_nodes[:lim]:
        if nid in nodes_dict:
            result_nodes.append(nodes_dict[nid])
        else:
            parts = nid.split("::")
            t = parts[0] if len(parts) > 1 else "concept"
            title = "::".join(parts[1:]) if len(parts) > 1 else nid
            result_nodes.append({
                "id": nid,
                "type": t,
                "title": title,
                "wiki_path": None,
                "aliases": [],
                "source_ids": [],
                "status": "draft"
            })

    result_edges = []
    for edge in collected_edges:
        if edge["source"] in limited_nodes_set and edge["target"] in limited_nodes_set:
            result_edges.append(edge)

    return {"nodes": result_nodes, "edges": result_edges}
