N = int(input())

queue = []
for _ in range(N):
    command = input().split()
    if command[0] == 'push':
        data = int(command[1])
        queue.append(data)
    elif command[0] == 'pop':
        if queue: print(queue.pop(0))
        else: print(-1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if queue: print(0)
        else: print(1)
    elif command[0] == 'front':
        if queue: print(queue[0])
        else: print(-1)
    elif command[0] == 'back':
        if queue: print(queue[len(queue)-1])
        else: print(-1)
