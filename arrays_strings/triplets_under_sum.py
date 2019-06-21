def find_triplets_under_sum(arr, sum):
    cache_matrix = [None] * len(arr)
    triplets_count = 0

    # init cache matrix O(n)
    for i in range(len(arr)):
        cache_matrix[i] = [None] * len(arr)

    # create sum cache matrix, O(n^2)
    for first_index in range(len(arr)):
        first_num = arr[first_index]

        # cache the diagonal
        if cache_matrix[first_index][first_index] is None:
            cache_matrix[first_index][first_index] = first_num

        for second_index in range(first_index, len(arr)):
            second_num = arr[second_index]

            # cache the diagonal
            if cache_matrix[second_index][second_index] is None:
                cache_matrix[second_index][second_index] = second_num

            # cache the sum
            if cache_matrix[first_index][second_index] is None:
                cache_matrix[first_index][second_index] = \
                    first_num + second_num

    for row_index in range(len(cache_matrix)):
        print(f'row_index: {row_index}')

        for column_index in range(row_index + 1, len(cache_matrix[row_index]) - 1):

            print(f'column_index: {column_index}')

            current_sum = cache_matrix[row_index][column_index] + \
                          cache_matrix[row_index][column_index + 1] - \
                          cache_matrix[row_index][row_index]

            print(f'triplet: ({cache_matrix[row_index][row_index]}, '
                  f'{cache_matrix[column_index][column_index]}, '
                  f'{cache_matrix[column_index + 1][column_index + 1]})')

            if current_sum < sum:
                triplets_count += 1

    return triplets_count


arr = [-2, 0, 1, 3]
triplets_count = find_triplets_under_sum(arr, 2)

print(f'triplets_count: {triplets_count}')











