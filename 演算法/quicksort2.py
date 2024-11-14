def partition(arr):
    pivot = arr[-1]
    left = [num for num in arr[:-1] if num<pivot]
    right = [num for num in arr[:-1] if num>=pivot]
    return left,pivot,right


def quicksort(arr):
    if len(arr)>1:
        left, pivot, right = partition(arr)
        return quicksort[left], pivot, quicksort[right]
    else:
        return arr



list = [1, 22, 11, 9, 99, 88, 13, 55, 8, 9, 9, 90, 44, 7, 18, 67, 9, 7, 42]
print(quicksort(list, 0, len(list)-1))
