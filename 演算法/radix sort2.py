def countingsort(arr, place):
    size = len(arr)
    output = [0]*size
    count = [0]*10
# count
    for i in arr:
        index = (i//place) % 10
        count[index] += 1
# cumulate count
    for i in range(1, 10):
        count[i] += count[i-1]

# place element in
    i = size - 1
    while i >= 0:
        index = (arr[i]//place) % 10
        output[count[index]-1] = arr[i]  # 倒著填入 0~n-1故-1
        count[index] -= 1
        i -= 1

    for i in range(0, size):
        arr[i] = output[i]


def radixsort(arr):
    maxelement = max(arr)

    place = 1
    while maxelement // place > 0:
        countingsort(arr, place)
        place *= 10

    return arr


# data = [121, 432, 564, 23, 1, 45, 788, 5555]
# print(radixsort(data))
# 節省空間複雜度的寫法

userinput = input("input numbers:\n").strip()
nums = [int(item) for item in userinput.split(',')]
print(radixsort(nums))
