cnt=0

case=int(input())
for i in range (case) :
    sco=[int(x) for x in input().split()]
    avg=sum(sco[1:])/sco[0]
    for j in sco[1:] :
        if(j>avg) :
            cnt+=1
    rate=cnt/sco[0]*100
    #res= round(rate,4)
    print("%0.4f" %rate +"%")
    

            
