N = input()

arr = [0 for _ in range(9)]

for i in range(len(N)):
    num = int(N[i])
    if num==9:
        num = 6
    arr[num] += 1

arr[6] = int((arr[6]-1) / 2) + 1

print(max(arr))
