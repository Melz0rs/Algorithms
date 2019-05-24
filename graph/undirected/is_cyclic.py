import disjoint_sets.union_find as union_find


# Complexity: O(V + E)
def is_cyclic(node_ids, node_id_to_node_ids):
    parents = {}

    for node_id in node_ids:
        parents[node_id] = node_id

    for source_node_id in node_ids:
        if source_node_id in node_id_to_node_ids:
            for target_node_id in node_id_to_node_ids[source_node_id]:
                source_node_parent = union_find.find_parent(parents, source_node_id)
                target_node_parent = union_find.find_parent(parents, target_node_id)

                if source_node_parent == target_node_parent:
                    return True

                union_find.union(parents, source_node_parent, target_node_parent)

    return False


def test():
    node_ids = {1, 2, 3, 4}
    edges = {
        1: {2, 3},
        2: {4}
    }

    is_graph_cyclic = is_cyclic(node_ids, edges)

    print(f"is_graph_cyclic: {is_graph_cyclic}")
