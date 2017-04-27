n = int(input())

stack = [n - x for x in range(n)]

arr = []
out = []
for _ in range(n):
    num = int(input())
    while not arr or arr[len(arr) - 1] != num:
        if stack:
            arr.append(stack.pop())
            out.append('+')
        else:
            out.append('x')
            break
    arr.pop()
    out.append('-')

if 'x' in out:
    print('NO')
else:
    for i in out:
        print(i)
