N, M, V = [int(x) for x in input().split()]

temp = [[] for x in range(N)]
for i in range(M):
    From, To = [int(x) - 1 for x in input().split()]
    temp[From].append(To)
    temp[To].append(From)

edge = []
for t in temp:
    edge.append(sorted(t))

def DFS(index, edge, visit):
    if index not in visit:
        visit.append(index)
    for e in edge[index]:
        if e not in visit:
            DFS(e, edge, visit)

def BFS(index, edge):
    queue = [index]
    visit = [index]
    while queue:
        pop = queue.pop(0)
        for e in edge[pop]:
            if e not in visit:
                visit.append(e)
                queue.append(e)
    return visit

index = V - 1
visit = []
DFS(index, edge, visit)
for v in visit:
    print(v+1, end=' ')
print()

visit = BFS(index, edge)
for v in visit:
    print(v+1, end=' ')
print()
