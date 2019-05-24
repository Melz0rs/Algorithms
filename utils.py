import collections


def flatten(x):
    result = []

    for el in x:
        if type(x) is dict:
            el = x[el]

        if isinstance(el, collections.Iterable) and not isinstance(el, str):
            result.extend(flatten(el))
        else:
            result.append(el)

    return result
