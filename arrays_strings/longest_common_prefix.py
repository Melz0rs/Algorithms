def longest_common_prefix(words):
    if words is None or len(words) == 0:
        return ''

    common_prefix = ''
    current_letter = ''
    flag = True
    index = 0

    while flag:
        common_prefix += current_letter

        flag = all(map(lambda word: len(word) > index, words))

        if flag:
            current_letter = words[0][index]

            flag = all(map(lambda word: word[index] == current_letter, words))

            index += 1

    return common_prefix


words = ["", "dog","racecar","car", ""]
common = longest_common_prefix(words)
print(f'common: {common}')

