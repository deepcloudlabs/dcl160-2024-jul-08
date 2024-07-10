n = 17
series = [n // 2 if n % 2 == 0 else 3 * n + 1 for n in iter(int, n) if n != 1]
print(series, len(series))
