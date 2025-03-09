def infer_relations(entities: list[str]) -> list[tuple[str, str, str]]:
    edges: list[tuple[str, str, str]] = []
    for idx in range(len(entities) - 1):
        edges.append((entities[idx], "related_to", entities[idx + 1]))
    return edges
