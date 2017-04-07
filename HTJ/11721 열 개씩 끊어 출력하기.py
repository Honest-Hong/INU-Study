string = input()

count = len(string) / 10
for i in range(int(count) + 1):
    print(string[10*i:10*(i+1)])
