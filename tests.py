# from arrays_strings.find_doubles_of_sum import find_sum_of_doubles
# arr = [5, 2, 1, 3, 6, 4]
# sum = 7
#
# doubles = find_sum_of_doubles(arr, sum)
#
# print(f'double: {doubles}')
#



from binary_tree import utils
from binary_tree.find_max_depth import find_max_depth

root = utils.generate([1, 2])

depth = find_max_depth(root)

print(f'max_depth: {depth}')



