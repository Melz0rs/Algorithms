class BinaryTreeNode:

    left = None
    right = None
    value = None

    def __init__(self, value=None):
        self.value = value

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
