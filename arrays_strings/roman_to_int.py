def roman_to_int(roman):
    letter_to_pre_for_subtractions = {
        'X': 'I',
        'V': 'I',
        'L': 'X',
        'C': 'X',
        'D': 'C',
        'M': 'C'
    }

    letter_values = {
        'I': 1,
        'X': 10,
        'V': 5,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    previous_letter = None
    total_sum = 0

    for i in range(len(roman) - 1, -1, -1):
        current_letter = roman[i]
        current_value = letter_values[current_letter]

        if previous_letter in letter_to_pre_for_subtractions and \
           letter_to_pre_for_subtractions[previous_letter] == current_letter:

            total_sum -= current_value

        else:
            total_sum += current_value

        previous_letter = current_letter

    return total_sum


sum = roman_to_int('MCMXCIV')
print(f'sum: {sum}')