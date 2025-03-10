names = ['C', 'C++', "JavaScript", "Python"]


for n in filter(lambda n: len(n) > 5, names):
    print(n)