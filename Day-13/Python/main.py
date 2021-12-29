import sys, itertools

dir_graph, graph = {}, {}
for line in sys.stdin:
    line = line.split()
    src, status, happ, dst = line[0], int(line[2] == 'gain'), int(line[3]), line[-1][:-1]
    if src not in dir_graph:
        dir_graph[src] = {dst: [-happ, happ][status]}
    else:
        dir_graph[src][dst] = [-happ, happ][status]

for s in dir_graph:
    for d in dir_graph[s]:
        if s not in graph:
            graph[s] = {d: dir_graph[s][d] + dir_graph[d][s]}
        else:
            graph[s][d] = dir_graph[s][d] + dir_graph[d][s]

perm = list(itertools.permutations(list(graph.keys())))
cost = -1e4
for seq in perm:
    tmp = 0
    for i in range(len(seq)):
        tmp += graph[seq[i]][seq[(i + 1) % len(seq)]]
    cost = max(cost, tmp)
print("Part 1:", cost)

perm2 = list(itertools.permutations(list(graph.keys()) + ['You']))
cost2 = -1e4
for seq in perm2:
    tmp = 0
    for i in range(len(seq)):
        tmp += graph.get(seq[i], {}).get(seq[(i + 1) % len(seq)], 0)
    cost2 = max(cost2, tmp)
print("Part 2:", cost2)