# global variable
x = 42


def sun(y):  # mutation -> stateful
    global x
    x = x + y ** 3
    return x


print(sun(3))
print(sun(5))
print(x)
