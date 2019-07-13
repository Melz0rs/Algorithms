def remove_duplicates_sorted_array(arr):
    if len(arr) == 0 or arr is None:
        return 0

    index = 0

    for i in range(1, len(arr)):
        print(f'arr[i]: {arr[i]}, arr[index]: {arr[index]}')
        if arr[i] > arr[index]:
            index += 1
            arr[index] = arr[i]

    for i in range(index + 1, len(arr)):
        arr[i] = -1

    return index + 1


arr = []
length = remove_duplicates_sorted_array(arr)

print(f'length: {length}, arr: {arr}')