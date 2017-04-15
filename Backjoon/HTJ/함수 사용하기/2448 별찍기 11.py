import math

def moveRight(strings):
    size = int(len(strings) / 3)
    for i in range(len(strings)):
        strings[i] = '   ' * size + strings[i] + '   ' * size
    return strings

def addStar(strings):
    newStar = []
    for i in range(len(strings)):
        newStar.append(strings[i] + ' ' + strings[i])
    strings = moveRight(strings)
    strings += newStar
    return strings

def printStar(size):
    strings = []
    
    newStar = []
    newStar.append('  *  ')
    newStar.append(' * * ')
    newStar.append('*****')
    strings += newStar

    for i in range(1, int(math.log(size / 3, 2)) + 1):
        strings = addStar(strings)

    for i in range(len(strings)):
        print(strings[i])

N = int(input())
printStar(N)
