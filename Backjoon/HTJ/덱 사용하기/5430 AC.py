T = int(input())
for _ in range(T):
    com = input()
    n = int(input())
    string = input()
    string = string[1:len(string)-1]
    arr = []
    if string:
        arr = [int(x) for x in string.split(',')]

    flag = False
    for c in com:
        if c == 'R':
            flag = not flag
        elif c == 'D':
            if arr:
                if flag:
                    arr.pop()
                else:
                    arr.pop(0)
            else:
                arr = None
                break

    if arr is None:
        print('error')
    else:
        if flag:
            arr.reverse()
        print('[', end='')
        for i in range(len(arr)):
            print(arr[i], end='')
            if i < len(arr) - 1:
                print(',', end='')
        print(']')
