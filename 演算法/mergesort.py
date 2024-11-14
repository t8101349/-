# merge sort


def mergesort(arr):
    if len(arr) <= 1:
        return arr
    left = []
    right = []

    # r = 0~mid
    # y = mid+1~end
    for i in range(len(arr)):
        if i < len(arr) // 2:
            left.append(arr[i])
        else:
            right.append(arr[i])

    # recursion
    mergesort(left)

    mergesort(right)

    # merge
    i = 0
    j = 0
    k = 0
    while len(left) > i and len(right) > j:
        if left[i] >= right[j]:
            arr[k] = right[j]
            j += 1
            k += 1
        elif left[i] < right[j]:
            arr[k] = left[i]
            i += 1
            k += 1
    while len(left) > i:
        arr[k] = left[i]
        i += 1
        k += 1
    while len(right) > j:
        arr[k] = right[j]
        j += 1
        k += 1

    return arr


list = [5, 6, 1, 3, 7, 9, 4, 6, 2, 1, 3, 4,
        6, 7, 8, 1, 56, 78, 12, 45, 37, 66, 100, 11]
print(mergesort(list))
