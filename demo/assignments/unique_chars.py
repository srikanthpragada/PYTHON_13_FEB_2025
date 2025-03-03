# take 5 names and display unique chars

names = ['Joe', 'James', 'Jack', 'Mark','Anders']
chars = set()

for name in names:
    chars = chars | set(name)

print( sorted(chars))

