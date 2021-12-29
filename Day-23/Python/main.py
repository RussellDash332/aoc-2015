import sys

cmds = []
for line in sys.stdin:
    cmds.append([line[:3], line[4:].strip()])

def simulate(d):
    pos = 0
    while pos < len(cmds):
        if cmds[pos][0] == 'inc':
            d[cmds[pos][1]] += 1
            pos += 1
        elif cmds[pos][0] == 'hlf':
            d[cmds[pos][1]] //= 2
            pos += 1
        elif cmds[pos][0] == 'tpl':
            d[cmds[pos][1]] *= 3
            pos += 1
        elif cmds[pos][0] == 'jmp':
            pos += int(cmds[pos][1])
        elif cmds[pos][0] == 'jio':
            if d[cmds[pos][1][0]] == 1:
                pos += int(cmds[pos][1][3:])
            else:
                pos += 1
        elif cmds[pos][0] == 'jie':
            if not d[cmds[pos][1][0]] % 2:
                pos += int(cmds[pos][1][3:])
            else:
                pos += 1
    return d['b']

print("Part 1:", simulate({'a': 0, 'b': 0}))
print("Part 2:", simulate({'a': 1, 'b': 0}))