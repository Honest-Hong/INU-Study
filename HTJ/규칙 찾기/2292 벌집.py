N = int(input())

N -= 1
count = 1
while N > 0:
    N -= 6 * count
    count += 1

print(count)
