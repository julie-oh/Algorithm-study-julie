def quicksort(arr):
    # stopping condition
    if len(arr) <= 1:
        return arr

    # partition step
    ## select pivot
    mid = len(arr) // 2
    pivot = arr[mid]  # value to compare

    # pivot swap - to remember the exact position
    arr[0], arr[mid] = arr[mid], arr[0]
    i = 1
    j = len(arr) - 1

    ## partition
    while i <= j:
        # boolean short-circuiting
        while i <= j and arr[i] <= pivot:
            i += 1

        while i <= j and arr[j] > pivot:
            j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]

    # i == j
    # restore pivot
    arr[0], arr[i - 1] = arr[i - 1], arr[0]

    # recursion step
    left_sorted = quicksort(arr[:i - 1])
    right_sorted = quicksort(arr[i - 1:])
    return left_sorted + right_sorted


def quicksort_functional(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left_partition = list(filter(lambda x: x <= pivot, arr))
    right_partition = list(filter(lambda x: x > pivot, arr))
    return quicksort(left_partition) + quicksort(right_partition)


if __name__ == '__main__':
    arr = [1, 4, 6, 2, 8, 10, 11, 8, 2, 3, 45, 9, 34, 3]
    arr_sorted = quicksort(arr)
    print(arr_sorted)
    print(quicksort_functional(arr))
