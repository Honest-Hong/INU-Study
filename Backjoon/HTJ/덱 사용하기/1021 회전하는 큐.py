N, M = [int(x) for x in input().split()]

deq = [x for x in range(N)]
pick = [int(x)-1 for x in input().split()]

cur = 0
move = 0
while pick:
    p = pick.pop(0)
    pos = deq.index(p)
    move += min(abs(pos - cur), len(deq) - abs(pos - cur))
    cur = pos
    deq.pop(cur)
    
print(move)
