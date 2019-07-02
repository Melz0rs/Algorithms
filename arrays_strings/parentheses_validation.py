def is_valid(s):
    stack = []
    pop_actions_set = {')', '}', ']'}
    open_to_close = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    for c in s:
        if c in pop_actions_set:
            if len(stack) == 0:
                return False

            popped = stack.pop()

            if open_to_close[popped] != c:
                return False

        else:
            stack.append(c)

    if len(stack) > 0:
        return False

    return True


str = "([)]"
valid = is_valid(str)

print(f'valid: {valid}')