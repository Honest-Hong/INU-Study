N = int(input())
scores = [int(x) for x in input().split()]

scoreMax = max(scores)
total = 0
for i in range(N):
    total += scores[i] / scoreMax * 100

print("%.2f"%(total/N))
