from binary_tree.BinaryTreeNode import BinaryTreeNode
from binary_tree.BinaryTree import BinaryTree


UP_CHAR = '^'
RIGHT_CHAR = '>'
LEFT_CHAR = '<' \
            ''

def serialize(binary_tree):
    root = binary_tree.root

    return __serialize_util(root)


def __serialize_util(node, serialized_string=''):
    serialized_string += node.value

    if node.left is not None:
        serialized_string += LEFT_CHAR

        serialized_string += __serialize_util(node.left)

    if node.right is not None:
        serialized_string += RIGHT_CHAR

        serialized_string += __serialize_util(node.right)

    serialized_string += UP_CHAR

    return serialized_string


def deserialize(string):
    nodes_stack = []
    current_node = BinaryTreeNode()

    for char in string:
        if char == UP_CHAR:
            if len(nodes_stack) > 0:
                current_node = nodes_stack.pop()
                pass

        if char == RIGHT_CHAR:
            nodes_stack.append(current_node)

            current_node.right = BinaryTreeNode()
            current_node = current_node.right
            pass

        if char == LEFT_CHAR:
            nodes_stack.append(current_node)

            current_node.left = BinaryTreeNode()
            current_node = current_node.left
            pass

        if char != RIGHT_CHAR and char != LEFT_CHAR and char != UP_CHAR:
            current_node.value = char
            pass

    return BinaryTree(current_node)
