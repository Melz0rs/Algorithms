def sqrt(x):
    if x <= 1:
        return x

    if x < 0:
        return None

    low = 0
    high = x
    mid = int((low + high) / 2)

    while low != mid:
        power = mid * mid

        if power == x:
            break

        if power > x:
            high = mid

        else:
            low = mid

        mid = int((low + high) / 2)

    return mid


square = sqrt(0)
print(f'square: {square}')