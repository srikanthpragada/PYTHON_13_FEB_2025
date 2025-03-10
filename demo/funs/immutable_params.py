def increment(n):
    print(id(n))
    n = n + 1
    print(id(n))

a = 100
print(id(a))
increment(a)
print(a)



