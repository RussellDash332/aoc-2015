import sys

m = []
for line in sys.stdin:
    m.append(list(map(lambda x: int(x == "#"), line.strip())))

r, c = len(m), len(m[0])

def adj(rx, cx):
    res = []
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            if dr**2 + dc**2 != 0 and rx + dr in range(r) and cx + dc in range(c):
                res.append((rx + dr, cx + dc))
    return res

D, D2 = {}, {}
for i in range(r):
    for j in range(c):
        D[(i, j)] = m[i][j]
        D2[(i, j)] = m[i][j]
for rx in [0, r - 1]:
    for cx in [0, c - 1]:
        D2[(rx, cx)] = 1

def tick(D, corner):
    new_D = {}
    for rx, cx in D:
        temp = sum(map(D.get, adj(rx, cx)))
        if D[(rx, cx)]:
            new_D[(rx, cx)] = int(temp in [2, 3])
        else:
            new_D[(rx, cx)] = int(temp == 3)
    if corner:
        for rx in [0, r - 1]:
            for cx in [0, c - 1]:
                new_D[(rx, cx)] = 1
    return new_D

# Helper debugging function
def draw(D):
    for i in range(r):
        print(str().join([[".","#"][D[(i, j)]]for j in range(c)]))
    print()

for _ in range(100):
    D = tick(D, False)
    D2 = tick(D2, True)
print("Part 1:", sum(D.values()))
print("Part 2:", sum(D2.values()))