def longest(str):
    str_length = len(str)

    if str_length <= 1:
        return str_length

    max_length = start = 0
    end = start + 1
    existing_letters = {str[start]}

    while end > start:
        if str[end] in existing_letters:
            existing_letters.remove(str[start])
            start += 1

            if start

        else:
            print(f'end: {end}, start: {start}')
            max_length = max(max_length, end + 1 - start)
            print(f'max_length: {max_length}')

            existing_letters.add(str[end])
            end += 1

    return max_length


length = longest('bbb')
print(f'length: {length}')