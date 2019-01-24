def sort(arr):
    if len(arr) < 2:
        return arr

    p_arr, p = partition(arr)
    return sort(p_arr[:p]) + [p_arr[p]] + sort(p_arr[p+1:])


def partition(arr):
    pivot_idx = len(arr) // 2
    pivot = arr[pivot_idx]

    arr[0], arr[pivot_idx] = arr[pivot_idx], arr[0]
    p1 = 1
    p2 = len(arr) - 1

    while p1 <= p2:
        while p1 <= p2 and str(arr[p1]) <= str(pivot):
            p1 += 1

        while p1 <= p2 and str(arr[p2]) > str(pivot):
            p2 -= 1

        if p1 <= p2:
            arr[p1], arr[p2] = arr[p2], arr[p1]

    arr[p2], arr[0] = arr[0], arr[p2]
    return arr, p2


if __name__ == '__main__':
    print(sort([1,23,12,146,210, 11]))