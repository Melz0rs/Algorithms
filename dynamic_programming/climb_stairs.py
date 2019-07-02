def climb_stairs(n, memo=None):
    if memo is None:
        memo ={}

    if n in memo:
        return memo[n]

    if n < 0:
        memo[n] = 0
        return 0

    if n == 0:
        memo[n] = 1
        return 1

    for step_size in range(1, 3):
        if n not in memo:
            memo[n] = 0

        memo[n] += climb_stairs(n - step_size, memo)

    return memo[n]


pathes_to_climb_stairs_count = climb_stairs(35)

print(f'pathes_to_climb_stairs_count : {pathes_to_climb_stairs_count }')