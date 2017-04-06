N = int(input())

cycle = 0
newNum = N
while N != newNum or cycle == 0:
    front = int(newNum / 10)
    back = newNum % 10
    resultSum = front + back
    newNum = back * 10 + resultSum % 10
    cycle += 1

print(cycle)
