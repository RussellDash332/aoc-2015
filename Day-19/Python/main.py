import sys

rep = []
for line in sys.stdin:
    line = line.strip().split(" => ")
    rep.append(line)
mol = rep[-1][0]
rep = rep[:-2]

def split(s):
    tmp, res = '', []
    for i in range(len(s)):
        if s[i].isupper() and tmp:
            res.append(tmp)
            tmp = s[i]
        else:
            tmp += s[i]
    return res + [tmp]

def simplify(s):
    for k in trans:
        s = s.replace(k, trans[k])
    return s

trans, ctr = {}, 0
for i in range(len(rep)):
    if rep[i][0] not in trans:
        trans[rep[i][0]] = chr(ctr + 32)
        ctr += 1
    for j in split(rep[i][1]):
        if j not in trans:
            trans[j] = chr(ctr + 32)
            ctr += 1

# Make everything single-character
for i in range(len(rep)):
    rep[i] = list(map(simplify, rep[i]))
mol = simplify(mol)

def replace(molecule, old, new):
    pos = []
    for i in range(len(molecule)):
        if molecule[i:i + len(old)] == old:
            pos.append(i)
    return set(map(lambda x: molecule[:x] + new + molecule[x + len(old):], pos))

res = set()
for pair in rep:
    res = res | replace(mol, *pair)
print("Part 1:", len(res))

# A*?
def find(target, curr, depth):
    if target == curr:
        return depth
    elif len(target) > len(curr):
        raise Exception

    next = set()
    for pair in rep:
        for tmp in replace(curr, *pair[::-1]):
            next.add(tmp)
    next = sorted(next, key=lambda x: (-len(x), x), reverse=True)

    # Start from the shortest
    while next:
        try:
            return find(target, next.pop(0), depth + 1)
        except:
            raise Exception
print("Part 2:", find(trans['e'], mol, 0))