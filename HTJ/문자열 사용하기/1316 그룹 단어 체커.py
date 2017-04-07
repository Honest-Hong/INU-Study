string = input()

string = string.upper()
arr = [0 for i in range(26)]
for i in range(len(string)):
    arr[ord(string[i]) - ord('A')] += 1

maxNumber = max(arr)
maxIndex = arr.index(maxNumber)
arr.pop(maxIndex)
try:
    arr.index(maxNumber)
    print('?')
except:
    print(chr(maxIndex + ord('A')))    
