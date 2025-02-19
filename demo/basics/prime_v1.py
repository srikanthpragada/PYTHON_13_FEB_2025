# Take a number and display whether it is prime
num = int(input("Enter a number :"))

count = 0
for n in range(2, num // 2 + 1):
    if num % n == 0:
       count += 1   # count = count + 1

if count == 0:
    print("Prime")
else:
    print("Not a prime")
