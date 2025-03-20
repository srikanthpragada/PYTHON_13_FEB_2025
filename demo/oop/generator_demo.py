def numbers():
    for n in range(1, 5):
        yield n


g = numbers()
print(type(g))

print(next(g))
print(next(g))
