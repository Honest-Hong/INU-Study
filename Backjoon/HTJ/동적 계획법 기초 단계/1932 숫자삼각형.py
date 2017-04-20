n = int(input())

arr = []
costs = [0 for x in range(n)]
for _ in range(n):
    num = [int(x) for x in input().split()]
    arr.append(num)

for i in range(n):
    if i == 0:
        continue
    for j in range(i + 1):
        up = []
        if j > 0:
            up.append(arr[i-1][j-1])
        if j < i:
            up.append(arr[i-1][j])
        arr[i][j] += max(up)

print(max(arr[n-1]))
