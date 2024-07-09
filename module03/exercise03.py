name = "jack shephard"
print(len(name))
print(name[0])
# IndexError: string index out of range
# error: print(name[13])
print(name[-1])
print(name[-13])
# IndexError: string index out of range
# error: print(name[-14])
print(name[::-1])
print(name[5:])
print(name[5::-1])
