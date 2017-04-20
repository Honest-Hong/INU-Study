import math

N = int(input())
fac = math.factorial(N)

count = 0
while fac % 10 == 0:
    count += 1
    fac = fac//10

print(count)
