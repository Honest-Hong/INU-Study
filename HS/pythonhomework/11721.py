ins=input()
length=len(ins)
m=1

for i in range(0,length) :
    if m==10 :
        print(ins[i])
        m=1
        
    else :
        print(ins[i],end='')
        m+=1       

    
