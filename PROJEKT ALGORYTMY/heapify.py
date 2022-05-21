def max_heapify(arr, n, i):
    l = (2 * i) + 1
    r = (2 * i) + 2
    if l <= (n - 1) and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    if r <= (n - 1) and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    for i in range((n - 1) // 2, -1, -1):
        max_heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)