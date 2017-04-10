arr = [x for x in input().split()]

A = [i for i in arr[0]]
B = [i for i in arr[1]]

A.reverse()
B.reverse()

strA = ''
for i in range(len(A)):
    strA += A[i]

strB = ''
for i in range(len(B)):
    strB += B[i]

print(max(int(strA), int(strB)))
