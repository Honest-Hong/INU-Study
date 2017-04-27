import math

N, K = [int(x) for x in input().split()]

bc = math.factorial(N) // (math.factorial(K) * math.factorial(N - K))
print(bc % 10007)
