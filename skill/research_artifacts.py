from __future__ import annotations

import re
from datetime import date as current_date


def _slugify(text: str) -> str:
    cleaned = re.sub(r"[^\w\u4e00-\u9fff]+", "-", text.strip().lower())
    cleaned = re.sub(r"-+", "-", cleaned).strip("-")
    return cleaned[:80] or "research-query"


def suggest_research_folder(query: str, date: str | None = None) -> str:
    day = date or current_date.today().isoformat()
    return f"docs/research/{day}-{_slugify(query)}/"


def make_materials_template(query: str) -> str:
    return f"""# Materials

Query: {query}

## Nodes Used

-

## Articles Used

-

## Source Markdown Anchors

- `Data/Spaces_ac_cn/markdown/`

## Asset Anchors

- `Data/Spaces_ac_cn/assets/`

## Methods Used

-

## Concepts Used

-

## Paths Used

-
"""


def make_search_log_template(query: str, depth: str = "Level 3") -> str:
    return f"""# Search Log

## Query Intent

{query}

## Search Depth

{depth}

## Entry Points

-

## Exploration Trace

- Searched:
- Reason:
- Result:
- Next turn:

## Concept Pool

-

## Method Pool

-

## Source / Raw Anchors

- article_id:
- source_markdown:
- asset_dir:
- section or line range:
- why raw source was needed:
- what was learned:
- source level:

## Transfer Candidates

-

## Failed / Weak Paths

-

## Open Threads

-

## Working Understanding

"""


def make_brief_report_template(query: str) -> str:
    return f"""# Brief Research Report

## 问题重述

{query}

## 核心发现

-

## 方法论抽象

-

## 架构启发

-

## 证据与来源

- 原文支持:
- 结构支持:
- 综合推理:
- 迁移猜想:

## 不确定性

-

## 后续探索方向

-
"""
