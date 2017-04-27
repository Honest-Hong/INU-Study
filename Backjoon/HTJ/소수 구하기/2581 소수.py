def isPrimary(number):
    if number == 1: return False
    for i in range(2, number//2 + 1):
        if number%i == 0:
            return False

    return True

N = int(input())
M = int(input())
arr = []
for i in range(N, M+1):
    if isPrimary(i):
        arr.append(i)

if arr:
    print(sum(arr))
    print(arr[0])
else:
    print(-1)
