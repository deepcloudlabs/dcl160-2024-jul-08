from functools import reduce

numbers = [4, 8, 15, 16, 23, 42]
# imperative programming
total = 0
# external loop
for number in numbers:
    if number % 2 == 0:
        cubed = number ** 3
        total += cubed
print(f"total is {total}")

# declarative programming
if_even = lambda n: n % 2 == 0 # lambda function
to_cube = lambda n: n ** 3
# internal loop -> functional programming: generator functions
total = sum(map(to_cube, filter(if_even, numbers)))
print(f"total is {total}")
