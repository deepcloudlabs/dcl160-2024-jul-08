n = 17
series = [n := n // 2 if n % 2 == 0 else 3 * n + 1 for _ in iter(int, 1)]
print(series, len(series))
