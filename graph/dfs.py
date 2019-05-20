# Complexity: O(V + E)
def dfs(node_id_to_node_ids, source_node_id, visit_fn, visited=None):

    if visited is None:
        visited = set()

    visit_fn(source_node_id, visited)

    if source_node_id in visited:
        return

    visited.add(source_node_id)
    # print(f"{source_node_id} ")

    neighbour_node_ids = node_id_to_node_ids[source_node_id]

    for neighbour_node_id in neighbour_node_ids:
            dfs(node_id_to_node_ids, neighbour_node_id, visited)


node_id_to_node_ids = {
    0: {1, 2},
    1: {2},
    2: {3, 0},
    3: {3}
}

dfs(node_id_to_node_ids, 2)
