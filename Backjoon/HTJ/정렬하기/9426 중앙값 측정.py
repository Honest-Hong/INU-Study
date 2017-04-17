def qsort(arr):
    left = 0
    right = len(arr) - 1;
    if right <= 0: return arr;
    
    pivot = (left + right)//2
    while True:
        while arr[left] < arr[pivot]:
            left += 1
        while arr[right] > arr[pivot]:
            right -= 1
        if left < right:
            a, b = arr[left], arr[right]
            arr[left], arr[right] = b, a
            
        if left == pivot:
            pivot = right
        elif right == pivot:
            pivot = left

        if left >= right:
            break

    return qsort(arr[:pivot]) + [arr[pivot]] + qsort(arr[pivot+1:])

N, K = [int(x) for x in input().split()]

arr = []
sumMid = 0
for i in range(N):
    arr += [int(input())]
    if i+1 >= K:
        sumMid += qsort(arr[i+1-K:])[(K-1)//2]

print(sumMid)
