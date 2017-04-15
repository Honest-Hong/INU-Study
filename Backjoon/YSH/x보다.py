import sys

N,X = input().split()
cand = input().split()

for i in range(0,len(cand)):
    if int(cand[i])<int(X):
        print(cand[i],end=" ")
