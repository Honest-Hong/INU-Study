N = input()
count=0
number=N
while True:
    if len(number)!=2:
        number='0'+number
    else:
        cal = str(int(number[0])+int(number[1]))
        if len(cal)==2:
            number=number[1]+cal[1]
        else:
            number=number[1]+cal[0]
        count+=1
        if int(number)==int(N):
            break;
print(count)
