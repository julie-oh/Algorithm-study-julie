def sort(arr):
    if len(arr) < 2:
        return arr

    re_arr, idx = partition(arr)

    return sort(arr[:idx]) + [arr[idx]] + sort(arr[idx + 1:])


def partition(arr):
    pivot_idx = len(arr) // 2
    pivot_val = arr[pivot_idx]
    arr[0], arr[pivot_idx] = arr[pivot_idx], arr[0]

    left = 1
    right = len(arr) - 1

    while left <= right:
        while left <= right and arr[left] <= pivot_val:
            left += 1

        while left <= right and arr[right] > pivot_val:
            right -= 1

        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]

    arr[0], arr[right] = arr[right], arr[0]
    return arr, right


if __name__ == '__main__':
    print(sort([1,23,12,146,210, 11]))