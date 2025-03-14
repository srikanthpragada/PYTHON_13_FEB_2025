import sys

if len(sys.argv) < 2:
    print('Sorry! Number is missing. ')
    exit()

num = int(sys.argv[1])

length = 10    # default length
if len(sys.argv) > 2:     # if length is given then use it
    length = int(sys.argv[2])

for n in range(1, length + 1):
    print(f"{num:4} * {n:2} = {num * n:6}")
