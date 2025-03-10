lst = [1, 4, 5, 8, 10]


for n in filter(lambda v: v % 2 == 0, lst):
    print(n)