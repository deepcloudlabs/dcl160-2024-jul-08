def fun(x=1, y=2, z=3):
    return x * y + z


print(fun())  # fun(1,2,3)
print(fun(5))  # fun(5,2,3)
print(fun(6, 8))  # fun(6,8,3)
print(fun(1, 2, 3))


def us_al(x, y=2):
    return x ** y


print(us_al(8))
print(us_al(8, 3))
