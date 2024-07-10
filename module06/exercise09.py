import sys
from functools import reduce
sys.set_int_max_str_digits(500_000)
numbers = range(1, 50_000)
result = reduce(lambda x, y: x * y, numbers, 1)
print(result)
