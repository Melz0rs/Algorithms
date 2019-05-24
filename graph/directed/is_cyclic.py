from graph.algorithms.dfs import dfs


# Complexity: O(V + E)
def is_cyclic(node_ids, node_id_to_node_ids):
    state = {"is_graph_cyclic": False}

    def has_already_visited(node_id, visited):
        if state["is_graph_cyclic"] is False:
            state["is_graph_cyclic"] = node_id in visited

    random_node = next(iter(node_ids))

    dfs(node_id_to_node_ids, random_node,
        visit_fn=lambda node_id, visited: has_already_visited(node_id, visited))

    return state["is_graph_cyclic"]


def test():
    node_ids = {1, 2, 3, 4}
    edges = {
        1: {2, 3},
        2: {4}
    }

    is_graph_cyclic = is_cyclic(node_ids, edges)

    print(f"is_graph_cyclic: {is_graph_cyclic}")
