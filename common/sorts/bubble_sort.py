# complexity: O(N^2)
def bubble_sort(arr):
    sorted_arr = arr.copy()
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]

    return sorted_arr


arr = [4, 5, 56, 12, 87, 2, 0, 99, 111, 43]

sorted_arr = bubble_sort(arr)

print(f"sorted_arr: {sorted_arr}")

