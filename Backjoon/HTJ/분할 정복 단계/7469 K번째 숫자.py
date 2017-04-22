n, m = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
for _ in range(m):
    i, j, k = [int(x)-1 for x in input().split()]
    print(sorted(arr[i:j+1])[k])

# Fail!
