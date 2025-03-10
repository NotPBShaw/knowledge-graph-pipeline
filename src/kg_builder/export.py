import json
from pathlib import Path


def export_edges(edges: list[tuple[str, str, str]], out: Path) -> None:
    out.write_text(json.dumps([{"src": s, "rel": r, "dst": d} for s, r, d in edges], indent=2))
