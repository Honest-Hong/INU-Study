N = int(input())
arr = list()
for _ in range(N):
    arr.append(int(input()))

arr = sorted(arr)
for i in arr:
    print(i)
