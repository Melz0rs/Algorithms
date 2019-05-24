# Complexity O(N*log(N))
def merge_sort(arr, is_smaller_fn=None):
    length = len(arr)

    if length > 1:
        if is_smaller_fn is None:
            is_smaller_fn = lambda a, b: a < b

        middle = len(arr) // 2

        left = arr[:middle]
        right = arr[middle:]

        merge_sort(left, is_smaller_fn)
        merge_sort(right, is_smaller_fn)

        l = r = k = 0

        while l < len(left) and r < len(right):
            if is_smaller_fn(left[l], right[r]):
                arr[k] = left[l]
                l += 1
            else:
                arr[k] = right[r]
                r += 1

            k += 1

        while l < len(left):
            arr[k] = left[l]
            l += 1
            k += 1

        while r < len(right):
            arr[k] = right[r]
            r += 1
            k += 1


def test():
    arr = [4, 5, 56, 12, 87, 2, 0, 99, 111, 43]

    merge_sort(arr)

    print(f"sorted_arr: {arr}")