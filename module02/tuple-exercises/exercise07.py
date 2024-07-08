employees = ("jack", "kate", "james", "ben", "sun", "jin", "kate", "jack", "kate")
print(employees)
print(len(employees))
print(employees.count("kate"))
print(employees.index("kate"))  # 1
print(employees.index("kate", 2))  # 6
print(employees.index("kate", 7))  # 8
# print(employees.index("adam"))  # ValueError
print(employees.count("adam"))  # ValueError
print("adam" in employees)  # False
print("jack" in employees)  # True
