import sys

lst = []
for line in sys.stdin:
    lst.append(line.strip())

def is_nice(s):
    vowels = 0
    for v in 'aeiou':
        vowels += s.count(v)
    if vowels < 3:
        return False

    for i in ['ab', 'cd', 'pq', 'xy']:
        if i in s:
            return False
    
    has_double = False
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            has_double = True
            break
    
    return has_double

def is_nice2(s):
    import string
    letters = string.ascii_lowercase

    has_aba = False
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            has_aba = True
            break
    if not has_aba:
        return False

    for i in letters:
        for j in letters:
            if s.count(i + j) > 1:
                return True
    return False

print("Part 1:", len(list(filter(is_nice, lst))))
print("Part 2:", len(list(filter(is_nice2, lst))))