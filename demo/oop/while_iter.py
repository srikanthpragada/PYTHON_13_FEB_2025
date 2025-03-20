
l = [1,2,3]

for n in l:
    print(n)


li = l.__iter__()
while True:
    try:
        v = li.__next__()
        print(v)
    except:
        break

