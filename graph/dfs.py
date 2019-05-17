# Complexity: O(n)
def dfs(node_id_to_node_ids, source_node_id, visited=None):

    if visited is None:
        visited = set()

    visited.add(source_node_id)
    print(f"{source_node_id} ")

    neighbour_node_ids = node_id_to_node_ids[source_node_id]

    for neighbour_node_id in neighbour_node_ids:
        if neighbour_node_id not in visited:
            dfs(node_id_to_node_ids, neighbour_node_id, visited)


node_id_to_node_ids = {
    0: {1, 2},
    1: {2},
    2: {3, 0},
    3: {3}
}

dfs(node_id_to_node_ids, 2)
