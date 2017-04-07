def isSequence(n):
    arr = []
    for i in range(len(str(n))):
        arr.insert(0, n % 10)
        n = int(n/10)
    if len(arr) < 2:
        return True
    else:
        d = arr[0] - arr[1]
        for i in range(1, len(arr) - 1):
            if arr[i] - arr[i+1] != d:
                return False
        return True

N = int(input())
count = 0
for i in range(1, N+1):
    if(isSequence(i)):
        count += 1

print(count)
