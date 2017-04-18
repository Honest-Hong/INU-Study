N, M = [int(x) for x in input().split()]

arr = [x for x in range(1, N + 1)]
index = 0
print('<', end='')
while arr:
    index = (index - 1 + M) % len(arr)
    print(arr.pop(index), end='')
    if arr:
        print(', ', end='')
print('>', end='')
