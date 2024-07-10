# global variable
x = 42


def sun(y):  # side effect free -> stateless
    # local variable
    x = y ** 3
    return x


print(sun(3))
print(x)
