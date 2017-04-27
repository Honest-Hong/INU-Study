import math

n, m = [int(x) for x in input().split()]
print(math.factorial(n) // (math.factorial(m) * math.factorial(n - m)))
