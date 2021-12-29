from hashlib import md5

s = input()
i = 1
while not md5((s + str(i)).encode('utf-8')).hexdigest().startswith('00000'):
    i += 1
print("Part 1:", i)

j = 1
while not md5((s + str(j)).encode('utf-8')).hexdigest().startswith('000000'):
    j += 1
print("Part 2:", j)