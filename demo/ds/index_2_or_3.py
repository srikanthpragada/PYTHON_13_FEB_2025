l = [1, 430, 40, 30, 22, 44, 55, 66, 89]

for idx, v in enumerate(l, start = 1):
    if idx % 2 == 0 or idx % 3 == 0:
        print(v)
