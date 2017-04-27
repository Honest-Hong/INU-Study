class House:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

N = int(input())

arr = []
for i in range(N):
    r, g, b = [int(x) for x in input().split()]
    house = House(r,g,b)
    arr.append(house)

costs = [arr[0].r, arr[0].g, arr[0].b]
for h in arr[1:]:
    t0 = min(costs[1], costs[2]) + h.r
    t1 = min(costs[0], costs[2]) + h.g
    t2 = min(costs[0], costs[1]) + h.b
    costs = [t0, t1, t2]

print(min(costs))
