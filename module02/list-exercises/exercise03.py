employees = [
    ("jack", "bauer", 1956, 100_000, ["IT"]),
    ("kate", "austen", 1988, 200_000, ["SALES", "FINANCE"]),
    ("james", "sawyer", 1986, 50_000, ["IT", "FINANCE", "SALES"]),
    ("ben", "linus", 1964, 300_000, ["IT", "HR"]),
    ("sun", "kwon", 1989, 400_000, ["IT"])
]
print(employees)
employees.sort(key=lambda employee: len(employee[4]), reverse=True)
print(employees)
