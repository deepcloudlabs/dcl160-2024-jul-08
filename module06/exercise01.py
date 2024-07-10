"""
I. Imperative Programming: procedural programming, oop
    Problem -> Algorithm -> Implementation -> Solution
    Data    -> Software
    Data Structure: list/set/tuple/dict/...
    loop: external loop -> for
    solution -> global variable
II. Declarative Programming: functional programming, oop
    Problem -> Description of the solution -> Solution
    Data -> Loop -> internal loop -> pipeline -> Solution
"""
employees = [
    {"fullname": "jack shephard", "department": "Sales", "salary": 100000, "year": 1978, "fulltime": True},
    {"fullname": "kate austen", "department": "IT", "salary": 200000, "year": 1985, "fulltime": False},
    {"fullname": "ben linus", "department": "Finance", "salary": 150000, "year": 1967, "fulltime": True},
    {"fullname": "james sawyer", "department": "HR", "salary": 70000, "year": 1979, "fulltime": True},
    {"fullname": "kim kwon", "department": "Sales", "salary": 120000, "year": 1986, "fulltime": True},
    {"fullname": "sun kwon", "department": "IT", "salary": 200000, "year": 1984, "fulltime": False},
    {"fullname": "hugo reyes", "department": "IT", "salary": 120000, "year": 1992, "fulltime": True}
]
# imperative approach
totalSalaryOfITEmployees = 0
for employee in employees:  # external to collection (list)
    if employee["department"] == "IT":
        totalSalaryOfITEmployees += employee["salary"]
print(totalSalaryOfITEmployees)
# declarative approach -> functional programming
#         HoF (Higher Order Function) -> filter/map/... , Pure Function
#         generator function -> filter/map/...
#         function composition (HoF) -> pipeline (Lazy)
to_salary = lambda employee: employee["salary"]
is_it_employee = lambda employee: employee["department"] == "IT"
totalSalaryOfITEmployees = sum(map(to_salary, filter(is_it_employee, employees)))
print(totalSalaryOfITEmployees)
