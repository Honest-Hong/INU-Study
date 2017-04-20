import math

comb = []
limit = math.pow(2,32)

n, m = [int(x) for x in input().split()]
while n != 0 or m != 0:
    if m == 0 or m == n:
        print(1)
    elif m == 1 or m == n-1:
        print(n)
    else:
        if len(comb) < n + 1:
            for i in range(len(comb), n+1):
                if i == 0:
                    comb.append([1])
                elif i == 1:
                    comb.append([1])
                else:
                    arr = [1]
                    for j in range(len(comb[i-1])-1):
                        val = comb[i-1][j] + comb[i-1][j+1]
                        if val <= limit:
                            arr.append(val)
                        else:
                            break
                    if i%2 == 0:
                        val = comb[i-1][len(comb[i-1])-1]*2
                        if val <= limit:
                            arr.append(val)
                    comb.append(arr)

        print(comb[n][min(m, n-m)])
    n,m = [int(x) for x in input().split()]

