import z3, string, sys

alphabet = string.ascii_lowercase
lst = [i + j for i in alphabet for j in alphabet] + list(alphabet)

def get(x):
    if x.isnumeric():
        return x # no need convert to int
    return f'var_{x}'

def replace_var(s):
    s = s.replace('\n', ' ')
    res = 'var_' + s[0] if s[0].isalpha() else s[0]
    for i in range(1, len(s)):
        if s[i].isalpha() and not s[i - 1].isalpha():
            res += 'var_' + s[i]
        else:
            res += s[i]
    return res

seq = []
for line in sys.stdin:
    line = line.strip().split(" -> ")
    cmd = line[0].split()
    seq.append([cmd, line])

def simulate(override, seed=0):
    for k in lst:
        exec(f'var_{k} = z3.BitVec(k, 16)')

    for cmd, line in seq:
        if len(cmd) == 1:
            exec(f'var_{line[1]} = {get(cmd[0])}')
            if override and line[1] == 'b':
                exec(f'var_{line[1]} = seed')
        elif cmd[0] == 'NOT':
            exec(f'var_{line[1]} = ~{get(cmd[1])}')
        elif cmd[1] == 'AND':
            exec(f'var_{line[1]} = {get(cmd[0])} & {get(cmd[2])}')
        elif cmd[1] == 'OR':
            exec(f'var_{line[1]} = {get(cmd[0])} | {get(cmd[2])}')
        elif cmd[1] == 'LSHIFT':
            exec(f'var_{line[1]} = {get(cmd[0])} << {get(cmd[2])}')
        elif cmd[1] == 'RSHIFT':
            exec(f'var_{line[1]} = {get(cmd[0])} >> {get(cmd[2])}')

    tmp = {}
    for k in lst:
        if k != str(eval('var_' + k)):
            tmp[k] = eval('var_' + k)

    while type(tmp['a']) != int and any(map(lambda x: type(x[1]) != int, tmp.items())):
        for var in tmp:
            bef = tmp[var]
            check = eval(replace_var(str(tmp[var])))
            if type(check) == int and type(tmp[var]) != int:
                tmp[var] = check
                exec(f'var_{var} = check')
    
    return tmp['a']

res = simulate(False)
print("Part 1:", res)
print("Part 2:", simulate(True, res))