N = [int(x) for x in input().split()]
days = 0
for i in range(1,N[0]):
    if i==1 | i==3 | i==5 | i==7 | i==8 | i==10 | i==12:
        days += 31
    elif i==2:
        days += 28
    else:
        days += 30

days += N[1]
days %= 7

if days==0:
    print('SUN')
if days==1:
    print('MON')
if days==2:
    print('TUE')
if days==3:
    print('WED')
if days==4:
    print('THU')
if days==5:
    print('FRI')
if days==6:
    print('SAT')
    
