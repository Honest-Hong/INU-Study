counts = [0, 0, 0]
def Count(paper, sx, sy, l):
    global counts
    val = paper[sx][sy]
    for i in range(sx, sx + l):
        for j in range(sy, sy + l):
            if paper[i][j] != val:
                div = l//3
                for k in range(3):
                    Count(paper, sx + k*div, sy, div)
                    Count(paper, sx + k*div, sy + div, div)
                    Count(paper, sx + k*div, sy + 2*div, div)
                return
    counts[val] += 1

N = int(input())
paper = [[] for x in range(N)]
for i in range(N):
    paper[i] = [int(x) + 1 for x in input().split()]

Count(paper, 0, 0, N)
for c in counts:
    print(c)
