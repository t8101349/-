arr = [[0, 6, 13], [10, 0, 4], [5, 999, 0]]
path = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]


def floyd(arr, path):
    vertex = [0, 1, 2]
    for k in vertex:
        for i in vertex:
            for j in vertex:
                if arr[i][j] > arr[i][k]+arr[k][j]:
                    arr[i][j] = arr[i][k]+arr[k][j]
                    path[i][j] = k

    return arr, path


print(floyd(arr, path))
