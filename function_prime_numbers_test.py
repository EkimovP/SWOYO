from function_prime_numbers import prime_numbers


def test_sieve_of_eratosthenes_valid_input():
    low_limit = 2
    high_limit = 30
    result = prime_numbers(low_limit, high_limit)
    assert result == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def test_sieve_of_eratosthenes_invalid_input():
    low_limit = "str"
    high_limit = (2,3)
    result = prime_numbers(low_limit, high_limit)
    assert result == []


def test_sieve_of_eratosthenes_negative_lower_limit():
    low_limit = -6
    high_limit = 30
    result = prime_numbers(low_limit, high_limit)
    assert result == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def test_sieve_of_eratosthenes_upper_limit_too_low():
    low_limit = 2
    high_limit = 1
    result = prime_numbers(low_limit, high_limit)
    assert result == []


def test_sieve_of_eratosthenes_upper_limit_is_2():
    low_limit = 2
    high_limit = 2
    result = prime_numbers(low_limit, high_limit)
    assert result == [2]