"""
GCD (Greatest Common Divisor)
Euclid's Algorithm
gcd(1071,462)

"""
x = 1071
y = 462
while x != y:
    if x > y:
        x = x - y
    else:
        y = y - x
print(x)
