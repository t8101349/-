def change(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def quicksort(arr, left, right):
    if left >= right:
        return

    pivot = arr[right]

    i = left
    j = right-1
    # sort
    while i < j:
        while arr[i] < pivot and i < j:
            i += 1
        while arr[j] >= pivot and i < j:
            j -= 1
        if i < j:
            change(arr, i, j)
    if arr[i] > pivot:
        change(arr, i, right)
    if arr[i] < pivot:
        i = right

    # for k in range(n):
    # if arr[k]<pivot:
    #       left.append(arr[k])
    #    else:
    #        right.append(arr[k])

    quicksort(arr, left, i-1)

    quicksort(arr, i+1, right)

    return arr


list = [1, 22, 11, 9, 99, 88, 13, 55, 8, 9, 9, 90, 44, 7, 18, 67, 9, 7, 42]
print(quicksort(list, 0, len(list)-1))
