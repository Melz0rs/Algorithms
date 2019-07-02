def two_sum(arr, sum):
    seen = {}

    for i in range(len(arr)):
        current_val = arr[i]
        looking_for = sum - current_val

        if looking_for in seen:
            return [seen[looking_for], i]

        seen[current_val] = i

    return None


arr = [2, 1, 7, 15]
indices = two_sum(arr, 9)

print(f'indices: {indices}')