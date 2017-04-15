def isGroup(string):
    arr = [-1 for j in range(26)]
    for i in range(len(string)):
        index = ord(string[i]) - ord('a')
        if arr[index] == -1 or arr[index] == i-1:
            arr[index] = i
            continue
        else:
            return False
    return True 

N = int(input())

count = 0
for i in range(N):
    string = input()
    if isGroup(string):
        count += 1

print(count)
