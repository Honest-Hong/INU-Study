T = int(input())
for _ in range(T):
    N, K = [int(x) for x in input().split()]
    time = [int(x) for x in input().split()]
    levels = [[0]]
    for __ in range(K):
        f, t = [int(x) - 1 for x in input().split()]
        level = 0
        for i in range(len(levels)):
            if f in levels[i]:
                level = i
                break
        try:
            if t not in levels[level+1]:
                levels[level+1].append(t)
        except:
            levels.append([])
            if t not in levels[level+1]:
                levels[level+1].append(t)

    W = int(input()) - 1

    level = 0
    for i in range(len(levels)):
        if W in levels[i]:
            level = i
            break
    
    cost = 0
    for l in levels[:level+1]:
        cost += max([time[i] for i in l])

    print(cost)
    
