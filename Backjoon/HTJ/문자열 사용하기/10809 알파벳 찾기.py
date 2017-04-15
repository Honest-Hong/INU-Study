word = input()

arr = [-1 for i in range(ord('z') - ord('a') + 1)]
for i in range(len(word)):
    index = ord(word[i]) - ord('a')
    if arr[index] == -1:
        arr[index] = i

for i in arr:
    print(i, end=' ')
