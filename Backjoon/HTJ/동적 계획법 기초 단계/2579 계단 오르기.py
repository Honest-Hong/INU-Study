n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

costs = [arr[0]]
for i in range(1, n):
    if i == 1:
        costs.append(arr[0] + arr[1])
    elif i == 2:
        costs.append(arr[i] + max(arr[0], arr[1]))
    elif i > 2:
        cost1 = costs[i-3] + arr[i-1]
        cost2 = costs[i-2]
        costs.append(arr[i] + max(cost1, cost2))

print(costs[n-1])
