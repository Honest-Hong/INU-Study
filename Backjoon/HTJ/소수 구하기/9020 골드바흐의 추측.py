def isP(p):
    if p==1: return False
    if p==2: return True
    for i in range(2,p):
        if p%i==0: return False
    return True

T = int(input())

for _ in range(T):
    n = int(input())
    p1 = n//2
    p2 = n//2 + n%2
    while not isP(p1) or not isP(p2):
        p1 -= 1
        p2 += 1
    print(p1, p2)
        
