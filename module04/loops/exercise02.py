numbers = [4, 8, 15, 16, 23, 42]
total = 0
for number in numbers:
    if number % 2 == 0:
        cubed = number ** 3
        total += cubed
print(f"total is {total}")
