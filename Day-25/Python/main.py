import re

r, c = map(int, re.findall(r'(\d+)', input()))
ans = 20151125
for _ in range((c + r) * (c + r - 1) //2 - r):
    ans = 252533 * ans % 33554393

print("Part 1:", ans)
print("Part 2: THE END!")