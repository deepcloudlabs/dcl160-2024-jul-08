def _3n_plus1(n: int) -> list[int]:
    print("_3n_plus1 just started...")
    series: list[int] = [n]
    while n > 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        series.append(n)
    print("_3n_plus1 about to return...")
    return series


for number in _3n_plus1(17):
    print(f"for: {number}")
    if number == 10:
        break
