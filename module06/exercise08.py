from functools import reduce

numbers = range(1,100)
result = reduce(lambda x,y: x+y, filter(lambda x: x % 2 == 1, numbers))
result = sum(filter(lambda x: x % 2 == 1, numbers))
print(result)