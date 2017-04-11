T = int(input())

arr = list(list())

arr.append(range(1,15))

for i in range(1,15):
    temp = list()
    for j in range(14):
        if j==0:
            temp.append(1)
        else:
            temp.append(temp[j-1] + arr[i-1][j])
    arr.append(temp)

for _ in range(T):
    n = int(input())
    k = int(input())

    print(arr[n][k-1])
