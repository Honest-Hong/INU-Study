n = int(input())

pivo = []
for i in range(n+1):
    if i == 0:
        pivo.append(0)
    elif i == 1:
        pivo.append(1)
    else:
        pivo.append(pivo[i-2]+pivo[i-1])

print(pivo[n])
