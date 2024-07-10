def is_even(number):
    return number % 2 == 0


def is_odd(number):
    return number % 2 != 0

result = is_even(42) # True
print(result) # True
result = is_even(549) # False
print(result) # False
is_odd(549)
