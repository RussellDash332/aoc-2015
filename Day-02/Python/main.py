import sys

area = 0
ribbon = 0
for line in sys.stdin:
    x, y, z = list(map(int, line.split("x")))
    area += 2 * (x * y + y * z + z * x) + min(x * y, y * z, z * x)
    ribbon += 2 * (x + y + z - max(x, y, z)) + x * y * z
print("Part 1:", area)
print("Part 2:", ribbon)