class BinaryTree:

    root = None

    def __init__(self, root):
        self.root = root

    def traverse_preorder(self, node=None):
        if node is None:
            node = self.root

        print(f'{node.value}')

        if node.left is not None:
            self.traverse_preorder(node.left)

        if node.right is not None:
            self.traverse_preorder(node.right)

