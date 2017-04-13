a = input()
c=0
for i in range(0,len(a)):
    print(a[i],end='')
    c = c+1
    if c%10 == 0:
        print()
