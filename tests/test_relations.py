from kg_builder.relations import infer_relations


def test_infer_relations_links_adjacent_entities() -> None:
    edges = infer_relations(["A", "B", "C"])
    assert len(edges) == 2
