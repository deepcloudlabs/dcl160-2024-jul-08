n = 17
series = [n]
while n != 1:
    """
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1    
    """
    n = n // 2 if n % 2 == 0 else 3 * n + 1
    series.append(n)
print(series, len(series))
