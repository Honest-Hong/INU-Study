N = int(input())

arr = set([N])

count = 0
while 1 not in arr:
    tmp = set([])
    count += 1
    for x in arr:
        if x%3 == 0:
            tmp.add(x//3)
        if x%2 == 0:
            tmp.add(x//2)
        tmp.add(x-1)
    arr = tmp

print(count)
