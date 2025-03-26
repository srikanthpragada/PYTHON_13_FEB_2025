import re

with  open("lines.txt", "rt") as f:
    contents = f.read()

contents = re.sub(' +', ' ', contents)
contents = re.sub(r'\n+', '\n', contents)

with open("lines.txt", "wt") as f:
    f.write(contents)

