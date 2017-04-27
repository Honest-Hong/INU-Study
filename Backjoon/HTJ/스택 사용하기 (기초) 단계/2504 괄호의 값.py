string = input()

stack = []
for t in string:
    if t == '(':
        stack.append('(')
    elif t == ')':
        top = stack.pop()
        if top == '(':
            stack.append(2)
        elif type(top) is int and stack:
            top2 = stack.pop()
            if top2 == '(':
                stack.append(2*top)
    elif t == '[':
        stack.append('[')
    elif t == ']':
        top = stack.pop()
        if top == '[':
            stack.append(3)
        elif type(top) is int and stack:
            top2 = stack.pop()
            if top2 == '[':
                stack.append(3*top)

    size = len(stack)
    if size > 1 and type(stack[size - 1]) is int and type(stack[size - 2]) is int:
        stack.append(stack.pop() + stack.pop())

if stack and type(stack[0]) is int:
    print(stack[0])
else:
    print(0)
