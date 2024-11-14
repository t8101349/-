def merge(left, right):
    result = []

    while len(left) and len(right):
        if left[0] <= right[0]:
            result.append(left.pop(0))  # pop

        else:
            result.append(right.pop(0))

    while len(left):
        result.append(left.pop(0))

    while len(right):
        result.append(right.pop(0))

    return result


def mergesort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    # left = [arr[i] for i in range(n//2)]
    # right = [arr[i] for i in range(n//2+1, n)]

    left = []
    right = []
    for i in range(len(arr)):
        if i < len(arr) // 2:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return merge(mergesort(left), mergesort(right))


list = [1, 3, 5, 7, 9, 8, 6, 4, 2, 0, 15, 65, 78, 21, 1, 66]

print(mergesort(list))
