import sys

nums = []
for line in sys.stdin:
    nums.append(int(line))

# Recursive
def sumset(arr, target):
    if not arr or target > sum(arr):
        return []
    elif target == sum(arr):
        return [arr]
    else:
        return list(map(lambda x: x + [arr[0]], sumset(arr[1:], target - arr[0]))) + sumset(arr[1:], target)

# Iterative
def sumset2(arr, target):
    res = [[]]
    for i in arr:
        res += list(map(lambda x: x + [i], res))
        # Optional to use this filter
        res = list(filter(lambda x: sum(x) <= target, res))
    return list(filter(lambda x: sum(x) == target, res))

def product(arr):
    res = 1
    for i in arr:
        res *= i
    return [len(arr), res]

print("Part 1:", min(map(product, sumset2(nums, sum(nums) // 3)))[1])
print("Part 2:", min(map(product, sumset2(nums, sum(nums) // 4)))[1])