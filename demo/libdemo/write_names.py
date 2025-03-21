
names = ['Larry', 'Ellison', 'Jeff', 'Mark', 'Jack']

# 1
f = open('names.txt', 'wt')

# 2
for name in names:
    f.write(name + '\n')

# 3
f.close()
