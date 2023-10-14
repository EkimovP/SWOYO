import pytest


def roman_numerals_to_int(roman_numeral):
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    prev_value = 0
    for numeral in reversed(roman_numeral):
        if numeral in roman_dict:
            value = roman_dict[numeral]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        else:
            return None  # Если встречается некорректный символ, возвращаем None
    return total


@pytest.mark.parametrize("roman, expected", [
    ('I', 1),
    ('IV', 4),
    ('MD', 1500),
])
def test_valid_roman_numerals(roman, expected):
    assert roman_numerals_to_int(roman) == expected


@pytest.mark.parametrize("invalid_roman", [
    'Invalid',
    (2, None),
    ((2,3), None),
    ('str', None),
])
def test_invalid_roman_numerals(invalid_roman):
    assert roman_numerals_to_int(invalid_roman) is None