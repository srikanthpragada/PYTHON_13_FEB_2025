marks = [90, 45, 80, 68, 30]

def grade(m):
    if m >= 80:
        return 'A'
    elif m >= 60:
        return 'B'
    else:
        return 'C'

for g in map(grade, marks):
    print(g)