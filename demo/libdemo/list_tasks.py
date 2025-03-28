from datetime import datetime

f = open("tasks.txt", "rt")

for line in f.readlines():
    parts = line.strip().split(",")
    if len(parts) < 2:
        continue   # ignore line as it has less than required data

    task = parts[0]
    stdate = datetime.strptime(parts[1].strip(), "%d-%m-%Y")
    if len(parts) > 2:
        enddate = datetime.strptime(parts[2].strip(), "%d-%m-%Y")
        result = (enddate - stdate).days
    else:
        result = -1

    print(f"{task:50} {result:3}")


f.close()





