number = int(input("Enter an integer: ").strip())
print(type(number))
print(number)
if number % 2 == 0:
    print(number, "is an even number")
else:
    print(number, "is an odd number")
