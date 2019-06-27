def make_duffel_bag_util(weights_and_values, capacity, duffel_bags=[]):
    # filter items i don't have capacity for
    weights_and_values = list(filter(lambda weight_and_value: capacity >= weight_and_value[0], weights_and_values))

    if len(weights_and_values) == 0:
        return duffel_bags

    current_item = weights_and_values[0]
    current_item_value = current_item[1]
    current_item_weight = current_item[0]

    for i in range(len(duffel_bags)):
        new_weight = duffel_bags[i][0] + current_item_weight

        if new_weight <= capacity:
            new_value = duffel_bags[i][1] + current_item_value

            duffel_bags[i] = (new_weight, new_value)

    duffel_bags.append(current_item)

    return make_duffel_bag_util(weights_and_values[1:], capacity, duffel_bags)


def make_duffel_bag(weights_and_values, capacity):
    duffel_bags = make_duffel_bag_util(weights_and_values, capacity)

    print(f'duffel_bags: {duffel_bags}')

    # sort descending the duffel bags and take the highest
    highest_duffel_bag = duffel_bags[0]

    return highest_duffel_bag



items_weights_and_values = [(7, 160), (3, 90), (2, 15), (4, 100), (1, 5), (1, 5), (1, 5), (10, 200), (12, 150), (8, 180), (2, 30)]
capacity = 20

defful_bag = make_duffel_bag(items_weights_and_values, capacity)

# print(f'duffel_bag: {defful_bag}')
