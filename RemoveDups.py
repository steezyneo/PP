unique = []

def remove_duplicates(arr):
    for i in range(len(arr)):
        if arr[i] not in unique:
            unique.append(arr[i])

    return unique

print(remove_duplicates([1,4,4,5,6]))