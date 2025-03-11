def positive(lst):
    for idx, value in enumerate(lst):
        if value < 0:
            lst[idx] = abs(value)


l = [-1, 4, -5, 10]
positive(l)
print(l)
