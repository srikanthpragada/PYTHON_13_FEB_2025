# Take a number and display whether it is prime
num = int(input("Enter a number :"))

for n in range(2, num // 2 + 1):
    if num % n == 0:
        print("Not prime")
        break
else:
    print("Prime")
