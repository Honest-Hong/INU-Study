res=0.0
n= int(input())
score=[int(x) for x in input().split()]
m=max(score)
for i in score :
    res+=i/m*100
avg=res/n
print("%0.2f" %avg)
