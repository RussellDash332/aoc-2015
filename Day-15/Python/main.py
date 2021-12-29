import sys, re

table = []
for line in sys.stdin:
    table.append(list(map(int, re.findall(r'([-\d]+)', line))))
table = list(zip(*table))

res, res2 = 0, 0
for a in range(101):
    for b in range(101):
        for c in range(101):
            if a + b + c <= 100:
                d = 100 - a - b - c
                temp = 1
                for k1, k2, k3, k4 in table[:-1]:
                    temp *= max(0, k1 * a + k2 * b + k3 * c + k4 * d)
                res = max(temp, res)
                cal1, cal2, cal3, cal4 = table[-1]
                if cal1 * a + cal2 * b + cal3 * c + cal4 * d == 500:
                    res2 = max(temp, res2)
print("Part 1:", res)
print("Part 2:", res2)