f = None
try:
    f = open("employees.txt", 'rt')

    for line in f.readlines():
        parts = line.split(",")
        # ignore line if it doesn't have name and salaries
        if len(parts) < 2:
            continue

        dept_name = parts[0]
        emp_count = len(parts) - 1

        total = sum(map(int, parts[1:]))
        avg = total // emp_count
        print(f'{dept_name:10} {total:10}  {avg:10}')
except Exception as ex:
    print("Error ->", ex)
finally:
    if f is not None:
        f.close()
