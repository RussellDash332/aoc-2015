target = int(input())
n = 1_000_000

presents = [0] * n
for i in range(1, n):
    tmp = i - 1
    while tmp < n:
        presents[tmp] += 10 * i
        tmp += i
    if presents[i - 1] >= target:
        print("Part 1:", i)
        break

presents = [0] * n
for i in range(1, n):
    tmp = i - 1
    for _ in range(50):
        if tmp >= n:
            break
        presents[tmp] += 11 * i
        tmp += i
    if presents[i - 1] >= target:
        print("Part 2:", i)
        break