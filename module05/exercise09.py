def _3n_plus1(n):
    series = [n]
    while n > 1:
        n = n // 2 if n % 2 == 0 else n * 3 + 1
        series.append(n)
    return series, len(series), series[-1] # tuple


result = _3n_plus1(17)
print(type(result))
print(result[0])
print(result[1])
print(result[2])
