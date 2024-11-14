# minheap
# def change(arr, x, y):


def heapify(arr, i, n):

    # n = len(arr)
    r = 2*i+2
    l = 2*i+1
    min = i

    if l <= (n-1):
        if arr[l] < arr[min]:
            min = l
    if r <= (n-1):
        if arr[r] < arr[min]:
            min = r

    if min != i:
        arr[i], arr[min] = arr[min], arr[i]
        heapify(arr, min, n)

    return arr


def buildheap(arr, n):
    # n = len(arr)
    parent = (n-2)//2
    for i in range(parent, -1, -1):
        heapify(arr, i, n)

    return arr


def heapsort(arr):
    # min heapsort

    buildheap(arr, len(arr))
    n = len(arr)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0, i)

    return arr


list = [5, 6, 1, 3, 7, 50, 4, 6, 2, 10, 3, 4,
        6, 7, 8, 1, 56, 78, 12, 45, 37, 66, 100, 11, 200]
heapsort(list)

print(list)
