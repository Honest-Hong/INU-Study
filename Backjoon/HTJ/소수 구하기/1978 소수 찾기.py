def isPrimary(number):
    if number == 1: return False
    for i in range(2, number//2 + 1):
        if number%i == 0:
            return False

    return True

N = int(input())
count = 0
for i in input().split():
    if isPrimary(int(i)):
        count += 1

print(count)
