N = [int(x) for x in input().split()]

array = [int(x) for x in input().split()]
result = []
for i in range(len(array)):
    if array[i] < N[1]:
        result.append(array[i])

for i in range(len(result)):
    print(result[i], end=' ')
