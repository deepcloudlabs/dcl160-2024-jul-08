min_value = min([100, 42, 55, 13, 47])
print(min_value)


def fun(min, max):
    # parameter min hides builtin function min!
    min_value = min([100, 42, 55, 13, 47])  # error -> TypeError: 'int' object is not callable


fun(3, 5)
