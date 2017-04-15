a = input()

while len(a)!=0:
    if len(a)>=10:
        print(a[0:10])
        a=a[10:]
    else:
        print(a[0:])
        a=""

