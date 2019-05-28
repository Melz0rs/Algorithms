from graph.algorithms.dfs import dfs


# Complexity: O(V + E)
def is_cyclic(node_ids, node_id_to_node_ids):
    outer_state = {'visited': set()}

    for node_id in node_ids:
        if node_id not in outer_state['visited']:
            state = {"is_graph_cyclic": False}

            def has_already_visited(node_id, visited):
                outer_state['visited'].union(visited)

                if state["is_graph_cyclic"] is False:
                    state["is_graph_cyclic"] = node_id in visited

            dfs(node_id_to_node_ids, node_id,
                visit_fn=lambda node_id, visited: has_already_visited(node_id, visited),visited=outer_state['visited'])

    return state["is_graph_cyclic"]


def test():
    node_ids = [4, 3, 2, 1]
    edges = {
        1: {2, 3},
        2: {4},
        3: {1}
    }

    is_graph_cyclic = is_cyclic(node_ids, edges)

    print(f"is_graph_cyclic: {is_graph_cyclic}")
