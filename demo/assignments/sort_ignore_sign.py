
nums = [ -10, 4, 5, 20, -50, -15, 22]

for n in sorted(nums, key = abs):
    print(n, end = ' ')