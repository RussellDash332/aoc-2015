import sys

s, m, e = 0, 0, 0
for line in sys.stdin:
    line = line.strip()
    s += len(line)
    m += len(eval(line))
    e += len(line) + line.count('"') + line.count("\\") + 2
print("Part 1:", s - m)
print("Part 2:", e - s)