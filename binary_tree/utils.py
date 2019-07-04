from binary_tree.BinaryTreeNode import BinaryTreeNode
from queue import Queue


def generate(arr):
    queue = Queue()
    root = BinaryTreeNode(arr[0])
    queue.put(root)
    index = 1

    while not queue.empty():
        node = queue.get()

        if len(arr) > index:
            node.left = BinaryTreeNode(arr[index])
            queue.put(node.left)

        if len(arr) > index + 1:
            node.right = BinaryTreeNode(arr[index + 1])
            queue.put(node.right)

        index += 2

    return root

