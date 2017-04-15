N = int(input())
result = list()
cnt = 0
for i in range(N):
    score = [int(i) for i in input().split()]
    avg = sum(score[1:])/score[0]
    for j in score[1:]:
        if j > avg: cnt += 1                  
    result.append(round((cnt/score[0])*100,3))
    cnt = 0

for i in rnage(len(result)):
    print("%.3f%%" % result[i]i)
