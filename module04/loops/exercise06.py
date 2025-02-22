"""
 A mathematician lives on a street where house numbers are consecutive
 starting from 1. He says that the sum of the house numbers less than
 his house number is equal to the sum of the house numbers greater
 than his house number. Knowing that his house number contains
 3 digits design an algorithm and write a Python script
 to find his house number.
 """
for mathematician_building_no in range(100, 1000):
    left_sum = 0
    right_sum = 0
    for building_no in range(1, mathematician_building_no - 1):
        left_sum += building_no
    building_no = mathematician_building_no + 1
    while right_sum < left_sum:
        right_sum += building_no
        building_no += 1
    if right_sum == left_sum:
        print(mathematician_building_no, building_no - 1)
        break
