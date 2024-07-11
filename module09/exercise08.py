import re

result = re.split(r"\s*,\s*", "1, 2, 3, 4, 5, 6, 7", maxsplit=4)
print(result)