# set: un-ordered, mutable, unique
numbers = {4, 8, 15, 16, 23, 42}
print(len(numbers))
print(numbers)
numbers.add(15)
numbers.add(15)
numbers.add(16)
numbers.add(23)
numbers.add(42)
numbers.add(15)
print(numbers)
numbers.remove(15)
print(numbers)
print(23 in numbers)
print(15 in numbers)
sorted_numbers = sorted(numbers)
# un-ordered: numbers.index(23)
print(type(sorted_numbers))
print(sorted_numbers)
