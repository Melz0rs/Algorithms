def find_max_depth(node):
    if node is None:
        return 0

    if node.left is None and node.right is None:
        return 1

    return 1 + max(find_max_depth(node.left), find_max_depth(node.right))

