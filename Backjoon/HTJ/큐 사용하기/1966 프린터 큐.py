T = int(input())
for _ in range(T):
    N, M = [int(x) for x in input().split()]
    order = [int(x) for x in input().split()]
    number = [x for x in range(N)]

    count = 0
    while True:
        if order[0] == max(order):
            count += 1
            if number[0] == M:
                print(count)
                break
            order.pop(0)
            number.pop(0)
        else:
            order.append(order.pop(0))
            number.append(number.pop(0))
