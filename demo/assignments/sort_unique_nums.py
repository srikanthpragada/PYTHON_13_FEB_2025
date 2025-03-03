
data = "10,5,20,50,33,2,10,35,90"

nums = set()
for num in data.split(","):
    nums.add(int(num))

for num in sorted(nums):
    print(num, end = ' ')

