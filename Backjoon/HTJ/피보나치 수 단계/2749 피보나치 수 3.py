n = int(input())

pivo = []
for i in range((n + 1)%1500000):
    if i==0:
        pivo.append(0)
    elif i==1:
        pivo.append(1)
    else:
        pivo.append((pivo[0] + pivo[1])%1000000)
        pivo.pop(0)

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    print(pivo[1])
