import re

st = "abc123xyz985pqr23"

numbers = re.findall(r'\d+', st)
print(numbers)

s = "".join(numbers)

print(s)


