import sys
a=int(input())

for i in range(1,a+1):
    for j in range(0,i):
        sys.stdout.write("*")
    print()
