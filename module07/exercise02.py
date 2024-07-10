list = [1, 2, "three", 4, 5]
try:
    # open the file
    # print(list[5])
    # int(list[2])
    print(list[-1])
except IndexError as ie:
    print(ie)
except ValueError as ve:
    print(ve)
finally:
    # close the file
    print("Finally, we arrived here.")
list = []
