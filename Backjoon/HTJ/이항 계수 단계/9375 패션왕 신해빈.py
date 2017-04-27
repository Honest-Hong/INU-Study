T = int(input())

for _ in range(T):
    n = int(input())
    kind = []
    wear = []
    for __ in range(n):
        w, k = input().split()
        if k in kind:
            index = kind.index(k)
            wear[index].append(w)
        else:
            kind.append(k)
            wear.append([w])

    nw = []
    for i in range(len(kind)):
        arr = []
        for w in wear:
            arr.append(len(w))
        nw.append(arr)
        

    print(nw)
