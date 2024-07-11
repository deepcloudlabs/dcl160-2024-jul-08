import re

line = "a\t\t\n\r     \t b   \t\t\t     c    d   \t e  \t   "
result = re.sub(r"\s+", ",", line.strip(), count=2)
print(result)
print(result.split(","))
