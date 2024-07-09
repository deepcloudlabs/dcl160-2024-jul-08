number = float(input("Enter an integer:").strip())
match number:
    case number if number == float("inf"):
        print(f"{number} is positive infinity")
    case number if number == float("-inf"):
        print(f"{number} is negative infinity")
    case number if number > 0:
        print(f"{number} is a positive integer")
    case number if number < 0:
        print(f"{number} is a negative integer")
    case number if number == 0:
        print(f"{number} is zero")
    case _:
        print(f"{number} is not a number")
