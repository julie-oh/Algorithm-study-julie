def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    p = partition(0, arr)
    return quick_sort(arr[:p]) + [arr[p]] + quick_sort(arr[p+1:])

def partition(pivot, arr):
    p = arr[pivot]
    left = 0
    right = len(arr) - 1

    while left <= right:
        while left <= right and p >= arr[left]:
            left += 1

        while left <= right and p < arr[right]:
            right -= 1

        if left <= right:
            # swap
            arr[left], arr[right] = arr[right], arr[left]

    arr[pivot], arr[right] = arr[right], arr[pivot]
    print(arr)
    return right

if __name__ == '__main__':
    print(quick_sort([2,2,3,41,3,0,1]))
