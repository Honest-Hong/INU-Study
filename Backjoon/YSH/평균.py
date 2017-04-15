N = input()
li = input().split()
li = list(map(int,li))
maxValue = max(li)

sum=0
for i in range(0,len(li)):
    sum+=li[i]/maxValue*100
result = sum/int(N)

print("%.2f"%round(result,2))
