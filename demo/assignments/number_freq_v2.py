data = [10, 10, 20, 10, 30, 40, 20]

nums = {}

for n in data:
    count = nums.get(n, 0)
    nums[n] = count + 1


for n, f in nums.items():
    print(n, f)
