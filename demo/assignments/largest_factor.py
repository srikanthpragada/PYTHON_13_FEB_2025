# Take a number and display its factors
num = int(input("Enter a number :"))

for n in range(num // 2, 0, -1):
    if num % n == 0:
        print(n)
        break


