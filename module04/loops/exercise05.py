number = int(input("Enter an integer: ").strip())
total = 0
loop = 0
while total <= number:
    total += 2 * loop + 1
    loop += 1
print(f"square root of {number} is {loop-1}")
