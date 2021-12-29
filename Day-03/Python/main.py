nav = input()
x, y, xs, ys, xr, yr = 0, 0, 0, 0, 0, 0
d = {(0, 0)}
ds, dr = {(0, 0)}, {(0, 0)}
for i in range(len(nav)):
    arrow = nav[i]
    if arrow == '^':
        y += 1
        if i % 2:
            yr += 1
        else:
            ys += 1
    elif arrow == 'v':
        y -= 1
        if i % 2:
            yr -= 1
        else:
            ys -= 1
    elif arrow == '<':
        x -= 1
        if i % 2:
            xr -= 1
        else:
            xs -= 1
    else:
        x += 1
        if i % 2:
            xr += 1
        else:
            xs += 1
    d.add((x, y))
    dr.add((xr, yr))
    ds.add((xs, ys))

print("Part 1:", len(d))
print("Part 2:", len(dr | ds))