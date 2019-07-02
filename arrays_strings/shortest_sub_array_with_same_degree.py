def find_shortest_subarray_with_same_degree(arr):
    initial_degree = get_array_degree(arr)
    left_index = 0
    right_index = len(arr)

    degree = initial_degree

    # Binary search going to the right finding the shortest array with the same degree
    while degree == initial_degree:
        current_index = int(len(arr[left_index:]) / 2)

        subarray = arr[current_index:]

        degree = get_array_degree(subarray)
        print(f'degree: {degree}')

    degree = initial_degree

    while degree == initial_degree:
        current_index = int(len(arr[:right_index]) / 2)
        subarray = arr[:current_index]

        degree = get_array_degree(subarray)
    # Binary search going to the right finding the shortest array with the same degree

    return right_index - left_index


def

def get_array_degree(arr):
    num_to_occurances = {}

    for num in arr:
        if num not in num_to_occurances:
            num_to_occurances[num] = 0

        num_to_occurances[num] += 1

    return max(map(lambda key: num_to_occurances[key], num_to_occurances))


arr = [1, 2, 2, 6, 1, 5]
shortest = find_shortest_subarray_with_same_degree(arr)

print(f'shortest: {shortest}')
