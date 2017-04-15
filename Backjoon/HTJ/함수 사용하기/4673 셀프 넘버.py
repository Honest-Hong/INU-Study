def d(n):
    result = n
    for i in range(len(str(n))):
        result += n % 10
        n = int(n/10)

    return result

array = []
for i in range(1,10001):
    array.append(d(i))

s1 = set(array)
s2 = set(range(1,10001))
final = sorted(s2 - s1)

for i in final:
    print(i)
