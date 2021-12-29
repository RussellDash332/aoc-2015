gift = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

import sys, re

num = 1
match1, match2 = False, False

for line in sys.stdin:
    line = re.findall(r'([a-z]+: \d+)', line)
    
    found1 = True
    for cat in line:
        cat = cat.split(": ")
        if gift[cat[0]] != int(cat[1]):
            found1 = False
            break
    if not match1 and found1:
        p1 = num
        match1 = True
    
    found2 = True
    for cat in line:
        cat = cat.split(": ")
        greater = ['cats', 'trees']
        fewer = ['pomeranians', 'goldfish']
        if cat[0] in greater and gift[cat[0]] >= int(cat[1]) or \
            cat[0] in fewer and gift[cat[0]] <= int(cat[1]) or \
            cat[0] not in greater + fewer and gift[cat[0]] != int(cat[1]):
            found2 = False
            break
    if not match2 and found2:
        p2 = num
        match2 = True
    num += 1

print("Part 1:", p1)
print("Part 2:", p2)