def fun(x=1, y=2, z=3):
    return x * y + z


print(fun(6))  # 1

print(fun(y=7,  z=8))  # 2

my_params = {
    "z": 8,
    # x --> 1
    "y": 7
}

print(fun(**my_params))  # 3
