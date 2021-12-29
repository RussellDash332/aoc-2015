import sys

D, D2 = {}, {}
for line in sys.stdin:
    line = line.split()
    cmd = line[-4]
    (x1, y1), (x2, y2) = list(map(int, line[-3].split(','))), list(map(int, line[-1].split(',')))
    if cmd == 'toggle':
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                D[(x, y)] = 1 - D.get((x, y), 0)
                D2[(x, y)] = D2.get((x, y), 0) + 2
    else:
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                D[(x, y)] = int(cmd == "on")
                D2[(x, y)] = max(0, D2.get((x, y), 0) + 2 * int(cmd == "on") - 1)
print("Part 1:", sum(D.values()))
print("Part 2:", sum(D2.values()))