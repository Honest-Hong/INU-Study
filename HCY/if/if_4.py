
a=int(input())
b=[int(i) for i in input().split()]
M = max(b)
for i in range(0,a):
    b[i] = b[i] / M * 100
print("%.2f" % float(sum(b)/a))
