employees = [
    {"fullname": "jack shephard", "department": "Sales", "salary": 100000, "year": 1978, "fulltime": True},
    {"fullname": "kate austen", "department": "IT", "salary": 200000, "year": 1985, "fulltime": False},
    {"fullname": "ben linus", "department": "Finance", "salary": 150000, "year": 1967, "fulltime": True},
    {"fullname": "james sawyer", "department": "HR", "salary": 70000, "year": 1979, "fulltime": True},
    {"fullname": "kim kwon", "department": "Sales", "salary": 120000, "year": 1986, "fulltime": True},
    {"fullname": "sun kwon", "department": "IT", "salary": 200000, "year": 1984, "fulltime": False},
    {"fullname": "hugo reyes", "department": "IT", "salary": 120000, "year": 1992, "fulltime": True}
]
to_salary = lambda employee: employee["salary"]
is_it_employee = lambda employee: employee["department"] == "IT"
is_parttime = lambda employee: not employee["fulltime"]


def fun_to_salary(employee: dict) -> float:
    print(f"fun_to_salary({employee})")
    return employee["salary"]


def fun_is_parttime(employee: dict) -> bool:
    print(f"fun_is_parttime({employee})")
    return not employee["fulltime"]


def fun_is_it_department(employee: dict) -> bool:
    print(f"fun_is_it_department({employee})")
    return employee["department"] == "IT"


totalSalaryOfITParttimeEmployees = sum(
    map(fun_to_salary, filter(fun_is_parttime, filter(fun_is_it_department, employees))))
print(totalSalaryOfITParttimeEmployees)
# employees -> filter -> filter -> map -> sum
# HoF: function -> takes functions as parameters
# Pure Function -> lambda function
# google -> MapReduce -> Hadoop: MR + HDFS
