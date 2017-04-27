T = int(input())

for _ in range(T):
    vps = input()
    stack = []
    ok = True
    for i in vps:
        if i=='(':
            stack.append(len(stack))
        elif i==')':
            if stack:
                stack.pop()
            else:
                ok = False
    if ok and not stack:
        print('YES')
    else:
        print('NO')
