def count_upper(s):
    count = 0
    for c in s:
        if c.isupper():
            count += 1

    return count


names = ['JAVA', 'Python', 'C#']

for n in map(count_upper, names):
    print(n)

for n in map(str.lower, names):
    print(n)