def merge(arr1, arr2):
    i, j = 0, 0
    le1, le2 = len(arr1), len(arr2)
    re = []
    while i < le1 and j < le2:
        v1, v2 = arr1[i], arr2[j]
        if v1 <= v2:
            re.append(v1)
            i += 1
        else:
            re.append(v2)
            j += 1
    if i < le1:
        re += arr1[i:]
    else:
        re += arr2[j:]
    return re

arr3 = [4, 6]
arr4 = [2, 3, 5, 8, 9, 11]
print(merge(arr3, arr4))

