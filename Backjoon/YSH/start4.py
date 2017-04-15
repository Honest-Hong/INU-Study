import sys
a=int(input())

for i in range(a,0,-1):
    for k in range(0,a-i):
        sys.stdout.write(" ")
    for j in range(0,i):
        sys.stdout.write("*")
    print()
