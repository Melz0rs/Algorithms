def min_cost_climb_stairs_util(cost, position, memo=None):
    if memo is None:
        memo = {}

    if position in memo:
        return memo[position]

    if position >= len(cost):
        memo[position] = 0
        return 0

    memo[position] = min(min_cost_climb_stairs_util(cost, position + 1, memo),
                         min_cost_climb_stairs_util(cost, position + 2, memo)) + cost[position]

    return memo[position]


def min_cost_climb_stairs(cost):
    memo = {}

    return min(min_cost_climb_stairs_util(cost, 0, memo), min_cost_climb_stairs_util(cost, 1, memo))


cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
min_cost = min_cost_climb_stairs(cost)

print(f'min_cost: {min_cost}')
