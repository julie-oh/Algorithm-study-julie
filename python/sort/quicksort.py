def quicksort(arr):
    if len(arr) <= 2:
        if len(arr) == 2 and arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]

        return arr
    else:
        p = partion(0, arr)
        return quicksort(arr[:p]) + [arr[p]] + quicksort(arr[p+1:])


def partion(pivot, arr):
    # print(arr)
    left = 0
    right = len(arr) - 1
    p = arr[pivot]

    while left <= right:
        while left <= right and arr[left] <= p:
            left += 1

        while left <= right and arr[right] > p:
            right -= 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]

    arr[0], arr[right] = arr[right], arr[0]

    #if right == len(arr) -1:
     #   return right

    return right

if __name__ == '__main__':
    testf_name = 'test-set/sort_test_set.txt'
    with open(testf_name, 'r') as testf:
        lines = testf.readlines()
        for line in lines:
            int_arr = [int(s) for s in line.strip().split(',')]
            quicksort(int_arr)

    print(quicksort([5, 1, 7, 9, 3]))
    print(quicksort([4,4,4,4,4,4]))
    print(quicksort([99,10,0,1,2,34]))
# 12, 323, 1, 10, 192, 191, 29, 21
# -1, 291, 210, 11, 01, 2983, 1930
