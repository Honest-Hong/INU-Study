N, M = [int(x) for x in input().split()]

arr = [x for x in range(M + 1)]

arr[0], arr[1] = 0, 0
for i in arr[2:]:
    j = 2 * i
    while j <= M:
        if arr[j]!=0:
            arr[j] = 0
        j += i

for i in range(N,M+1):
    if arr[i] != 0:
        print(i)
