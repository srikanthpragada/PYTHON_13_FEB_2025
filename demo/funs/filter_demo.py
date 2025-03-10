lst = [1, 4, 5, 8, 10]


def iseven(n: any) -> bool :
    return n % 2 == 0


for n in filter(iseven, lst):
    print(n)

for n in filter(lambda v: v % 2 == 0, lst):
    print(n)