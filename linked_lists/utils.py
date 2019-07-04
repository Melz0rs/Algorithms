def to_string(node):
    s = ''

    while node:
        s += f'{node.val}'

        if node.next:
            s += ' -> '

        node = node.next

    return s


def generate(arr):