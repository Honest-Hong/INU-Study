N=int(input())
score = [int(i) for i in input().split(' ')]
maxN = max(score)
for i in range(N):
    score[i] = score[i]/maxN*100
print('%.2f' % float(sum(score)/N))
