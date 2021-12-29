import sys

conts = []
for line in sys.stdin:
    conts.append(int(line))

def gather(d1, d2):
    d = d1.copy()
    for k in d2:
        d[k] = d.get(k, 0) + d2[k]
    return d

def cc(amt, conts):
    if amt == 0:
        return {0: 1}
    elif amt < 0 or not conts:
        return {}
    return gather(cc(amt, conts[1:]), dict(map(lambda x: (x[0] + 1, x[1]), cc(amt - conts[0], conts[1:]).items())))

d = cc(150, conts)
print("Part 1:", sum(d.values()))
print("Part 2:", d[min(d)])