# complexity: O(N^2)
def maxsort(arr):
    length = len(arr)
    sorted_arr = arr.copy()

    for i in range(length):
        max_index = 0

        for j in range(0, length - i):
            if sorted_arr[j] > sorted_arr[max_index]:
                max_index = j

        sorted_arr[length - i - 1], sorted_arr[max_index] = sorted_arr[max_index], sorted_arr[length - i - 1]

    return sorted_arr


def test():
    arr = [4, 5, 56, 12, 87, 2, 0, 99, 111, 43]

    sorted_arr = maxsort(arr)

    print(f"sorted_arr: {sorted_arr}")
