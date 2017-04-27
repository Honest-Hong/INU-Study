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

N = int(input())
arr = [int(input()) for _ in range(N)]

print(qsort(arr))
