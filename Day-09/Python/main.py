import sys

graph = {}
for line in sys.stdin:
    line = line.split()
    src = line[0]
    dst = line[2]
    dist = int(line[4])
    if src not in graph:
        graph[src] = {dst: dist}
    else:
        graph[src][dst] = dist
    if dst not in graph:
        graph[dst] = {src: dist}
    else:
        graph[dst][src] = dist

def cost(graph, s, maximize):
    cities = list(graph.keys())
    total = 0
    T, curr = {s}, s
    while len(T) != len(cities):
        mc, mv = None, [float('inf'), 0][int(maximize)]
        for i in graph[curr]:
            if i not in T:
                if (maximize and mv < graph[curr][i]) or (not maximize and mv > graph[curr][i]):
                    mc, mv = i, graph[curr][i]
        curr = mc
        T = T | {mc}
        total += mv
    return total

print("Part 1:", min(map(lambda x: cost(graph, x, maximize=False), list(graph.keys()))))
print("Part 2:", max(map(lambda x: cost(graph, x, maximize=True), list(graph.keys()))))