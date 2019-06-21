from binary_tree.BinaryTree import BinaryTree
from binary_tree.BinaryTreeNode import BinaryTreeNode
from binary_tree.string_serializer import serialize, deserialize


root = BinaryTreeNode('a')
binary_tree = BinaryTree(root)

root.insert_left('s')
root.insert_right('d')

left = root.left
right = root.right

left.insert_right('q')
right.insert_left('w')

serialized_string = serialize(binary_tree)

print(f'serialized_string: {serialized_string}')

deserialized_binary_tree = deserialize(serialized_string)

deserialized_binary_tree.traverse_preorder()



