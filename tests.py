# from arrays_strings.find_doubles_of_sum import find_sum_of_doubles
# arr = [5, 2, 1, 3, 6, 4]
# sum = 7
#
# doubles = find_sum_of_doubles(arr, sum)
#
# print(f'double: {doubles}')
#



from binary_tree.BinaryTree import BinaryTree
from binary_tree.BinaryTreeNode import BinaryTreeNode
from binary_tree.bst.find_second_largest import find_second_largest


root = BinaryTreeNode(5)
binary_tree = BinaryTree(root)

root.insert_left(3)
root.insert_right(8)

left = root.left
right = root.right

left.insert_right(5)
left.insert_left(1)

right.insert_left(7)
right.insert_right(12)

right = right.right

right.insert_left(10)

left = right.left

left.insert_left(9)
left.insert_right(11)

second_largest = find_second_largest(root)

print(f'second_largest: {second_largest.value}')



