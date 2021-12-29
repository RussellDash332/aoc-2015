import sys, re

table = []
for line in sys.stdin:
    table.append([*list(map(int, re.findall(r'(\d+)', line))), True, 0])

dist = [0] * len(table)
pts = [0] * len(table)
for t in range(2503):
    for i in range(len(table)):
        if table[i][3]: # flying
            dist[i] += table[i][0]
            table[i][4] += 1
            if table[i][4] == table[i][1]:
                table[i][3], table[i][4] = False, 0
        else: # resting
            table[i][4] += 1
            if table[i][4] == table[i][2]:
                table[i][3], table[i][4] = True, 0
    for i in range(len(table)):
        if dist[i] == max(dist):
            pts[i] += 1 
print("Part 1:", max(dist))
print("Part 2:", max(pts))