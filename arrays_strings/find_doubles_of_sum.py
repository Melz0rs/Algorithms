from common.sorts.merge_sort import merge_sort


def find_sum_of_doubles(arr, sum):
    arr_length = len(arr)
    i = 0
    j = arr_length - 1
    doubles = []

    merge_sort(arr)

    while i < j:
        current_sum = arr[i] + arr[j]

        if current_sum == sum:
            doubles.append((arr[i], arr[j]))

        if current_sum > sum:
            j -= 1

        else:
            i += 1

    return doubles

#
# arr = [5, 2, 1, 3, 6, 4]
# sum = 7
#
# doubles = find_sum_of_doubles(arr, sum)
#
# print(f'double: {doubles}')

