unique = []

def has_duplicates(arr):
    for i in range(len(arr)):
        if arr[i] in unique:
            return False
        unique.append(arr[i])
    return True

print(has_duplicates([1,4,5,6]))