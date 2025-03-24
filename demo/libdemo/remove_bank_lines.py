# Remove blank lines from the file

FILENAME = "test.txt"

# Read all lines and place non-blank lines in a list
lines = []
with  open(FILENAME, "rt") as f:
    for line in f.readlines():
        if len(line.strip()) > 0:
            lines.append(line)


# write lines from list to file
with open(FILENAME, "wt") as f:
    for line in lines:
        f.write(line)




