string = input()

count = 0
for i in range(len(string)):
    value = ord(string[i]) - ord('A')
    if value <= 2:
        count += 3
    elif value <= 5:
        count += 4
    elif value <= 8:
        count += 5
    elif value <= 11:
        count += 6
    elif value <= 14:
        count += 7
    elif value <= 18:
        count += 8
    elif value <= 21:
        count += 9
    else:
        count += 10

print(count)
