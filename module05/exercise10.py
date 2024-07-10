def is_even(number: int) -> bool:
    """
    is_even returns true if number is even, false otherwise
    :param number: an integer number to be tested for evenness
    :return: bool
    """
    return number % 2 == 0

print(is_even(42))