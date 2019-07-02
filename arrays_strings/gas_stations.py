def gas_stations(gas, cost):

    for start_index in range(len(gas)):
        accumulated_gas = 0

        for i in range(len(gas)):
            current_index = (start_index + i) % len(gas)
            current_gas_station = gas[current_index]

            accumulated_gas += current_gas_station - cost[current_index]

            if accumulated_gas < 0:
                break

        if accumulated_gas >= 0:
            return start_index

    return -1


gas = [1, 2, 1, 4]
cost = [3, 2, 2, 1]

start_index = gas_stations(gas, cost)
#w
print(f'start_index: {start_index}')