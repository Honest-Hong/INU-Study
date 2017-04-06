C = int(input())

for i in range(C):
    raw = [int(x) for x in input().split()]
    count = raw[0]
    score = sorted(raw[1:])
    avg = sum(score) / count

    upAvg = 0
    for j in range(count):
        if score[count - 1 - j] > avg:
            upAvg += 1
        else:
            break

    print("%.3f%%"%(upAvg / count * 100))
