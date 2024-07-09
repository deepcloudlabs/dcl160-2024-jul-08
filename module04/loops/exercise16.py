week_day = "friday"
match week_day:
    case "monday":
        day = 1
    case "tuesday":
        day = 2
    case "wednesday":
        day = 3
    case "thursday":
        day = 4
    case "friday":
        day = 5
    case "saturday":
        day = 6
    case _:
        day = 0
print(day)
