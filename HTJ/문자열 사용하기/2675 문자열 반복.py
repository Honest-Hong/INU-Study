T = int(input())

for i in range(T):
    raw = input().split()
    num = int(raw[0])
    string = ''
    for j in range(len(raw[1])):
        string += raw[1][j] * num

    print(string)
