N = int(input())

deck = []
for _ in range(N):
    com = [x for x in input().split()]
    if com[0]=='push_front':
        deck.insert(0, int(com[1]))
    elif com[0]=='push_back':
        deck.append(int(com[1]))
    elif com[0]=='pop_front':
        if deck: print(deck.pop(0))
        else: print(-1)
    elif com[0]=='pop_back':
        if deck: print(deck.pop())
        else: print(-1)
    elif com[0]=='size':
        print(len(deck))
    elif com[0]=='empty':
        if deck: print(0)
        else: print(1)
    elif com[0]=='front':
        if deck: print(deck[0])
        else: print(-1)
    elif com[0]=='back':
        if deck: print(deck[len(deck) - 1])
        else: print(-1)
