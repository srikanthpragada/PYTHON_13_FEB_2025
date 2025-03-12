import sys

if len(sys.argv) < 2:
    print("Sorry! Number is missing!")
    exit()

num = int(sys.argv[1])

for n in range(2, num // 2 + 1):
    if num % n == 0:
        print(n, end = ' ')
