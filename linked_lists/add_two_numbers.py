# from linked_lists.Node import LinkedListNode

class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def add_two_numbers(l1, l2):
    previous_output_node = None
    current_output_node = LinkedListNode(0)
    output_root_node = current_output_node

    while l1 is not None and l2 is not None:
        current_sum = l1.val + l2.val

        current_output_node.val += current_sum

        if current_output_node.val >= 10:
            current_output_node.next = LinkedListNode(int(current_output_node.val / 10))
            current_output_node.val = current_output_node.val % 10

        l1 = l1.next
        l2 = l2.next

        if current_output_node.next is None:
            current_output_node.next = LinkedListNode(0)

        previous_output_node = current_output_node
        current_output_node = current_output_node.next

    if l1 is not None:
        remainders_list = l1
    else:
        remainders_list = l2

    while remainders_list is not None:
        if current_output_node is None:
            current_output_node = LinkedListNode(remainders_list.val)
        else:
            current_output_node.val += remainders_list.val

            if current_output_node.val >= 10:
                current_output_node.next = LinkedListNode(int(current_output_node.val / 10))
                current_output_node.val = current_output_node.val % 10

        if current_output_node.next is None:
            current_output_node.next = LinkedListNode(0)

        previous_output_node = current_output_node
        current_output_node = current_output_node.next
        remainders_list = remainders_list.next

    if current_output_node.val == 0:
        previous_output_node.next = None

    return output_root_node


root_node_1 = LinkedListNode(1)

root_node_2 = LinkedListNode(9)
# root_node_2.next = LinkedListNode(9)

sum = add_two_numbers(root_node_1, root_node_2)

sum_str = ''

while sum:
    sum_str += f'{sum.val}'

    if sum.next:
        sum_str += ' -> '

    sum = sum.next

print(f'sum: {sum_str}')

