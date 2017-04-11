T = int(input())

for i in range(T):
    num = [int(x) for x in input().split()]
    value = num[1] - num[0]

    flag = 1
    level = 0
    count = 0
    while value > 0:
        if flag:
            level += 1
            flag = 0
        else:
            flag = 1
        value -= level
        count += 1
        
    print(count)

