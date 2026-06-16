from __future__ import annotations

import os
from pathlib import Path


_REPO_MARKERS = ("purpose.md", "schema.md")


def library_root(default: Path) -> Path:
    configured = os.environ.get("SUJIANLIN_LIBRARY_ROOT")
    if configured:
        return Path(configured).expanduser().resolve()
    return default.resolve()


def discover_root() -> Path:
    """Auto-discover the library root, preferring SUJIANLIN_LIBRARY_ROOT.

    Fallback: walk up from this file's directory looking for repo markers
    (purpose.md + schema.md). This works whether the module is imported from
    the repo or from an installed copy.
    """
    configured = os.environ.get("SUJIANLIN_LIBRARY_ROOT")
    if configured:
        return Path(configured).expanduser().resolve()

    current = Path(__file__).resolve().parent
    for _ in range(5):
        if all((current / marker).exists() for marker in _REPO_MARKERS):
            return current
        parent = current.parent
        if parent == current:
            break
        current = parent

    raise RuntimeError(
        "Cannot discover library root. Set SUJIANLIN_LIBRARY_ROOT "
        "to the shared library directory containing graph/ and Data/Spaces_ac_cn/."
    )
