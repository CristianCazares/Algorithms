import random

array = []
for i in range(11):
    array.append(random.randint(-10, 10))
    
print(array)

def merge(arr, l , r, mid):
    n1 = mid - l + 1
    n2 = r - mid
    
    arrL = [0] * n1
    arrR = [0] * n2
    for i in range(0, n1):
        arrL[i] = arr[l + i]
    for i in range(0, n2):
        arrR[i] = arr[mid + 1 + i]
    
    print("\n\n\n")

    i = j = 0
    k = l
    while i < n1 and j < n2:
        if arrL[i] <= arrR[j]:
            arr[k] = arrL[i]
            i += 1
        else:
            arr[k] = arrR[j]
            j += 1
        k += 1

def mergeSort(arr, l, r):
    if l < r:
        mid = l + (r - l) // 2
        print(f'arr:{arr}, l:{l}, r:{r}, mid:{mid}')
        mergeSort(arr, l, mid)
        mergeSort(arr, mid + 1, r)
        merge(array, l, r, mid)

def MergeSort(arr):
    mergeSort(arr, 0, len(arr) - 1)

MergeSort(array)
print(array)