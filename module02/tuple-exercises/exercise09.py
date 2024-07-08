jack = ("jack", "bauer", 100_000, "tr1", ["IT", "Sales"])
first_name, last_name, *rest = jack  # unpacking
print(first_name)
print(last_name)
print(rest)
