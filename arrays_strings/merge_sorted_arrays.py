def merge_sorted_arrays(arr1, arr1_count, arr2, arr2_count):
    index1 = arr1_count - 1
    index2 = arr2_count - 1

    if index2 < 0:
        return

    output_index = len(arr1) - 1

    while output_index >= 0:
        if (arr1[index1] > arr2[index2] or index2 < 0) and index1 >= 0:
            arr1[output_index] = arr1[index1]
            index1 -= 1

        else:
            arr1[output_index] = arr2[index2]
            index2 -= 1

        output_index -= 1


arr1 = [2, 0]
merge_sorted_arrays(arr1, 1, [1], 1)
print(f'arr1: {arr1}')
