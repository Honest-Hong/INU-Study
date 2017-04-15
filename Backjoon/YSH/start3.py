import sys
a=int(input())

for i in range(a,0,-1):
    for j in range(0,i):
        sys.stdout.write("*")
    print()
