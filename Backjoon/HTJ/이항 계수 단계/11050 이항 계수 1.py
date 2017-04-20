import math

N, K = [int(x) for x in input().split()]

print(math.factorial(N) // (math.factorial(K) * math.factorial(N - K)))
