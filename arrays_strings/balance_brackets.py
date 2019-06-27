import time


def balance_brackets(n, iter=0):
    atomic_brackets = '()'

    if n == 1:
        return [atomic_brackets], iter

    brackets, iter = balance_brackets(n - 1, iter)
    new_brackets = set()

    for bracket in brackets:
        for i in range(0, len(bracket)):
            iter += 1
            current_brackets = bracket[:i] + atomic_brackets + bracket[i:]

            new_brackets.add(current_brackets)

    return new_brackets, iter


start_time = time.time()
balanced_brackets, iter = balance_brackets(3)
end_time = time.time()

elapsed_time = end_time - start_time

print(f'balanced_brackets: {balanced_brackets}')
print(f'elapsed_time_1: {elapsed_time}')

# arr = []
#
#
# def parens(left, right, string):
#     # if no more brackets can be added then add the final balanced string
#     if left == 0 and right == 0:
#         arr.append(string)
#
#     # if we have a left bracket left we add it
#     if left > 0:
#         parens(left - 1, right + 1, string + "(")
#
#     # if we have a right bracket left we add it
#     if right > 0:
#         parens(left, right - 1, string + ")")
#
#
# # the parameters parens(x, y, z) specify:
# # x: left brackets to start adding
# # y: right brackets we can add only after adding a left bracket
# # z: the string so far
#
# start_time = time.time()
# parens(3, 0, "")
# end_time = time.time()
#
# elapsed_time_2 = end_time - start_time
#
#
# print(f'elapsed_time_2: {elapsed_time_2}')
