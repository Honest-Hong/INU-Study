case = input()

for i in range(0,int(case)):
    li = input().split()
    li = list(map(int,li))
    average=sum(li[1:])/(len(li)-1)
    count=0
    for j in range(1,len(li)):
        if li[j]>average:
            count+=1
    print("%.3f"%round(count/li[0]*100,4)+'%')
                   
