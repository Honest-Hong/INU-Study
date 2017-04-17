arr = [x for x in range(123456*2 + 1)]

arr[0], arr[1] = 0, 0
for i in arr[2:]:
    j = 2 * i
    while j <= 123456*2:
        if arr[j]!=0:
            arr[j] = 0
        j += i

inputs = []
n = int(input())
while n!=0:
    inputs.append(n)
    n = int(input())

for n in inputs:
    count = 0
    for i in range(n + 1, n*2 + 1):
        if arr[i] != 0: 
            count += 1
    print(count)
