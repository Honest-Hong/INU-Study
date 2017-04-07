A = int(input())
B = int(input())
C = int(input())

mul = str(A * B * C)

arr = [0 for i in range(10)]
for i in range(len(mul)):
    arr[int(mul[i])] += 1

for i in range(10):
    print(arr[i])
