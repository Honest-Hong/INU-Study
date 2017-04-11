T = int(input())

for _ in range(T):
    num = [int(x) for x in input().split()]
    H = num[0]
    W = num[1]
    N = num[2] - 1

    room = int(N / H)
    floor = N % H

    print("%d%02d"%(floor+1,room+1))
