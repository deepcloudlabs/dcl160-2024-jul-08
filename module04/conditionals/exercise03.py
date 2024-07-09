"""
Leap year Test
2000 Leap Year          -> 4
2001 Not a Leap Year
2002 Not a Leap Year
2003 Not a Leap Year
2004 Leap Year

2100 Not a Leap Year -> 100
2200 Not a Leap Year -> 100
2300 Not a Leap Year -> 100
2400 Leap Year       -> 400
"""
# 11:53
year = int(input("Enter a year: ").strip())
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a Leap Year")
        else:
            print(year, "is a Not a Leap Year")
    else:
        print(year, "is a Leap Year")
else:
    print(year, "is a Not a Leap Year")
