def Index(num):
    index = 0
    while num > 0:
        index += 1
        num -= index
    return index

def startIndex(num):
    return int(num*(num-1)/2 + 1)

X = int(input())

index = Index(X)

x = 1
y = 1
if index % 2 == 1:
    x = index
else:
    y = index
for i in range(X - startIndex(index)):
    if index % 2 == 1:
        x -= 1
        y += 1
    else:
        x += 1
        y -= 1

print("%d/%d"%(x,y))
