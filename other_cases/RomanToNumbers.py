letter_values = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}


def roman_to_number(roman_letters):
    result = 0
    try:
        assert (roman_letters not in ["None", None, "", " "] and type(
            roman_letters) == str), "Wrong content (Does not contain Roman numerals)"
        previous_value = 0
        for letter in reversed(roman_letters.upper()):
            value = letter_values.get(letter, 0)
            result, previous_value = result + (
                value if (previous_value <= value) else (-value)), value
        return result
    except AssertionError as ex:
        print("Message: ", ex)
        return result


print("Result: ", roman_to_number("LXVII"))
