def find_largest(node):
    if node.right is not None:
        largest_node, largest_node_parent = find_largest(node.right)

        if largest_node == node.right:
            return largest_node, node

        else:
            return largest_node, largest_node_parent

    else:
        return node, None


def find_second_largest(root):
    largest_node, largest_node_parent = find_largest(root)

    if largest_node.left is not None:
        second_largest_node, _ = find_largest(largest_node.left)

    else:
        second_largest_node = largest_node_parent

    return second_largest_node


