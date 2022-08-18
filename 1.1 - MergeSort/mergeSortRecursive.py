import random

array = []
for i in range(11):
    array.append(random.randint(-10, 10))
    
print(array)

def merge(l, r):
    i = j = 0
    result = []
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
    
    result += l[i:]
    result += r[j:]
    return result

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    l = mergeSort(arr[:mid])
    r = mergeSort(arr[mid:])

    return merge(l, r)

print(mergeSort(array))
