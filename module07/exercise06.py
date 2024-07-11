with open("employees.txt", mode="rt") as employees:
    try:
        for line in employees:
            full_name, department, salary, birth_year, full_time = line.strip().split(",")
            print(f"{full_name},{department},{salary},{birth_year},{full_time}")
    except IOError as e:
        print(e)
# file is closed!
