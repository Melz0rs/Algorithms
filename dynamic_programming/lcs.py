def longest_common_subsequence(str_a, str_b, a_index=0, b_index=0):
    if a_index == len(str_a) or b_index == len(str_b):
        return 0

    if str_a[a_index] == str_b[b_index]:
        return 1 + longest_common_subsequence(str_a, str_b, a_index + 1, b_index + 1)

    else:
        return max(longest_common_subsequence(str_a, str_b, a_index + 1, b_index),
                   longest_common_subsequence(str_a, str_b, a_index, b_index + 1))


a = "AGGTAB"
b = "GXTXAYB"

lcs = longest_common_subsequence(a, b)

print(f'lcs: {lcs}')
