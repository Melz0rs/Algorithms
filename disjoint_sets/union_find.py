def union(parents, root, node):
    root_parent = find_parent(parents, root)
    node_parent = find_parent(parents, node)

    parents[node_parent] = root_parent


def find_parent(parents, item):
    if parents[item] != item:
        parents[item] = find_parent(parents, parents[item])

    return parents[item]
