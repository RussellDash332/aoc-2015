num = input()
def tick(num):
    curr, cnt = num[0], 0
    res = ''
    for i in range(len(num)):
        if num[i] == curr:
            cnt += 1
        else:
            res += str(cnt) + curr
            curr, cnt = num[i], 1
    return res + (str(cnt) + num[i]) * int(cnt > 0)

for _ in range(40):
    num = tick(num)
print("Part 1:", len(num))
for _ in range(10):
    num = tick(num)
print("Part 2:", len(num))