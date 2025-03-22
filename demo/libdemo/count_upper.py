with open("names.txt") as f:
    upper = 0
    for c in f.read():
        if c.isupper():
            upper += 1

    print('Upper count = ', upper)
