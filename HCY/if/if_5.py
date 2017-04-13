
a=int(input())

for j in range(0,a):
    b=[int(i) for i in input().split()]
    avrg = sum(b[1:])/b[0]
    cnt = 0
    for k in b[1:]:
       if k>avrg:
           cnt = cnt + 1
    print("%.3f" % float(cnt/b[0]*100))
