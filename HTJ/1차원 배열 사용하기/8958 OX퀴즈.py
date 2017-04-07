N = int(input())

for i in range(N):
    ox = input()
    score = 0
    total = 0
    for j in range(len(ox)):
        if ox[j] == 'O':
            score += 1
            total += score
        else:
            score = 0

    print(total)
