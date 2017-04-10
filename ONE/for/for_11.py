arr = list(str(input()))
arr.reverse()
length = len(arr)
cnt = 1

for i in range(length):
    print(arr.pop(),end='')
    if cnt % 10 == 0 : print()
    cnt = cnt + 1
print()
