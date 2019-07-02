import sys


def max_sub_array(arr):
    previous_max_sum = -sys.maxsize
    current_sum = 0

    for num in arr:
        current_sum += num
        previous_max_sum = max(previous_max_sum, current_sum)

        current_sum = max(0, current_sum)

    return previous_max_sum


arr = [-2]
sub_arr = max_sub_array(arr)

print(f'max_sub_array: {sub_arr}')
