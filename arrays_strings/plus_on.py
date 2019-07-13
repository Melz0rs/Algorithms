def plus_one(arr):
    length = len(arr)
    bias = 0
    should_add_one = True

    if all(map(lambda x: x == 9, arr)):
        bias = 1

    output_arr = [-1 for i in range(length + bias)]

    for i in range(length - 1, -1, -1):
        current_num = arr[i]
        print(f'i: {i}')

        if should_add_one:
            current_num += 1

            if current_num != 10:
                should_add_one = False

        output_arr[i + bias] = current_num % 10

    if bias == 1:
        output_arr[0] = 1

    return output_arr


arr = [1, 2, 3]
new_arr = plus_one(arr)

print(f'new_arr: {new_arr}')


