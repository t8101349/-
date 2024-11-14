from heapq import heapify
# maxheap

# class Node:
# def __init__(self, arr, i):
# self.data = arr[i]
# self.c1 = 2*i+1
# self.c2 = 2*i+2


def heapify(arr, n,  i):
    largest = i
    l = 2*i+1
    r = 2*i+2
    if l < n:
        if arr[l] > arr[largest]:
            largest = l
    if r < n:
        if arr[r] > arr[largest]:
            largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def build_heap(arr, n):
    parent = (n-2)//2
    for i in range(parent, -1, -1):
        heapify(arr, n, i)
    # 優化:從parent開始


def heapsort(arr):
    n = len(arr)
    build_heap(arr, n)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr


list = [5, 6, 1, 3, 7, 9, 4, 6, 2, 1, 3, 4,
        6, 7, 8, 1, 56, 78, 12, 45, 37, 66, 100, 11]
heapsort(list)
print(list)
