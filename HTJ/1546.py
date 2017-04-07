N = int(input())
num = [float(x) for x in input().split()]

maxNum = max(num);

result = 0.0
for i in range(len(num)):
    result += num[i]/maxNum*100.0

print(round(result/len(num), 2))
