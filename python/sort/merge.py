def merge(arr):
    if len(arr) <= 2:
        if len(arr) == 1:
            return arr
        else:
            if arr[0] > arr[1]:
                arr[0], arr[1] = arr[1], arr[0]
            return arr
    else:
        devide = len(arr) // 2

        return merge_sort(merge(arr[:devide]), merge(arr[devide:]))


def merge_sort(arr1, arr2):
    len1 = 0
    len2 = 0
    re_arr = []
    print(arr1,arr2)
    while not (len(arr1) == len1 or len(arr2) == len2):
        if  arr2[len2] < arr1[len1]:
            re_arr.append(arr2[len2])
            len2 += 1
        else:
            re_arr.append(arr1[len1])
            len1 += 1

        if len(arr1) == len1:
            re_arr += arr2[len2:]
        if len(arr2) == len2:
            re_arr += arr1[len1:]

    # assert len(re_arr) == len(arr1) + len(arr2)

    return re_arr


if __name__ == '__main__':
    print(merge([1,4,5,2,8,1,3, 2, 4, 99 , 3, 4]))
    print(merge([4, 4, 4, 4, 4, 4, 4]))
    # testf_fname = 'test-set/sort_test_set.txt'
    # with open(testf_fname, 'r') as testf:
    #     lines = testf.readlines()
    #     for line in lines:
    #         int_arr = [int(s) for s in line.strip().split(',')]
    #         print(merge(int_arr))
