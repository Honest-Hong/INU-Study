T = int(input())

for _ in range(T):
    num = [int(x) for x in input().split()]
    M = num[0]
    N = num[1]
    x = num[2]
    y = num[3]

    i = 0
    j = 0
    a = i*M + x
    b = j*N + y
    while a != b:
        if a > b:
            j += 1
            b = j*N + y
        else:
            i += 1
            a = i*M + x
        if i * j > M * N:
            i = -1
            break
    if i != -1:
        print(i*M + x)
    else:
        print(-1)
