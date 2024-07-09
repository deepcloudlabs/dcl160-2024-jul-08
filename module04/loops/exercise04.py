numbers = [4, 8, None, 15, None, None, 16, None, 23, None, 42, None]
# irregular loop
while numbers.count(None) > 0:
    numbers.remove(None)  # True
print(numbers)
