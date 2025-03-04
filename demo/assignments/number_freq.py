nums = {}
while True:
    n = int(input("Enter number [0 to stop] :"))
    if n == 0:
        break

    if n in nums:
        nums[n] = nums[n] + 1  # increment count of existing number
    else:
        nums[n] = 1  # encountered first time

for n, f in nums.items():
    print(n, f)
