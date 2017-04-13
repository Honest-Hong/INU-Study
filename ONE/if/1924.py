mon, day = input().split(' ')
print(mon, day)
N = 0

for i in range(int(mon)-1):
    if mon in [1,3,5,7,8,10,12]: N += 31
    elif mon in [4,6,9,11]: N += 30
    else: N += 28

for i in range(1,int(day)):
    N += 1

print("N=%d"%N)

N = N % 7
if   N == 1: print("MON")
elif N == 2: print("TUE")
elif N == 3: print("WED")
elif N == 4: print("THU")
elif N == 5: print("FRI")
elif N == 6: print("SAT")
else       : print("SUN")
