class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def merge(a, b):
    if a is None and b is None:
        return None

    node = LinkedListNode(-1)
    output_root = node

    while a is not None and b is not None:
        node.val = min(a.val, b.val)

        node.next = LinkedListNode(-1)
        node = node.next

        if a.val < b.val:
            a = a.next
        else:
            b = b.next

    if a:
        node.val = a.val
        node.next = a.next
    else:
        node.val = b.val
        node.next = b.next

    return output_root


root_node_1 = LinkedListNode(1)
root_node_1.next = LinkedListNode(2)
root_node_1.next.next = LinkedListNode(4)

root_node_2 = LinkedListNode(1)
root_node_2.next = LinkedListNode(3)
root_node_2.next.next = LinkedListNode(4)

merged = merge(root_node_1, root_node_2)

s = ''

while merged:
    while merged:
        s += f'{merged.val}'

        if merged.next:
            s += ' -> '

        merged = merged.next

print(f'{s}')
