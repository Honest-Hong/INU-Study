arr = [int(x) for x in input().split()]
while arr[0] != 0:
    n = arr[0]
    arr = arr[1:]

    size = 0
    for i in range(n):
        for j in range(i, n):
            height = min(arr[i:j+1])
            val = (j - i + 1) * height
            if size < val:
                size = val
    arr = [int(x) for x in input().split()]
