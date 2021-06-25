# 1ans]
import numpy as np
arr=np.array([1,2,3])
print(arr.sum())
print('-----'*20)


# 2ans]
arr1=np.array([5,8,3])
print(arr1.max())
print('-----'*20)


# 3ans]
def rotateArray(arr, n, d):
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i + 1
    i = 0
    while (d < n):
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
    arr[:] = arr[: i] + temp
    return arr
arr = [1, 2, 3, 4, 5, 6, 7]
print("Array after left rotation is: ", end=' ')
print(rotateArray(arr, len(arr), 2))
print('-----'*20)


# 4ans]
def splitArr(arr, n, k):
    for i in range(0, k):
        x = arr[0]
        for j in range(0, n - 1):
            arr[j] = arr[j + 1]
        arr[n - 1] = x
arr = [12, 10, 5, 6, 52, 36]
n = len(arr)
position = 2

splitArr(arr, n, position)

for i in range(0, n):
    print(arr[i], end=' ')
print('-----'*20)


# 5ans]
def isMonotonic(A):
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1)))
A = [6, 5, 4, 4]
print(isMonotonic(A))