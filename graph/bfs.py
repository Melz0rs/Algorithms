# Complexity: O(V + E)
def bfs(node_id_to_node_ids, source_node_id):

    visited_node_ids_to_hops = {source_node_id: 0}
    queue = [source_node_id]

    while queue:

        current_node_id = queue.pop()
        print(f"{current_node_id} ")

        current_node_hops = visited_node_ids_to_hops[current_node_id]

        neighbour_node_ids = node_id_to_node_ids[current_node_id]

        for neighbour_node_id in neighbour_node_ids:
            if neighbour_node_id not in visited_node_ids_to_hops:
                visited_node_ids_to_hops[neighbour_node_id] = current_node_hops + 1

                queue.append(neighbour_node_id)

    return visited_node_ids_to_hops


node_id_to_node_ids = {
    1: {2, 3, 6},
    2: {1, 4, 3},
    3: {1, 2, 5, 6},
    4: {2},
    5: {3, 6},
    6: {3, 1, 5}
}

node_ids_to_hops = bfs(node_id_to_node_ids, 1)

print(f"node_ids_to_hops: {node_ids_to_hops}")
