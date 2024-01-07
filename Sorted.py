def isSorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return False
    return True
    
print(isSorted([1, 5, 7, 9, 9]))
