# generator function -> lazy
def _3n_plus1(n: int) -> list[int]:
    print("_3n_plus1 just started...")
    yield n
    while n > 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        print(f"yielding {n}")
        yield n
    print("_3n_plus1 about to return...")


result = _3n_plus1(17)
print(next(result))
print(next(result))