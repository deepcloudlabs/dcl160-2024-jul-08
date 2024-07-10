"""
1. Text I/O -> HRF
    x : int = 3_615_549 -> memory [4B] -> persist -> file
    Disk: 3|6|1|5|5|4|9 [7B]
    numbers = [4,8,15,16,23,42] [24B]
    Disk: 4|8|1|5|1|5|2|3|4|2   [10B]
          4,8,15,16,23,42       [15B]
2. Binary I/O
    x : int = 3_615_549 -> memory [4B] -> persist -> file
    Disk: [4B]
    numbers = [4,8,15,16,23,42] [24B]
"""
