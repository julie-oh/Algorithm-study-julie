def selection(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
               min_idx = j

        if not i == min_idx:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    print(arr)

if __name__ == '__main__':
    test_fname = 'test-set/sort_test_set.txt'
    with open(test_fname, 'r') as testf:
        lines = testf.readlines()
        for line in lines:
            int_arr = [int(s) for s in line.strip().split(',')]
            selection(int_arr)