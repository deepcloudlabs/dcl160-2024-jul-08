numbers = [4, 8, None, 15, None, 16, None, 23, None, 42, None]
values = [value for value in numbers if value is not None]
none_values = [value for value in numbers if value is None]
print(numbers)
print(values)
print(none_values)
