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


def is_symmetric(root):



root = BinaryTreeNode(1)

root.insert_left(2)
root.insert_right(2)

left = root.left
right = root.right

left.insert_right(4)
left.insert_left(3)

right.insert_right(3)
right.insert_left(4)

is_symmetric = is_symmetric(root)

print(f'is_symmetric: {is_symmetric}')

