day = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
numofDays=[31,28,31,30,31,30,31,31,30,31,30,31]

x,y=input().split()

sumofDays=int(y)

for i in range(0,int(x)-1):
    sumofDays+=numofDays[i]
print(day[sumofDays%7])
